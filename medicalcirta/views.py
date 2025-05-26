
from django.http import JsonResponse
from django.shortcuts import render, redirect


from patient.models import Patient 
from docs.models import Docs 
from state.models import StateModel 
from operation.models import Operation 


def HomePage(request):
    if 'login' not in request.session:
        request.session['login'] = False

    return render(request, "index.html")



def LoginDoc(request):
    if 'logindoc' not in request.session:
        request.session['logindoc'] = False

    if request.session['logindoc'] == False:
        err_auth = False
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']

            obj = Docs.objects.filter(email=email, password=password)
            if obj.exists():
                request.session['logindoc'] = True
                request.session['id'] = obj[0].id
                return redirect('/doctor')
            else:
                err_auth = True

        return render(request, "login_doc.html", {"err_auth":err_auth})
    else:
        return redirect('/doctor')


def Login(request):
    if 'login' not in request.session:
        request.session['login'] = False

    if request.session['login'] == False:
        err_auth = False
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']

            obj = Patient.objects.filter(email=email, password=password)
            if obj.exists():
                request.session['login'] = True
                request.session['fullname'] = obj[0].fullname
                request.session['id'] = obj[0].id
                return redirect('/user')
            else:
                err_auth = True

        return render(request, "login.html", {"err_auth":err_auth})
    else:
        return redirect('/user')


def Signup(request):
    if 'login' not in request.session:
        request.session['login'] = False

    if request.session['login'] == False:
        success = False
        err_email = False
        err_password= False

        if request.method == "POST":
            
            fullname = request.POST['fullname']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            disease = request.POST['disease']
            detail = request.POST['detail']

            if password != cpassword or len(password) < 6:
                err_password = True
            
            else:
                #check if patient exist with the same email
                em = Patient.objects.filter(email=email)
                if em.exists():
                    err_email = True
                else:
                    npatient = Patient()
                    npatient.fullname = fullname
                    npatient.address = address
                    npatient.password = password
                    npatient.email = email
                    npatient.phone = phone
                    npatient.disease = disease
                    npatient.detail = detail
                    npatient.save()

                    success = True

        return render(request, "signup.html", {"success":success, 'err_psw':err_password, 'err_email':err_email})
    else:
        return redirect('/user')
    





def PatientHome(request):
    if "login" not in request.session:
        request.session['login'] = False

    if request.session['login'] == True:
        return render(request, "patient.html")
    else:
        return redirect('/')
    



def DoctorHome(request):
    if "logindoc" not in request.session:
        request.session['logindoc'] = False

    if request.session['logindoc'] == True:
        return render(request, "doctor.html")
    else:
        return redirect('/')
    

def WaitingList(request):
    if "logindoc" not in request.session:
        request.session['logindoc'] = False

    if request.session['logindoc'] == True:
        return render(request, "waitinglist.html")
    else:
        return redirect('/')
    
def DocMessage(request):
    if "logindoc" not in request.session:
        request.session['logindoc'] = False

    if request.session['logindoc'] == True:
        return render(request, "doc_msg.html")
    else:
        return redirect('/')
    

def Logout(request):
    request.session['login'] = False
    request.session['logindoc'] = False
    return redirect('/')



def Traitement(request):
    if "login" not in request.session:
        request.session['login'] = False

    if request.session['login'] == True:
        return render(request, "traitement.html")
    else:
        return redirect('/')
    

def Remission(request):
    if "login" not in request.session:
        request.session['login'] = False

    if request.session['login'] == True:
        return render(request, "remission.html")
    else:
        return redirect('/')
    
def Historique(request):
    if "login" not in request.session:
        request.session['login'] = False

    if request.session['login'] == True:
        return render(request, "historique.html")
    else:
        return redirect('/')
    

def Symp(request):
    if "login" not in request.session:
        request.session['login'] = False

    if request.session['login'] == True:
        return render(request, "symptoms.html")
    else:
        return redirect('/')
    



def PostState(request):
    if request.method == 'POST':
        poussee = request.POST.get('poussee')
        symp = request.POST.get('symp')
        aliments = request.POST.get('aliments')
        echo = request.POST.get('echo')
        coloscopie = request.POST.get('coloscopie')
        sang = request.POST.get('sang')
        iduser = request.session['id']

        st = StateModel()
        st.poussee = poussee
        st.symp = symp
        st.echo = echo
        st.regime = aliments
        st.coloscopie = coloscopie
        st.sang = sang
        st.iduser = iduser
        st.save()

        return JsonResponse({'done': True})
    
    return JsonResponse({'error': 'Méthode non autorisée'}, status=400)



def PostOperation(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        type = request.POST.get('type')
        detail = request.POST.get('detail')
        iduser = request.session['id']

        st = Operation()
        st.date = date
        st.type_operation = type
        st.detail = detail        
        st.iduser = iduser
        st.save()

        return JsonResponse({'done': True})
    
    return JsonResponse({'error': 'Méthode non autorisée'}, status=400)