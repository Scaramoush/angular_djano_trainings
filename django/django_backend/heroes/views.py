# from django.shortcuts import HttpResponse
from django.http import JsonResponse
# Create your views here.

heroes = [
  {'id': '11', 'name': 'Mr. Nice'},
  { 'id': 12, 'name': 'Narco' },
  { 'id': 13, 'name': 'Bombasto' },
  { 'id': 14, 'name': 'Celeritas' },
  { 'id': 15, 'name': 'Magneta' },
  { 'id': 16, 'name': 'RubberMan' },
  { 'id': 17, 'name': 'Dynama' },
  { 'id': 18, 'name': 'Dr IQ' },
  { 'id': 19, 'name': 'Magma' },
  { 'id': 20, 'name': 'Я, любимый' }
]

def get_heroes(request):
    response = JsonResponse({'data': heroes})
    response.setdefault('Access-Control-Allow-Origin', '*')
    return response
