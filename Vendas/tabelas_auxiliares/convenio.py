import time

def test_cadastro_convenio(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/CadastroConvenios")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirCadastroConvenios')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txEmpresa")     
    
        servicos.clicar_elemento_por_id('btnGravarCadastroConvenios')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_convenio: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_convenio: OK')
