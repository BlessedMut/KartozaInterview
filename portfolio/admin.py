from django.contrib import admin

from portfolio.models import Profiles


# Register Profiles model
@admin.register(Profiles)
class CustomUserAdmin(admin.ModelAdmin):
    """
    This class defines the layout of how rows will be displayed in our database in Django admin, this class takes
    a list of the required columns and in our case, we will include all the table fields.
    """
    list_display = ("username", "first_name", "last_name", "email", "address", "phone", "lat", "lon")
