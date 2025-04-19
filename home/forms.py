# forms.py
from django import forms
from .models import MaqomlarModel, MaqomlarTuri

class MaqomlarModelForm(forms.ModelForm):
    class Meta:
        model = MaqomlarModel
        fields = ['maqom_nomi', 'ijrochi_surati', 'maqom_sozlari', 'maqom_ijrochisi']
        widgets = {
            'maqom_nomi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maqom nomini kiriting...'}),
            'maqom_sozlari': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Maqom so‘zlarini kiriting...'}),
            'maqom_ijrochisi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maqom ijrochisini kiriting...'}),
            'ijrochi_surati': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
    def __init__(self, *args, **kwargs):
        # Remove 'maqom_turi' from kwargs and store it
        maqom_turi = kwargs.pop('maqom_turi', None)
        super().__init__(*args, **kwargs)  # Call the parent constructor

        # Optionally, use maqom_turi if needed (e.g., for validation or defaults)
        self.maqom_turi = maqom_turi
        
    # Maqom turi tanlashda yangi kategoriya qo'shish imkoniyati
    def clean_maqom_turi(self):
        tur_nomi = self.cleaned_data.get('maqom_turi')
        
        # Agar tanlangan kategoriya bo'lmasa va yangi kategoriya kiritilgan bo'lsa
        if not tur_nomi:
            yangi_kategoriya = self.cleaned_data.get('yangi_kategoriya')
            if yangi_kategoriya:
                # Yangi kategoriya mavjudligini tekshiramiz
                if not MaqomlarTuri.objects.filter(tur_nomi=yangi_kategoriya).exists():
                    kategoriya = MaqomlarTuri.objects.create(tur_nomi=yangi_kategoriya)
                else:
                    kategoriya = MaqomlarTuri.objects.get(tur_nomi=yangi_kategoriya)
                return kategoriya
        return tur_nomi
