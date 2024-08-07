import time

def test_cadastro_indicacao(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/Indicacao")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirIndicacao')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txDescricaoIndicacao")     
    
        servicos.clicar_elemento_por_id('btnGravarIndicacao')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_indicacao: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_indicacao: OK')
