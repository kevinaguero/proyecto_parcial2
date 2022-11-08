from django.contrib.auth.decorators import permission_required
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from apps.vianda.forms import InfoSolicitudViandaForm
from apps.vianda.models import InfoSolicitudVianda


# Create your views here.

@permission_required('vianda.add_infosolicitudvianda',raise_exception=True)
def solicitud_vianda_create(request):
    nuevo_programa = None
    if request.method == 'POST':
        vianda_form = InfoSolicitudViandaForm(request.POST)
        if vianda_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nueva_vianda = vianda_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente la vianda {}'.format(nueva_vianda))
            return redirect(reverse('vianda:vianda_lista'))
    else:
        vianda_form = InfoSolicitudViandaForm()

    return render(request, 'vianda/vianda_form.html',
                  {'form': vianda_form})

@permission_required('vianda.view_infosolicitudvianda',raise_exception=True)
def vianda_lista(request):
    viandas = InfoSolicitudVianda.objects.all()
    return render(request, 'vianda/lista.html',
                  {'viandas': viandas})
