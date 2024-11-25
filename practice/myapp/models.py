# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bills(models.Model):
    booking = models.ForeignKey('Booking', models.DO_NOTHING, blank=True, null=True)
    date_of_service = models.DateTimeField()
    service_car = models.ForeignKey('ServicesCar', models.DO_NOTHING, blank=True, null=True)
    spare_part_car = models.ForeignKey('SparePartsCar', models.DO_NOTHING, blank=True, null=True)
    service_moto = models.ForeignKey('ServicesMoto', models.DO_NOTHING, blank=True, null=True)
    spare_part_moto = models.ForeignKey('SparePartsMoto', models.DO_NOTHING, blank=True, null=True)
    total = models.TextField()  # This field type is a guess.
    manager = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    master = models.ForeignKey('Employees', models.DO_NOTHING, related_name='bills_master_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bills'


class Booking(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    service_centre = models.ForeignKey('ServiceCenters', models.DO_NOTHING, blank=True, null=True)
    type_of_transport = models.SmallIntegerField()
    service_car = models.ForeignKey('ServicesCar', models.DO_NOTHING, blank=True, null=True)
    service_moto = models.ForeignKey('ServicesMoto', models.DO_NOTHING, blank=True, null=True)
    master = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    date_of_order = models.DateTimeField()
    date_of_service = models.DateTimeField()
    total = models.TextField(blank=True, null=True)  # This field type is a guess.
    manager = models.ForeignKey('Employees', models.DO_NOTHING, related_name='booking_manager_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking'


class BookingStatistics(models.Model):
    stat_date = models.DateField(primary_key=True)
    bookings_amount = models.IntegerField(blank=True, null=True)
    bills_amount = models.IntegerField(blank=True, null=True)
    most_popular_service_car = models.TextField(blank=True, null=True)
    most_popular_service_moto = models.TextField(blank=True, null=True)
    total_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_statistics'


class Clients(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    client_surname = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_father_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    bonus_amount = models.IntegerField()
    spent_money = models.TextField()  # This field type is a guess.
    status = models.CharField(max_length=10)
    last_booking = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clients'


class CurrentCity(models.Model):
    center_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_city'


class Employees(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    age = models.SmallIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=100)
    salary = models.TextField()  # This field type is a guess.
    information = models.TextField(blank=True, null=True)
    center = models.ForeignKey('ServiceCenters', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Schedule(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    service_centre = models.ForeignKey('ServiceCenters', models.DO_NOTHING, blank=True, null=True)
    date_of_service = models.DateTimeField()
    slot = models.DurationField()
    is_available = models.BooleanField()
    booked_by = models.ForeignKey(Booking, models.DO_NOTHING, db_column='booked_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class ServiceCenters(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    index_number = models.IntegerField(blank=True, null=True)
    type_of_transport = models.SmallIntegerField()
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    amount_of_employees = models.SmallIntegerField()
    services = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'service_centers'


class ServicesCar(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    service_centre = models.ForeignKey(ServiceCenters, models.DO_NOTHING, db_column='service_centre', blank=True, null=True)
    spare_parts = models.ForeignKey('SparePartsCar', models.DO_NOTHING, db_column='spare_parts', blank=True, null=True)
    price = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'services_car'


class ServicesMoto(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    service_centre = models.ForeignKey(ServiceCenters, models.DO_NOTHING, db_column='service_centre', blank=True, null=True)
    spare_parts = models.ForeignKey('SparePartsMoto', models.DO_NOTHING, db_column='spare_parts', blank=True, null=True)
    price = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'services_moto'


class SparePartsCar(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    part_name = models.CharField(max_length=100)
    availability = models.ForeignKey(ServiceCenters, models.DO_NOTHING, db_column='availability', blank=True, null=True)
    price = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'spare_parts_car'


class SparePartsMoto(models.Model):
    id_number = models.SmallAutoField(primary_key=True)
    part_name = models.CharField(max_length=100)
    availability = models.ForeignKey(ServiceCenters, models.DO_NOTHING, db_column='availability', blank=True, null=True)
    price = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'spare_parts_moto'


class Spent(models.Model):
    sum = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'spent'


class Users(models.Model):
    id_number = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    pass_word = models.CharField(max_length=255)
    role_name = models.CharField(max_length=50)
    service_center = models.ForeignKey(ServiceCenters, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
