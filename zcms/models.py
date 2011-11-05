from django.db import models

site_values = [(0, 'LIVE'),
                        (1, 'STAGING'),
                        (2, 'TEST'),
                        (3, 'DEVELOPMENT'),
                        (99, 'TO BE DELETED')]

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
    fallback = models.ForeignKey("Language", related_name='child', blank=True, null=True)
    
    def __unicode__(self):
        return self.iso_code
    
    def __str__(self):
        return self.__unicode__()

class CMSComponent(models.Model):
    """ Represents a component in the CMS. A component is a large 'thing', e.g. a template
or big text whereas a Token is a small 'thing' - a small piece of text for example, no
more than 200 characters long."""
    cid = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.cid
    
    def __str__(self):
        return self.__unicode__()
        
class CMSComponentValue(models.Model):
    component = models.ForeignKey(CMSComponent)
    channel = models.ForeignKey(Channel)
    site = models.IntegerField(choices = site_values, default = 0)
    value = models.TextField()
    
    def __unicode__(self):
        return "%s/%s" % (self.component.cid, self.channel)
    
    def __str__(self):
        return self.__unicode__()
       
class CMSToken(models.Model):
    """ Represents a token in the CMS. A component is a large 'thing', e.g. a template
whereas a Token is a small 'thing' - a small piece of text for example.
"""
    cid = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.cid
    
    def __str__(self):
        return self.__unicode__()

class CMSTokenValue(models.Model):
    """ The value of a token in a given language. """
    token = models.ForeignKey(CMSToken)
    language = models.ForeignKey(Language)
    site = models.IntegerField(choices = site_values, default = 0)
    value = models.TextField()
    
    def __unicode__(self):
        return "%s/%s" % (self.token, self.language)
    
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
    
class Slot(models.Model):
    """ Slots are regions in a page that have content that is chosen according to rules. """
    slot = models.CharField(max_length = 20)
    summary = models.CharField(max_length = 150)

    def __unicode__(self):
        return self.slot
    
    def __str__(self):
        return self.__unicode__()
    
class SlotContent(models.Model):
    """SlotContent entries define the CMSComponent to be inserted in a given slot 
according to specified rules. At first it was imagined that this would be straight-forward 
time-based rules. But why restrict ourselves? This is Python. This is dynamic. And
whilst it might be considered a bit low level or ugly, why not have some code-like 
content to build sophisticated rules? This code is in the database. 

Each line in the text field is a single expression. Each expression must evaluate to 
True for the rule to trigger. The first slot rule to trigger wins. Slot entries for a 
given slot can be ordered by the Rank column.

An slot with an empty rules entry is ignored always. This is equivalent to setting 
enabled=False. This can ensure a set of slot rules always terminates in a result.

Any rule preceeded by # is considered a comment
"""
    slot = models.ForeignKey(Slot)
    rank = models.IntegerField(default = 1)
    enabled = models.BooleanField(default = True)
    rules = models.TextField()
    component = models.CharField(max_length = 100)
    is_token = models.BooleanField()
