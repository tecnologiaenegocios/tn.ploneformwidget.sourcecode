from Products.CMFCore.utils import getToolByName
from z3c.form import interfaces as z3cforminterfaces
from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.browser.widget import addFieldClass
from z3c.form.widget import FieldWidget
from zope.schema.interfaces import ISourceText

import zope.component
import zope.interface
import zope.schema


class ISourceCodeWidget(z3cforminterfaces.ITextAreaWidget):

    editor_mode = zope.schema.TextLine(
        title=u'Editor mode',
        description=u'One of the available Ace modes',
        default=u'text'
    )

    editor_theme = zope.schema.TextLine(
        title=u'Editor theme',
        description=u'One of the available Ace themes',
        default=u'textmate'
    )

    editor_height = zope.schema.TextLine(
        title=u'Editor height',
        description=u'CSS value for height property of editor area',
        default=u'400px',
    )


class SourceCodeWidget(TextAreaWidget):
    zope.interface.implementsOnly(ISourceCodeWidget)

    klass = u'sourceCodeWidget'
    value = None
    editor_mode = ISourceCodeWidget['editor_mode'].default
    editor_theme = ISourceCodeWidget['editor_theme'].default
    editor_height = ISourceCodeWidget['editor_height'].default

    _adapterValueAttributes = TextAreaWidget._adapterValueAttributes
    _adapterValueAttributes += ('editor_mode', 'editor_theme', 'editor_height')

    def update(self):
        super(SourceCodeWidget, self).update()
        addFieldClass(self)
        base_url = (
            self.get_portal_url() +
            '/++resource++tn.ploneformwidget.sourcecode/'
        )
        self.js_files = [
            (base_url + filename)
            for filename in (
                'ace/ace.js',
                'widget.js',
            )
        ]

    def get_portal_url(self):
        return getToolByName(self.context, 'portal_url')()

    def js_params(self):
        return u"""<script type="text/javascript">//<![CDATA[
        jQuery(function() {
            jQuery('#' + '%(id)s').data('tn.ploneformwidget.sourcecode.editorData', {
                mode:   '%(mode)s',
                theme:  '%(theme)s',
                height: '%(height)s',
            });
        });//]]></script>""" % (dict(
            id=self.id,
            mode=self.editor_mode,
            theme=self.editor_theme,
            height=self.editor_height,
        ))


@zope.component.adapter(ISourceText, z3cforminterfaces.IFormLayer)
@zope.interface.implementer(z3cforminterfaces.IFieldWidget)
def SourceCodeFieldWidget(field, request):
    """IFieldWidget factory for CodeWidget."""
    return FieldWidget(field, SourceCodeWidget(request))
