===================================
Django Dynamic Models Test
===================================

About:
-----------------------------------

Just testing dynamic generation of models using templates and exec function.

How it works:
-----------------------------------
In my_app.definitions.py have MY_MODELS_LIST that is where are defined all my dynamic models informations:

Name
Description
Field Name

In my_app.factory.py is the method that creates the source of a model using this template::

    class %(CLASS_NAME)s(models.Model):
        "%(CLASS_DESC)s"
        
        %(FIELD_NAME)s = models.CharField(max_length=256)

        def __unicode__(self):
            return self.%(FIELD_NAME)s

The class are created just replacing the CLASS_NAME, CLASS_DESC and FIELD_NAME for the ones in the definitions.py file.

In my_app.models.py it calls the factory for each element in MY_MODELS_LIST, and then use exec to run the source_code of each one.

Result:
-----------------------------------
In manage.py shell::

    >>>from my_app.models import Foo, Bars, Other
    >>>f = Foo()
    >>>Foo.__doc__
    'Foo model'
    >>>f.foo_field = "fooooooo"
    >>>f.foo_field
    'fooooooo'
