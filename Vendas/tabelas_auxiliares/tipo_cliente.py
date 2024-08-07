import time

def test_cadastro_tipo_cliente(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/TipoCliente")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirTipoCliente')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txDescricaoTipoCliente")     
    
        servicos.clicar_elemento_por_id('btnGravarTipoCliente')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_tipo_cliente: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_tipo_cliente: OK')
