import os
import sys
from drfecommerce.settings import base

def main():
    if base.DEBUG :
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfecommerce.settings.local')
    else :
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfecommerce.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
