from django.shortcuts import render, redirect
from .models import Appointment


def booking(request):
    if request.method == 'POST':
        data = request.POST
        client_id = data.get('client_id')
        service_id = data.get('service_id')
        scheduled_date = data.get('scheduled_date')
        status = data.get('status')

        Appointment.objects.create(
            client_id=client_id,
            service_id=service_id,
            status=status,
            scheduled_date=scheduled_date,
        )
        return redirect('/booking/')

    queryset = Appointment.objects.all()
    context = {'booking': queryset}
    return render(request, 'clinic/booking.html', context)


def update_booking(request, id):
    queryset = Appointment.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        client_id = data.get('client_id')
        service_id = data.get('service_id')
        scheduled_date = data.get('scheduled_date')
        status = data.get('status')

        queryset.client_id = client_id
        queryset.status = status
        queryset.scheduled_date = scheduled_date
        queryset.service_id = service_id
        queryset.save()
        return redirect('/booking/')

    context = {'booking': queryset}
    return render(request, 'clinic/update_booking.html', context)


def delete_booking(request, ID):
    queryset = Appointment.objects.get(id=ID)
    queryset.delete()
    return redirect('/booking/')

