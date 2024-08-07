from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_cadastro_sublinha1(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/SubLinha1Esferico")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirSubLinha1Esferico')
        time.sleep(1)          
        
        servicos.preenche_input_dev("#txtDescricaoSubLinha1Esferico")     

        servicos.seleciona_selectbox("txtSelectTipo")
    
        servicos.clicar_elemento_por_id('btnGravarSubLinha1Esferico')
         
        time.sleep(1)
        
    except:
         servicos.gerar_log('test_cadastro_sublinha1: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_sublinha1: OK')
