from django.utils.html import escape
from wagtail.core import hooks
from wagtail.core.rich_text import LinkHandler
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler, InlineStyleElementHandler
from draftjs_exporter.dom import DOM

class NewWindowExternalLinkHandler(LinkHandler):
    identifier = 'external'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs["href"]
        return '<a href="%s" target="_blank" rel="noopener noreferrer">' % escape(href)

class ObfuscateEmail(LinkHandler):
    # TODO: Add email obfuscator here
    identifier = 'email'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs["href"]
        return '<a href="%s" class="email-link">' % escape(href)


@hooks.register('register_rich_text_features')
def register_external_link(features):
    features.register_link_type(NewWindowExternalLinkHandler)

@hooks.register('register_rich_text_features')
def register_email_link(features):
    features.register_link_type(ObfuscateEmail)


# Rich text language switch
@hooks.register('register_rich_text_features')
def register_lang_feature(features):
    feature_name = 'lang'
    type_ = 'LANG'
    tag = 'span'
    langIcon = ['M962.8,19.4c3.9,0.5,7.6,1.2,11.3,2.5c12.2,4.4,22,14.2,26.5,26.5c1.8,4.9,2.4,9.9,2.7,15.1v708.3c-0.2,5.2-0.9,10.2-2.7,15.1c-4.4,12.2-14.2,22-26.5,26.5c-4.9,1.7-9.9,2.4-15.1,2.7H618.3L363.8,985.7l-3.3,2c-5.8,2.9-11.7,4.9-18.2,5.4c-18.1,1.2-35.7-9.1-43.3-25.6c-2.7-5.9-3.8-12.1-4.1-18.5V816H73.6l-3.8-0.2c-5.2-0.7-10.1-1.7-14.9-4c-11.7-5.5-20.7-16.1-24-28.6c-1-3.8-1.3-7.6-1.5-11.5V63.4c0.2-5.2,0.9-10.2,2.7-15.1c4.4-12.2,14.2-22,26.5-26.5c4.9-1.8,9.9-2.4,15.1-2.7C370.1,19.2,669.5,19.3,962.8,19.4L962.8,19.4zM117.9,107.7v619.8h221.3c5.2,0.2,10.2,0.9,15.1,2.7c12.2,4.5,22,14.3,26.5,26.5c1.8,5,2.4,9.9,2.7,15.1v94.3l196.8-131.2l3.2-2c3.4-1.7,6.7-3.2,10.4-4.1c3.6-1,7.3-1.2,11-1.4h309.9V107.7L117.9,107.7zM648.7,239.1c-0.1-15.1-0.1-30.1,0.5-45.1c0.2-4.2,1-8.3,2.4-12.3c3.9-11.1,12.3-20.5,23-25.5c4.5-2.1,9.3-3.4,14.2-3.9c1.9-0.2,3.8-0.2,5.7-0.2c5,0.2,9.8,1.1,14.5,2.8c12.2,4.6,21.9,14.6,26.2,26.9c1.5,4.4,2.3,8.9,2.4,13.4c0.2,14.7,0.5,29.3,0.5,44c30,0.2,60.1,0.7,90.2,1.5c6.5,0.5,12.7,2,18.5,5.1c5,2.6,9.5,6.3,13.2,10.6c3.2,3.8,5.8,8.2,7.6,12.8c1.5,4,2.4,8.2,2.7,12.5c1.2,16.6-7.3,32.9-21.7,41.3c-6.2,3.7-13.1,5.5-20.3,6.1l-4,0.1c-0.6,6.6-1.2,13.2-2.1,19.7c-1,7.8-2.1,15.4-3.4,23.1c-8.7,51-25.4,101-49.6,146.8c12.9,7.9,26.4,15.1,40.1,21.5c6.9,3.2,13.9,6.2,21,8.9c4,1.5,8.1,2.9,12.1,4.4c1.8,0.7,1.8,0.7,3.6,1.6c7,3.7,12.9,8.8,17.3,15.5c2.4,3.9,4.3,8.1,5.5,12.5c3.8,14,0.4,29.3-9.1,40.4c-2.9,3.4-6.5,6.4-10.4,8.8c-8.9,5.5-19.7,7.7-30.1,6.1c-5.6-0.9-10.9-2.9-16.1-4.9c-21.5-7.9-42.3-17.8-62.3-28.9c-6.8-3.8-13.6-7.8-20.3-11.9c-14,17.3-29.4,33.5-46,48.4c-14.2,12.7-29.3,24.2-45.2,34.8c-2.1,1.3-2.1,1.2-4.3,2.4c-6,2.9-12.4,4.7-19.1,4.9c-5.8,0.1-11.6-0.9-17.1-3c-4.6-1.7-8.9-4.3-12.7-7.5c-14.2-12-19.3-32.3-12.7-49.7c3-7.9,8.2-14.3,14.7-19.5c4.7-3.3,9.5-6.5,14.2-9.8c10.7-7.9,20.9-16.4,30.5-25.6c9.3-8.8,18-18.1,26.1-28c-22.3-19.4-42.9-40.9-60.3-64.7c-6.8-9.3-13.2-19-18.8-29.1c-3.4-6.1-6.9-12.3-8.4-19.2c-3.1-14.2,1.1-29.3,11.1-39.9c3.2-3.3,6.8-6.1,10.8-8.3c5.8-3.2,12.1-4.9,18.7-5.4c2-0.1,2-0.1,3.9-0.1c3.3,0.2,6.5,0.6,9.7,1.4c11,2.8,20.1,9.7,26.3,19.1c2.4,3.9,4.4,8.1,6.8,12c13.1,21.9,30,41.3,48.6,58.6c13.6-28.2,23.8-58.1,30.4-88.7c3.2-14.9,5.6-30.1,7.3-45.3c-58.9,0.5-117.9,0-176.8-1.5c-7.2-0.5-14.1-2.4-20.3-6.1c-14.4-8.5-23-24.7-21.7-41.3c0.3-4.3,1.2-8.5,2.7-12.5c1.8-4.6,4.4-9,7.6-12.8c3.7-4.4,8.2-8,13.2-10.6c5.8-3.1,12-4.6,18.4-5.1C588.5,239.9,618.6,239.4,648.7,239.1L648.7,239.1zM338.1,240.6c0.9,0,1.9,0,2.8,0c0.2,0,0.5,0,0.6,0h0.6c3.9,0.4,7.6,1,11.3,2.3c1.3,0.4,2.5,0.9,3.7,1.5c0.5,0.2,1,0.4,1.5,0.7c1.6,0.7,3.1,1.6,4.6,2.6c4.1,2.7,7.7,5.9,10.7,9.8c1.9,2.4,3.5,5.1,4.9,7.8c47.3,102.8,89.2,208,133.8,312c2.9,7.3,4.2,14.9,3.3,22.7c-1.9,15.6-12.2,29.3-26.5,35.5c-4.3,1.8-8.8,2.9-13.4,3.4c-5.4,0.5-10.9,0-16.1-1.5c-5.2-1.5-10.1-3.9-14.5-7.1c-5.6-4.3-9.9-9.7-13.2-15.9c-9.7-21-19.2-42.2-28.5-63.4c-43.4,0.6-86.8,0.6-130.2,0c-8.9,20.4-17.8,40.8-26.6,61.3c-3.3,7.1-7.9,13.3-14.2,18c-3.7,2.7-7.9,4.9-12.2,6.4c-14.9,5.1-31.6,1.7-43.5-8.6c-4.1-3.5-7.5-7.8-10-12.7c-2.5-4.8-4.1-10-4.8-15.4c-0.8-7,0.2-13.9,2.4-20.5c41.8-105.1,89.1-208.1,133.6-312.1c1.3-2.8,2.7-5.5,4.5-8.1c2.8-4,6.2-7.5,10.2-10.3c1.4-1,2.9-2,4.4-2.9c0.5-0.2,1-0.5,1.5-0.8c1.2-0.6,2.4-1.1,3.7-1.6c3.6-1.5,7.3-2.3,11.2-2.9c0.2,0,0.4,0,0.6,0c0.2,0,0.4,0,0.6-0.1C336.2,240.6,337.1,240.6,338.1,240.6L338.1,240.6zM339.6,399.5c-8.8,20.5-17.7,41-26.6,61.5c17.5-0.1,34.9-0.1,52.5,0C356.8,440.6,348.2,420,339.6,399.5z']
    # Icon Language by Explanaicon, Noun Project

    control = {
        'type': type_,
        'description': 'Text in different language',
        'icon': langIcon,
        'style': {'backgroundColor': 'Linen'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: {'element': tag, 'props': {'lang': 'unknown'}}}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    # Add the feature to the default features list
    features.default_features.append('lang')
