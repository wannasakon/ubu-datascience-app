from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from joblib import load
import pandas as pd
# from .predictors import predict
# from .models import House
# Create your views here.
def index(req):
    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    x4 = 0.0
    x5 = 0.0
    x6 = 0.0
    result ='result'
    df = pd.read_excel('https://archive.ics.uci.edu/ml/machine-learning-databases/00477/Real%20estate%20valuation%20data%20set.xlsx')
    df.head()
    if req.method == 'POST':
        print('เขา POST มา')
        #print(req.POST)
        x1 = float(req.POST['x1'])
        x2 = float(req.POST['x2'])
        x3 = float(req.POST['x3'])
        x4 = float(req.POST['x4'])
        x5 = float(req.POST['x5'])
        x6 = float(req.POST['x6'])
        # from sklearn.svm import LinearSVC 
        # model = LinearSVC()
        import numpy as np
        
        fm = np.array([[x1, x2, x3, x4, x5, x6]])
        # fm = x[['X2' ,'X3' , 'X4', 'X5', 'X6',]]
        # tv = x[['Y']]
        md = load('./houseapp/static/houseapp.model')
        result = md.predict(fm)
        
    else:
        print('เขากด enter มา')
    return render(req, 'houseapp/index.html', { 
        'result': result,
        'x1':x1,
        'x2':x2,
        'x3':x3,
        'x4':x4,
        'x5':x5,
        'x6':x6,
    })

# def api_species(req):
#     # 1. JsonResponse() // ภากร
#     # 2. serializer // 
#     # 3. json.dumps() // Nim, 
#     import json
#     species = House.objects.all();
#     data = serializers.serialize('json', species, fields=('sid', 'name'))
#     data = json.loads(data)
#     return JsonResponse(data, safe=False)