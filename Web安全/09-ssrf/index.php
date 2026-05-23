<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>页面抓取工具</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;display:flex;flex-direction:column;align-items:center;padding:3rem 1rem;min-height:100vh}
    .card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:2rem;width:580px;max-width:100%;margin-bottom:1.5rem}
    h1{color:#58a6ff;font-size:1.2rem;letter-spacing:2px;margin-bottom:.3rem}
    .desc{color:#8b949e;font-size:.85rem;margin-bottom:1.2rem}
    .input-group{display:flex;gap:.5rem}
    input[type=text]{flex:1;background:#0d1117;border:1px solid #30363d;border-radius:6px;padding:.7rem;color:#c9d1d9;font-size:.9rem;outline:none;font-family:monospace}
    input[type=text]:focus{border-color:#58a6ff}
    button{padding:.6rem 1.5rem;background:#238636;border:none;border-radius:6px;color:#fff;font-size:.9rem;cursor:pointer}
    button:hover{background:#2ea043}
    pre{background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:1rem;font-size:.85rem;overflow-x:auto;color:#c9d1d9;line-height:1.6;margin-top:0}
  </style>
</head>
<body>
<div class="card">
  <h1>🔗 页面抓取工具</h1>
  <p class="desc">输入一个 URL，帮你抓取页面内容。</p>
  <form method="GET">
    <div class="input-group">
      <input type="text" name="url" placeholder="例如 https://example.com" value="<?=htmlspecialchars($_GET['url'] ?? '')?>" required>
      <button type="submit">抓取</button>
    </div>
  </form>
</div>
<?php if (isset($_GET['url'])): ?>
<div class="card">
  <h1>📥 抓取结果</h1>
  <pre><?php
    $url = $_GET['url'];
    $content = file_get_contents($url);
    echo $content !== false ? htmlspecialchars($content) : '(抓取失败)';
  ?></pre>
</div>
<?php endif; ?>
</body>
</html>