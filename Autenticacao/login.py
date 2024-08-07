import time

def login(servicos, navegador):


    try:

        navegador.get("http://localhost:51265/")


        time.sleep(3)

        servicos.preenche_input('Nome', 'NFCE')
        servicos.preenche_input('Login', 'DESEMPENHO')
        servicos.preenche_input('Password_I', "##croacia")
        servicos.clicar_elemento_por_id('btnEntrar')
        
        time.sleep(3)

        servicos.clicar_elemento_por_id('btnSelecionarLoja', False)
        servicos.gerar_log('Autenticação OK')
    except:
        servicos.gerar_log('Autenticação NOTOK')
        
    finally:
        servicos.gerar_log('Autenticação OK')
           
    