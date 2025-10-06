linguagem = input('Digite uma linguagem: ')
match linguagem:
    case 'JavaScript': 
        print('Desenvolvedor Web')
    case 'Python':
        print('Cientista de dados')
    case 'PHP':
        print('Desenvolvedor Backend')
    case 'Solidity':
        print('Desenvolvedor Blockchain')
    case 'Java':
        print('Desenvolvedor Mobile ou Backend')
    case _ :
        print('Linguagem não encontrada')