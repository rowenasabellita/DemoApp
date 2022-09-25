# -*- coding: utf-8 -*-
# Copyright (c) 2022, Rowenaapp and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Competition(Document):
	pass


@frappe.whitelist()
def get_participants(sport):
	return frappe.db.sql("select * from `tabAthlete` where sports = %s ", sport, as_dict=1)

@frappe.whitelist()
def get_games(sport):
	return frappe.db.sql("select * from `tabGame` where sport = %s ", sport, as_dict=1)