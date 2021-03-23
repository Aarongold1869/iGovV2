from django.contrib import admin

# Register your models here.
from .models import *
    
class BillLikeAdmin(admin.TabularInline):
    model = BillLike

class BillDislikeAdmin(admin.TabularInline):
    model = BillDislike

class BillCommentAdmin(admin.TabularInline):
    model = BillComment

class BillAdmin(admin.ModelAdmin):
    inlines = [
        BillLikeAdmin,
        BillDislikeAdmin,
        BillCommentAdmin
    ]
    
    list_display = ['__str__', 'user_bill_author']
    search_fields = ['user__username',]
    class Meta:
        model = Bill
    
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
admin.site.register(Bill, BillAdmin)