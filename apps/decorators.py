import markdown as md

from functools import wraps
from flask import Markup, render_template

def with_markdown(template):
    """Convert Markdown syntax into HTML and insert into the base
    template. Includes Pygments support.
    """
    def decorator(fn):
        @wraps(fn)
        def decorated_fn(*args, **kwargs):
            ctx = fn(*args, **kwargs)
            if ctx is None:
                ctx = {}
            source = render_template(template)
            extensions = ['codehilite', 'fenced_code']
            contents = Markup(md.markdown(source, extensions=extensions))
            ctx['contents'] = contents
            return render_template('_base_md.html', **ctx)
        return decorated_fn
    return decorator
