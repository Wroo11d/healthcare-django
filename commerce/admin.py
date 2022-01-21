from django.contrib import admin

from commerce.models import (

    Doctor, Hospital, DoctorCategory, HospitalCategory,HospitalType,DoctorType
)
"""class InlineProductImage(admin.TabularInline):
    model = ProductImage"""


"""class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductImage,]
    list_display = ('id', 'name', 'qty', 'description', 'cost', 'price', 'discounted_price')
    list_filter = ('category', 'label', 'merchant', 'vendor')
    search_fields = ('name', 'qty', 'description', 'cost', 'price', 'discounted_price', 'merchant__name')
"""

admin.site.register(Doctor)
admin.site.register(DoctorCategory)
admin.site.register(HospitalCategory)
admin.site.register(Hospital)
admin.site.register(HospitalType)
admin.site.register(DoctorType)
