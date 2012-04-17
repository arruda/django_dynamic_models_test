from django.db import models
from definitions import MY_MODELS_LIST
from factory import model_factory

#runs the generated models sources
for model_infos in MY_MODELS_LIST:
    model_source = model_factory(model_infos['name'],model_infos['desc'],model_infos['field'])
    exec(model_source)

