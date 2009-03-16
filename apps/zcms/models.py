from django.db import models

class Channel(models.Model):
    """ A channel may represent a country, a category of visitor... anything."""
    name = models.CharField(max_length = 20, unique = True)
    parent = models.ForeignKey("Channel", related_name='child', blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class Language(models.Model):
    """ Language is much as you'd expect """
    name = models.CharField(max_length = 20, unique = True)
    iso_code = models.CharField(max_length = 5, unique = True)
    
    def __unicode__(self):
        return self.iso_code
    
    def __str__(self):
        return self.__unicode__()

class CMSComponent(models.Model):
    """ Represents a component in the CMS. A component is a large 'thing', e.g. a template
or big text whereas a Token is a small 'thing' - a small piece of text for example, no
more than 200 characters long."""
    cid = models.CharField(max_length = 20)
    channel = models.ForeignKey(Channel)
    language = models.ForeignKey(Language)
    value = models.TextField()
    
    def __unicode__(self):
        return self.cid
    
    def __str__(self):
        return self.__unicode__()
    
    def shortValue(self):
        """ For representation in admin """
        MAX_CHARS = 100
        sv = self.value[:MAX_CHARS]
        if len(self.value) > MAX_CHARS:
            sv+='...'
        return sv
       
class CMSToken(models.Model):
    """ Represents a token in the CMS. A component is a large 'thing', e.g. a template
whereas a Token is a small 'thing' - a small piece of text for example, no 
more than 200 characters long. """
    cid = models.CharField(max_length = 20)
    channel = models.ForeignKey(Channel)
    language = models.ForeignKey(Language)
    value = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.value
    
    def __str__(self):
        return self.__unicode__()

class URL(models.Model):
    """ Used to map to a component """
    name = models.CharField(max_length = 20)
    url = models.CharField(max_length = 255, unique = True)
    enabled = models.BooleanField(default = True)
    component_name = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.url
    
    def __str__(self):
        return self.__unicode__()
    
    