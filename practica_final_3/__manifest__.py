# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sistema DOQ - Práctica Final 3",
    "summary": "Práctica Final 3 del curso Sistema DOQ",
    "version": "14.0.1.0.0",
    "category": "Sistema DOQ",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ['stock', 'sale'],
    "data": ['views/pack.xml', 'security/ir.model.access.csv'],
}
