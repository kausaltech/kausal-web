from django.db import models

from wagtail.core.models import Page
from wagtailtrans.models import TranslatablePage
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class LandingPage(TranslatablePage):
    body = StreamField([
        ## Hero Section
        ('hero', blocks.StructBlock([
            ('in_navigation',
                blocks.CharBlock(
                required=False,
                help_text="Fill if you want this section added in page navigation",)
            ),
            ('lead', blocks.CharBlock(required=False)),
            ('headline', blocks.CharBlock()),
            ('content', blocks.RichTextBlock(required=False)),
            ('cta_link', blocks.CharBlock(required=False, help_text="Link (# or url) to CTA content")),
            ('cta_button', blocks.CharBlock(required=False, help_text="CTA Button text")),
            ('hero_image', ImageChooserBlock(required=False)),
        ], icon='home', template='landing/blocks/hero.html',
        help_text="Front page main hero section",)),
        ## Basic Content Section
        ('content_section', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(
                required=False,
                help_text="Fill if you want this section added in page navigation",)
            ),
            ('headline', blocks.CharBlock(required=False)),
            ('lead', blocks.CharBlock(required=False)),
            ('content', blocks.RichTextBlock()),
            ('section_image', ImageChooserBlock(required=False))
        ], icon='doc-full-inverse', template='landing/blocks/content_section.html',
        help_text="Basic content section")),
        ## Product Features Section
        ('features_list', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(
                required=False,
                help_text="Fill if you want this section added in page navigation",)
            ),
            ('headline', blocks.CharBlock()),
            ('lead', blocks.CharBlock(required=False)),
            ('content', blocks.RichTextBlock(required=False)),
            ('features', blocks.ListBlock(
                blocks.StructBlock([
                    ('title', blocks.CharBlock()),
                    ('image', ImageChooserBlock()),
                    ('description', blocks.RichTextBlock()),
                ],
                icon='radio-full')
            , template='landing/blocks/features.html')),
        ], icon='list-ul', template='landing/blocks/features_list.html',
        help_text="Product Features Section")),
        ## Contact Section
        ('contact_section', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(
                required=False,
                help_text="Fill if you want this section added in page navigation",)
            ),
            ('headline', blocks.CharBlock(required=False)),
            ('lead', blocks.CharBlock(required=False)),
            ('content', blocks.RichTextBlock()),
            ('section_image', ImageChooserBlock(required=False))
        ], icon='mail', template='landing/blocks/contact_section.html',
        help_text="Contact Section")),
        ## Team Section
        ('team_list', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(
                required=False,
                help_text="Fill if you want this section added in page navigation",)
            ),
            ('headline', blocks.CharBlock()),
            ('lead', blocks.CharBlock(required=False)),
            ('content', blocks.RichTextBlock(required=False)),
            ('team_members', blocks.ListBlock(
                blocks.StructBlock([
                    ('name', blocks.CharBlock()),
                    ('work_title', blocks.CharBlock()),
                    ('image', ImageChooserBlock(required=False)),
                    ('description', blocks.RichTextBlock(required=False)),
                ],
                icon='user')
            ,template='landing/blocks/team_member.html', required=False)),
        ], icon='group', template='landing/blocks/team_members.html',
        help_text="Section for displaying a list of persons")),
        ## Announcement Section
        ('announcement_section', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(
                required=False,
                help_text="Fill if you want this section added in page navigation",)
            ),
            ('headline', blocks.CharBlock(required=False)),
            ('lead', blocks.CharBlock(required=False)),
            ('content', blocks.RichTextBlock()),
            ('section_image', ImageChooserBlock(required=False))
        ], icon='warning', template='landing/blocks/announcement_section.html',
        help_text="Banner section for special announcements")),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
