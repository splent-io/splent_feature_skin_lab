"""
Tests for splent_feature_skin_lab.

A skin is a config feature: it registers no routes, it publishes design
tokens and one stylesheet the theme cascades after its own. So what is
worth asserting is that the tokens reach the app, that the stylesheet gets
the last word, and that this skin really is a different identity from the
other one rather than a copy with two colours changed.
"""

from splent_framework.assets.asset_registry import get_assets
from splent_io.splent_feature_skin_lab import ISIA_TOKENS


def test_tokens_are_published_to_the_theme(test_client):
    assert test_client.application.config["THEME_TOKENS"] == ISIA_TOKENS


def test_stylesheet_is_registered_last(test_client):
    # get_assets resolves each URL with url_for, so it needs a request
    # context; without one every asset is skipped and the list comes back
    # empty.
    with test_client.application.test_request_context():
        urls = get_assets("css")
    assert any("skin_lab.css" in url for url in urls)
    # Order 200, so it cascades after the theme base and after every
    # feature stylesheet. That is what makes a skin a skin.
    assert "skin_lab.css" in urls[-1]


def test_every_token_the_theme_expects_is_provided():
    """A missing token falls back to the theme default, which would mean a
    stray colour from another identity leaking into this one."""
    from splent_io.splent_feature_theme.tokens import DEFAULT_TOKENS

    assert set(DEFAULT_TOKENS) <= set(ISIA_TOKENS)
