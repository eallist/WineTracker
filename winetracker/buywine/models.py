from django.contrib.auth.models import User
from django.db import models


class Wine(models.Model):
    VINTAGE_TYPE_CHOICES = (('S', 'Single Year'), ('M', 'Mixed Vintage'))
    SWEET_OR_DRY_CHOICES = (('SWT', 'Sweet'), ('SSWT', 'Semi-Sweet'), ('SDRY', 'Semi-Dry'), ('DRY', 'Dry'),
                            ('DSRT', 'Dessert'))

    varietal = models.ForeignKey('buywine.Varietal')
    sweet_or_dry = models.CharField(null=True, blank=True, max_length=4, choices=SWEET_OR_DRY_CHOICES)
    residual_sugar = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    winery = models.ForeignKey('buywine.Winery', null=False, blank=False)
    vintner = models.ForeignKey('buywine.Vintner', null=True, blank=True)  # if different from winery
    vineyard = models.ForeignKey('buywine.Vineyard', null=True, blank=True)
    vintage_type = models.CharField(max_length=1, null=False, blank=False, choices=VINTAGE_TYPE_CHOICES)
    vintage_year = models.IntegerField(null=False, blank=False)
    created_on = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    created_by = models.ForeignKey(User, null=False, blank=True, related_name='wine_created_by')
    updated_on = models.DateTimeField(null=False, blank=True, auto_now=True)
    updated_by = models.ForeignKey(User, null=False, blank=True, related_name='wine_updated_by')

    class Meta:
        db_table = 'wt_wine'
        unique_together = ('varietal', 'winery', 'vineyard', 'vintage_year')
        ordering = ['varietal', 'vintage_year', 'winery']

    def __unicode__(self):
        desc = '{winery} {varietal} {vintage_year} {vintage_type}'.format(
            winery=self.winery, varietal=self.varietal, vintage_year=self.vintage_year,
            vintage_type=self.vintage_type if self.vintage_type == 'M' else '')
        return unicode(desc)


