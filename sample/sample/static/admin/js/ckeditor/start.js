window.onload = function() {
	CKEDITOR.replaceAll({}, {
        filebrowserBrowseUrl : '/admin/filebrowser/browse/?pop=3',
    filebrowserUploadUrl : '/admin/filebrowser/upload/',
    filebrowserImageBrowseUrl : '/admin/filebrowser/browse/?&filter_type=Image',
    filebrowserImageUploadUrl : '/admin/filebrowser/upload/',
    filebrowserWindowWidth  : 800,
    filebrowserWindowHeight : 500
    });
}
