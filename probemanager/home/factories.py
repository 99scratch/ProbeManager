import logging
import inspect
import os


class CommonMixin:

    @classmethod
    def get_logger(cls):
        return logging.getLogger(__name__.split('.')[0] + '.' +
                                 os.path.basename(inspect.getfile(cls)) + '-' + cls.__name__)

    @classmethod
    def get_all(cls):
        cls.get_logger().debug("######TEST GET ALL")
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, id):
        cls.get_logger().debug("######TEST GET ID")
        try:
            probe = cls.objects.get(id=id)
        except cls.DoesNotExist as e:
            cls.get_logger().debug('Tries to access an object that does not exist : ' + str(e))
            return None
        return probe

    @classmethod
    def get_last(cls, nbr):
        return cls.objects.all()[:nbr]
