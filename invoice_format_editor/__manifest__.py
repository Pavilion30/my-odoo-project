# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Invoice Format Editor',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Invoice Report, Report Editor, Customise Invoice Report, '
               'Invoice Report Templates, Account Reports, Odoo18, '
               'Odoo Apps, Report Templates, Odoo18, Odoo Apps',
    'description': """Invoice Format Editor For Configuring the Invoice Templates""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['account', 'web', 'sale_management'],
    'data': ['security/ir.model.access.csv',
             'data/design_templates.xml',
             'data/normal_preview_templates.xml',
             'data/modern_preview_templates.xml',
             'data/old_standard_preview_templates.xml',
             'views/doc_layout_views.xml',
             'views/base_document_layout_views.xml',
             'views/custom_external_layout_templates.xml',
             'reports/normal_invoice_templates.xml',
             'reports/modern_invoice_templates.xml',
             'reports/old_standard_invoice_templates.xml',
             'reports/report_invoice_templates.xml',
             'reports/preview_layout_report_templates.xml',
             ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
