import time

def test_cadastro_pronome_tratamento(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/PronomeTratamento")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirPronomeTratamento')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txDescricaoPronomeTratamento")     
    
        servicos.clicar_elemento_por_id('btnGravarPronomeTratamento')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_pronome_tratamento: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_pronome_tratamento: OK')
