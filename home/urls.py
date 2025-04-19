from django.urls import path
from . import views

urlpatterns = [
    # Bosh sahifa uchun URL
    path("base/", views.BoshSahifaView, name="boshsahifa"),  # Bosh sahifa
    path("ad/", views.admin, name="admin"), 
    path('admin/', views.admin_all_maqom , name="admin_all"),
    # Barcha mahsulotlar sahifasi
    path("", views.BarchaMahsulotlarView, name="barchamahsulotlar"),  # Barcha mahsulotlar

    # Maqomni o'chirish
    path('maqom/ochirish/<int:id>/', views.MaqomOchirishView, name='maqom_ochirish'),

    # Maqomni ko'rish
    path("korish/<int:id>/", views.MaqomKorishView, name="maqom_korish"),
    path('category/<str:category>/', views.Bycategory, name='Bycategory'),
    path('create/', views.MaqomQoshishView, name='create_product'),
    # login/logout
    path("logout/",views.logout_view,name="logout"),
    path("login/",views.login_view,name="login"),

    # Maqom turlari uchun URL'lar
    path("buzruk/", views.MaqomTuriView, name="buzruk"),  # Buzruk maqomlari
    path("rost/", views.MaqomTuriView, name="rost"),      # Rost maqomlari
    path("navo/", views.MaqomTuriView, name="navo"),      # Navo maqomlari
    path("dugoh/", views.MaqomTuriView, name="dugoh"),    # Dugoh maqomlari
    path("segoh/", views.MaqomTuriView, name="segoh"),    # Segoh maqomlari
    path("iroq/", views.MaqomTuriView, name="iroq"),      # Iroq maqomlari
    path("category_add_view" , views.category_add_view , name="category_add_view")
]
