# -*- coding: utf-8 -*-
# Copyright (c) 2022, Rowenaapp and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StudentProfile(Document):

	def before_save(self):
		student = frappe.get_doc({"doctype": "Student Section", "full_name":self.full_name, "section":self.section})
		created_student_doc = student.insert(ignore_permissions=True)

	def on_trash(self):
		frappe.db.sql(f""" DELETE FROM `tabStudent Section` WHERE full_name = '{self.full_name}' AND section = '{self.section}' """)
		frappe.db.commit()



	
