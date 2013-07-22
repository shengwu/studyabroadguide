import logging
import os
from django import template
from django.conf import settings

__all__  = (
    'asset',
)
register = template.Library()
logger   = logging.getLogger(__name__)
TAGS     = {
    '.js':  u'<script src="{file}"{attr}></script>',
    '.properties':  u'<link rel="resource" type="application/l10n" href="{file}"{attr} />',
    '.css': u'<link  href="{file}" rel="stylesheet" media="{media}"{attr}/>',
}

class AssetBadTypeException(Exception):
    """Unrecognized asset type."""
class AssetNotFoundException(Exception):
    """Asset file was not found."""

@register.simple_tag(takes_context=True)
def asset(context, asset_name, media=None, defer=None):
    """Smart generation of HTML inclusion strings (<script> <link> etc)
    (currently not) including a cache-busting mechanism."""

    asset_type      = os.path.splitext(asset_name)[1]
    external_asset  = asset_name.startswith(('http', '//'))
    attrs           = {}
    if defer:
        attrs[defer] = 'defer'
    attr = u' '.join([u'%s="%s"' % (k, v) for (k, v) in attrs.iteritems()])
    tag_args = {'media': media or 'screen',
                'attr':  (' ' + attr) if attr else ''}

    if asset_type not in TAGS.keys():
        if settings.DEBUG:
            raise AssetBadTypeException(u"Asset tag got unexpected asset file extension {!r} from {!r}".format(asset_type, asset_name))
        else:
            return u'<!-- Unknown asset extension {!r} -->'.format(asset_type)

    # Don't allow inserting the same file twice.
    if '_MEDIA_TAG_INCLUDES' not in context:
        context['_MEDIA_TAG_INCLUDES'] = {asset_type: [] for asset_type in TAGS.keys()}
    if asset_name in context['_MEDIA_TAG_INCLUDES'][asset_type]:
        if settings.DEBUG:
            logger.warning("Asset %r was already included and will not be included twice; skipping", asset_name)
        return u''
    context['_MEDIA_TAG_INCLUDES'][asset_type].append(asset_name)

    # We can do extra helpful work when in DEBUG mode.
    if settings.DEBUG:
        # Verify the file exists.
        if not external_asset and not os.path.exists(os.path.join(settings.MEDIA_ROOT, asset_name)):
            raise AssetNotFoundException("Asset %r could not be found in %s.%s" % (
                asset_name, settings.MEDIA_ROOT, " Hint: asset paths should not start with a /." if asset_name.startswith('/') else ''))

        # Warn on odd media types.
        if media and asset_type == '.js':
            logging.warning("Specifying a media=%r type for a Javascript asset (%r) is not supported.",
                            media, asset_name)

        # Warn on defer attribute for CSS files.
        if defer and asset_type == '.css':
            logging.warning("Specifying defer=True for a CSS asset (%r) is not supported.",
                            asset_name)

        # Warn if including third party assets via http:// or https://; they should use the
        #  // protocol shortcut.
        if asset_name.startswith('http'):
            logger.warning("Including third-party assets should use // instead of http(s):// otherwise we will trigger SSL content errors.")

    # Return the link/script tag, with cache-buster if appropriate.
    return TAGS[asset_type].format(file=_generate_asset_path(asset_name), **tag_args)


def _generate_asset_path(asset_name):
    """Generates the client-side path name of a given asset_name."""
    # Set MEDIA_ASSET_BUST_CACHE_TEST = True to visually tag all assets that came through {% asset %} tag.
    if getattr(settings, 'MEDIA_ASSET_BUST_CACHE_TEST', False):
        asset_name += '#via-asset-tag'

    # Assets via http or protocol // get short-cut through cache busting.
    if asset_name.startswith(('http', '//')):
        return asset_name

    # Serve from /site_media/$buster/asset/name.ext or directly from cloudfront.net/$buster/
    if hasattr(settings, 'MEDIA_ASSET_BASE_URL'):
        base_path = settings.MEDIA_ASSET_BASE_URL
    elif settings.DEBUG:
        base_path = '/static'
    else:
        # static site url
        base_path = 'static_base_url'
        pass
    return os.path.join(base_path, asset_name)

