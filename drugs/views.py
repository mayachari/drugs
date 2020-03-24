import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Molecule, Drug
# Create your views here.

def display_mols(request):
    mols = Molecule.objects.all()
	
    return render(request,'display_mols.html', {'mols':mols})
	
def display_drugs(request):
    drugs = Drug.objects.all()
	
    return render(request,'display_drugs.html', {'drugs':drugs})

	
def content_upload(request):
    template = "content_upload.html"	
    prompt = {
        'Order':'idcode, GuidetoPharma, DrugCentral, BindingDB, ChEMBL, Orphanet, DisGeNET, PDB, PDBnum'
	}
    if request.method=="GET":
        return render(request,template,prompt)
    csv_file=request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        message.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    #next(io_string)
    for row in csv.reader(io_string, delimiter=',', quotechar="|"):
	    _, created = Molecule.objects.update_or_create(
            idcode = row[0],
            name = row[1],
            GuidetoPharma = row[2],
            DrugCentral = row[3],
          #  DrugBank = row[4],
            BindingDB = row[4],
            ChEMBL = row[5],
            Orphanet = row[6],
            DisGeNET = row[7],
            PDB = row[8],
            PDBnum = row[9]
                )
    context = {}
    return render(request, template, context)
	
def drug_upload(request):
    template = "drug_upload.html"	
    prompt = {
        'Order':'molidcode, drugidcode, drugname '
	}
    if request.method=="GET":
        return render(request,template,prompt)
    csv_file=request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        message.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    #next(io_string)
    for row in csv.reader(io_string, delimiter=',', quotechar="|"):
        try:
            m = Molecule.objects.get(idcode=row[0])
            _, created = Drug.objects.update_or_create(
                molecule = m,
                drugid = row[1],
                drugname = row[2],
                    )
        except ObjectDoesNotExist:
            print("")

    context = {}
    return render(request, template, context)    