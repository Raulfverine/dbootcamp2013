/** 
 * Some functions from php.js (see phpjs.org)
 *
 * @version 2.0.2
 * @author Maik Kulbe <info@linux-web-development.de>
 * @copyright (c) 2010 Maik Kulbe
 */

/**
 * RegEx escaping
 */
RegExp.escape = function(text) {
    return text.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
};

/**
 * KEY FUNCTION NAMESPACE
 */
var pp = 
{	
	//needs a new Icon - best would be an icon per decoding type
	//icon: "popupIcon.png",
	icon: "../images/icon128.png",
	/**
     * Version number
     * 
     * @var String
     */
   version: "2.0.2",
    /**
     * list all functions so we can use this while saving
     * @var Array 
     */
   checkboxes: Array( "functions_rot13",
                      "functions_timestamp",
                      "functions_crc32",
                      "functions_bin2hex",
                      "functions_bin2txt",
                      "functions_html_entity_decode",
                      "functions_htmlentities",
                      "functions_htmlspecialchars",
                      "functions_htmlspecialchars_decode",
                      "functions_uri_encode",
                      "functions_uri_decode",
                      "functions_md5",
                      "functions_sha1",
                      "functions_quoted_printable_decode",
                      "functions_quoted_printable_encode",
                      "functions_escapeshellarg",
                      "functions_base64_encode",
                      "functions_base64_decode",
                      "functions_unserialize",
                      "functions_leet_decode",
                      "functions_leet_encode",
                      "functions_reverse"),

    menuIds: {},

    lastMessage: '',

	PhrasesEnglish:
		new Array('crap', 'dude', 'hacker',
		  'hacks', 'you', 'cool', 'oh my god',
		  'fear', 'power', 'own', 'lol',
		  'what the hell', 'elite', 'for the win', 
		  'oh really', 'good game'),

	PhrasesLeet:
		new Array('carp', 'dood', 'haxor', 'hax', 'joo',
		  'kewl', 'omg', 'ph43', 'powwah', 'pwn', 'lawl',
		  'wth', 'leet', 'ftw', 'o rly', 'gg'),

	LettersEnglish:
		new Array('n', 'b', 'k', 'd', 'e', 'f', 'g', 'h',
		  'p', 'm', 'r', 'l', 'o', 'q', 's', 't',
		  'u', 'x', 'w', 'y', 'z', 'c', 'a', 'j', 
		  'i', 'v', ' '),

	LettersLeet: 
		new Array('/\\/', '|}', '|X', '[)', '3', '|=', 'gee', '|-|',
		  '|*', '(\\/)', '|2', '1', '()', '0', '$', '+',
		  '|_|', '><', '\\X/', '\'/', '2', '<', '/\\', '_|', 
		  '|', '\\/', '  '),
			 	       
	checkInstall: function() {
        if(!localStorage.getItem('ppinstalled'+pp.version) || localStorage.getItem('ppinstalled'+pp.version) != 'true') {
            if(!localStorage.getItem("message_type")) 
                localStorage.setItem("message_type", "alert");
            if(!localStorage.getItem("message_type1"))
                localStorage.setItem("message_type1", "1"); 
            if(!localStorage.getItem("message_type2"))
                localStorage.setItem("message_type2", "0");
            if(!localStorage.getItem("message_type3"))
                localStorage.setItem("message_type3", "0");
            if(!localStorage.getItem("message_type4"))
                localStorage.setItem("message_type4", "0");
            if(!localStorage.getItem("message_type5"))
                localStorage.setItem("message_type5", "0");
            
            for (var el in pp.checkboxes) {
                if (pp.checkboxes.hasOwnProperty(el)) {
                    if(localStorage.getItem(pp.checkboxes[el]) != "0" &&
                            localStorage.getItem(pp.checkboxes[el]) != "1") {
                        localStorage.setItem(pp.checkboxes[el], "1");
                    }
                }
            }

            localStorage.setItem('ppinstalled'+pp.version, 'true');
            if(localStorage.getItem('pplastversion')) {
                localStorage.removeItem('ppinstalled'+localStorage.getItem('lastversion'));
            }
            localStorage.setItem('pplastversion',pp.version);
            
        }   
	 },
	
	createPopup: function(title, text)
	{
		var type = localStorage.getItem("message_type");
		
		if(localStorage.getItem("message_automatic_clipboardcopy") == 1) {
			pp.copyToClipboard(text);
		}
        
        pp.lastMessage = text;
		
		switch (type) {
			case 'console':
				text = pp.base64_encode(text);

				chrome.tabs.executeScript(null, {file:'js/contentWorker.js'});
				
				chrome.tabs.executeScript(null, {code:"console.log('ppcoder:: FUNCTION: " + title + "');"});
				chrome.tabs.executeScript(null, {code:"console.log('ppcoder:: VALUE:');"});
				window.setTimeout(function(){
                    chrome.tabs.executeScript(
                        null, 
                        {code:"ppcontent.logConsole('" + text + "');"}
                    );
                },400);
				
				break;
			case 'alert': 
				alert(title + '\n\n' + text);
				console.log(text);
				break;
			case 'div':
				chrome.tabs.insertCSS(null, {file: "styles/content.css"});
				chrome.tabs.executeScript(null, {file:'js/contentWorker.js'});
				
                window.setTimeout(function() {
                    text = pp.base64_encode(text);
					chrome.tabs.executeScript(
                        null, 
                        {code:"ppcontent.createDiv('" + title + "', '" + text + "');"}
                    );
                },400);

                break;
            case 'inplace':
				chrome.tabs.executeScript(null, {file:'js/contentWorker.js'});
				
                window.setTimeout(function() {
                    text = pp.base64_encode(text);
					chrome.tabs.executeScript(
                        null, 
                        {code:"ppcontent.replaceText('" + text + "');"}
                    );
                },400);
                break;                
			default:
			case 'notification':
				var popup = window.webkitNotifications.createNotification( pp.icon, title, text);
				popup.show();
				break;
		}	
	},
	copyToClipboard: function(text) {
		var bg = chrome.extension.getBackgroundPage();
		var clipboard = bg.document.getElementById("clipboard");
		clipboard.style.display = "block";
		clipboard.value = text;
		clipboard.select();
		bg.document.execCommand("Copy");
		clipboard.style.display = "none";
        return true;
	},
	rot13decode: function(text) 
	{
		var keycode	= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		var textrot	= new String();

		for(var i = 0; i < text.length; i++)
		{
			var codechar = text.substring(i, i + 1);
			var pos = keycode.indexOf(codechar.toUpperCase());

			if(pos >= 0)
			{
				pos = (pos + keycode.length / 2) % keycode.length;
				codechar = (codechar == codechar.toUpperCase()) ? keycode.substring(pos, pos + 1) : keycode.substring(pos, pos + 1).toLowerCase();
			}
			textrot	= textrot + codechar;
		}
			
		return textrot;
	},

	menus: false,
	
	menuLoadTime: 1000,
	
	createContextMenu: function() {
	var changed = false,
            createMenu = function(name, infotext, ptFunction) {
                var menu;

                if(localStorage.getItem("functions_" + name) == '1' && !pp.menuIds[name]) {
                    // Menu for selected text
                    menu = {
                        "title"     : infotext, 
                        "contexts"  : ["selection", "editable"],
                        "onclick"   : function (info, tab) {
                            pp.createPopup(infotext, ptFunction(info.selectionText));
                        } 
                    };
                    pp.menuIds[name]=chrome.contextMenus.create(menu);

                    // Menu for normal page
                    menu = {
                        "title"     : infotext, 
                        "contexts"  : ["page"],
                        "onclick"   : function (info, tab) {

                            var bg = chrome.extension.getBackgroundPage(),
                                clipboard = bg.document.getElementById("clipboard"),
                                clipboardText;

                            clipboard.style.display = "block";
                            clipboard.select();
                            bg.document.execCommand("Paste");
                            clipboardText = clipboard.value;
                            clipboard.style.display = "none";

                            pp.copyToClipboard(ptFunction(clipboardText));
                        } 
                    };
                    pp.menuIds[name]=chrome.contextMenus.create(menu);

                    changed = true;
                } else if(localStorage.getItem("functions_" + name) == '0' && pp.menuIds[name]) {
                    console.log(pp.menuIds[name]);
                    chrome.contextMenus.remove(pp.menuIds[name]);
                    pp.menuIds[name] = null;
                }
            };

        pp.menus = true;
	    
        /**
         * MENU ITEM DEFINITIONS
    	 */
    	createMenu('rot13',                     'Rot13 Decode',                      pp.rot13decode);

    }
};
