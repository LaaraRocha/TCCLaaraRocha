from Scripts import CT01Loginnosistema as login
from Scripts import CT02Cadastrodegrupo as grupo
from Scripts import CT03Cadastrodepublicao as publicacao
from Scripts import CT04Cadastrodeclassificado as classificado
from Scripts import CT05Cadastrodedestaque as destaque
from Scripts import CT06Cadastrodecompromisso as compromisso
from Scripts import CT07Pontosdousuario as pontos

def main():
    # Testes de Login
    testeLogin = login.TestCT01Loginnosistema()
    testeLogin.setup_method("test")
    testeLogin.test_cT01Loginnosistema()
    
    print("Teste de Login: OK!")
    
    # Testes de Cadastro de Grupo
    testeGrupo = grupo.TestCT02Cadastrodegrupo()
    testeGrupo.setup_method("test")
    testeGrupo.test_cT02Cadastrodegrupo()
    
    print("Teste de Grupos: OK!")
    
    # Testes de Cadastro de Publicacao
    testePublicacao = publicacao.TestCT03Cadastrodepublicao()
    testePublicacao.setup_method("test")
    testePublicacao.test_cT03Cadastrodepublicao()

    print("Teste de Publicações: OK!")
    
    # Testes de Cadastro de Classificado
    testeClassificado = classificado.TestCT04Cadastrodeclassificado()
    testeClassificado.setup_method("test")
    testeClassificado.test_cT04Cadastrodeclassificado()
    
    print("Teste de Classificados: OK!")
    
    # Testes de Cadastro de Destaque
    testeDestaque = destaque.TestCT05Cadastrodedestaque()
    testeDestaque.setup_method("test")
    testeDestaque.test_cT05Cadastrodedestaque()

    print("Teste de Destaques: OK!")

    # Testes de Cadastro de Compromisso
    testeCompromisso = compromisso.TestCT06Cadastrodecompromisso()
    testeCompromisso.setup_method("test")
    testeCompromisso.test_cT06Cadastrodecompromisso()

    print("Teste de Compromissos: OK!")

    # Testes de Cadastro de Pontos
    testePontos = pontos.TestCT07Pontosdousuario()
    testePontos.setup_method("test")
    testePontos.test_cT07Pontosdousuario()

    print("Teste de Pontos: OK!")

    return "Todos os testes foram executados com sucesso!"

retorno = main();

print(retorno)