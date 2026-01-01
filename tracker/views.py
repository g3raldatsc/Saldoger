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

    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    total_income = transactions.filter(type='IN').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(type='OUT').aggregate(Sum('amount'))['amount__sum'] or 0
    
    saldo = total_income - total_expense

    context = {
        'transactions': transactions,
        'form': form,
        'total_income': total_income,
        'total_expense': total_expense,
        'saldo': saldo
    }
    return render(request, 'tracker/transaction_list.html', context)

# fitur reset  data (01/01/2026)

def reset_data(request):
    Transaction.objects.all().delete()
    return redirect('transaction_list')