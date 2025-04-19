from django.shortcuts import render,redirect,get_object_or_404
from .models import MaqomlarModel,MaqomlarTuri
from .forms import MaqomlarModelForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def category_add_view(request):
    if request.method == "POST":
        value = request.POST.get('yangi-maqom-turi-qiymati')
        yangi_maqom = MaqomlarTuri(tur_nomi=value)
        yangi_maqom.save()
        print("helloooooooo")
        return redirect("create_product")


def BoshSahifaView(request):
    return render(request,"base.html")

@login_required(login_url='login')
def admin(request):
    return render(request,"admin/admin.html")

@login_required(login_url='login')
def admin_all_maqom(request):
    mahsulotlar = MaqomlarModel.objects.all()
    context = {
        "mahsulotlar":mahsulotlar
    }
    return render(request , "admin/all_product_admin.html" , context=context)

def Bycategory(request, category):
    # Kategoriyani topish
    try:
        category_obj = MaqomlarTuri.objects.get(tur_nomi=category)
    except MaqomlarTuri.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Kategoriya topilmadi!'})

    # Kategoriyaga tegishli ma'lumotlarni olish
    categories = MaqomlarModel.objects.filter(maqom_turi=category_obj)
    context = {
        'categories': categories,
        'category_name': category_obj.tur_nomi,  # Bosilgan kategoriya nomi
    }

    return render(request, 'barcha_mahsulotlar.html', context)



def MaqomTuriView(request, tur_nomi):
    maqomlar = MaqomlarModel.objects.filter(maqom_turi__tur_nomi=tur_nomi)
    context = {
        "maqomlar": maqomlar,
        "tur_nomi": tur_nomi,
    }
    return render(request, "maqom_turi_sahifa.html", context)


def BarchaMahsulotlarView(request):
    mahsulotlar = MaqomlarModel.objects.all()
    all_category = MaqomlarTuri.objects.all()
    context = {
        "mahsulotlar":mahsulotlar,
        'all_category':all_category
    }
    return render(request,"barcha_mahsulotlar.html",context=context)
   
@login_required(login_url='login')
def MaqomQoshishView(request):
    all_category = MaqomlarTuri.objects.all()
    
    if request.method == 'POST':
        tur = int(request.POST.get('turi'))  # Get the selected 'turi' value from the form
        
        form = MaqomlarModelForm(request.POST, request.FILES)
        
        if form.is_valid():
            maqom_instance = form.save(commit=False)  # Create the model instance without saving to the database
            maqom_instance.maqom_turi = MaqomlarTuri.objects.get(pk=tur)  # Assign the 'maqom_turi'
            maqom_instance.save()  # Save the instance to the database
            messages.success(request, "Maqom muvaffaqiyatli qo'shildi!")
            return redirect('admin_all')  # Redirect to the admin page
        else:
            messages.error(request, "Formada xatoliklar mavjud.")
    else:
        form = MaqomlarModelForm()  # Initial state of the form

    context = {
        "all_category": all_category,
        "form": form
    }
    return render(request, 'maqom_qoshish.html', context=context)


def MaqomOchirishView(request, id):
    maqom = get_object_or_404(MaqomlarModel, id=id)  # Maqomni olish
    if request.method == 'POST':
        maqom.delete()  # Maqomni o'chirish
        return redirect('admin_all')  # Maqomlar ro'yxatiga qaytish
    return render(request, 'maqom_ochirish.html', {'maqom': maqom})


def MaqomKorishView(request,id):
    maqomlar = get_object_or_404(MaqomlarModel,id=id)
    return render(request,"maqom_korish.html",{"maqomlar":maqomlar})

def delete_product(request, id):
    product = get_object_or_404(MaqomlarModel, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('barchamahsulotlar')
    return render(request, 'maqom_ochirish.html', {'product': product})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz.")
            return redirect('admin_all')  # Kirgandan keyin asosiy sahifaga yo'naltirish
        else:
            messages.error(request, "Login yoki parol noto'g'ri.")
    return render(request, 'admin/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "Tizimdan chiqdingiz.")
    return redirect('barchamahsulotlar')