# -*- coding: utf-8 -*-
{
    'name': "Todo app extension",

   
    'description': """
        a todo app extension
    """,

    'author': "me",
   


    # any module necessary for this one to work correctly
    'depends': ['todo_app'],
    'application': True,
    'data': [
             'todo_view.xml',
             'security/todo_access_rules.xml'
             ],

    
}
