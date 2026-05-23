<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>XML 解析器</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;display:flex;flex-direction:column;align-items:center;padding:3rem 1rem;min-height:100vh}
    .card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:2rem;width:580px;max-width:100%;margin-bottom:1.5rem}
    h1{color:#58a6ff;font-size:1.2rem;letter-spacing:2px;margin-bottom:.3rem}
    .desc{color:#8b949e;font-size:.85rem;margin-bottom:1.2rem}
    textarea{width:100%;background:#0d1117;border:1px solid #30363d;border-radius:6px;padding:.7rem;color:#c9d1d9;font-size:.85rem;resize:vertical;min-height:120px;outline:none;font-family:monospace}
    textarea:focus{border-color:#58a6ff}
    button{padding:.6rem 1.5rem;background:#238636;border:none;border-radius:6px;color:#fff;font-size:.9rem;cursor:pointer;margin-top:.6rem}
    button:hover{background:#2ea043}
    pre{background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:1rem;font-size:.85rem;overflow-x:auto;color:#c9d1d9;line-height:1.6;margin-top:0}
  </style>
</head>
<body>
<div class="card">
  <h1>📋 XML 解析器</h1>
  <p class="desc">提交 XML 数据，服务器会解析并显示结果。</p>
  <form method="POST" enctype="text/plain">
    <textarea name="xml" placeholder="<root><item>Hello</item></root>"></textarea>
    <button type="submit">解析</button>
  </form>
</div>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $xml = file_get_contents('php://input');
  if (!empty($xml)):
?>
<div class="card">
  <h1>📤 解析结果</h1>
  <pre><?php
    $dom = new DOMDocument();
    $dom->loadXML($xml, LIBXML_NOENT | LIBXML_DTDLOAD);
    $root = $dom->documentElement;
    echo htmlspecialchars($dom->saveXML($root));
  ?></pre>
</div>
<?php endif; } ?>
</body>
</html>