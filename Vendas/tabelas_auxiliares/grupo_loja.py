import time

def test_cadastro_grupo_loja(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/GrupoLoja")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirGrupoLoja')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txtDescGrupoLoja")     
    
        servicos.clicar_elemento_por_id('btnGravarGrupoLoja')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_grupo_loja: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_grupo_loja: OK')
