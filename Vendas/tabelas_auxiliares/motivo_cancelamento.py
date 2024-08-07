import time

def test_cadastro_motivo_cancelamento(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/MotivoCancelamentoVenda")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirMotivoCancelamentoVenda')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txDescricaoMotivoCancelamento")     
    
        servicos.clicar_elemento_por_id('btnGravarMotivoCancelamentoVenda')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_motivo_cancelamento: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_motivo_cancelamento: OK')
