import os, threading, time
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)
FLAG = os.environ.get('FLAG', 'flag{placeholder}')

# 留言存储（内存，简单起见）
comments = []

INDEX = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>留言板 - SLsec Guestbook</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;padding:2rem;min-height:100vh;display:flex;flex-direction:column;align-items:center}
    .card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:2rem;width:580px;max-width:100%;margin-bottom:1.5rem}
    h1{font-size:1.2rem;color:#58a6ff;letter-spacing:2px;margin-bottom:.5rem}
    .desc{color:#8b949e;font-size:.85rem;margin-bottom:1.2rem}
    textarea{width:100%;background:#0d1117;border:1px solid #30363d;border-radius:6px;padding:.7rem;color:#c9d1d9;font-size:.9rem;resize:vertical;min-height:80px;outline:none}
    textarea:focus{border-color:#58a6ff}
    button{padding:.6rem 1.5rem;background:#238636;border:none;border-radius:6px;color:#fff;font-size:.9rem;cursor:pointer;margin-top:.6rem}
    button:hover{background:#2ea043}
    .comment{background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:.8rem 1rem;margin-bottom:.6rem;font-size:.9rem;word-break:break-all}
    .comment .meta{font-size:.75rem;color:#8b949e;margin-bottom:.2rem}
    .report{margin-top:1rem;text-align:center}
    .report a{color:#58a6ff;font-size:.85rem}
  </style>
</head>
<body>
<div class="card">
  <h1>📋 SLsec 留言板</h1>
  <p class="desc">管理员会定期查看留言，你可以在留言里留下想说的话。</p>
  <form method="POST" action="/comment">
    <textarea name="content" placeholder="写点什么……" required></textarea>
    <button type="submit">提交留言</button>
  </form>
</div>
<div class="card">
  <h2 style="font-size:1rem;color:#c9d1d9;margin-bottom:.8rem">已有留言 ({{ comments|length }})</h2>
  {% for c in comments %}
    <div class="comment">
      <div class="meta">{{ c.time }}</div>
      <div>{{ c.content | safe }}</div>
    </div>
  {% endfor %}
  {% if not comments %}
    <p style="color:#555;font-size:.85rem;text-align:center;padding:1rem">暂无留言</p>
  {% endif %}
</div>
<div class="report">
  <a href="/report">📢 通知管理员审核</a>
</div>
</body>
</html>'''

STEAL_LOG = []

def bot_visit(url, cookie_value):
    """用 Playwright 访问页面，携带 flag cookie"""
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True,
                args=['--no-sandbox', '--disable-setuid-sandbox'])
            ctx = browser.new_context()
            ctx.add_cookies([{
                'name': 'flag',
                'value': cookie_value,
                'domain': 'localhost',
                'path': '/'
            }])
            page = ctx.new_page()
            page.goto(url, timeout=10000)
            time.sleep(2)  # 等待 XSS 触发
            browser.close()
    except Exception as e:
        pass

@app.route('/')
def index():
    return render_template_string(INDEX, comments=comments)

@app.route('/comment', methods=['POST'])
def add_comment():
    content = request.form.get('content', '').strip()
    if content:
        from datetime import datetime
        comments.insert(0, {
            'content': content,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    return redirect('/')

@app.route('/steal')
def steal():
    c = request.args.get('c', '')
    STEAL_LOG.append(c)
    return 'ok'

@app.route('/report')
def report():
    # 启动后台线程让 bot 访问
    t = threading.Thread(target=bot_visit, args=('http://localhost:5000/', FLAG), daemon=True)
    t.start()
    t.join(timeout=15)
    return render_template_string('''<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><title>已通知</title>
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:#0f1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh}
  .card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:2.5rem;text-align:center;max-width:400px}
  h1{color:#58a6ff;margin-bottom:.5rem;font-size:1.1rem}
  p{color:#8b949e;font-size:.85rem}
  a{color:#58a6ff}
</style></head>
<body>
<div class="card">
  <h1>✅ 已通知管理员</h1>
  <p>管理员将在稍后查看留言。</p>
  <p style="margin-top:1rem"><a href="/">返回留言板</a></p>
</div>
</body>
</html>''')

@app.route('/log')
def log():
    return '\n'.join(STEAL_LOG) if STEAL_LOG else '(empty)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
