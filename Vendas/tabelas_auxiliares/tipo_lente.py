import time

def test_cadastro_tipo_lente(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/TipoLente")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirTipoLente')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txDescricaoTipoLente")     
    
        servicos.clicar_elemento_por_id('btnGravarTipoLente')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_tipo_lente: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_tipo_lente: OK')
