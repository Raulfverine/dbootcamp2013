var menuPP = 
{
 version: "0.1",
 options: Array("test_message_1"),
 checkboxes: Array("functions_analyze_email_header",),

 tabs: [
    'message',
    'credits'
 ],

  init: function() {
	 console.log("init");
  },
 
 checkInstall: function() {
     if(!localStorage.getItem('PPinstalled'+this.version) || localStorage.getItem('PPinstalled'+this.version) != 'true') {
         if(!localStorage.getItem("message_type1")) 
             localStorage.setItem("message_type1", "alert");
         if(!localStorage.getItem("message_automatic_clipboardcopy"))
             localStorage.setItem("message_automatic_clipboardcopy", "0");
         
         for (el in menuPP.checkboxes) {
             if(menuPP.checkboxes.hasOwnProperty(el)) {
                 if(localStorage.getItem(el) != "0" && localStorage.getItem(el) != "1") {
                     localStorage.setItem(el, "1");
                 }
             }
         }

         localStorage.setItem('D3installed'+this.version, 'true');
         if(localStorage.getItem('D3lastversion')) {
        	 localStorage.removeItem('D3installed'+localStorage.getItem('lastversion'));
         }
         localStorage.setItem('D3lastversion',this.version);
         
     }   
 },
 
 /**
  * Save options to localStorage
  */
 save_options: function(alertText) {
     console.log("Called save_options");
	 if(alertText == undefined) {
		 alert = true;
	 }
     var value = false;
     for (option in menuPP.options) {
         if(menuPP.options.hasOwnProperty(option)) {
		     if(document.getElementById(menuPP.options[option]) && document.getElementById(menuPP.options[option]).checked == true) {
			     value = document.getElementById(menuPP.options[option]).value; 
		     }
         }
	 }

     localStorage.setItem("message_type", value ? value : "notifications");
     
     if(document.getElementById("message_automatic_clipboardcopy").checked == true) {
    	 localStorage.setItem("message_automatic_clipboardcopy", 1);
     } else {
    	 localStorage.setItem("message_automatic_clipboardcopy", 0);
     }

	 console.log('Updating functions');
	 for (option in menuPP.checkboxes) {
         if (menuPP.checkboxes.hasOwnProperty(option)) {
		     var elem = document.getElementById(menuPP.checkboxes[option]);
		     var value = "0";
		     if(elem.checked) {
			     value = elem.checked ? "1" : "0";
		     } else {
                value = "0";
             }

		     localStorage.setItem(menuPP.checkboxes[option], value); 
         }
	 }
 },

 /**
  * Restore options from localStorage
  */
 restore_options: function() {
	 var type 				= localStorage.getItem("message_type") ? 
			 						localStorage.getItem("message_type") : 
			 						"notifications"; 
	 var somethingChecked   = false;
	 
	 if(localStorage.getItem("message_automatic_clipboardcopy") == 1) {
		 document.getElementById("message_automatic_clipboardcopy").checked = true;
     } else {
    	 document.getElementById("message_automatic_clipboardcopy").checked = false;
     }
	 
	 for (option in menuPP.options) {
         if (menuPP.options.hasOwnProperty(option)) {
		     var optionValue = document.getElementById(menuPP.options[option]).value;
		     if(optionValue==type) {
			     document.getElementById(menuPP.options[option]).checked = true;
			     somethingChecked = true;
		     }
         }
	 }

	 if(somethingChecked == false) {
		 document.getElementById('message_type2').checked = true;
	 }
	 
	 for (option in menuPP.checkboxes) {
         if (menuPP.checkboxes.hasOwnProperty(option)) {
		     var value = localStorage.getItem(menuPP.checkboxes[option]) == 1 ? true : false;
		     var elem = document.getElementById(menuPP.checkboxes[option]).checked = value;
         }
	 }
 },
 
 /**
  * menu tab functions
  */
 showTab: function(name) {
    var deactivate = function(id) {
            document.getElementById(id).className        = '';
            document.getElementById(id+'-tab').className = '';
        },
        activate = function(id) {
            document.getElementById(id).className        = 'active';
            document.getElementById(id+'-tab').className = 'active';
        };

    for (n in menuPP.tabs) {
        if (menuPP.tabs.hasOwnProperty(n)) {
            if (menuPP.tabs[n] !== name) {
                deactivate(menuPP.tabs[n]);
            } else {
                activate(menuPP.tabs[n])
            }
        }
    }

    document.location.hash = name;
 }
};

menuPP.init();

var inputs = document.querySelectorAll('input');
for (el in inputs) {
    if (inputs.hasOwnProperty(el) && inputs[el] && el != 'length') {
	    inputs[el].addEventListener('change', function() {
            menuPP.save_options(false);
        });
    }
}

var listenerForTab = function(n) {
    document.getElementById(n + '-tab').addEventListener('click', function () {
        menuPP.showTab(n);
    });
}

for (tab in menuPP.tabs) {
    if (menuPP.tabs.hasOwnProperty(tab)) {
        listenerForTab(menuPP.tabs[tab]);
    }
}

if (document.location.hash) {
    menuPP.showTab(document.location.hash.substr(1));
} else {
    menuPP.showTab('message')
}
