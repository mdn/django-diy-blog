#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_python_version():
    """Ensure the script is being run with a compatible Python version."""
    if sys.version_info < (3, 6):
        raise RuntimeError("Django requires Python 3.6 or higher.")

def main():
    """Run administrative tasks."""
    check_python_version()

    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_diy_blog.settings')
        logger.info('DJANGO_SETTINGS_MODULE not set, defaulting to django_diy_blog.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logger.error(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?", exc_info=True
        )
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
