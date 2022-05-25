dificeis = [30,  ['Qual foi o maior campeonato de e-Sports de 2021?', '2021 League of Legends World Championship', 'The International 10', 'MPL Indonesia Season 8', 'PGL Major Stockholm', 'Valorant Champions', '1', 'O mundial do grande lolzinho foi o campeonato mais assistido de 2021, com a Edward Gaming vencendo a equipe que era atual campeã DAMWON.'], ['Qual desses jogos bane mais hackers em uma semana?', 'PUBG Mobile', 'League Of Legends', 'Valorant', 'Dota 2', 'CS:GO', '1', 'PUBG Mobile é o jogo que mais bane hackers em uma semana atualmente, com números que vão até 3,8 milhões.']]
medias = [20, ['Qual dos anticheats abaixo causou grande problema no seu lançamento, mas também é considerado um dos melhores do mercado?', 'Easy Anticheat', 'Valve Anticheat', 'Vanguard Anticheat', 'ESL Anticheat', 'Gamers Club Anticheat', '3', 'O Vanguard, anticheat do jogo Valorant, causou grande problema aos usuários ao desativar uma opção da placa de vídeo, a qual fazia a mesma girar mais devagar e em vários casos, queimar a mesma.'], ['Qual jogador brasileiro teve uma acusação ao vivo de estar usando hack e até tem um vídeo meme sobre o caso?', 'ASPX', 'Sacy', 'Scream', 'Fallen', 'Coldzera', '1', 'O vídeo em questão é esse: https://www.youtube.com/watch?v=76hji9gdvOE. ASPX foi pego usando hack na WCG Brasil em 2009 e até virou meme, por gaguejar quando foi questionado porque mirou em um certo lugar.'], ['Uma equipe brasileira de Valorant foi pega no Mundial abusando de um bug, o qual dava vantagem para eles sobre os inimigos e foram punidos de uma forma bem injusta, qual foi essa equipe?', 'LOUD', 'Vivo Keyd', 'NIP', 'Sharks', 'Vikings', '2', 'A equipe em questão foi a Vivo Keyd, e uma partida contra o time Acend. A Keyd foi punida em 7 rounds em um mapa que tinha sido vencido por eles, e que após a punição foi perdido, fazendo a Acend continuar viva no campeonato e enfim ser campeã Mundial.']]
faceis = [10, ['Qual desses é considerado um tipo de trapaça em um jogo de tiro sem habilidades?', 'Matar um inimigo pela parede.', 'Ver um inimigo atrás da parede.', 'Matar um inimigo por uma fumaça.', 'Matar um inimigo com uma granada.', 'Matar um inimigo pulando.', '2', 'Ao menos que o jogo tenha algum tipo de habilidade como o Valorant, é impossível fazer isso sem a utilização de programas de terceiros ou algum tipo de bug, ou seja, trapaça.'], ['Qual desses é considerado um tipo de trapaça em um jogo MOBA (Multiplayer Online Battle Arena) ?', 'Desviar das habilidades dos oponentes.', 'Utilizar um bug que lhe dá vantagem.', 'Comprar um item.', 'Conversar com seus aliados.', 'Usar um personagem forte.', '2', 'Utilizar algum bug que lhe dê vantagem é algo não só eticamente errado, nas regras do próprio campeonato provavelmente terá uma regra contra isso, como se fosse o anti doping nos esportes normais.'], ['Qual a alternativa correta da diferença entre Glitch e Bug no universo dos jogos?', 'Bug é algo controlável pelo usuário e glitch é algo aleatório, sem controle.', 'Bugs são feitos pelo próprio usuário com a intenção de se beneficiar no jogo, já o glitch é algo que pode acontecer a qualquer momento.', 'Bug é um defeito do jogo que pode ocorrer aleatoriamente, o qual pode prejudicar ou beneficiar o usuário, já o glitch é algo que o próprio usuário faz e serve geralmente para a diversão do mesmo.', 'Bug é um inseto em inglês e glitch um defeito no jogo.', 'Um glitch é ficar preso em uma parte do jogo e um bug seria ver através das paredes.', '3', 'A terceira alternativa já é a explicação da pergunta.']]
def quiz():
    print('Inicio do quiz')
    resposta = ''
    valor = 0
    pontuacao = 0
    for i in faceis + medias + dificeis: 
        if type(i) == int: 
            valor = i
            continue
        print('Pergunta:', i[0], '\nAlternativas:') 
        for x in range(1,6):
            print(str(x) + ') ' +  i[x]) 
        resposta = input('Digite o número da alternativa correta: ')
        if resposta == i[6]: 
            pontuacao += valor
        else:
            print("Você errou, explicação:" , i[7])
    fim(pontuacao)

def fim(pontuacao):
    print('Sua pontuação foi de:', pontuacao)

quiz()