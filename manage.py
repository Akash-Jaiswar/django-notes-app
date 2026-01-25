# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notesapp.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()




#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notesapp.settings')

    # 🔥 HACK: Simple HTTP response without views/urls
    if len(sys.argv) > 1 and sys.argv[1] == "runserver":
        from django.core.management.commands.runserver import Command as RunserverCommand
        from django.http import HttpResponse
        from django.urls import path
        from django.conf import settings
        from django.core.wsgi import get_wsgi_application
        from django.core.management import execute_from_command_line

        def home(request):
            return HttpResponse("🔥 Django is running inside Docker. No urls.py needed!")

        # Inject fake URL config
        settings.ROOT_URLCONF = type("Temp", (), {
            "urlpatterns": [path("", home)]
        })

        get_wsgi_application()
        execute_from_command_line(sys.argv)
        return

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django") from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
