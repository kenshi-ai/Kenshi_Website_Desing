<?php
// contact.php
// Receives the contact form and emails the message.

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    header("Location: contact.html");
    exit;
}

$to = "kenshi.ltd@gmail.com";
$subject = "New contact request - Kenshi.AI website";

$name = trim($_POST["name"] ?? "");
$email = trim($_POST["email"] ?? "");
$message = trim($_POST["message"] ?? "");

// Basic length limits to reduce abuse.
$substr = function_exists('mb_substr') ? 'mb_substr' : 'substr';
$name = $substr($name, 0, 120);
$email = $substr($email, 0, 200);
$message = $substr($message, 0, 5000);

if ($name === "" || $email === "" || $message === "") {
    header("Location: contact.html?success=0");
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    header("Location: contact.html?success=0");
    exit;
}

// Sanitize message (keep readable newlines).
$message = str_replace(array("\r\n", "\r"), "\n", $message);
$message = strip_tags($message);

$serverName = $_SERVER["SERVER_NAME"] ?? "example.com";
$serverName = preg_replace('/[^a-zA-Z0-9\.\-]/', '', $serverName);
$from = "no-reply@" . ($serverName !== "" ? $serverName : "example.com");

$body =
    "New contact form submission from Kenshi.AI website\n\n" .
    "Name: {$name}\n" .
    "Email: {$email}\n\n" .
    "Message:\n{$message}\n";

$headers = [];
$headers[] = "From: {$from}";
$headers[] = "Reply-To: {$email}";
$headers[] = "Content-Type: text/plain; charset=UTF-8";
$headersStr = implode("\r\n", $headers);

$sent = @mail($to, $subject, $body, $headersStr);

if ($sent) {
    header("Location: contact.html?success=1");
    exit;
}

// Fallback for debugging on environments where mail() may be misconfigured.
error_log("Contact email failed. Server=" . $serverName . ", from={$email}");
@file_put_contents(
    __DIR__ . "/contact-log.txt",
    date("c") . " | {$email} | {$name}\n{$message}\n\n----\n",
    FILE_APPEND
);

header("Location: contact.html?success=0");
exit;
?>
