from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_cadastro_cor(servicos, navegador):
    

    try:

        navegador.get("http://localhost:51265/CadastroCoresProdutos")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirCadastroCoresProdutos')

        time.sleep(1)  
        
        
        servicos.preenche_input_dev("#txtDescricaoCoresProduto")
        
        servicos.seleciona_selectbox("txtSelectTipo")
    
    
        time.sleep(5)  
    
    
        servicos.clicar_elemento_por_id('btnGravarCadastroCoresProdutos')
        
        
        time.sleep(1)
        
    except:
         servicos.gerar_log('test_cadastro_cor: NOTOK')     

    finally:
        servicos.gerar_log('test_cadastro_cor: OK')
