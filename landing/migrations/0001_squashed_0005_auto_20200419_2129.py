# Generated by Django 3.0.5 on 2020-04-19 23:41

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    replaces = [('landing', '0001_initial'), ('landing', '0002_auto_20200419_1820'), ('landing', '0003_auto_20200419_1821'), ('landing', '0004_auto_20200419_2127'), ('landing', '0005_auto_20200419_2129')]

    initial = True

    dependencies = [
        ('wagtailtrans', '0009_create_initial_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('body', wagtail.core.fields.StreamField([('hero', wagtail.core.blocks.StructBlock([('in_navigation', wagtail.core.blocks.CharBlock(help_text='Fill if you want this section added in page navigation', required=False)), ('lead', wagtail.core.blocks.CharBlock(required=False)), ('headline', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('cta_link', wagtail.core.blocks.CharBlock(help_text='Link (# or url) to CTA content', required=False)), ('cta_button', wagtail.core.blocks.CharBlock(help_text='CTA Button text', required=False)), ('hero_image', wagtail.images.blocks.ImageChooserBlock(required=False))], help_text='Front page main hero section', icon='home', template='landing/blocks/hero.html')), ('content_section', wagtail.core.blocks.StructBlock([('in_navigation', wagtail.core.blocks.CharBlock(help_text='Fill if you want this section added in page navigation', required=False)), ('headline', wagtail.core.blocks.CharBlock(required=False)), ('lead', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock()), ('section_image', wagtail.images.blocks.ImageChooserBlock(required=False))], help_text='Basic content section', icon='doc-full-inverse', template='landing/blocks/content_section.html')), ('features_list', wagtail.core.blocks.StructBlock([('in_navigation', wagtail.core.blocks.CharBlock(help_text='Fill if you want this section added in page navigation', required=False)), ('headline', wagtail.core.blocks.CharBlock()), ('lead', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.RichTextBlock())], icon='radio-full'), template='landing/blocks/features.html'))], help_text='Product Features Section', icon='list-ul', template='landing/blocks/features_list.html')), ('contact_section', wagtail.core.blocks.StructBlock([('in_navigation', wagtail.core.blocks.CharBlock(help_text='Fill if you want this section added in page navigation', required=False)), ('headline', wagtail.core.blocks.CharBlock(required=False)), ('lead', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock()), ('section_image', wagtail.images.blocks.ImageChooserBlock(required=False))], help_text='Contact Section', icon='mail', template='landing/blocks/contact_section.html')), ('team_list', wagtail.core.blocks.StructBlock([('in_navigation', wagtail.core.blocks.CharBlock(help_text='Fill if you want this section added in page navigation', required=False)), ('headline', wagtail.core.blocks.CharBlock()), ('lead', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)), ('team_members', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('work_title', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False))], icon='user'), template='landing/blocks/team_member.html'))], help_text='Section for displaying a list of persons', icon='group', template='landing/blocks/team_members.html')), ('announcement_section', wagtail.core.blocks.StructBlock([('in_navigation', wagtail.core.blocks.CharBlock(help_text='Fill if you want this section added in page navigation', required=False)), ('headline', wagtail.core.blocks.CharBlock(required=False)), ('lead', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock()), ('section_image', wagtail.images.blocks.ImageChooserBlock(required=False))], help_text='Banner section for special announcements', icon='warning', template='landing/blocks/announcement_section.html'))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
    ]
