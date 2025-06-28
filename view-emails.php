<?php
// Simple password check
if ($_POST['password'] !== 'YOUR_SECRET_PASSWORD') {
    echo '<form method="POST">
          <input type="password" name="password" placeholder="Enter admin password">
          <button>View Emails</button>
          </form>';
    exit;
}

// Display emails
$emails = file('subscribers.secure');
echo "<h1>Subscribers</h1><ul>";
foreach ($emails as $line) {
    $parts = explode("||", trim($line));
    echo "<li>" . htmlspecialchars($parts[1]) . " <small>(" . $parts[0] . ")</small></li>";
}
echo "</ul>";
?>