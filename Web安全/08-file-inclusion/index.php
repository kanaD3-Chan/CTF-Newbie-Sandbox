<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>文件查看器</title>
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
    .nav a{color:#58a6ff;text-decoration:none;font-size:.85rem;margin-right:1rem}
    .nav a:hover{text-decoration:underline}
  </style>
</head>
<body>
<div class="card">
  <h1>📄 文件查看器</h1>
  <p class="desc">选择要查看的页面。</p>
  <div class="nav">
    <a href="?file=home.php">🏠 首页</a>
    <a href="?file=about.php">ℹ️ 关于</a>
    <a href="?file=contact.php">📧 联系</a>
  </div>
</div>
<div class="card">
  <h1>📖 内容</h1>
  <pre><?php
    $file = $_GET['file'] ?? 'home';
    include($file);
  ?></pre>
</div>
</body>
</html>