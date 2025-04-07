import sys
import os
from django.core.wsgi import get_wsgi_application

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite/mysite.settings')

application = get_wsgi_application()
