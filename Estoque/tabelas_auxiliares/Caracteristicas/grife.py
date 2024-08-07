from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_cadastro_grife(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/Grife")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirGrife')
        time.sleep(1)          
        
        servicos.preenche_input_dev("#txtDescricaoGrife")     

        time.sleep(3) 
    
        servicos.clicar_elemento_por_id('btnGravarGrife')
         
        time.sleep(1)
        
    except:
         servicos.gerar_log('test_cadastro_grife: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_grife: OK')
