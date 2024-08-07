from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def transferencia(servicos, navegador, sequencial):
    

    try:

        navegador.get("http://localhost:51265/TransferenciaEstoque")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluir')

        time.sleep(1)  
    
    
        servicos.seleciona_selectbox('txtLojaDestino', 2)
    
        servicos.preenche_input_dev("#txtCodProduto", sequencial)
        
        servicos.clicar_botao_pesquisa("#txtCodProduto")
    
        icone_salvar = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "i.fa.fa-save.center.fa-2x"))
            )

        botao_salvar = icone_salvar.find_element(By.XPATH, "./ancestor::div[contains(@class, 'dx-button-content')]")
        
        botao_salvar.click()
    
    
        servicos.clicar_elemento_por_id('btnSalvar')


        botao_confirmar = WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirmar') and contains(@class, 'btn-danger')]")))

        botao_confirmar.click()
        
        servicos.gerar_log('Transferência: OK')

    

    finally:
        servicos.gerar_log('Transferência: NOTOK')
