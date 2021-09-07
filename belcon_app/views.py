from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from . models import *
from django.contrib import messages
import bcrypt
import base64

def index(request):
    return render(request, 'form.html')

def success(request):
    return render(request, 'success.html')

def create_profile(request):
    if request.method == "POST":
        expiry_date = ''
        phone_f3 = request.POST['field3_p1']
        phone_m3 = request.POST['field3_p2']
        phone_l4 = request.POST['field3_p3']
        phone_number_formatted = f'{phone_f3}-{phone_m3}-{phone_l4}'
        orignal_social = request.POST['field5']
        formated_social = f'{orignal_social[0]}{orignal_social[1]}{orignal_social[2]}-{orignal_social[3]}{orignal_social[4]}-{orignal_social[5]}{orignal_social[6]}{orignal_social[7]}{orignal_social[8]}'
        message = formated_social
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        if request.POST['field41'] == '' or request.POST['field41'] == "":
            expiry_date = '2090-01-01'
        else:
            expiry_date = request.POST['field41']
        new_employee = UserDetails.objects.create(
            start_date=request.POST['field0'], 
            first_name=request.POST['field1'], 
            middle_initial=request.POST['minitial'], 
            last_name=request.POST['lastname'], 
            date_of_birth=request.POST['field2'], 
            cell_phone= phone_number_formatted,
            email=request.POST['field4'], 
            social_security=base64_message, 
            street=request.POST['field6'], 
            city=request.POST['field7'], 
            state=request.POST['field8'], 
            zip_code=request.POST['field9'], 
            ubic_number=request.POST['field10'], 
            union=request.POST['field11'], 
            local=request.POST['field12'], 
            position=request.POST['field13'], 
            gender=request.POST['field14'], 
            company_anti_discrimination_policy=request.POST['field15'], 
            consent_for_anti_discrimination=request.POST['field16'], 
            direct_deposit_option=request.POST['field17'], 
            bank_name=request.POST['field18'], 
            routing_number=request.POST['field19'], 
            account_number=request.POST['field20'], 
            w4filing_status=request.POST['field21'], 
            total_number_allowances=request.POST['field22'], 
            step2=request.POST['field23'], 
            step3_a=request.POST['field24'], 
            step3_b=request.POST['field25'], 
            step3c_total=request.POST['field26'], 
            step4_a=request.POST['field27'], 
            step4_b=request.POST['field28'], 
            step4_c=request.POST['field29'], 
            step2b1=request.POST['field30'], 
            step2b2a=request.POST['field31'], 
            step2b2b=request.POST['field32'], 
            step2b2c=request.POST['field100'], 
            step2b3=request.POST['field101'], 
            step2b4=request.POST['field33'], 
            step4b1=request.POST['field34'], 
            step4b2=request.POST['field35'], 
            step4b3=request.POST['field36'], 
            step4b4=request.POST['field37'], 
            step4b5=request.POST['field38'], 
            immigration_status=request.POST['field39'], 
            alien_restriation_number=request.POST['field40'], 
            expiry_date=expiry_date, 
            alien_restriation_number2=request.POST['field42'],
            form_admission_number=request.POST['field43'], 
            foreign_passport_number=request.POST['field44'],
            direct_deposit_check=request.FILES.get('direct_deposit_check', None),
            id_1=request.FILES.get('id_1', None),
            id_2=request.FILES.get('id_2', None),
            signature=request.POST['signature'])
        return redirect('/success')
    else:
        return redirect('/')   


def show(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'employee': UserDetails.objects.all(),
        # 'view_current': UserDetails.objects.filter(id=id),
    }
    return render(request, 'show.html', context)

def view(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    my_profile = UserDetails.objects.filter(id=id)
    my_social = my_profile[0].social_security
    base64_message_c = my_social
    base64_bytes_c = base64_message_c.encode('ascii')
    message_bytes_c = base64.b64decode(base64_bytes_c)
    message_c = message_bytes_c.decode('ascii')
    context = {
    'view_social': message_c,
    'view_current': UserDetails.objects.filter(id=id)  
    }
    return render(request, 'view.html', context)

def delete(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        UserDetails.objects.get(id=id).delete()
        return redirect('/show')

def login_page(request):
    if 'user_id' in request.session:
        return redirect('/show')
    else:
        return render(request, 'login.html')    

def register_page(request):
    if 'user_id' in request.session:
        return redirect('/show')
    else:
        return render(request, 'register.html')      


def register(request):
    if request.method == 'POST':
        errors = Employer.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register_page')
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        if Employer.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Email already exists')
            return redirect('/register_page')
        new_user = Employer.objects.create(email=request.POST['email'], password=pw_hash)
        # request.session['name'] = new_user.first_name
        request.session['user_id'] = new_user.id
        return redirect('/login_page')
    return redirect('/register_page')

def login(request):
    if request.method == 'POST':
        logged_user = Employer.objects.filter(email=request.POST['email'])
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['email'] = logged_user.email
                request.session['user_id'] = logged_user.id
            return redirect('/show')
        if not Employer.objects.filter(email=request.POST['email'], password=request.POST['password']):
            print('Invalid login')
            messages.error(request, "Invalid login details")
            return redirect('/login_page')
    return redirect('/login_page')    


def logout(request):
    request.session.flush()
    request.session.clear()
    return redirect('/')    