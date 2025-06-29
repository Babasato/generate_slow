<?php
// Simple password protection (change this password!)
$admin_password = 'your_secure_password_here';

if (!isset($_POST['password']) || $_POST['password'] !== $admin_password) {
    ?>
    <!DOCTYPE html>
    <html>
    <head><title>Admin Access</title></head>
    <body>
        <h2>Enter Admin Password</h2>
        <form method="POST">
            <input type="password" name="password" required>
            <button type="submit">Access</button>
        </form>
    </body>
    </html>
    <?php
    exit;
}

// Display emails
echo '<h2>Captured Emails</h2>';
echo '<style>body{font-family:Arial,sans-serif;padding:20px;} .email{padding:10px;border-bottom:1px solid #ccc;}</style>';

if (file_exists('emails.txt')) {
    $emails = file('emails.txt', FILE_IGNORE_NEW_LINES);
    $count = count($emails);
    echo "<p><strong>Total: $count emails</strong></p>";
    
    foreach (array_reverse($emails) as $email) {
        echo '<div class="email">' . htmlspecialchars($email) . '</div>';
    }
} else {
    echo '<p>No emails captured yet.</p>';
}

echo '<br><a href="?">Logout</a>';
?>