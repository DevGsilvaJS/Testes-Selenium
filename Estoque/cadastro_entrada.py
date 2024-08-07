import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def cadastro_entrada(servicos, navegador):
    
    try:
        navegador.get("http://localhost:51265/Produto")
        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluir')
        time.sleep(1)
        
        
        script = 'return $("#txtCodigo").dxTextBox("instance").option("value");'

# Execute o script e armazene o valor
        valor = navegador.execute_script(script)

        script = """
            var widget = $("#ddlNCM").dxSelectBox("instance");
            widget.option("value", "60");
            """
        navegador.execute_script(script)

        servicos.seleciona_selectbox('ddlFornecedor')
        time.sleep(1)
        
        

        servicos.preenche_input_obrigatorio("#txtMVMQUANTIDADE", 5)
        servicos.preenche_input_obrigatorio("#txtCustoUnitario", 150)
        servicos.preenche_input_obrigatorio("#txtmarkup", 100)
        servicos.preenche_input_obrigatorio("#txtPrecoVenda", 300)

        servicos.preenche_input_dev("#collapseAtrinutosProduto > div > div:nth-child(1) > div:nth-child(1) > div > div > div.dx-texteditor-container > div.dx-texteditor-input-container")
        servicos.preenche_input_dev("#collapseAtrinutosProduto > div > div:nth-child(1) > div:nth-child(2) > div > div > div.dx-texteditor-container > div.dx-texteditor-input-container")
        servicos.preenche_input_dev("#collapseAtrinutosProduto > div > div:nth-child(1) > div:nth-child(3) > div > div > div.dx-texteditor-container > div.dx-texteditor-input-container")
        servicos.preenche_input_dev("#collapseAtrinutosProduto > div > div:nth-child(1) > div:nth-child(4) > div > div > div.dx-texteditor-container > div.dx-texteditor-input-container")
        servicos.preenche_input_dev("#collapseAtrinutosProduto > div > div:nth-child(1) > div:nth-child(5) > div > div > div.dx-texteditor-container > div.dx-texteditor-input-container")
        servicos.preenche_input_dev("#collapseAtrinutosProduto > div > div:nth-child(1) > div:nth-child(6) > div > div > div.dx-texteditor-container > div.dx-texteditor-input-container")
        servicos.preenche_input_dev("#collapseAtrinutosProduto > div > div:nth-child(1) > div:nth-child(7) > div > div > div.dx-texteditor-container > div.dx-texteditor-input-container")
        servicos.preenche_input_dev("#collapseAtrinutosProduto > div > div:nth-child(1) > div:nth-child(8) > div > div > div.dx-texteditor-container > div.dx-texteditor-input-container")   
        
        
   
        
        time.sleep(1)
           
        WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#txtCodigoFantasia"))
            )

        servicos.preenche_input_obrigatorio("#txtCodigoFantasia", servicos.gerar_texto(10))
        servicos.clicar_elemento_por_id('btnSalvar')
        time.sleep(3)

        WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#mdOpcaoCadastro > div > div"))
            )

        opcao_entrada_produto = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.ID, "optionsRadios3"))
            )
        opcao_entrada_produto.click()

        botao_prosseguir = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.ID, "btnProsseguir"))
            )
        botao_prosseguir.click()
        time.sleep(3)

        servicos.preenche_input_dev("#txtMVNNUMNOTA > div.dx-texteditor-container > div.dx-texteditor-input-container", 12345)
        servicos.preenche_input_obrigatorio("#txtMVNNUMNOTA", 12345)
        time.sleep(2)

        botao_expandir = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-toggle='collapse'] > button.clsbtnMaisFiltro"))
            )
        botao_expandir.click()
        time.sleep(1)
            
            
        modal = WebDriverWait(navegador, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jconfirm-box")))
        botao_ok = modal.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
        botao_ok.click()

        servicos.seleciona_selectbox('ddlCFOPPadrao')
        servicos.clicar_elemento_por_id("btnRepassar")
        servicos.clicar_elemento_por_id("btnSalvar")           
            
        time.sleep(2)

        botao_sim = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='SIM']"))
            )
        botao_sim.click()            
            
        time.sleep(2)

        return valor 

    except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")
            return False 

    finally:
        servicos.gerar_log("ENTRADA DE ESTOQUE: OK")