# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    'name': 'Trobz Base',
    'version': '12.1.0.0',
    'category': 'Trobz Standard Modules',
    'summary': 'General features for all projects',
    'author': 'Trobz',
    'website': 'http://trobz.com',
    'depends': [
        'access_right_generator',
        'mail',
        'user_profile',
        'web'
    ],
    'data': [
        # DATA
        'data/base/ir_config_parameter_data.xml',

        # SECURITY
        'security/trobz_base_security.xml',

        # VIEW
        # 'view/base/trobz_maintenance_error_view.xml',
        'view/base/ir_module_view.xml',
        'view/base/res_users_view.xml',
        'view/base/res_groups_view.xml',

        # MENU
        'menu/trobz_base_menu.xml',

        # POST OBJECT
        'data/base/function_data.xml',
    ],
    'demo': [],
    'test': [],
    'qweb': [
        # 'static/src/template/base.xml'
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
    'active': False,
}
