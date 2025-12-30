from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'category', 'amount', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        }
        labels = {
            'type': 'Jenis Transaksi',
            'category': 'Kategori',
            'amount': 'Jumlah (Rp)',
            'date': 'Waktu Transaksi',  
        }