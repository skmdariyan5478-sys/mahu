from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

base_html = """
<!DOCTYPE html>
<html>
<head>
    <title>For Mahira</title>
    <style>
        body {{
            background: linear-gradient(to right, #ffdde1, #ee9ca7);
            font-family: 'Georgia', serif;
            text-align: center;
            color: #4a2c2a;
            transition: all 0.8s ease;
        }}
        .container {{
            margin-top: 15%;
            animation: fadeIn 2s ease;
        }}
        h1 {{ font-size: 2.5em; margin-bottom: 20px; }}
        p {{ font-size: 1.2em; margin-bottom: 30px; }}
        a, button {{
            background: #d16ba5;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 25px;
            text-decoration: none;
            font-size: 1.1em;
            transition: 0.3s;
        }}
        a:hover, button:hover {{
            background: #ff758c;
            transform: scale(1.05);
        }}
        @keyframes fadeIn {{ from {{opacity: 0;}} to {{opacity: 1;}} }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def chapter1():
    content = """
    <h1>✨ First Impression ✨</h1>
    <p>Mahira, the very first time I saw you, the world felt softer, brighter, and infinitely more beautiful.</p>
    <a href="/chapter2">Next ➝</a>
    """
    return base_html.format(content=content)

@app.get("/chapter2", response_class=HTMLResponse)
async def chapter2():
    content = """
    <h1>💫 Moments I Loved 💫</h1>
    <p>Every laugh, every glance, every quiet moment with you is etched in my heart forever.</p>
    <a href="/chapter3">Next ➝</a>
    """
    return base_html.format(content=content)

@app.get("/chapter3", response_class=HTMLResponse)
async def chapter3():
    content = """
    <h1>❤️ Why You're Special ❤️</h1>
    <p>You are my safe place, my joy, my inspiration. Mahira, you make my life magical.</p>
    <a href="/proposal">Final Chapter ➝</a>
    """
    return base_html.format(content=content)

@app.get("/proposal", response_class=HTMLResponse)
async def proposal_get():
    content = """
    <h1>🔒 Final Proposal 🔒</h1>
    <p>Enter the secret key to unlock my heart:</p>
    <form method="POST">
        <input type="password" name="password" placeholder="Enter password">
        <button type="submit">Unlock</button>
    </form>
    """
    return base_html.format(content=content)

@app.post("/proposal", response_class=HTMLResponse)
async def proposal_post(password: str = Form(...)):
    if password == "041108":
        content = """
        <h1>💍 Mahira, Will You Be Mine? 💍</h1>
        <p>From the first impression to every cherished moment, you are my forever. 
        Say yes, and let's write the rest of our chapters together.</p>
        """
    else:
        content = """
        <h1>🔒 Final Proposal 🔒</h1>
        <p>Enter the secret key to unlock my heart:</p>
        <form method="POST">
            <input type="password" name="password" placeholder="Enter password">
            <button type="submit">Unlock</button>
        </form>
        <p style="color:red;">Wrong password, try again.</p>
        """
    return base_html.format(content=content)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

