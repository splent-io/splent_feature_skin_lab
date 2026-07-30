"""Where this skin reaches parts of the product it does not own.

The public shell takes its stylesheet through the asset registry, which is
what a skin is for. The back office does not: splent_feature_admin ships a
Bootstrap shell of its own, so a reader who follows the sign-in link lands
somewhere that looks like a different site.

That is fixed from here, with a stylesheet and nothing else, through the
layout.head.css slot the shell already renders. The admin feature is not
touched, not subclassed, and does not know this exists.
"""

from flask import current_app, url_for
from markupsafe import Markup

from splent_framework.hooks.template_hooks import register_template_hook


def admin_stylesheet():
    """The skin's back-office stylesheet, and the tokens it is written in.

    The tokens come first and are not optional. The theme declares its
    ``--brand-*`` block in the public shell's template only, so on an admin
    page there are none, and a stylesheet written against them resolves to
    nothing: the file loads, the page does not change, and the only clue is
    that it looks exactly as it did before.
    """
    from splent_io.splent_feature_theme.tokens import get_tokens, tokens_to_css

    tokens = tokens_to_css(get_tokens(current_app))
    href = url_for("skin_lab.assets", subfolder="css", filename="admin_lab.css")
    return Markup(
        f'<style id="brand-tokens">{tokens}</style>'
        f'<link rel="stylesheet" href="{href}">'
    )


register_template_hook("layout.head.css", admin_stylesheet, order=200)
