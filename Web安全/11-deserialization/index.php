<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>数据恢复工具</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f1117;color:#c9d1d9;font-family:'Segoe UI',sans-serif;display:flex;flex-direction:column;align-items:center;padding:3rem 1rem;min-height:100vh}
    .card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:2rem;width:580px;max-width:100%;margin-bottom:1.5rem}
    h1{color:#58a6ff;font-size:1.2rem;letter-spacing:2px;margin-bottom:.3rem}
    .desc{color:#8b949e;font-size:.85rem;margin-bottom:1.2rem}
    input[type=text]{width:100%;background:#0d1117;border:1px solid #30363d;border-radius:6px;padding:.7rem;color:#c9d1d9;font-size:.85rem;outline:none;font-family:monospace;margin-bottom:.6rem}
    input[type=text]:focus{border-color:#58a6ff}
    button{padding:.6rem 1.5rem;background:#238636;border:none;border-radius:6px;color:#fff;font-size:.9rem;cursor:pointer}
    button:hover{background:#2ea043}
    pre{background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:1rem;font-size:.85rem;overflow-x:auto;color:#c9d1d9;line-height:1.6;margin-top:1rem}
  </style>
</head>
<body>
<div class="card">
  <h1>🔄 数据恢复工具</h1>
  <p class="desc">输入序列化数据，系统会将其恢复为对象。</p>
  <form method="GET">
    <input type="text" name="data" placeholder='O:4:"User":1:{s:4:"name";s:5:"admin";}' value="<?=htmlspecialchars($_GET['data'] ?? '')?>">
    <button type="submit">恢复</button>
  </form>
<?php
class User {
  public $name = 'guest';
  public function __wakeup() {
    echo '<pre>用户: ' . htmlspecialchars($this->name) . '</pre>';
  }
}
class Shell {
  public $cmd;
  function __wakeup() {
    system($this->cmd);
  }
}
if (isset($_GET['data'])) {
  $data = $_GET['data'];
  $obj = unserialize($data);
}
?>
</div>
</body>
</html>