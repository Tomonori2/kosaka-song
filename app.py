from flask import Flask, send_from_directory
import os

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(_BASE_DIR, "index.html")


@app.route("/<path:filename>")
def static_files(filename):
    """index.html・曲(songs/)・manifest・sw・アイコンを配信（.envやコードは渡さない）"""
    if filename.startswith(".") or filename.endswith((".env", ".py")):
        return ("Not found", 404)
    return send_from_directory(_BASE_DIR, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5070))
    app.run(host="0.0.0.0", port=port)
