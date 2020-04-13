from django.db import models

from wagtail.core.models import Page
from wagtailtrans.models import TranslatablePage
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class LandingPage(TranslatablePage):
    body = StreamField([
        ('hero', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(required=False, help_text="Fill if you want this section added in page navigation",)),
            ('headline', blocks.CharBlock()),
            ('lead', blocks.CharBlock(required=False)),
            ('content', blocks.RichTextBlock()),
            ('hero_image', ImageChooserBlock(required=False)),
        ], icon='image')),
        ('content_section', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(required=False, help_text="Fill if you want this section added in page navigation",)),
            ('content', blocks.RichTextBlock()),
            ('section_image', ImageChooserBlock(required=False))
        ], icon='doc-full-inverse')),
        ('features_list', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(required=False, help_text="Fill if you want this section added in page navigation",)),
            ('headline', blocks.CharBlock()),
            ('features', blocks.ListBlock(
                blocks.StructBlock([
                    ('title', blocks.CharBlock()),
                    ('image', ImageChooserBlock()),
                    ('description', blocks.RichTextBlock()),
                ], icon='doc-full-inverse')
            , icon='table')),
        ])),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
