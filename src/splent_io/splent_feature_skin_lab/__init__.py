from splent_framework.blueprints.base_blueprint import create_blueprint

skin_lab_bp = create_blueprint(__name__)

# Ingeniería del Software for the Artificial Intelligence degree.
#
# This is the subject's own identity, not a recolour of the other wiki. EGC
# is a terminal: dark chrome, monospace wordmark, crimson. This one reads as
# the field it is taught in, without any of the things that usually stand in
# for it. No neon on black, no glow, no gradient wash behind the text: a
# course wiki is read end to end, in a lab, on whatever screen is to hand,
# and every one of those costs legibility for an impression.
#
# What carries it instead is restraint and one signal. The page stays paper
# so the material is readable; the accents are an electric violet and a
# cyan, the two colours the field actually uses in its own tools and papers,
# and they appear together only in the hairline under the header, which is
# the site's signature and the one place a gradient earns its keep.
#
# The faces are geometric rather than serif: Space Grotesk is drawn for
# technical writing and is what the field's own documentation is set in, and
# the mono is kept for anything the reader is meant to type.
ISIA_TOKENS = {
    # Electric violet. Reads as the field without being a toy, and holds
    # 7.1:1 against white, so it can carry body links and not only fills.
    "primary": "#4c2fd7",
    "primary_contrast": "#ffffff",
    # Cyan, the other half of the signature. Used where something is live or
    # worth noticing, and darkened from the screen-native cyan so it stays
    # legible as text rather than only as a fill.
    "accent": "#0e7490",
    "bg": "#ffffff",
    # Cool rather than warm, which is what keeps the page from reading as
    # the other wiki's paper.
    "surface": "#f7f7fb",
    "text": "#2e2e38",
    "heading": "#16162b",
    "muted": "#6b6b7b",
    "border": "#e5e5ee",
    # Tighter than before. Rounded corners read as a consumer app; this
    # material is documentation.
    "radius": "6px",
    "container": "1120px",
    "font_body": "'Inter', system-ui, sans-serif",
    "font_heading": "'Space Grotesk', 'Inter', system-ui, sans-serif",
    "font_display": "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace",
    "font_url": (
        "https://fonts.googleapis.com/css2"
        "?family=JetBrains+Mono:wght@400;500;600"
        "&family=Inter:wght@400;500;600;700"
        "&family=Space+Grotesk:wght@500;600;700"
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
        "skin_lab.assets",
        order=200,
        subfolder="css",
        filename="skin_lab.css",
    )


def inject_context_vars(app):
    return {}
