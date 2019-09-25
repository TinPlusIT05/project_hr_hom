# -*- coding: utf-8 -*-
{
    'name': 'Project project_hr_12 installer',
    'version': '1.0',
    'category': 'Trobz Standard Modules',
    'description': """
This module will install all module dependencies of project_hr_12.
    """,
    'author': 'Trobz',
    'website': 'http://www.trobz.com',
    'depends': [
        'trobz_base',
        'hr',
        'hr_contract',
        'hr_holidays',
    ],
    'data': [
        # ============================================================
        # SECURITY SETTING - GROUP - PROFILE
        # ============================================================
        # 'security/',
        "security/ir.model.access.csv",

        # ============================================================
        # DATA
        # ============================================================
        # 'data/',
        "data/hr_gas_allowance_data.xml",

        # ============================================================
        # VIEWS
        # ============================================================
        # 'view/',
        "views/hr_employee_view.xml",
        "views/hr_contract_view.xml",
        "views/hr_gas_allowance_view.xml",

        # ============================================================
        # MENU
        # ============================================================
        # 'menu/',
        "menu/hr_gas_allowance.xml",

        # ============================================================
        # FUNCTION USED TO UPDATE DATA LIKE POST OBJECT
        # ============================================================
        # "data/project_hr_12_update_functions_data.xml",
    ],

    'test': [],
    'demo': [],

    'installable': True,
    'active': False,
    'application': True,
}
