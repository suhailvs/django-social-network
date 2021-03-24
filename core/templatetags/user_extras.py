from django import template
import hashlib

register = template.Library()

@register.filter
def gravatar_url(username, size=40):
    # TEMPLATE USE:  {{ email|gravatar_url:150 }}
    username_hash = hashlib.md5(username.lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{username_hash}?s={size}&d=identicon"
