;(function($) {
  $(function() {
    $('textarea.sourceCodeWidget').each(function() {
      var $el = $(this);
      var $form = $(this.form);
      var editorData = $el.data('tn.ploneformwidget.sourcecode.editorData');

      var textareaId = $el.attr('id');
      var id = 'editor-' + textareaId;

      var name = $el.attr('name');
      var contents = $el.val();

      $el.after('<div id="' + id + '"></div>');

      $('#' + id).css({
        height: editorData.height,
        position: 'relative',
        width: '100%'
      });

      var editor = ace.edit(id);
      var session = editor.getSession()
      editor.setTheme('ace/theme/' + editorData.theme);
      session.setMode('ace/mode/' + editorData.mode);
      session.setValue(contents);

      $form.submit(function() {
        var contents = editor.getSession().getValue();
        $form.append('<textarea id="' + textareaId +
                     '" name="' + name + '"></textarea>');
        $('#' + textareaId, $form).hide().val(contents);
      });

      $el.remove();
    });
  });
})(jQuery);
