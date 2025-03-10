from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(admin.ModelAdmin):
    exclude = ("groups", "user_permissions", "date_joined", "last_login")
    list_display = ("user_id", "email", "name")
    readonly_fields = ["user_id"]
    fieldsets = (
        (None, {"fields": ("user_id", "password", "name", "email", "work_time")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "user_id",
                    "name",
                    "password",
                    "email",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    ordering = ("email",)
    search_fields = ("email", "name")


admin.site.register(CustomUser, CustomUserAdmin)
