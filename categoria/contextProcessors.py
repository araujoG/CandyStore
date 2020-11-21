from categoria.models import Categoria

def categorias(request):
    categorias = Categoria.objects.all()

    return {
        'listaCategorias': categorias ,
    }