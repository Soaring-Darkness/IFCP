from app import app
from flask import Flask, render_template, url_for, request, flash


@app.route('/panel/', methods=['POST', 'GET'])
def panel():
    return render_template('panel.html')
