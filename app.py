from __future__ import unicode_literals
from flask import Flask, render_template, flash, redirect, url_for
from index import InfoForm
from config import Config
from datetime import timedelta
from main import start

# 设置静态文件缓存过期时间
app = Flask(__name__)
app.config.from_object(Config)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=0.1)


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        info = start(form.fileopen.data.filename, form.term.data, form.filestore.data.filename)
        print(form.term.data)
        return render_template('query.html', form=form, flag=1, info=info)
    return render_template('query.html', form=form, flag=0)


if __name__ == '__main__':
    app.run()
