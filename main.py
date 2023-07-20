import os

def generate_django_project_skeleton(project_name):
    # Создаем корневую папку для проекта
    os.mkdir(project_name)
    os.chdir(project_name)

    # Создаем каталоги для основных компонентов Django
    os.mkdir('static')
    os.mkdir('templates')
    
    # Создаем файлы с набросками для Django проекта
    with open('manage.py', 'w') as manage_file:
        manage_file.write('#!/usr/bin/env python\n')
        manage_file.write('import os\n')
        manage_file.write('import sys\n\n')
        manage_file.write('if __name__ == "__main__":\n')
        manage_file.write('    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{}.settings")\n'.format(project_name))
        manage_file.write('    try:\n')
        manage_file.write('        from django.core.management import execute_from_command_line\n')
        manage_file.write('    except ImportError as exc:\n')
        manage_file.write('        raise ImportError(\n')
        manage_file.write('            "Couldn\'t import Django. Are you sure it\'s installed and "')
        manage_file.write('            "available on your PYTHONPATH environment variable? Did you "')
        manage_file.write('            "forget to activate a virtual environment?"\n')
        manage_file.write('        ) from exc\n')
        manage_file.write('    execute_from_command_line(sys.argv)\n')

    with open('settings.py', 'w') as settings_file:
        settings_file.write('DEBUG = True\n')
        settings_file.write('SECRET_KEY = \'your_secret_key_here\'\n')
        settings_file.write('ALLOWED_HOSTS = []\n')
        settings_file.write('INSTALLED_APPS = [\n')
        settings_file.write('    # Add your installed apps here\n')
        settings_file.write(']\n')
        settings_file.write('MIDDLEWARE = [\n')
        settings_file.write('    # Add your middleware classes here\n')
        settings_file.write(']\n')
        settings_file.write('ROOT_URLCONF = "{}.urls"\n'.format(project_name))
        settings_file.write('TEMPLATES = [\n')
        settings_file.write('    {\n')
        settings_file.write('        \'BACKEND\': \'django.template.backends.django.DjangoTemplates\',\n')
        settings_file.write('        \'DIRS\': [os.path.join(BASE_DIR, "templates")],\n')
        settings_file.write('        \'APP_DIRS\': True,\n')
        settings_file.write('        \'OPTIONS\': {\n')
        settings_file.write('            \'context_processors\': [\n')
        settings_file.write('                # Add your context processors here\n')
        settings_file.write('            ],\n')
        settings_file.write('        },\n')
        settings_file.write('    },\n')
        settings_file.write(']\n')
        settings_file.write('WSGI_APPLICATION = "{}.wsgi.application"\n'.format(project_name))
        settings_file.write('DATABASES = {\n')
        settings_file.write('    \'default\': {\n')
        settings_file.write('        # Add your database configuration here\n')
        settings_file.write('    }\n')
        settings_file.write('}\n')
        settings_file.write('LANGUAGE_CODE = \'en-us\'\n')
        settings_file.write('TIME_ZONE = \'UTC\'\n')
        settings_file.write('USE_I18N = True\n')
        settings_file.write('USE_L10N = True\n')
        settings_file.write('USE_TZ = True\n')
        settings_file.write('STATIC_URL = \'/static/\'\n')

    with open('urls.py', 'w') as urls_file:
        urls_file.write('from django.urls import path\n\n')
        urls_file.write('urlpatterns = [\n')
        urls_file.write('    # Add your URL patterns here\n')
        urls_file.write(']\n')

    print(f'Проект "{project_name}" сгенерирован успешно!')

if __name__ == "__main__":
    project_name = input("Введите имя вашего Django проекта: ")
    generate_django_project_skeleton(project_name)
