from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.blocks import StructBlock, PageChooserBlock, StaticBlock

from wagtail.wagtailadmin.edit_handlers import FieldPanel

class HeadingandSubHeadingBlock(StructBlock):
    heading = blocks.CharBlock()
    subheading = blocks.CharBlock(required=False)

class ArticlePreviewBlock(StructBlock):
    title = blocks.CharBlock(classname="full title")
    excerpt = blocks.RichTextBlock()
    image = ImageChooserBlock()
    link_page = PageChooserBlock()

    class Meta:
        icon = "cogs"

class TextImageBlock(StructBlock):
    title = blocks.CharBlock(required=False, classname="full title")
    text = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        icons = "cogs"

class ThreeColumnBlock(StructBlock):
    first_column = TextImageBlock()
    second_column = TextImageBlock()
    third_column = TextImageBlock()

class PreviousBlogsBlock(StaticBlock):

    class Meta:
        icons = "cogs"

class StandardPage(Page):
    #body_rich = RichTextField(null=True, blank=True)

    body = StreamField([
        ('block_heading', HeadingandSubHeadingBlock(classname="full title")),
        ('paragraph_text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('article_preview', ArticlePreviewBlock()),
        ('words_and_images', TextImageBlock()),
        ('video', EmbedBlock()),
        ('three_column_content', ThreeColumnBlock()),
        ('previous_blogs', PreviousBlogsBlock())
    ])
    #header_image = models.ForeignKey(
    #    'wagtailimages.Image',
    #    null=True,
    #    blank=True,
    #    on_delete=models.SET_NULL,
    #    related_name='+'
    #)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
