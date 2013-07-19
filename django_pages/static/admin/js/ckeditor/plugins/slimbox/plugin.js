/*
Copyright (c) 2003-2009, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

/**
 * @file Slimbox plugin.
 */

(function() {
	var pluginName = 'slimbox';

	// Регистрируем имя плагина .
	CKEDITOR.plugins.add( pluginName, {
		init : function( editor ) {
			// Добавляем команду на нажатие кнопки
			editor.addCommand( pluginName,new CKEDITOR.dialogCommand( 'slimbox' ));
			// Указываем где скрипт окна диалога.
			CKEDITOR.dialog.add( pluginName, this.path + 'dialogs/slimbox.js' );
			// Добавляем кнопочку
			editor.ui.addButton( 'slimbox', {
				label : 'Create Lightbox', //Title кнопки
				command : pluginName,
				icon : this.path + 'logo.gif' //Путь к иконке
			});
		}
	});
})();
