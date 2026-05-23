from flask import Flask, render_template_string, Response
import os

app = Flask(__name__)
FLAG = os.environ.get('FLAG', 'flag{placeholder}')

PAGE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>HTTP Header Inspector</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f1117;color:#c9d1d9;font-family:'Courier New',monospace;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;gap:1.5rem;padding:2rem}
    .card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:2rem 2.5rem;max-width:560px;width:100%;box-shadow:0 4px 24px #0004}
    h1{font-size:1.1rem;letter-spacing:2px;color:#58a6ff;margin-bottom:1rem}
    p{color:#8b949e;line-height:1.7;font-size:.9rem}
    .hint{margin-top:1.2rem;background:#0d1117;border-left:3px solid #58a6ff;padding:.8rem 1rem;font-size:.85rem;color:#79c0ff}
    .tool{display:inline-block;background:#21262d;border:1px solid #30363d;border-radius:4px;padding:.15rem .5rem;font-size:.8rem;color:#e3b341}
    kbd{background:#21262d;border:1px solid #444;border-radius:3px;padding:.1rem .4rem;font-size:.8rem}
  </style>
</head>
<body>
<div class="card">
  <h1>// HTTP Header Inspector</h1>
  <p>这个页面看起来很普通，什么都没有。</p>
  <p style="margin-top:.8rem">但 HTTP 响应不只有 body——<strong style="color:#c9d1d9">响应头</strong>里也可以藏东西。</p>
  <div class="hint">
    提示：打开浏览器开发者工具 <kbd>F12</kbd>，切换到
    <span class="tool">Network</span> 面板，刷新页面，
    点击第一个请求，查看 <span class="tool">Response Headers</span>。
  </div>
</div>
</body>
</html>'''

@app.route('/')
def index():
    resp = Response(render_template_string(PAGE), mimetype='text/html')
    resp.headers['X-Flag'] = FLAG
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
