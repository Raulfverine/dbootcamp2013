<script type="text/javascript">
    function CopyHTMLToClipboard() {    
        if (document.body.createControlRange) {
            var htmlContent = document.getElementById('MainContent_lblHtml');
            var controlRange;

            var range = document.body.createTextRange();
            range.moveToElementText(htmlContent);

            //Uncomment the next line if you don't want the text in the div to be selected
            range.select();

            controlRange = document.body.createControlRange();
            controlRange.addElement(htmlContent);

            //This line will copy the formatted text to the clipboard
            controlRange.execCommand('Copy');         

            alert('Your HTML has been copied\n\r\n\rGo to Word and press Ctrl+V');
        }
    }    
</script>