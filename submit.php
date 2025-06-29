<?php
// Basic security - prevent direct access
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: index.html');
    exit;
}

// Get and sanitize email
$email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);

// Validate email
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    die('Invalid email address. <a href="javascript:history.back()">Go back</a>');
}

// File to store emails
$file = 'emails.txt';

// Check if email already exists
if (file_exists($file)) {
    $existing_emails = file_get_contents($file);
    if (strpos($existing_emails, $email) !== false) {
        die('Email already subscribed! <a href="index.html">Go back</a>');
    }
}

// Add email with timestamp
$timestamp = date('Y-m-d H:i:s');
$entry = $email . ' - ' . $timestamp . PHP_EOL;

// Save email to file
if (file_put_contents($file, $entry, FILE_APPEND | LOCK_EX)) {
    // Success - redirect or show message
    echo '<!DOCTYPE html>
    <html>
    <head>
        <title>Success!</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            .success { color: #28a745; font-size: 24px; margin-bottom: 20px; }
            .message { font-size: 18px; margin-bottom: 30px; }
            .btn { background: #6366f1; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; }
        </style>
    </head>
    <body>
        <div class="success">✅ Success!</div>
        <div class="message">Thank you for subscribing! We\'ll send you the best math resources for busy homeschool parents.</div>
        <a href="index.html" class="btn">Back to Home</a>
    </body>
    </html>';
} else {
    die('Error saving email. Please try again. <a href="javascript:history.back()">Go back</a>');
}
?>