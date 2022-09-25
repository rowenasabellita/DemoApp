# Copyright (c) 2013, Rowenaapp and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):	
	if not filters: filter = {}

	columns, data = [], []

	columns = get_columns()
	a_data = get_data(filters) 	 	

	if not a_data:
		frappe.msgprint(_('No records found.'));
		return columns, a_data

	for a in a_data:
		row = 	frappe._dict({
				'firstname': a.firstname,
				'middlename': a.middlename,
				'lastname': a.lastname,
				'age': a.age,
				'birthday': a.birthday,
				'sports': a.sports,
		})
		data.append(row)

	return columns, data


def get_columns():
	return [
		{
			'fieldname': 'firstname',
			'label': _('First Name'),
			'fieldtype': 'Data',
			'width': '120',
		},
		{
			'fieldname': 'middlename',
			'label': _('Middle Name'),
			'fieldtype': 'Data',
			'width': '120',
		},
		{
			'fieldname': 'lastname',
			'label': _('Last Name'),
			'fieldtype': 'Data',
			'width': '120',
		},
		{
			'fieldname': 'age',
			'label': _('Age'),
			'fieldtype': 'int',
			'width': '120',
		},
		{
			'fieldname': 'birthday',
			'label': _('Birthday'),
			'fieldtype': 'Date',
			'width': '120',
		},
		{
			'fieldname': 'sports',
			'label': _('Sport'),
			'fieldtype': 'Data',
			'width': '120',
		},

	]

def get_data(filters):
	conditions = get_condition(filters)
	data = frappe.get_all(
		doctype='Athlete',
		fields=['firstname','middlename','lastname','age','birthday','sports'],
		filters=conditions,
		order_by="firstname desc"
	)
	return data



def get_condition(filters):
	conditions = {}
	for key, val in filters.items():
		if filters.get(key):
			conditions[key] = val

	return conditions