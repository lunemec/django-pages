window.onload = function() {
	CKEDITOR.replaceAll( function(textarea, config) {
        config.autoGrow_onStartup = true;
        config.filebrowserBrowseUrl = '/admin/filebrowser/browse/?pop=3';
        config.filebrowserWindowWidth  = 1000;
        config.filebrowserWindowHeight = 800;
        config.language = 'cs';
        config.extraPlugins = 'autogrow,popup,filebrowser,preview';
        config.removePlugins = 'about';
        config.font_names = 'AlternateGothicFSNo1, Arial;' + 'Arial;';
    });
}
