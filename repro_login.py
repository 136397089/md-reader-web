from flask import Flask, render_template_string
import json
from template.login_template import LOGIN_TEMPLATE
from translations import TRANSLATIONS

app = Flask(__name__)

@app.route('/')
def test():
    lang = 'zh'
    t = TRANSLATIONS[lang]
    translations_json = json.dumps(t)
    public_key = "MOCK_KEY"
    
    try:
        rendered = render_template_string(
            LOGIN_TEMPLATE, 
            public_key=public_key, 
            error=None,
            t=t,
            lang=lang,
            translations_json=translations_json
        )
        return rendered
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(port=5001)
