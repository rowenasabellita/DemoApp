// Copyright (c) 2016, Rowenaapp and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Athlete"] = {
	"filters": [
		{
			"fieldname": "firstname",
			"label": __("First Name"),
			"fieldtype": "Data",
		},
		{
			"fieldname": "middlename",
			"label": __("Middle Name"),
			"fieldtype": "Data",
		},
		{
			"fieldname": "lastname",
			"label": __("Last Name"),
			"fieldtype": "Data",
		},
		{
			"fieldname": "sports",
			"label": __("Sport"),
			"fieldtype": "Link",
			"options": "Sport",
		},
	]
};
