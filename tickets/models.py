from django.db import models

TICKET_TYPES = [
    ('1', 'Programmer Pass - 15,000 MMK'),
    ('2', 'Tech Explorer - 30,000  MMK'),
    ('3', 'Digital Architect - 50,000 MMK'),
    ('4', 'IT Elite - 100,000 MMK')
]


class Ticket(models.Model):
    email = models.EmailField(null=False)
    name = models.CharField(max_length=256, null=False, default='Default Name')
    phone = models.CharField(max_length=20)
    screenshot = models.ImageField(
        upload_to='payment_screenshots/', blank=True, null=True)
    ticket_type = models.CharField(max_length=4, choices=TICKET_TYPES)
    coupon_code = models.CharField(
        max_length=20, blank=True, null=True)  # New coupon code field

    def save(self, *args, **kwargs):
        # Ensure that either coupon_code or screenshot is provided, but not both
        if not self.screenshot and not self.coupon_code:
            raise ValueError(
                'Either a screenshot or a coupon code must be provided.')
        if self.coupon_code:
            coupon = CouponCode.objects.get(code=self.coupon_code)
            if coupon.is_redeemed:
                raise ValueError('This coupon code has already been redeemed.')
            if coupon.ticket_type != self.ticket_type:
                raise ValueError(
                    'Coupon code is not valid for the selected ticket type.')
            coupon.is_redeemed = True  # Mark coupon as redeemed
            coupon.save()

        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.get_ticket_type_display()}'


class CouponCode(models.Model):
    code = models.CharField(max_length=20, unique=True)  # Coupon code field
    ticket_type = models.CharField(
        max_length=4, choices=TICKET_TYPES)  # Applicable ticket type
    # Flag to check if coupon is redeemed
    is_redeemed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    redeemed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.code} - {self.ticket_type}'

    class Meta:
        verbose_name = 'Coupon Code'
        verbose_name_plural = 'Coupon Codes'


class CustomDonation(models.Model):
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20)
    screenshot = models.ImageField(upload_to='payment_screenshots/')
    amount = models.CharField(max_length=12)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=96)
    account = models.TextField()
    description = models.TextField()
