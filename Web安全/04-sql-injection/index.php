<?php
error_reporting(0);
include "connect.php";

$flag    = '';
$error   = '';
$success = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // 漏洞：直接拼接 SQL，无过滤
    $sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
    $result = $conn->query($sql);

    if ($result && $result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if (isset($row['flag'])) {
            $flag    = $row['flag'];
            $success = true;
        } else {
            $success = true;
        }
    } else {
        $error = '用户名或密码错误。';
    }
}
?>
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>登录 - SLsec Admin</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh}
    .card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:2.5rem 2.5rem;width:360px;box-shadow:0 8px 32px #0006}
    .logo{text-align:center;margin-bottom:1.8rem}
    .logo span{font-size:2rem}
    .logo h1{font-size:1.1rem;color:#58a6ff;letter-spacing:2px;margin-top:.4rem}
    label{display:block;font-size:.8rem;color:#8b949e;margin-bottom:.3rem;margin-top:1rem}
    input{width:100%;background:#0d1117;border:1px solid #30363d;border-radius:6px;padding:.6rem .9rem;color:#c9d1d9;font-size:.95rem;outline:none}
    input:focus{border-color:#58a6ff}
    button{width:100%;margin-top:1.5rem;padding:.7rem;background:#238636;border:none;border-radius:6px;color:#fff;font-size:1rem;cursor:pointer;letter-spacing:1px}
    button:hover{background:#2ea043}
    .error{margin-top:1rem;background:#3d1a1a;border:1px solid #f85149;border-radius:6px;padding:.6rem .9rem;color:#f85149;font-size:.85rem}
    .success{margin-top:1rem;background:#0d2818;border:1px solid #238636;border-radius:6px;padding:.8rem 1rem;color:#3fb950;font-size:.9rem;word-break:break-all}
    .flag-label{font-size:.75rem;color:#8b949e;margin-bottom:.3rem}
  </style>
</head>
<body>
<div class="card">
  <div class="logo">
    <span>🔐</span>
    <h1>ADMIN LOGIN</h1>
  </div>
  <form method="POST">
    <label>用户名</label>
    <input type="text" name="username" placeholder="username" autocomplete="off">
    <label>密码</label>
    <input type="password" name="password" placeholder="password">
    <button type="submit">登 录</button>
  </form>
  <?php if ($error): ?>
    <div class="error"><?= htmlspecialchars($error) ?></div>
  <?php endif; ?>
  <?php if ($success): ?>
    <div class="success">
      <div class="flag-label">// 登录成功</div>
      <?= htmlspecialchars($flag) ?>
    </div>
  <?php endif; ?>
</div>
</body>
</html>
