# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Cybernetics Plus Install Bootstrap Icons 1.9.0 in Odoo
#
###################################################################################

{
    'name': 'Bootstrap Icons',
    'version': '13.1.9.0.1',
    'summary': """ 
            Cybernetics Plus Install Bootstrap Icons 1.9.0 in Odoo
            .""",
    'description': """ 
            Cybernetics Plus Install Bootstrap Icons 1.9.0 in Odoo
            .""",
    'author': 'Cybernetics Plus Co., Ltd.',
    'website': 'https://www.cybernetics.plus',
    'live_test_url': 'https://www.cybernetics.plus',
    'images': ['static/description/banner.gif'],
    'category': 'Extra Tools',
    'license': 'AGPL-3',
    'price': 1.9,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': True,
    'contributors': [
        'Developer <dev@cybernetics.plus>',
    ],
    'assets': {
        'web.assets_qweb': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.assets_common_minimal': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.assets_common': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.assets_common_lazy': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.assets_backend': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        "web.assets_backend_legacy_lazy": [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.assets_frontend': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.assets_frontend_minimal': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.assets_frontend_lazy': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.assets_backend_prod_only': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.report_assets_common': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
        'web.report_assets_pdf': [
            'ctp_bootstrap_icons/static/src/css/bootstrap-icons.css',
        ],
    },
}
