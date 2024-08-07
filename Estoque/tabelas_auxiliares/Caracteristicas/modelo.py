from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_cadastro_modelo(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/CadastroModeloFamilia")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirCadastroModeloFamilia')
        time.sleep(1)          
        
        servicos.preenche_input_dev("#txtDescricaoModeloFamilia")     

        servicos.seleciona_selectbox("txtSelectTipo")
    
        servicos.clicar_elemento_por_id('btnGravarCadastroModeloFamilia')
         
        time.sleep(1)
        
    except:
         servicos.gerar_log('test_cadastro_modelo: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_modelo: OK')
