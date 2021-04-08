from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser

# from .forms import UserCreationForm, UserChangeForm

class CustomUserAdmin(UserAdmin):

	model = CustomUser
	list_display = ('email', 'is_staff', 'is_active',)

	filter_horizontal = ()
	list_filter       = ()
	filter_horizontal = ()
	# fieldsets = (
	#     (None, {'fields': ('email', 'password')}),
	#     ('Permissions', {'fields': ('is_staff', 'is_active')}),
	# )
	# add_fieldsets = (
	#     (None, {
	#         'classes': ('wide',),
	#         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
	#     ),
	# )
	# search_fields = ('email',)
	ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
