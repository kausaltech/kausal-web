from django.db import models

from django.db.models import CharField
from wagtail.core.models import Page
from wagtailtrans.models import TranslatablePage
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

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
       ## Testimonials Section
        ('testimonials_section', blocks.StructBlock([
            ('in_navigation', blocks.CharBlock(
                required=False,
                help_text="Fill if you want this section added in page navigation",)
            ),
            ('headline', blocks.CharBlock(required=False)),
            ('lead', blocks.CharBlock(required=False)),
            ('content', blocks.RichTextBlock(required=False)),
            ('testimonials', blocks.ListBlock(
                blocks.StructBlock([
                    ('content', blocks.RichTextBlock()),
                    ('name', blocks.CharBlock()),
                    ('title', blocks.CharBlock(required=False)),
                    ('organization', blocks.CharBlock(required=False)),
                    ('image', ImageChooserBlock()),
                ],
                icon='radio-full')
            , template='landing/blocks/testimonials_list.html')),
        ], icon='openquote', template='landing/blocks/testimonials_section.html',
        help_text="Testimonials Section")),
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

class calendyPage(TranslatablePage):

    # Database fields

    cta_text = CharField(
        max_length=255,
        help_text="Call to action on button")
    blurb = RichTextField()
    body = RichTextField()
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    calendy_link = CharField(max_length=255)

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('blurb', classname="full"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('main_image'),
        FieldPanel('calendy_link', classname="full"),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('cta_text', classname="full"),
    ]

    # Parent page / subpage type rules

    parent_page_types = ['landing.LandingPage']
    subpage_types = []
