import time

def test_cadastro_justificativa_desconto(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/JustificativaDesconto")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirJustificativaDesconto')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txDescricaoJustificativaDesconto")     
    
        servicos.clicar_elemento_por_id('btnGravarJustificativaDesconto')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_justificativa_desconto: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_justificativa_desconto: OK')
