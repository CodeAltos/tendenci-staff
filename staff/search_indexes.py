from haystack import indexes

from tendenci.apps.perms.indexes import TendenciBaseSearchIndex

from staff.models import Staff


class StaffIndex(TendenciBaseSearchIndex):
    name = indexes.CharField(model_attr='name')
    department = indexes.CharField(model_attr='department', null=True)
    position = indexes.CharField(model_attr='position', null=True)

    def get_model(self):
        return Staff