class Bottle(models.Model):
    wine = models.ForeignKey('buywine.wine')
    date_purchased = models.DateField()
    quantity = models.IntegerField(null=False, blank=False, default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'wt_bottle'
        ordering = ['wine', 'date_purchased', 'price']

    def __unicode__(self):
        desc = '{wine} {date} {price}'.format(wine=self.wine, date=self.date_purchased, price=self.price)


class Varietal(models.Model):
    varietal_name = models.CharField(max_length=255, default='', unique=True)
    varietal_desc = models.TextField(default='', null=True, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'wt_varietal'
        ordering = ['varietal_name']

    def __unicode__(self):
        return unicode(self.varietal_name)


class Winery(models.Model):
    winery_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    winery_address = models.ForeignKey('buywine.WineryAddress', null=True, blank=True)
    winery_phone = models.CharField(max_length=40, null=True, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'wt_winery'
        verbose_name_plural = 'Wineries'
        ordering = ['winery_name']

    def __unicode__(self):
        return unicode(self.winery_name)


class WineryComment(models.Model):
    winery = models.ForeignKey('buywine.Winery', null=False, blank=False)
    comment_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    comment_user = models.ForeignKey(User, null=False, blank=True)
    comment = models.TextField(default='')

    class Meta:
        db_table = 'wt_winery_comments'
        ordering = ['winery', 'comment_date']


class WineryVintner(models.Model):
    winery = models.ForeignKey('buywine.Winery', null=False, blank=False)
    vintner = models.ForeignKey('buywine.Vintner', null=False, blank=False)

    class Meta:
        db_table = 'wt_map_winery_vintner'
        unique_together = ('winery', 'vintner')
        ordering = ['winery', 'vintner']


class Vintner(models.Model):
    last_name = models.CharField(max_length=255, default='', blank=True)
    first_name = models.CharField(max_length=255, default='', blank=False)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'wt_vintner'
        unique_together = ('last_name', 'first_name')
        ordering = ['last_name', 'first_name']


    def __unicode__(self):
        return unicode('{first_name} {last_namee'.format(first_name=self.first_name, last_name=self.last_name))


class VintnerComment(models.Model):
    vintner = models.ForeignKey('buywine.Vintner', null=False, blank=False)
    comment_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    comment_user = models.ForeignKey(User, null=False, blank=True)
    comment = models.TextField(default='')

    class Meta:
        db_table = 'wt_vintner_comments'
        ordering = ['vintner', 'comment_date']


class WineryVineyard(models.Model):
    winery = models.ForeignKey('buywine.Winery', null=False, blank=False)
    vineyard = models.ForeignKey('buywine.Vineyard', null=False, blank=False)


    class Meta:
        db_table = 'wt_map_winery_vineyard'
        unique_together = ('winery', 'vineyard')
        ordering = ['winery', 'vineyard']


class Vineyard(models.Model):
    vineyard_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    vineyard_address = models.ForeignKey('buywine.VineyardLocation', null=True, blank=True)
    vineyard_location_desc = models.TextField(null=False, blank=False)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'wt_vineyard'
        ordering = ['vineyard_name']

    def __unicode__(self):
        return unicode(self.vineyard_name)


class VineyardComment(models.Model):
    vineyard = models.ForeignKey('buywine.Vineyard')
    comment_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    comment_user = models.ForeignKey(User, null=False, blank=True)
    comment = models.TextField(default='')

    class Meta:
        db_table = 'vineyard_comments'
        ordering = ['vineyard', 'comment_date']


class WineryAddress(models.Model):
    address_line_1 = models.TextField(null=True, blank=True)
    address_line_2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.ForeignKey('buywine.State', null=True, blank=True)
    province = models.ForeignKey('buywine.Province', null=True, blank=True)
    country = models.ForeignKey('buywine.Country', null=False, blank=False)
    zip_code = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        db_table = 'wt_winery_address'
        verbose_name_plural = 'Winery Addresses'
        unique_together = ('address_line_1', 'address_line_2', 'city', 'state', 'province', 'country', 'zip_code')

    def __unicode__(self):
        addy = '{addy1} {addy2} {city} {state} {province} {country} {zip}'.format(
            addy1='{0} - '.format(self.address_line_1) if self.address_line_1 else '',
            addy2='{0} - '.format(self.address_line_2) if self.address_line_2 else '',
            city='{0} - '.format(self.city) if self.city else '',
            state='{0} - '.format(self.state) if self.state else '',
            province='{0} - '.format(self.province) if self.province else '',
            country='{0} - '.format(self.country) if self.country else '',
            zip='{0}'.format(self.zip_code) if self.zip_code else '')
        return unicode(addy)


class VineyardLocation(models.Model):
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.ForeignKey('buywine.State', null=True, blank=True)
    province = models.ForeignKey('buywine.Province', null=True, blank=True)
    country = models.ForeignKey('buywine.Country', null=False, blank=False)
    vineyard_location_desc = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'wt_vineyard_location'
        ordering = ['city', 'state', 'province', 'country']
        unique_together = ('city', 'state', 'province','country', 'vineyard_location_desc')

    def __unicode__(self):
        loc = '{city} {state} {province} {country} {loc}'.format(
            city='{0} - '.format(self.city) if self.city else '',
            state='{0} - '.format(self.state) if self.state else '',
            province='{0} - '.format(self.province) if self.province else '',
            country='{0} - '.format(self.country) if self.country else '',
            loc='{0}'.format(self.vineyard_location_desc) if self.vineyard_location_desc else '')
        return unicode(loc)


class Country(models.Model):
    country_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    country_abbrev = models.CharField(max_length=10, null=False, blank=False, unique=True)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'wt_country'
        verbose_name_plural = 'Countries'
        ordering = ['country_name']

    def __unicode__(self):
        return unicode(self.country_name)


class State(models.Model):
    state_name = models.CharField(max_length=255, null=False, blank=True)
    state_abbrev = models.CharField(max_length=40, null=False, blank=True)
    country = models.ForeignKey('buywine.Country')
    viaible=models.BooleanField(default=True)

    class Meta:
        db_table = 'wt_state'
        unique_together = (('state_name', 'country'), ('state_abbrev', 'country'))
        ordering = ['country', 'state_name']

    def __unicode__(self):
        return unicode('{state_name}'.format(state_name=self.state_name))


class Province(models.Model):
    province_name = models.CharField(max_length=255, null=False, blank=False)
    province_abbrev = models.CharField(max_length=40, null=False, blank=False)
    country = models.ForeignKey('buywine.Country')
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'wt_province'
        unique_together = (('province_name', 'country'), ('province_abbrev', 'country'))
        ordering = ['country', 'province_name']

    def __unicode__(self):
        return unicode('{province_name}'.format(province_name=self.province_name))


class Region(models.Model):
    region_name = models.CharField(max_length=255, null=False, blank=False)
    region_abbrev = models.CharField(max_length=40, null=False, blank=False)
    country = models.ForeignKey('buywine.Country')
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'wt_region'
        unique_together = (('region_name', 'country'), ('region_abbrev', 'country'))
        ordering = ['country', 'region_name']

    def __unicode__(self):
        return unicode('{region_name}'.format(region_name=self.region_name))


class WineComment(models.Model):
    wine = models.ForeignKey('buywine.Wine', null=False, blank=False)
    comment_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    comment_user = models.ForeignKey(User, null=False, blank=True)
    comment = models.TextField(default='')

    class Meta:
        db_table = 'wt_wine_comments'
        ordering = ['wine', 'comment_date']


class WineServed(models.Model):
    wine = models.ForeignKey('buywine.Wine', null=False, blank=False)
    event_date = models.DateField(null=False, blank=False)
    event_description = models.TextField(null=True, blank=True)
    num_bottles = models.IntegerField(null=False, blank=True, default=1)
    created_on = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    created_by = models.ForeignKey(User, null=False, blank=True)

    class Meta:
        db_table = 'wt_wine_served'
        verbose_name_plural = 'Wine Served'
        ordering = ['wine', 'event_date']
