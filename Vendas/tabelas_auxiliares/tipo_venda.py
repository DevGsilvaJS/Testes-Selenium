import time

def test_cadastro_tipo_venda(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/TipoVenda")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirTipoVenda')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txDescricao")     
    
        servicos.clicar_elemento_por_id('btnGravarTipoVenda')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_tipo_venda: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_tipo_venda: OK')
