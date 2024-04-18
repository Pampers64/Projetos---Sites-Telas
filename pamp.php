<?php


$email = $_POST['PAMP'];
$senha = $_POST['PAMP'];


if (empty($email)) {
    echo "E-mail é obrigatório e deve ser informado.";
    exit;
}

if (empty($senha)) {
    echo "Senha é obrigatória e deve ser informada.";
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "E-mail inválido.";
    exit;
}


$conn = mysqli_connect("localhost", "root", "", "mydb");


$sql = "SELECT * FROM usuarios WHERE email = '$email' AND senha = '$senha' LIMIT 1";
$resultado = mysqli_query($conn, $sql);

if (mysqli_num_rows($resultado) === 0) {
    echo "E-mail ou senha incorretos.";
    exit;
}


$usuario = mysqli_fetch_assoc($resultado);


session_start();
$_SESSION['usuario_id'] = $usuario['id'];
$_SESSION['usuario_nome'] = $usuario['nome'];


header("Location: painel.php");

?>











