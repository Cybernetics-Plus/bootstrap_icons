# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Install Bootstrap Icons 1.10.5 in Odoo
#
#    Copyright (C) 2021-TODAY Cybernetics Plus Technologies (<https://www.cybernetics.plus>).
#    Author: Cybernetics Plus Techno Solutions (<https://www.cybernetics.plus>)
#
###################################################################################

{
    "name": "Bootstrap Icons",
    "version": "13.1.10.5.1",
    "summary": """ 
            Install Bootstrap Icons 1.10.5 in Odoo
            .""",
    "description": """ 
            Install Bootstrap Icons 1.10.5 in Odoo
            .""",
    "author": "Cybernetics+",
    "company": "Cybernetics Plus Co., Ltd.",
    "maintainer": "Cybernetics Plus Co., Ltd.",
    "website": "https://www.cybernetics.plus",
    "live_test_url": "https://www.cybernetics.plus",
    "images": ["static/description/banner.gif"],
    "category": "Extra Tools",
    "license": "AGPL-3",
    "price": 1.9,
    "currency": "EUR",
    "installable": True,
    "application": False,
    "auto_install": False,
    "contributors": [
        "C+ Developer <dev@cybernetics.plus>",
    ],
    "assets": {
        "web.assets_qweb": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_common_minimal": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_common": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_common_lazy": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_backend": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_backend_legacy_lazy": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_frontend": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_frontend_minimal": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_frontend_lazy": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.assets_backend_prod_only": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.report_assets_common": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
        "web.report_assets_pdf": [
            "ctp_bootstrap_icons/static/src/css/bootstrap-icons.min.css",
        ],
    },
}
