# -*- coding: utf-8 -*-
{
    'name': "Todo app",

   
    'description': """
        a todo app
    """,

    'author': "me",
   


    # any module necessary for this one to work correctly
    'depends': ['hr'],
    'application': True,
    'data': [
             'todo_view.xml',
             'security/ir.model.access.csv'
             ],

    
}
