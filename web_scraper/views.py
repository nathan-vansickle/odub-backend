from django.shortcuts import render
import subprocess
from django.http import JsonResponse


def run_scrapers(request):
    try:
        url = 'https://www.guitarcenter.com/All-Deals.gc?N=18144'
        result = subprocess.run(['python3', 'web_scraper/guitarcenter_scraper.py', url], check=True, text=True, capture_output=True)
        return JsonResponse({'results': result.stdout})
    except subprocess.CalledProcessError:
        return JsonResponse({'result': 'Error executing web scrapers'})

