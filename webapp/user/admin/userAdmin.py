from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('kakaoId',
                    'thumbnail_image',
                    'email',
                    'phone_number',
                    'name',
                    'birth_date',
                    'job',
                    'univ',
                    'major',
                    )
    # list_filter = ('',)
