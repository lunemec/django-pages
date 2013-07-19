CKEDITOR.on( 'dialogDefinition', function( ev )
{
// Take the dialog name and its definition from the event data.
var dialogName = ev.data.name;
var dialogDefinition = ev.data.definition;

// Check if the definition is from the dialog window you are interested in (the "Image" dialog window).
if ( dialogName == 'image' )
{
// Get a reference to the "Image Advanced" tab.
var infoTab = dialogDefinition.getContents( 'advanced' );

//var cssField = infoTab.get( 'txtGenClass' );
//cssField['default'] = 'lightbox';

var linkTab = dialogDefinition.getContents( 'info' );
var link = linkTab.get( 'txtUrl' );

//var advancedTab = dialogDefinition.getContents('advanced');
//var relField = advancedTab.get('')

    link['onChange'] = function(evt){
        var dialog = CKEDITOR.dialog.getCurrent();
        dialog.getContentElement('Link', 'txtUrl').setValue(dialog.getContentElement('info', 'txtUrl').getValue());
    }

}
});

window.onload = function() {

    var tas = document.getElementsByTagName('textarea');

    for(var i=0;i<tas.length;i++)
    {   
        CKEDITOR.replace(tas[i].id, 
                    {
                        filebrowserBrowseUrl :'/static/admin/js/ckeditor/filemanager/browser/default/browser.html?Connector=/connector/browser/?',
                        filebrowserImageBrowseUrl : '/static/admin/js/ckeditor/filemanager/browser/default/browser.html?Connector=/connector/browser/?',
                    });
    }
    
}
