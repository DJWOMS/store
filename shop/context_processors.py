from .models import Category


def list_categoryes(request):
    """Список категорий в меню"""
    return {"menu_categoryes": Category.objects.all()}
