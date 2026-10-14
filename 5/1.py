from flask import Flask

app = Flask(__name__)


POSTS = [
    {"id": 1, "title": "1", "content": "111111."},
    {"id": 2, "title": "2", "content": "222222."},
]

@app.route("/")
def hello():
    return "Hello from Flask in Docker!"

@app.route("/about")
def about():
    return "<h1>About company</h1><p>Info.</p>"

@app.route("/contacts")
def contacts():
    return """
    <h1>contacts</h1>
    <p>Телефон: +7 (XXX) XXX-XX-XX</p>
    <p>Email: info@example.com</p>
    """

@app.route("/posts")
def posts_list():
    html = "<h1>Posts</h1><ul>"
    for post in POSTS:
        html += f"<li><strong>{post['title']}</strong>: {post['content']}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
