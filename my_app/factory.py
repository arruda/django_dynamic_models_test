# -*- coding: utf-8 -*-
"""
    factory
    ~~~~~~~~~~~~~~

    Generates a class based on a template

    :copyright: (c)  2012  by Arruda.
    :license: MIT, see LICENSE FILE for more details.
"""


#:This template is used to generate other models
MODEL_TEMPLATE =\
"""
class %(CLASS_NAME)s(models.Model):
    "%(CLASS_DESC)s"
    
    %(FIELD_NAME)s = models.CharField(max_length=256)

    def __unicode__(self):
        return self.%(FIELD_NAME)s
"""

def model_factory(name,desc,field):
    """Fabricates a model with the given name, using MODEL_TEMPLATE as reference.
    """
    
    format_dict = {
                   'CLASS_NAME' : name.capitalize(),
                   'CLASS_DESC' : desc,
                   'FIELD_NAME' : field,
                   }
    
        
    model_source = MODEL_TEMPLATE % format_dict    
    return model_source

