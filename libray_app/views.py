from django.shortcuts import render, redirect
from .models import *
from django.db.models import Sum
from datetime import date,datetime


def borrow(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        student = Student.objects.get(id=student_id)
        status = 'Borrowed'
        books_id = request.POST.getlist('select')
        for book_id in books_id:
            book = Book.objects.get(id=book_id)
            bo = Borrow(qty=1, status=status)
            bo.save()
            bo.student.add(student)
            bo.book.add(book)
            return redirect('borrow')

    student = Student.objects.all()
    books = Book.objects.all()

    data = []
    for book in books:
        left = Borrow.objects.filter(status='Borrowed', book__title=book.title).aggregate(Sum('qty'))
        if left['qty__sum'] is None:
            l = 0
        else:
            l = int(left['qty__sum'])
        data.append(book.available - l)

    context = {
        'student': student,
        'data': zip(books, data)

    }
    return render(request, 'borrow.html', context)


def returning(request):
    if request.method=="POST":
        b_id=int(request.POST['b_id'])
        bo=Borrow.objects.get(id=b_id)
        bo.date = datetime.now()
        bo.status='Returned'

        bo.save()
        return redirect('ren')
    borrow1=Borrow.objects.all()
    context={
     'b1':borrow1
    }

    return render(request,'return.html',context)
