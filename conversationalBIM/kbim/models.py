from django.db import models

# Create your models here.

class AutodeskAPIs(models.Model):
    api_title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.api_title

class AutodeskTokens(models.Model):
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    token_type = models.CharField(max_length=100)
    expires_in = models.DateTimeField()
    def get_latest_token(self):
        return AutodeskTokens.objects.order_by('expires_in').first()

""" class ViewerAPI(models.Model):


class DataManagementAPI(models.Model):


class ModelDerivativeAPI(models.Model):


class DesignAutomationAPI(models.Model):


class RealityCaptureAPI(models.Model):


class BIM360API(mdoels.Model):


class WebhooksAPI(models.Model):


class TokenAPI(models.Model):"""

