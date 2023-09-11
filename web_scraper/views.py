from django.shortcuts import render
import subprocess
from django.http import JsonResponse


def run_scrapers(request):
    try:
        gc_url = "https://www.guitarcenter.com/All-Deals.gc?N=18144"
        mf_url = "https://www.musiciansfriend.com/hot-deals?N=500001#plpSortAndRefine"
        gc_result = subprocess.run(['python3', 'web_scraper/guitarcenter_scraper.py', gc_url], check=True, text=True, capture_output=True)
        mf_result = subprocess.run(["python3", "web_scraper/musiciansfriend_scraper.py", mf_url], check=True, text=True, capture_output=True)
        return JsonResponse({'results': mf_result.stdout + gc_result.stdout})
    except subprocess.CalledProcessError:
        return JsonResponse({'result': 'Error executing web scrapers'})

