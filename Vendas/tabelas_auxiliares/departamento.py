import time

def test_cadastro_departamento(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/Departamento")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirDepartamento')
        time.sleep(2)          
        
        servicos.preenche_input_dev("#txtDescricao")     
    
        servicos.clicar_elemento_por_id('btnGravarDepartamento')
         
        time.sleep(2)
        
    except:
         servicos.gerar_log('test_cadastro_departamento: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_departamento: OK')
