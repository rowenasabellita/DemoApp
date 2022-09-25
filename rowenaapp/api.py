import frappe
from frappe import _

def test_query():
    query = frappe.db.sql(""" SELECT firstname, middlename, lastname, sports FROM `tabAthlete` """)
    return query