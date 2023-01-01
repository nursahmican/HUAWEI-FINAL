from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Image
from .models import Result
from .forms import ImageForm
from .huawei import modelart
from io import BytesIO, BufferedReader
import base64
import json
# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            # base64_data = base64.b64encode(request.FILES["image"].read()).decode("utf-8")
            imageFile = request.FILES["image"]
          
            resp_str = modelart(request.FILES["image"].file.read())
            resp =json.loads(resp_str)
            a = form.save()
            predicted_label = resp.get("predicted_label", "")
            
            dict_resp = {}
            for i in resp["scores"]:
                dict_resp[i[0]] = i[1]
            
                
            
            normal = dict_resp.get("Normal")
            other_abnormalities = dict_resp.get("Other_Abnormalities")
            pathological_myopia = dict_resp.get("Pathological_Myopia")
            hypertension = dict_resp.get("Hypertension")
            glaucoma = dict_resp.get("Glaucoma")
            diabetes = dict_resp.get("Diabetes")
            cataract = dict_resp.get("Cataract")
            age_related_macular_degeneration = dict_resp.get("Age_Related_Macular_Degeneration")
            
            result = Result.objects.create(
                image=a, 
                predicted_label=predicted_label,
                normal=normal,
                other_abnormalities=other_abnormalities,
                hypertension=hypertension,
                pathological_myopia=pathological_myopia,
                glaucoma=glaucoma,
                diabetes=diabetes,
                cataract=cataract,
                age_related_macular_degeneration=age_related_macular_degeneration
                )
            result.save()
            
            
            
            # resp=modelart(filename)
    
            return redirect('result', pk=result.id)
    else:
        form = ImageForm()
    return render(request, 'diseases/index.html', {'form':form})

def results(request):
    results = Result.objects.all()
    context = {
        "results":results
    }
    
    return render(request, "diseases/results.html", context=context)
    
def result(request, pk):
    result= get_object_or_404(Result, pk=pk)
    print(result)


    return render(request, "diseases/result.html", context={"result":result})
