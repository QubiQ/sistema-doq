# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Módulo 5 Práctica 1",
    "summary": "Módulo 5 Práctica 1 Solución",
    "version": "15.0.1.0.0",
    "category": "Base",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['sale'],
    "data": ['security/ir.model.access.csv',
             'data/menu.xml',
             'views/books_book.xml',
             'views/books_author.xml',
             'views/books_genre.xml'],
}
