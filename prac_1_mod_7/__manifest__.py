# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Práctica 1 Informes",
    "summary": "Sistema DOQ Práctica 1 Informes",
    "version": "14.0.1.0.0",
    "category": "Pro",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['sale', 'account'],
    "data": [
        'views/layout.xml',
        'views/reports.xml',
        'views/report_sale.xml',
        'views/report_invoice.xml',
    ],
}
