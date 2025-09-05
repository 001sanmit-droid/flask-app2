from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
