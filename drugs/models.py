from django.db import models

# Create your models here.

class Molecule(models.Model):
    idcode = models.CharField(db_index=True, max_length=200, default='BLAHBLAH')
    name = models.CharField(max_length=200)
    GuidetoPharma = models.CharField(max_length=200)
    DrugCentral = models.CharField(max_length=200)
  #  DrugBank = models.CharField(max_length=200)
    BindingDB = models.CharField(max_length=1000)
    ChEMBL = models.CharField(max_length=1000)
    Orphanet = models.CharField(max_length=1000)
    DisGeNET = models.CharField(max_length=1000)
    PDB = models.CharField(max_length=1000)
    PDBnum = models.IntegerField()
    
    def __str__(self):
        return self.idcode
    
    class Meta:
        ordering = ['idcode']	

class Drug(models.Model):
    drugid = models.CharField(db_index=True, max_length=200, default='BLAHBLAH2')
    drugname = models.CharField(max_length=200)
    molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE)

    def __str__(self):
        return self.drugid  
    
    class Meta:
        ordering = ['drugid']	
    	


   	
 

