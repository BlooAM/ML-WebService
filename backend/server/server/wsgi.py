import os
import inspect
from django.core.wsgi import get_wsgi_application

from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()