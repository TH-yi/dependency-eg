from django.shortcuts import render
from django.http import JsonResponse
from .utils import parse_and_save_sentences

def analyze_sentences(request):
    if request.method == 'POST':
        sentences = request.POST.get('sentences').split('\n')
        parse_and_save_sentences(sentences)
        return JsonResponse({'status': 'success'})
    return render(request, 'analysis/form.html')
