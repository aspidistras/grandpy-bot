"""runs the app"""

from flask import Flask
from botapp import app

if __name__ == "__main__":
    app.run(debug=True)
