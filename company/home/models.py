from django.db import models


class B2BCommerce(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class LoyaltyAndIncentives(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Manufacturers (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Distributors (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Retailers (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PartnerWith (models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class EverythingConnects(models.Model):
    description = models.TextField()
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class OnePlatform(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class SmartConnected(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class OpenToIntegrations(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class QuickToMarket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class PersonalizedSupport(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class GlobalSecure(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class HeaderHome(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title



