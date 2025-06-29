<?php
// Debugging version - saves to a TEST file first
$email = $_POST['email'];

// 1. Try saving to a test file (everyone can access)
file_put_contents('test-debug.txt', "Working! Email: $email\n", FILE_APPEND);

// 2. Then try secure file
file_put_contents('subscribers.secure', "$email\n", FILE_APPEND);

// 3. Show what happened
echo "<h1>Debug Info</h1>";
echo "<pre>";
print_r([
    'email_received' => $email,
    'test_file_exists' => file_exists('test-debug.txt'),
    'secure_file_exists' => file_exists('subscribers.secure'),
    'permissions' => substr(sprintf('%o', fileperms('subscribers.secure')), -4)
]);
echo "</pre>";
?>