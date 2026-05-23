<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>管理中心</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;display:flex;flex-direction:column;align-items:center;padding:3rem 1rem;min-height:100vh}
    .card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:2rem;width:580px;max-width:100%;margin-bottom:1.5rem;text-align:center}
    h1{color:#58a6ff;font-size:1.2rem;letter-spacing:2px;margin-bottom:.5rem}
    .role-badge{display:inline-block;background:#21262d;border:1px solid #30363d;border-radius:20px;padding:.3rem 1rem;font-size:.8rem;color:#8b949e;margin-bottom:1rem}
    .denied{color:#f85149;font-size:.95rem;padding:1rem}
    .granted{color:#3fb950;font-size:.95rem;padding:1rem;word-break:break-all}
    .hint{color:#8b949e;font-size:.8rem;margin-top:1rem;border-top:1px solid #21262d;padding-top:1rem}
  </style>
</head>
<body>
<div class="card">
  <h1>🔐 管理中心</h1>
  <?php
  $role = $_COOKIE['role'] ?? 'guest';
  echo '<div class="role-badge">当前身份：' . htmlspecialchars($role) . '</div>';

  if ($role === 'admin') {
    $flag = file_get_contents('/flag');
    echo '<div class="granted">' . htmlspecialchars($flag) . '</div>';
  } else {
    echo '<div class="denied">❌ 访问被拒绝。只有管理员可以查看 flag。</div>';
  }
  ?>
  <div class="hint">
    提示：你的身份信息存储在 Cookie 中。
  </div>
</div>
</body>
</html>