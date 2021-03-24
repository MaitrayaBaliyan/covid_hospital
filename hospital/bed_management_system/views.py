from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

@login_required(login_url='/admin/login/')
def index(request):
	context = {}
	return render(request, 'bed_management_system/index.html', context)

@csrf_exempt
@login_required(login_url='/admin/login/')
def check_status(request):
	if request.method == 'POST':
		id = request.POST.get('bed_id', None)
		if id:
			url = f'http://127.0.0.1:8000/api/bed/{id}'
			r = requests.get(url)
			if r.status_code == 200:
				data = r.json()
				messages.success(request, f"<strong>Bed Type:</strong> {data['type']}</br><strong>Status</strong>: {data['status']}<br><strong>Patient Name:</strong> {data['patient_name']}</br><strong>Alloted/Free Date:</strong> {data['alloted_on']}")
			elif r.status_code == 404:
				messages.info(request, f"Bed with the id : <strong>{id}</strong> not found")
		else:
			messages.info(request, 'Bed Id Required')
	else:
		messages.info(request, 'POST Method Required')

	context = {}
	if request.META.get('HTTP_REFERER', ''):
		return redirect(request.META['HTTP_REFERER'])
	return render(request, 'bed_management_system/index.html', context)


@login_required(login_url='/admin/login/')
def list(request, section=None, status=None):
	context = {}
	query_string = ''
	if status == 'NOT_FREE':
		status = 'NOT FREE'

	if section and status:
		query_string = f'?type={section}&status={status}'
	elif section:
		query_string = f'?type={section}'
	elif status:
		query_string = f'?status={status}'

	url = f'http://127.0.0.1:8000/api/bed/{query_string}'
	r = requests.get(url)
	if r.status_code == 200:
		context['searched_data'] = r.json()

	return render(request, 'bed_management_system/index.html', context)


@login_required(login_url='/admin/login/')
def user_logout(request):
        context = {}
        logout(request)
        return redirect('/')


@csrf_exempt
@login_required(login_url='/admin/login/')
def discharge(request):
	if request.method == 'POST':
		id = request.POST.get('bed_id', None)
		if id:
			url = f'http://127.0.0.1:8000/api/bed/{id}/'
			r = requests.put(url)
			if r.status_code == 200:
				data = r.json()
				messages.success(request, f"<strong>Bed No:</strong> {data['id']}</br><strong>Status</strong>: {data['status']}<br><strong>Patient Name:</strong> {data['patient_name']}</br><strong>Alloted/Free Date:</strong> {data['alloted_on']}")
			elif r.status_code == 404:
				messages.info(request, f"Bed with the id : <strong>{id}</strong> not found")
		else:
			messages.info(request, 'Bed Id Required')
	else:
		messages.info(request, 'POST Method Required')

	context = {}
	if request.META.get('HTTP_REFERER', ''):
		return redirect(request.META['HTTP_REFERER'])
	return render(request, 'bed_management_system/index.html', context)


@csrf_exempt
@login_required(login_url='/admin/login/')
def allocatement(request):
	if request.method == 'POST':
		patient_name = request.POST.get('patient_name', None)
		bed_type = request.POST.get('bed_type', None)
		if bed_type and patient_name:
			url = f'http://127.0.0.1:8000/api/bed/'
			payload = { 'patient_name' : patient_name, 'type' : bed_type }
			r = requests.post(url, payload)
			print(r.status_code)
			if r.status_code == 200:
				data = r.json()
				messages.success(request, f"<strong>Bed No:</strong> {data['id']}</br><strong>Bed Type:</strong> {data['type']}</br><strong>Status</strong>: {data['status']}<br><strong>Patient Name:</strong> {data['patient_name']}</br><strong>Alloted/Free Date:</strong> {data['alloted_on']}")
			elif r.status_code == 404:
				messages.info(request, f"Bed with the id : <strong>{id}</strong> not found")
			elif r.status_code == 400:
				messages.info(request, f"Not available as of now")
		else:
			messages.info(request, 'Parameters Required')
	else:
		messages.info(request, 'POST Method Required')

	context = {}
	print("urls : ", request.META['HTTP_REFERER'])
	if request.META.get('HTTP_REFERER', ''):
		return redirect(request.META['HTTP_REFERER'])
	return render(request, 'bed_management_system/index.html', context)