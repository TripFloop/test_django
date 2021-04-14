from news_app.models import MenuItem


def context_menu(request):
    menu_items = MenuItem.objects.all()
    return {"menu_items": menu_items}
