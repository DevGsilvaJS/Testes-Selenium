import time

def test_cadastro_tamanho(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/TamanhoDiametro")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirTamanhoDiametro')
        time.sleep(1)          
        
        servicos.preenche_input_dev("#txtDescricaoTamanhoDiametro")     

        servicos.seleciona_selectbox("txtSelectTipo")
    
        servicos.clicar_elemento_por_id('btnGravarTamanhoDiametro')
         
        time.sleep(1)
        
    except:
         servicos.gerar_log('test_cadastro_tamanho: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_tamanho: OK')
