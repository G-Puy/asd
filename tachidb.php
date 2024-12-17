<?php
\$conn = new mysqli('10.1.1.4', 'wordpress_user', 'XxFPf8%^m5GT83sy', 'wordpress');
if (\$conn->connect_error) {
    die('Connection failed: ' . \$conn->connect_error);
}
\$result = \$conn->query('SELECT * FROM wp_users');
while (\$row = \$result->fetch_assoc()) {
    echo 'User: ' . \$row['user_login'] . ' - Password: ' . \$row['user_pass'] . \"\\n\";
}
\$conn->close();
?>
