from splent_framework.blueprints.base_blueprint import create_blueprint

skin_isia_bp = create_blueprint(__name__)

# Ingeniería del Software for the Artificial Intelligence degree.
#
# The subject is taught in a young degree and the material is read as
# documentation, so this leans academic and quiet rather than institutional:
# a deep indigo that reads as engineering without being corporate blue, a
# teal accent for the things a reader acts on, and warm neutrals so long
# stretches of prose do not glare. It is deliberately a different family
# from the EGC skin, because the point of two products from one line is that
# each looks like its own subject.
ISIA_TOKENS = {
    "primary": "#2c3e8f",
    "primary_contrast": "#ffffff",
    # Teal, used where something is actionable or worth noticing. Chosen to
    # keep contrast against both the page and the indigo.
    "accent": "#0f766e",
    "bg": "#ffffff",
    # Very slightly warm, which is easier on the eye than a blue-grey when
    # the page is mostly text.
    "surface": "#f7f7f5",
    "text": "#33333a",
    "heading": "#1b2340",
    "muted": "#6b7280",
    "border": "#e3e3e0",
    # Softer than EGC's, to match a less angular identity.
    "radius": "8px",
    "container": "1120px",
    "font_body": "'Source Sans 3', system-ui, sans-serif",
    "font_heading": "'Source Serif 4', Georgia, serif",
    "font_display": "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace",
    "font_url": (
        "https://fonts.googleapis.com/css2"
        "?family=JetBrains+Mono:wght@400;500;600"
        "&family=Source+Sans+3:wght@400;500;600;700"
        "&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700"
        "&display=swap"
    ),
}


def init_feature(app):
    from splent_framework.assets.asset_registry import register_asset

    # A skin publishes tokens and one stylesheet. Order 200 puts it after
    # the theme base and after every feature, so it gets the last word on
    # anything it chooses to restyle.
    app.config["THEME_TOKENS"] = ISIA_TOKENS
    register_asset(
        "css",
        "skin_isia.assets",
        order=200,
        subfolder="css",
        filename="skin_isia.css",
    )


def inject_context_vars(app):
    return {}
