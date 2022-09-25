// Copyright (c) 2022, Rowenaapp and contributors
// For license information, please see license.txt

frappe.ui.form.on('Athlete', {
	birthday: function(frm) {
		var today = new Date();
		var birthDate = new Date(frm.doc.birthday); 
		var age = today.getFullYear() - birthDate.getFullYear(); 
		var month = today.getMonth() - birthDate.getMonth(); 
		if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) { 
			age--; 
		} 

		frm.set_value('age', age)
	},

	lastname: function(frm){
		var firstName = frm.doc.firstname;
		var middleName = frm.doc.middlename;
		var lastName = frm.doc.lastname;
		var fullName = firstName.concat(' '+ middleName + ' ' + lastName);

		frm.set_value('full_name', fullName);
	}
});
