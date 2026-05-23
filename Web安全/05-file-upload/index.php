<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>图片上传 - SLsec Imgur</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh}
    .card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:2.5rem;width:400px;box-shadow:0 8px 32px #0006}
    .logo{text-align:center;margin-bottom:1.5rem}
    .logo span{font-size:2.2rem}
    .logo h1{font-size:1.1rem;color:#58a6ff;letter-spacing:2px;margin-top:.4rem}
    .logo p{color:#8b949e;font-size:.8rem;margin-top:.3rem}
    .dropzone{border:2px dashed #30363d;border-radius:8px;padding:2rem;text-align:center;cursor:pointer;transition:all .2s}
    .dropzone:hover{border-color:#58a6ff;background:#0d1117}
    .dropzone input{display:none}
    .dropzone label{cursor:pointer;display:block}
    .dropzone label span{display:block;font-size:2rem;margin-bottom:.5rem}
    button{width:100%;margin-top:1.2rem;padding:.7rem;background:#238636;border:none;border-radius:6px;color:#fff;font-size:1rem;cursor:pointer}
    button:hover{background:#2ea043}
    .msg{margin-top:1rem;border-radius:6px;padding:.7rem 1rem;font-size:.85rem}
    .msg.ok{background:#0d2818;border:1px solid #238636;color:#3fb950}
    .msg.err{background:#3d1a1a;border:1px solid #f85149;color:#f85149}
    .msg a{color:#58a6ff}
    .hint{color:#8b949e;font-size:.75rem;margin-top:.8rem;text-align:center}
  </style>
</head>
<body>
<div class="card">
  <div class="logo">
    <span>🖼️</span>
    <h1>SLsec IMGUR</h1>
    <p>上传你的图片</p>
  </div>
  <form method="POST" enctype="multipart/form-data">
    <div class="dropzone" onclick="document.getElementById('file').click()">
      <label>
        <input type="file" name="file" id="file" required>
        <span>📁</span>
        <span style="color:#8b949e;font-size:.85rem">点击选择文件</span>
      </label>
    </div>
    <button type="submit" name="submit">上 传</button>
  </form>
  <?php
  if (isset($_POST['submit'])) {
      $target_dir = 'uploads/';
      if (!is_dir($target_dir)) mkdir($target_dir, 0755, true);

      $filename = basename($_FILES['file']['name']);
      $target   = $target_dir . $filename;

      // 只检查了 Content-Type（客户端可控，可伪造）
      $allowed = ['image/jpeg', 'image/png', 'image/gif'];
      if (!in_array($_FILES['file']['type'], $allowed)) {
          echo '<div class="msg err">仅允许上传 jpg/png/gif 格式。</div>';
      } else {
          if (move_uploaded_file($_FILES['file']['tmp_name'], $target)) {
              echo '<div class="msg ok">上传成功！<br><a href="' . $target . '">查看文件</a></div>';
          } else {
              echo '<div class="msg err">上传失败。</div>';
          }
      }
  }
  ?>
  <div class="hint">支持 jpg、png、gif 格式</div>
</div>
</body>
</html>
