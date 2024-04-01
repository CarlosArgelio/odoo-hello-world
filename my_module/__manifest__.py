# __manifest__.py

{
    'name': 'Mi Módulo Hola Mundo',
    'version': '1.0',
    'summary': 'Módulo de ejemplo para mostrar un mensaje Hola Mundo en Odoo',
    'description': """
        Este es un módulo de ejemplo para mostrar un mensaje Hola Mundo en Odoo.
    """,
    'author': 'Tu Nombre',
    'website': 'https://www.tusitio.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'views/hola_mundo_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
