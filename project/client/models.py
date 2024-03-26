from django.db import models


class Country(models.Model):
    id_country = models.IntegerField(primary_key=True, verbose_name='id_country')
    country_name = models.CharField(max_length=255)

    class Meta:
        __name__ = 'client'


class City(models.Model):
    id_city = models.IntegerField(primary_key=True, verbose_name='id_city')
    city_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        __name__ = 'city'


class Street(models.Model):
    id_street = models.IntegerField(primary_key=True, verbose_name='id_street')
    street_name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        __name__ = "street"


class PostCode(models.Model):
    id_post_code = models.IntegerField(primary_key=True, verbose_name='id_post_code')
    post_code = models.CharField(max_length=90)

    class Meta:
        __name__ = 'post_code'


class Address(models.Model):
    id_address = models.IntegerField(primary_key=True, verbose_name='id_address')
    id_street = models.ForeignKey(Street, on_delete=models.CASCADE)
    door_number = models.IntegerField()
    postcode = models.ForeignKey(PostCode, on_delete=models.CASCADE)
    client = models.OneToOneField('Client', on_delete=models.CASCADE)

    class Meta:
        __name__ = 'address'


class Client(models.Model):
    id_client = models.IntegerField(primary_key=True, verbose_name='id_client')
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=15)
    email = models.EmailField()
    birth_date = models.DateField()
    active = models.BooleanField()

    class Meta:
        __name__ = 'client'


class ClientType(models.Model):
    id_client_type = models.IntegerField(primary_key=True, verbose_name='id_client_type')
    type_name = models.CharField(max_length=255)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    class Meta:
        __name__ = 'client_type'


class ServiceType(models.Model):
    id_service_type = models.IntegerField(primary_key=True, verbose_name='id_service_type')
    service_name = models.CharField(max_length=150)

    class Meta:
        __name__ = 'service_type'


class Service(models.Model):
    id_service = models.IntegerField(primary_key=True, verbose_name='id_client')
    service_name = models.CharField(max_length=150)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    current_service_price_money = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        __name__ = 'service'


class ClientService(models.Model):
    id_client_service = models.IntegerField(primary_key=True, verbose_name='id_client_service')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_date = models.DateField()

    class Meta:
        __name__ = 'client_service'


class Package(models.Model):
    id_package = models.IntegerField(primary_key=True, verbose_name='id_package')
    package_name = models.CharField(max_length=150)
    current_package_price_money = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField()

    class Meta:
        __name__ = 'package'


class ClientPackage(models.Model):
    id_client_package = models.IntegerField(primary_key=True, verbose_name='id_client_package')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField()

    class Meta:
        __name__ = 'client_package'


class PackageService(models.Model):
    id_package_service = models.IntegerField(primary_key=True, verbose_name='id_package_service')
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        __name__ = 'package_service'


class InvoiceService(models.Model):
    id_invoice_service = models.IntegerField(primary_key=True, verbose_name='id_invoice_service')
    client_service = models.ForeignKey(ClientService, on_delete=models.CASCADE)
    final_service_price_money = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        __name__ = 'invoice_service'


class InvoicePackage(models.Model):
    id_invoice_package = models.IntegerField(primary_key=True, verbose_name='id_invoice_package')
    client_package = models.ForeignKey(ClientPackage, on_delete=models.CASCADE)
    final_package_price_money = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        __name__ = 'invoice_package'


class PackagePromotion(models.Model):
    id_package_promotion = models.IntegerField(primary_key=True, verbose_name='id_package_promotion')
    discount_code = models.CharField(max_length=255)
    active = models.BooleanField()

    class Meta:
        __name__ = 'package_promotion'


class PackagePromotionPackage(models.Model):
    id_package_promotion_package = models.IntegerField(primary_key=True, verbose_name='id_package_promotion_package')
    package_promotion = models.ForeignKey(PackagePromotion, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    class Meta:
        __name__ = ' package_promotion_package'


class ServicePromotion(models.Model):
    id_service_promotion = models.IntegerField(primary_key=True, verbose_name='id_service_promotion')
    discount_code = models.CharField(max_length=255)
    active = models.BooleanField()

    class Meta:
        __name__ = 'service_promotion'


class ServicePromotionService(models.Model):
    id_service_promotion_service = models.IntegerField(primary_key=True, verbose_name='id_service_promotion_service')
    service_promotion = models.ForeignKey(ServicePromotion, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        __name__ = 'service_promotion_service'


# Assuming there are loyalty program tables for client services and packages.
class ClientServiceLoyalty(models.Model):
    id_client_service_loyalty = models.IntegerField(primary_key=True, verbose_name='id_client_service_loyalty')
    client_service = models.ForeignKey(ClientService, on_delete=models.CASCADE)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField()

    class Meta:
        __name__ = 'client_service_loyalty'


class ClientPackageLoyalty(models.Model):
    id_client_package_loyalty = models.IntegerField(primary_key=True, verbose_name='id_client_package_loyalty')
    client_package = models.ForeignKey(ClientPackage, on_delete=models.CASCADE)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField()

    class Meta:
        __name__ = 'client_package_loyalty'
