# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 03:19:21 2023

@author: yugandhar.gantala
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:28:05 2023

@author: yugandhar.gantala
"""


from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
#from rest_framework.response import Response
import json


## Load the required libraries
import numpy as np
import pandas as pd

import os
import openai
# Create your views here.
import os
OPENAI_API_KEY= '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'


def index(request):
    return render(request, "input.html")


def addition(request):

    text = request.GET['text']


    if not text.isdigit():
        a = text
        
        
        question=a
        openai.api_key = OPENAI_API_KEY
        
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=question,
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        
        txt = response['choices'][0].text
        data = pd.DataFrame({'Raw_data': txt},index=[0])

        output=data.to_json(orient='records')
        return JsonResponse(json.loads(output), safe = False)

        #return render(request, "result.html", {"result": predictions1})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})



