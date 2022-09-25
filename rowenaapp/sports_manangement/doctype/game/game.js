// Copyright (c) 2022, Rowenaapp and contributors
// For license information, please see license.txt

frappe.ui.form.on('Game', {
	end_date_and_time: function(frm){
		var start = new Date(frm.doc.start_date_and_time);
		var end = new Date(frm.doc.end_date_and_time);
	
	
		if (end <= start){
			alert("Can't select earlier end date than the start date.");
			var value = null;
			frm.set_value('end_date_and_time',value);
	
		}else{
			var diff =  (start - end) / 1000;
			diff /= (60 * 60);
			var duration = Math.abs(Math.round(diff));
			frm.set_value('duration', duration);
		}
	}
});
