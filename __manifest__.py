# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Nómina Colombiana',
    'category': 'Human Resources',
    'depends': ['hr_payroll'],
    "author"  :  "William Peña",
  "license"   :  "Other proprietary",
  "website"   :  "https://www.ogsistemas.com",
    'description': """
Nomina Colombiana
======================

* Nómina Básica Colombiana
    """,

    'data': [
        'views/l10n_co_hr_payroll_view.xml',
        'data/l10n_co_hr_payroll_data.xml',
    ],
}
