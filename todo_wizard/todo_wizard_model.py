# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp import exceptions # will be used in the code

import logging
_logger = logging.getLogger(__name__)

class TodoWizard(models.TransientModel):
	_name = 'todo.wizard'
	task_ids = fields.Many2many('todo.task', string='Tasks')
	new_deadline = fields.Date('Deadline to Set')
	new_user_id = fields.Many2one(
	'res.users',string='Responsible to Set')