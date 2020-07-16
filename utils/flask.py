from flask import render_template
from config import config

def my_render_template(template, **context):
    context['config'] = config
    return render_template(template, **context)