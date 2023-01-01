from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from app import views
from .forms import Password_change,User_login
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),

    path('accounts/login/',auth_views.LoginView.as_view(template_name="pages/login.html",authentication_form=User_login),name="login"),
    path('changepass/',auth_views.PasswordChangeView.as_view(template_name="pages/changepass.html",form_class=Password_change,success_url='/donepass/'),name="passchange"),
    path('do^ne^pa^ss/',views.done_pass,name="donepass"),


    path('accounts/profile/',views.user_profile,name='profile'),
    path('address/',views.address_page,name='address'),
    # path('update/<int:id>',views.update,name='update'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name="logout"),
    path('cart/',views.user_cart,name="cart"),
    path('showcart/',views.show_cart,name="showcart"),
    path('nocart/',views.no_cart,name="nocart"),
    path('plus/',views.plus_cart),
    path('minus/',views.minus_cart),
    path('remove/',views.remove_cart),
    path('product-detail/<int:id>',views.product_detail,name="product-detail"),
    path('info/',views.info,name="info"),
    path('m^o^bm^o^b/',views.mobile,name="mobile"),
    path('m^o^bm^o^b/<slug:item>',views.mobile,name="mobile-item"),
    path('r^ce^nt',views.recent_search,name="recent_search"),
    path('checkout1/',views.check_out,name="check-out"),
    path('payment/',views.payment_done,name="payment"),
    path('order/',views.my_order,name="order"),

    # path('prfile/',views.user_profile,name="mobile-item"),
] 

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
