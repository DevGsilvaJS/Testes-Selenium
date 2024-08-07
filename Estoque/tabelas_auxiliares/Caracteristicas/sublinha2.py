import time

def test_cadastro_sublinha2(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/SubLinha2Cilindrico")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirSubLinha2Cilindrico')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txtDescricaoSubLinhaCilindrica")     

        servicos.seleciona_selectbox("txtSelectTipo")
    
        servicos.clicar_elemento_por_id('btnGravarSubLinha2Cilindrico')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_sublinha2: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_sublinha2: OK')
