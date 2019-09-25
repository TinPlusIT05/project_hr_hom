# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    'name': 'User Profile',
    'version': '12.1.0.0',
    'category': 'Trobz Standard Modules',
    'summary': 'Add new feature profile to res.groups',
    'author': 'Trobz',
    'website': 'http://trobz.com',
    'depends': [],
    'data': [
        # DATA
        'data/ir_module_category_data.xml',

        # VIEW
        'view/base/res_groups_view.xml',
        'view/base/res_users_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'active': False,
}
