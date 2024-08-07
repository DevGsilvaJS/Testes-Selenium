from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def inventario(servicos, navegador, sequencial):
    

    try:

        navegador.get("http://localhost:51265/Inventario")

        time.sleep(3)
        
        servicos.preenche_input_dev("#edtCodigoSequenciaInventario > div.dx-texteditor-container", sequencial)
        
        servicos.clicar_elemento_por_id("#btnpesquisarInventario", True)
        
        time.sleep(2)        

        wait = WebDriverWait(navegador, 10)
        
        grid = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grdProdutoInvetario")))
        quantidade_celula = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grdProdutoInvetario > div > div.dx-datagrid-rowsview.dx-datagrid-nowrap.dx-scrollable.dx-visibility-change-handler.dx-scrollable-both.dx-scrollable-simulated.dx-scrollable-scrollbars-alwaysvisible > div > div > div.dx-scrollable-content > div > table > tbody > tr.dx-row.dx-data-row.dx-row-lines.dx-column-lines > td.ColorValor")))
        quantidade_celula.click()
        
        input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#grdProdutoInvetario td.ColorValor input.dx-texteditor-input")))

        input_element.clear()
        input_element.send_keys("1")
        
        servicos.clicar_elemento_por_id('btnAlterarInventario')   
        
        time.sleep(1)
        
        textarea_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#txtJustificativaAjuste textarea.dx-texteditor-input")))


        textarea_element.click()


        textarea_element.clear()
        textarea_element.send_keys("Ajuste de inventario")
        
        servicos.clicar_elemento_por_id('btnGravarInventario')                   
       

    finally:
        servicos.gerar_log('Saída Estoque: OK')
