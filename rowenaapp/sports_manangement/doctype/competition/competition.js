// Copyright (c) 2022, Rowenaapp and contributors
// For license information, please see license.txt

frappe.ui.form.on('Competition', {
	get_athletes: function(frm) {
		frappe.call({
			"method": "rowenaapp.sports_manangement.doctype.competition.competition.get_participants",
			"args": {"sport": cur_frm.doc.sport},
			"callback": function(r){
				r.message.map((val, idx)=>{
					var child_table = frm.add_child("participants")
					child_table.athlete = val.full_name
				})
				frm.refresh_field("participants")
			}
		});

		frappe.call({
			"method" :"rowenaapp.sports_manangement.doctype.competition.competition.get_games",
			"args": {"sport": cur_frm.doc.sport},
			"callback" : function(r){
				let rows = ``;

				let html = ``;

				for (let i in r.message){
					rows += `
						<tr style="cursor: pointer;">
							<td>${r.message[i].score || ""}</td>
							<td>${r.message[i].start_date_and_time || ""}</dt>
							<td>${r.message[i].end_date_and_time || ""}</dt>
							<td>${r.message[i].duration || ""}</td>
						</tr>`
				}

				html = `<table class="table"><tr><th>Score</th> <th>Start Date and Time</th> <th>End Date and Time</th> <th>Duration</th></tr>${rows}</table>`
				
				cur_frm.set_df_property("games",'options',frappe.render(html, {}))
			}
		})
	},

	make_game: function(frm){
		
		frappe.set_route(['Form', 'Game', 'New Game'])

	}
	

});