from __future__ import absolute_import, unicode_literals

from django.db import models

from django.db import models
from django import forms

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index

from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock, DateTimeBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel,MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel

# Image size choice
SIZE_CHOICES = (
    ('auto', "Auto"),
    ('cover', "Cover"),
    ('50%', "Small"),
    ('200%', "Large"),
)

 # Image size choice in %
PERCENT_CHOICES = (
    ('10%', "10%"),
    ('20%', "20%"),
    ('30%', "30%"),
    ('40%', "40%"),
    ('50%', "50%"),
    ('60%', "60%"),
    ('70%', "70%"),
    ('80%', "80%"),
    ('90%', "90%"),
    ('100%', "100%"),
)

COLOUR_CHOICES = (
    ('white', "White"),
    ('black', "Black"),
)

# Text alignment choice
ALIGN_CHOICES = (
    ('left', "Left"),
    ('right', "Right"),
    ('center', "Centre"),
)

class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True

class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))

class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()

class GoogleMapBlock(blocks.StructBlock):
    map_long = blocks.CharBlock(required=True,max_length=255)
    map_lat = blocks.CharBlock(required=True,max_length=255)
    map_zoom_level = blocks.CharBlock(default=14,required=True,max_length=3)

    class Meta:
        template = 'home/includes/google_map.html'
        icon = 'cogs'
        label = 'Google Map'

class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"

# One column block

class OneColumnBlock(blocks.StructBlock):

    back_image = ImageChooserBlock(blank=True)
    background_size = blocks.ChoiceBlock(choices=SIZE_CHOICES,default="auto")
    background_x_position = blocks.ChoiceBlock(choices=PERCENT_CHOICES,default="50%")
    background_y_position = blocks.ChoiceBlock(choices=PERCENT_CHOICES,default="50%")
    text_align = blocks.ChoiceBlock(choices=ALIGN_CHOICES,default="center")
    one_column = blocks.StreamBlock([
           ('heading', blocks.CharBlock(classname="full title")),
           ('paragraph', blocks.RichTextBlock()),
        ], icon='arrow-left', label='Parallax content')

    class Meta:
        template = 'home/includes/one_column_block.html'
        icon = 'placeholder'
        label = 'Parallax Column'


# Two column block

class TwoColumnBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="white")
    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'home/includes/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'

# Three column block

class ThreeColumnBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="white")
    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-left', label='Left column content')

    center_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-right', label='Center column content')

    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
        ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'home/includes/three_column_block.html'
        icon = 'placeholder'
        label = 'Three Columns'

class HomeStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    pullquote = PullQuoteBlock()
    one_column = OneColumnBlock()
    two_columns = TwoColumnBlock()
    three_columns = ThreeColumnBlock()
    embedded_video = EmbedBlock(icon="media")
    google_map = GoogleMapBlock()

# Carousel items

class CarouselItem(LinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField("Embed URL", blank=True)
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.HomePage', related_name='carousel_items')



#Home Page

class HomePage(Page):
    noticias = RichTextField(blank=True)
    body = RichTextField(blank=True)
    videos = StreamField(HomeStreamBlock())
    
    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('noticias'),
        index.SearchField('title'),
        index.SearchField('videos'),
    ]

    class Meta:
        verbose_name = "Homepage"

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('noticias', classname="noticias"),
    FieldPanel('body'),
    StreamFieldPanel('videos'),
    InlinePanel('carousel_items', label="Carousel items"),
]

HomePage.promote_panels = Page.promote_panels

class HomePageCarouselItem():
    image = models.ForeignKey('wagtailimages.Image')
    embed_url = models.URLField("Embed URL", blank=True)
    caption = models.CharField(max_length=255, blank=True)
    page = ParentalKey('HomePage', related_name='carousel_items')

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
    ]


#Bio page

class BioPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField(HomeStreamBlock())
    image1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(max_length=255, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('image1'),
        index.SearchField('image2'),
        index.SearchField('image3'),
        index.SearchField('caption')
    ]

    content_panels = Page.content_panels + [
    
    	FieldPanel('intro', classname="full"),
    	StreamFieldPanel('body'),
    	ImageChooserPanel('image1'),
    	ImageChooserPanel('image2'),
    	ImageChooserPanel('image3'),
    	# FieldPanel('body', classname="full"),
    	

    ]

# Local (Onde nos encontrar)
class LocalPage(Page):
	intro = models.CharField(max_length=250)
	body = StreamField(HomeStreamBlock())

	search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

	content_panels = Page.content_panels + [
    
    	FieldPanel('intro', classname="full"),
    	StreamFieldPanel('body'),
    ]

# Contact page

class ContactFields(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel('telephone'),
        FieldPanel('email'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('post_code'),
    ]

    class Meta:
        abstract = True

class ContactPage(Page, ContactFields):
    intro = RichTextField(blank=True)
    text = RichTextField(blank=True)
    body = StreamField(HomeStreamBlock())
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('intro'),
        index.SearchField('text'),
    ]

ContactPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    FieldPanel('text', classname='text'),
    StreamFieldPanel('body'),
    MultiFieldPanel(ContactFields.panels, "Contact"),
]

ContactPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')



class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)


FormPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel('form_fields', label="Form fields"),
    FieldPanel('thank_you_text', classname="full"),
    MultiFieldPanel([
        FieldPanel('to_address', classname="full"),
        FieldPanel('from_address', classname="full"),
        FieldPanel('subject', classname="full"),
    ], "Email")
]


# Related links
class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True

class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


#Person Page
class PersonPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.PersonPage', related_name='related_links')


class PersonPage(Page, ContactFields):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    intro = RichTextField(blank=True)
    biography = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
        index.SearchField('intro'),
        index.SearchField('biography'),
    ]

PersonPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('first_name'),
    FieldPanel('last_name'),
    FieldPanel('intro', classname="full"),
    FieldPanel('biography', classname="full"),
    ImageChooserPanel('image'),
    MultiFieldPanel(ContactFields.panels, "Contact"),
    InlinePanel('related_links', label="Related links"),
]

PersonPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]

class EquipePage(Page):
    intro = RichTextField(blank=True)
    body = StreamField(HomeStreamBlock())
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
    
        FieldPanel('intro', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]

class SubequipePage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    image1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image4 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    bio1 = RichTextField(blank=True)
    bio2 = RichTextField(blank=True)
    bio3 = RichTextField(blank=True)
    bio4 = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('image1'),
        index.SearchField('image2'),
        index.SearchField('image3'),
        index.SearchField('image4'),
        index.SearchField('bio1'),
        index.SearchField('bio2'),
        index.SearchField('bio3'),
        index.SearchField('bio4'),
    ]

    content_panels = Page.content_panels + [
    
        FieldPanel('intro', classname="full"),
        FieldPanel('body'),
        ImageChooserPanel('image1'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image3'),
        ImageChooserPanel('image4'),
        FieldPanel('bio1'),
        FieldPanel('bio2'),
        FieldPanel('bio3'),
        FieldPanel('bio4'),
    ]


# Agenda Index Page

class AgendaIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(AgendaIndexPage, self).get_context(request)
        eventos = self.get_children().live().order_by('-first_published_at')
        context['eventos'] = eventos
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class AgendaPage(Page):
    intro = RichTextField(blank=True)
    date = models.DateTimeField(auto_now=False)
    body = RichTextField(blank=True)
    local = RichTextField()
    mapa = StreamField(HomeStreamBlock())
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('date'),
        index.SearchField('local'),
        
    ]

    content_panels = Page.content_panels + [
    
        FieldPanel('intro', classname="full"),
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('local'),
        StreamFieldPanel('mapa'),
        ImageChooserPanel('image'),
    ]


