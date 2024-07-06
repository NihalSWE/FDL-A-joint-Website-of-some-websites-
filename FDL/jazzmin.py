JAZZMIN_SETTINGS = {
    "site_title": "Future Destination Ltd Admin",
    "site_header": "Future Destination Ltd",
    "site_brand": "FDL",  # SPL typography with blue color
    "site_icon": "/static/assets/img/favicon.ico",  # Path to your site icon (favicon)
    "welcome_sign": "Welcome to Future Destination Ltd Admin",
    "copyright": "Future Destination Ltd",
    "user_avatar": "/static/assets/img/avatar.png",  # Default user avatar
    "menu_icon": "feather icon-menu",  # Icon for the menu toggle
    "show_sidebar": True,  # Show sidebar
    "navigation_expanded": True,  # Expanded navigation by default
    "icons": {
        "auth": "fas fa-users-cog",     # Icon for authentication section
        "auth.user": "fas fa-user",     # Icon for User model
        "auth.Group": "fas fa-users",   # Icon for Group model
        "products": "fas fa-box-open",  # Example icon for products app
        "about": "fas fa-info-circle",  # Example icon for about app
        "team": "fas fa-users",         # Example icon for team app
    },
    "default_icon_parents": "fas fa-chevron-circle-right",  # Default icon for parent items
    "default_icon_children": "fas fa-circle",               # Default icon for child items
    "related_modal_active": False,  # Disable related modals
    "custom_css": None,  # No custom CSS file
    "custom_js": None,   # No custom JS file
    "use_google_fonts_cdn": True,  # Use Google Fonts CDN
    "show_ui_builder": False,  # Disable UI builder
    "changeform_format": "horizontal_tabs",  # Change form format to horizontal tabs
    "changeform_format_overrides": {
        "auth.user": "collapsible",  # Customize change form for User model
        "auth.group": "vertical_tabs"  # Customize change form for Group model
    },
    "theme": "cosmo",  # Use a professional and polished theme
    "dark_mode_theme": "darkly",  # Use a dark theme for dark mode
    "actions_sticky_top": True,  # Make action buttons sticky at the top
    "order_with_respect_to": ["auth", "auth.user", "auth.Group"],  # Order the apps in the sidebar
    "buttons": {
        "back": "btn-outline-primary",
        "close": "btn-outline-secondary",
        "save": "btn-outline-success",
        "delete": "btn-outline-danger",
    },
    "language_chooser": False,  # Hide the language chooser
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
    "dark_mode_theme": "darkly",
    "navbar": "navbar-dark bg-primary",
    "sidebar": "sidebar-dark-primary",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "sidebar_fixed": True,
    "footer_fixed": False,
    "actions_sticky_top": True,
    "sidebar_nav_child_indent": True,
    "dark_mode_switch": True,
    "footer": "dark",
    "css": """
        body.login {
            background-color: #343a40 !important;
            color: #ffffff !important;
        }
        body.login .card {
            background-color: #4e73df !important;
        }
        body.login .card-body {
            color: #ffffff !important;
        }
    """,
}