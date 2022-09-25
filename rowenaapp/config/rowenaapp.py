from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Rowena App"),
			"icon": "octicon octicon-briefcase",
			"items": [
				{
					"type": "doctype",
					"name": "ToDo",
					"label": _("To Do"),
					"description": _("Documents assigned to you and by you."),
					"onboard": 1,
				}
            ]
		}
	]
