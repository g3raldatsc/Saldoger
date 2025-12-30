from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum  
from .models import Transaction
from .forms import TransactionForm

@login_required
def transaction_list(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    # Ambil data transaksi
    
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    # Total Pemasukan dan Pengeluaran
    # aggregate(Sum('amount')) akan menghasilkan dictionary, misal: {'amount__sum': 50000}
    # Saya pakai 'or 0' supaya kalau tidak ada data, nilainya jadi 0 (bukan None/Error)
    
    total_income = transactions.filter(type='IN').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(type='OUT').aggregate(Sum('amount'))['amount__sum'] or 0

    # Hitung Saldo
    saldo = total_income - total_expense

    return render(request, 'tracker/transaction_list.html', {
        'form': form,
        'transactions': transactions,
        'total_income': total_income,   # Kirim data ke HTML
        'total_expense': total_expense, # Kirim data ke HTML
        'saldo': saldo
    })