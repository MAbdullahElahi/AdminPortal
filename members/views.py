from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from . import models
from django.urls import reverse
from . import data
import json
from datetime import date

# Create your views here.
@login_required
def index(req):
    user = req.user
    
    if user.is_authenticated:
        sales = data.get_sales_data(user.username)
        try:
            total_amount = sum(sale['Amount'] for sale in sales if sale['Status'])
        except: total_amount = 0
        
            
        return render(req, 'index.html', {"sales": sales, "total_amount":total_amount, "user": user})
               
    return render(req, 'index.html', {})

def login_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(req, user)
            messages.success(req, f"Successfully Logged in as {username}")
            return redirect("/")
        else: 
            messages.error(req, f"Invalid Credentials OR no user found with username {username}")
            return redirect("/")
        
    else:
        return HttpResponse("""<h1>Method NOT Allowed</h1><br><h2>Error 405</h2>""")


@login_required
def addSale(req):
    if req.method == "POST":
        name = req.POST.get('name', '')
        holder_name = req.POST.get('holder_name', '')
        contact_num = req.POST.get('contact_num', '').strip()
        contact_num = contact_num if contact_num else '0000000000'  # Provide a default value if empty
        location = req.POST.get('location', '')
        assignment = req.POST.get('assignment', '')
        amount = req.POST.get('amount', '0.0')
        try:
            amount = float(amount)  # Ensure amount is a float
        except ValueError:
            amount = 0.0
        date_value = req.POST.get('date', '')
        date_value = date_value if date_value else None  # Handle empty date
        date_completed = req.POST.get('date_complete', str(date.today()))  # Provide today's date as default
        account_num = req.POST.get('account_num', '0000000')
        socials = req.POST.get('socials', '{}')  # Default to empty JSON object

        # Convert socials to a valid JSON object if it's a string
        try:
            socials = json.loads(socials) if socials != '{}' else {}
        except json.JSONDecodeError:
            socials = {"socials": "empty"}  # Default to empty JSON object on error

        # Use .get() to avoid MultiValueDictKeyError
        status = req.POST.get('status', False)
        status = True if status == 'on' else False  # Checkbox value handling

        sales_data = {
            "Name": name,
            "Holder": holder_name,
            "ContactNumber": contact_num,
            "Location": location,
            "Assignment": assignment,
            "Amount": amount,
            "Date": date_value,
            "DateComplete": date_completed,
            "AccountNumber": account_num,
            "Socials": socials,
            "Status": status
        }

        try:
            sale = models.Sales(**sales_data)  # Ensure you're using the correct model
            sale.save()
            print("Data saved successfully")  # Log success message
            return redirect("/")
        except Exception as e:
            print(f"Error: {str(e)}")  # Log the error message
            return HttpResponse(f"Error: {str(e)}")

    return HttpResponse(sales_data)

@login_required
def updateSale(req):
    if req.method == 'POST':
        # Retrieve data from POST request
        record_id = req.POST.get('record_id')
        record_name = req.POST.get('record_name')
        record_holder_name = req.POST.get('record_holder_name')
        record_contact_num = req.POST.get('record_contact_num')
        record_location = req.POST.get('record_location')
        record_assignment = req.POST.get('record_assignment')
        record_amount = req.POST.get('record_amount')
        record_date = req.POST.get('record_date')
        record_date_completed = req.POST.get('record_date_completed')
        record_account_num = req.POST.get('record_account_num')
        record_socials = req.POST.get('record_socials')
        
        # Handle checkbox for status
        record_status = req.POST.get('record_status', False)  # Default value if not present
        record_status = True if record_status == 'on' else False  # Convert to boolean

        try:
            sale = models.Sales.objects.get(id=record_id)
            sale.Name = record_name
            sale.Holder = record_holder_name
            sale.ContactNumber = record_contact_num
            sale.Location = record_location
            sale.Assignment = record_assignment
            sale.Amount = record_amount
            sale.Date = record_date
            sale.DateComplete = record_date_completed
            sale.AccountNumber = record_account_num
            sale.Socials = {'socials': record_socials}  # Assuming Socials is a JSONField
            sale.Status = record_status
            sale.save()

            return redirect('/')  # Redirect to success page
        except models.Sales.DoesNotExist:
            return HttpResponse("Sale record not found.")
        except Exception as e:
            return HttpResponse(f"Error updating sale: {str(e)}")

    return HttpResponse("Method not allowed.")


@login_required
def deleteSale(req):
    if req.method == 'POST':
        record_id = req.POST.get('record_id_to_delete')
        
        sale = get_object_or_404(models.Sales, pk=record_id)        
        
        sale.delete()
        
        return redirect('/')
        

def logout_user(req):
    logout(req)
    messages.success(req, "Successfully logged out.")
    return redirect("/")











