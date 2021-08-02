"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

from django.views.generic.base import TemplateView

from django.conf.urls import handler400, handler403, handler404, handler500

# import model
from expenses.models import Expense



urlpatterns = [
    path("admin/", admin.site.urls),
    # Local apps URL Configuration
    path("", include("income.urls")),
    path("accounts/", include("accounts.urls")),
    path("expenses/", include("expenses.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Customizing-error-views
handler404 = "accounts.views.page_not_found_error"
handler500 = "accounts.views.page_error"
# handler403 = "accounts.views.error_403"
# handler400 = "accounts.views.error_400"
