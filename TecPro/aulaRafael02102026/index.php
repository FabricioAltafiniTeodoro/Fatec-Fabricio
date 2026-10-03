<?php
    require_once "Conta.php";
    require_once "Administrador.php";
    require_once "Item.php";
    require_once "Inventario.php";
    require_once "Jogador.php";
    require_once "Personagem.php";

    // Criando instância de Classe Conta
    $conta = new Conta(1, "patati@patata.com", "12345678");
    echo $conta->login("12345678") ? "Login realizado com sucesso \n <br>" :" Senha incorreta \n <br>";
    echo "ID: " . $conta->getId() . " <br>";
    echo "E-mail: " . $conta->getEmail() . " <br>";

    // Criando instância da Classe Administrador
    $admin = new Administrador("Moderador");
    $admin->banirJogador("Patati");
    echo "<br>";
    echo "Cargo: " . $admin->getCargo() . " <br>";

    // Criando instância da Classe Jogador
    $jogador = new Jogador("Patati", 1, 0, 50);
    echo "Apelido: " . $jogador->getApelido() . " <br>";
    echo "Nível: " . $jogador->getNivel() . " <br>";
    echo "XP: " . $jogador->getXp() . " <br>";
    echo "Moedas: " . $jogador->getMoedas() . " <br>";
    $jogador->ganharXp(30);
    echo "<br>";
    $jogador->gastarMoedas(20);
    echo "<br>";

    // Criando instância da Classe Personagem
    $personagem = new Personagem("Arthur", "Guerreiro", "1");
    echo "Nome: " . $personagem->getNome() . " <br>";
    echo "Classe: " . $personagem->getClasse() . " <br>";
    echo "Nível: " . $personagem->getNivel() . " <br>";
    $personagem->atacar();
    echo "<br>";

    // Criando instância da Classe Item
    $espada = new Item("Espada", "Rara", 100);
    echo "Item: " . $espada->getNome() . " <br>";
    echo "Raridade: " . $espada->getRaridade() . " <br>";
    echo "Valor: " . $espada->getValor() . " <br>";
    $espada->usar();
    echo "<br>";

    // Criando instância da Classe Inventario
    $inventario = new Inventario(5);
    echo "Capacidade: " . $inventario->getCapacidade() . " <br>";
    $inventario->adicionarItem($espada);
    echo "<br>";
?>