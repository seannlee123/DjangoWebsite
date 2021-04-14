from Userlog.models import * 






#related object set
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null = True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null = True)
 
parent = ParentModel.objects.first()
#return all child models related to its parent
parent.childmodel_set.all()

