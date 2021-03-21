from django.contrib import admin

# Register your models here.
from .models import *

# class Bill (admin.TabularInline):
#     model = PostShare
    
# class PostLikeAdmin(admin.TabularInline):
#     model = PostLike

# class PostAdmin(admin.ModelAdmin):
#     inlines = [
#         PostLikeAdmin,
#         PostShareAdmin,
#     ]
    
#     list_display = ['__str__', 'user']
#     search_fields = ['user__username', 'user__email', 'content']
#     class Meta:
#         model = Post
    
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Locality)
admin.site.register(Address)
admin.site.register(RepresentativeTitle)
admin.site.register(Party)
admin.site.register(BillAuthor)
admin.site.register(UserBillAuthor)
admin.site.register(Subsection)
admin.site.register(BillType)
admin.site.register(Bill)