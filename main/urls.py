from django.urls import path
from main.views import show_main, create_product, edit_product, show_html, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, delete_product, increment_amt, decrement_amt

app_name = 'main'

urlpatterns = [
    path('', show_main, name="show_main"),
    path('create-product', create_product, name='create_product'),
    path('edit-product/<int:id>/', edit_product, name='edit_product'),
    path('html/', show_html, name="show_html"),
    path('xml/', show_xml, name="show_xml"),
    path('json/', show_json, name="show_json"),
    path('xml/<int:id>/', show_xml_by_id, name="show_xml_by_id"),
    path('json/<int:id>/', show_json_by_id, name="show_json_by_id"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
    path('increment-amount/<int:id>/', increment_amt, name='increment_amount'),
    path('decrement-amount/<int:id>/', decrement_amt, name='decrement_amount'),
]