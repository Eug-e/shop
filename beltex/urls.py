from django.urls import path
from beltex.views import index
from beltex.views import Ver
from beltex.views import ex41
from beltex.views import login_user
from beltex.views import log_out
from beltex.views import Form
from beltex.views import Ajax_path
from beltex.views import Aja
from beltex.views import back
from beltex.views import Costs
from beltex.views import Spec
from django.conf import settings
from django.conf.urls.static import static
from beltex.views import Obj
from beltex.views import contacts
from beltex.views import cost
from beltex.views import Reg
from beltex.views import guest
from beltex.views import inbox
from beltex.views import spec_upd
from beltex.views import upload

urlpatterns = [
    path('line1', index),
    path('line3', Ver),
    path('line4', ex41),
    path('line6', login_user),
    path('line7', log_out),
    path('line8', Reg),
    path('line10', Form),
    path('line11', Ajax_path),
    path('line12', Aja),
    path('line13', back),
    path('line14', Costs),
    path('line15', Spec),
    path('line16', Obj),
    path('line17', contacts),
    path('cost', cost),
    path('home', guest),
    path('inbox_message', inbox),
    path('get_specialist', spec_upd),
    path('upload', upload),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
