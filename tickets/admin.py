from django.contrib import admin
from .models import *
from django.utils import timezone


class CouponCodeAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('code', 'ticket_type', 'is_redeemed',
                    'created_at', 'redeemed_at')
    search_fields = ('code',)  # Enable search by code
    # Enable filtering by ticket type and redemption status
    list_filter = ('ticket_type', 'is_redeemed')
    # Make timestamps read-only
    readonly_fields = ('created_at', 'redeemed_at')

    # Optionally, if you want to handle auto-redeem when editing:
    def save_model(self, request, obj, form, change):
        if obj.is_redeemed and not obj.redeemed_at:
            # Auto-fill redeemed_at timestamp when coupon is redeemed
            obj.redeemed_at = timezone.now()
        super().save_model(request, obj, form, change)


admin.site.register(CouponCode, CouponCodeAdmin)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('email', 'name', 'phone', 'ticket_type',
                    'screenshot', 'get_ticket_type_display')

    # Add a search box for specific fields
    search_fields = ('email', 'phone', 'ticket_type')

    # Add filter options on the right
    list_filter = ('ticket_type',)

    # Fieldsets to group fields in the detail view
    fieldsets = (
        ('Contact Information', {
            'fields': ('email', 'name', 'phone',)
        }),
        ('Ticket Details', {
            'fields': ('ticket_type', 'screenshot')
        }),
    )

    # Ordering by email
    ordering = ('email',)


@admin.register(CustomDonation)
class CustomDonationAdmin(admin.ModelAdmin):

    # Fields to display in the list view
    list_display = ('email', 'phone', 'amount', 'screenshot')

    # Add a search box for specific fields
    search_fields = ('email', 'phone', 'amount')

    # Fieldsets to group fields in the detail view
    fieldsets = (
        ('Contact Information', {
            'fields': ('email', 'phone')
        }),
        ('Donation Details', {
            'fields': ('amount', 'screenshot')
        }),
    )

    # Ordering by email
    ordering = ('email',)


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'account', 'description')

    # Add a search box for name and account
    search_fields = ('name', 'account')

    # Fieldsets to group fields in the detail view
    fieldsets = (
        ('Payment Information', {
            'fields': ('name', 'account', 'description')
        }),
    )

    # Ordering by name
    ordering = ('name',)
