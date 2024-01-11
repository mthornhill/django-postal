"""
Code imported and optimized from django-piston 0.2.3rc1
"""
import warnings
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .utils import rc

typemapper = {}
handler_tracker = []


class HandlerMetaClass(type):
    """
    Metaclass that keeps a registry of class -> handler
    mappings.
    """

    def __new__(mcs, name, bases, attrs):
        new_mcs = type.__new__(mcs, name, bases, attrs)

        def already_registered(model, anon):
            for k, (m, a) in typemapper.iteritems():
                if model == m and anon == a:
                    return k

        if hasattr(new_mcs, "model"):
            if already_registered(new_mcs.model, new_mcs.is_anonymous):
                if not getattr(settings, "PISTON_IGNORE_DUPE_MODELS", False):
                    warnings.warn(
                        "Handler already registered for model %s, "
                        "you may experience inconsistent results." % new_mcs.model.__name__
                    )

            typemapper[new_mcs] = (new_mcs.model, new_mcs.is_anonymous)
        else:
            typemapper[new_mcs] = (None, new_mcs.is_anonymous)

        if name not in ("BaseHandler",):
            handler_tracker.append(new_mcs)

        return new_mcs


class BaseHandler(object):
    """
    Basehandler that gives you CRUD for free.
    You are supposed to subclass this for specific
    functionality.

    All CRUD methods (`read`/`update`/`create`/`delete`)
    receive a request as the first argument from the
    resource. Use this for checking `request.user`, etc.
    """

    __metaclass__ = HandlerMetaClass

    allowed_methods = ("GET", "POST", "PUT", "DELETE")
    anonymous = is_anonymous = False
    exclude = ("id",)
    fields = ()

    def flatten_dict(self, dct):
        return dict([(str(k), dct.get(k)) for k in dct.keys()])

    def has_model(self):
        return hasattr(self, "model") or hasattr(self, "queryset")

    def queryset(self, request):
        return self.model.objects.all()

    def value_from_tuple(tu, name):
        for int_, n in tu:
            if n == name:
                return int_
        return None

    def exists(self, **kwargs):
        if not self.has_model():
            raise NotImplementedError

        try:
            self.model.objects.get(**kwargs)
            return True
        except self.model.DoesNotExist:
            return False

    def read(self, request, *args, **kwargs):
        if not self.has_model():
            return rc.NOT_IMPLEMENTED

        pkfield = self.model._meta.pk.name

        if pkfield in kwargs:
            try:
                return self.queryset(request).get(pk=kwargs.get(pkfield))
            except ObjectDoesNotExist:
                return rc.NOT_FOUND
            except MultipleObjectsReturned:  # should never happen, since we're using a PK
                return rc.BAD_REQUEST
        else:
            return self.queryset(request).filter(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        if not self.has_model():
            return rc.NOT_IMPLEMENTED

        attrs = self.flatten_dict(request.data)

        try:
            inst = self.queryset(request).get(**attrs)
            return rc.DUPLICATE_ENTRY
        except self.model.DoesNotExist:
            inst = self.model(**attrs)
            inst.save()
            return inst
        except self.model.MultipleObjectsReturned:
            return rc.DUPLICATE_ENTRY

    def update(self, request, *args, **kwargs):
        if not self.has_model():
            return rc.NOT_IMPLEMENTED

        pkfield = self.model._meta.pk.name

        if pkfield not in kwargs:
            # No pk was specified
            return rc.BAD_REQUEST

        try:
            inst = self.queryset(request).get(pk=kwargs.get(pkfield))
        except ObjectDoesNotExist:
            return rc.NOT_FOUND
        except MultipleObjectsReturned:  # should never happen, since we're using a PK
            return rc.BAD_REQUEST

        attrs = self.flatten_dict(request.data)
        for k, v in attrs.iteritems():
            setattr(inst, k, v)

        inst.save()
        return rc.ALL_OK

    def delete(self, request, *args, **kwargs):
        if not self.has_model():
            raise NotImplementedError

        try:
            inst = self.queryset(request).get(*args, **kwargs)

            inst.delete()

            return rc.DELETED
        except self.model.MultipleObjectsReturned:
            return rc.DUPLICATE_ENTRY
        except self.model.DoesNotExist:
            return rc.NOT_HERE
