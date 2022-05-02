# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Práctica Final 2",
    "summary": "Sistema DOQ Práctica Final 2",
    "version": "15.0.1.0.0",
    "category": "Pro",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['sale'],
    "data": [
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/product_pack_line.xml',
        'views/reports.xml',
        'views/report_product_template.xml',
    ],
}
