from django.shortcuts import render,get_object_or_404,redirect
from .forms import LibroForm
from LibrosApp.models import Libros
from django.db.models import Q

def add(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            nuevo_libro = form.cleaned_data['nombre']
            nuevo_autor = form.cleaned_data['autor']
            nuevo_descripcion = form.cleaned_data.get('descripcion', '')
            nuevo_codigo = form.cleaned_data['codigo']
      

            nuevoproducto = Libros(
                nombre=nuevo_libro,
                autor=nuevo_autor,
                descripcion=nuevo_descripcion,
                codigo=nuevo_codigo,
                estado='A'
            )
            nuevoproducto.save()
            return render(request, 'agregar/crear_producto.html', {'form': LibroForm(), 'success': True})
    else:
        form = LibroForm()

    return render(request, 'agregar/crear_producto.html', {'form': form})




from django.shortcuts import redirect

def editar(request, libro_id):
    libro = get_object_or_404(Libros, id=libro_id)  # Obtiene el producto por su id
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)  # Pasar la instancia del producto al formulario
        if form.is_valid():
            form.save()  # Guardar los cambios en el producto existente
            return redirect('index')  # Redirige a la página de inicio
    else:
        form = LibroForm(instance=libro)  # Pasar la instancia del producto al formulario para mostrar los valores existentes

    return render(request, 'editar/edit.html', {'form': form, 'libro': libro})  # Pasar el producto al contexto de la plantilla


def cambiarEstado(request, libro_id):
    libro = Libros.objects.get(pk=libro_id)    
    if request.method == 'POST':
        libro.estado = 'i' 
        libro.save()
        return redirect("index")  
    form = LibroForm(instance=libro)
    return render(request, 'eliminar/eliminar.html', {
        'form': form,
        'libro': libro
    })


def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q')  # Obtener el valor de búsqueda del formulario
        # Realizar la búsqueda en la base de datos
        resultados = Libros.objects.filter(Q(nombre__icontains=query) | Q(codigo__icontains=query))
        context = {'resultados': resultados, 'query': query}
        return render(request, 'buscar/busqueda.html', context)

    return render(request, 'buscar/busqueda.html')
