from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def importacao_estorno(servicos, navegador):
    try:

        navegador.get("http://localhost:51265/")


        navegador.get("http://localhost:51265/ImportacaoXML")

        time.sleep(3)

        file_path = os.path.join(os.getcwd(), '123456.xml')

        upload_element = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.ID, "fileupload"))
        )
        upload_element.send_keys(file_path)

        time.sleep(3)
        

        servicos.clicar_elemento_por_id("#step1 > a.btn.btn-success.btn-flat.next", True)
        time.sleep(1)

        navegador.execute_script(
            "$('#txtPlanoDefaultFornecedor').dxDropDownBox('instance').option('value', null);"
        )
        navegador.execute_script(
            "$('#txtCentroDefaultFornecedor').dxDropDownBox('instance').option('value', null);"
        )

        dropdown_1 = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="txtCentroDefaultFornecedor"]/div[1]/div/div[1]'))
        )
        navegador.execute_script("arguments[0].scrollIntoView(true);", dropdown_1)
        dropdown_1.click()

        loja_element_1 = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='LOJA']"))
        )
        loja_element_1.click()

        dropdown_2 = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="txtPlanoDefaultFornecedor"]/div[1]/div/div[1]'))
        )
        navegador.execute_script("arguments[0].scrollIntoView(true);", dropdown_2)
        dropdown_2.click()

        loja_element_2 = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='DESPESAS']"))
        )
        loja_element_2.click()

        time.sleep(2)

        servicos.clicar_elemento_por_id("#step2 > a.btn.btn-success.btn-flat.next", True)
        time.sleep(1)
        servicos.clicar_elemento_por_id("#step3 > a.btn.btn-success.btn-flat.next", True)

        time.sleep(1)
        servicos.clicar_elemento_por_id("#step4 > a.btn.btn-success.btn-flat.next", True)

        try:
            wait = WebDriverWait(navegador, 10)
            modal_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.jconfirm-content-pane")))

            # Verifique se o elemento está visível
            if modal_element.is_displayed():
                modal_presente = True
            else:
                modal_presente = False

        except Exception as e:
            print("Modal não encontrada ou erro ao verificar a modal:", e)
            modal_presente = False

        if modal_presente:
            servicos.clicar_elemento_por_id("#bodyLayout > div.jconfirm.jconfirm-light.jconfirm-open > div.jconfirm-scrollpane > div > div > div > div > div > div > div > div.jconfirm-buttons > button", True)

        wait = WebDriverWait(navegador, 10)
        select_all_checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.dx-select-checkbox")))
        time.sleep(2)

        select_all_checkbox.click()

        servicos.clicar_elemento_por_id('#btnCadastraProdutos', True)
        time.sleep(2)
        servicos.clicar_elemento_por_id('#bodyLayout > div.jconfirm.jconfirm-light.jconfirm-open > div.jconfirm-scrollpane > div > div > div > div > div > div > div > div.jconfirm-buttons > button.btn.btn-success', True)
        time.sleep(2)
        servicos.clicar_elemento_por_id('#bodyLayout > div.jconfirm.jconfirm-light.jconfirm-open > div.jconfirm-scrollpane > div > div > div > div > div > div > div > div.jconfirm-buttons > button', True)
        servicos.clicar_elemento_por_id("#step4 > a.btn.btn-success.btn-flat.next", True)

        servicos.preenche_input_obrigatorio("#txtMarkupABA5", 200)

        checkbox = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.ID, "chkOpcaoVenda"))
        )
        checkbox.click()

        servicos.clicar_elemento_por_id("#step5 > a.btn.btn-success.btn-flat.next", True)
        time.sleep(1)
        servicos.clicar_elemento_por_id("#step6 > a.btn.btn-success.btn-flat.next", True)

        checkbox = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.ID, "chkDarEntradaABA6"))
        )
        checkbox.click()

        checkbox = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.ID, "chkGerarFinanceiroABA6"))
        )
        checkbox.click()

        servicos.clicar_elemento_por_id("btnFinalizaImportacao")

        servicos.clicar_elemento_por_id(".jconfirm-buttons > button:nth-child(2)", True)

        time.sleep(1)

        servicos.clicar_elemento_por_id(".jconfirm-buttons > button:nth-child(2)", True)

        time.sleep(1)

        servicos.clicar_elemento_por_id(".jconfirm-buttons > button:nth-child(2)", True)

        time.sleep(2)


    finally:
        servicos.gerar_log("IMPORTACAO DE XML: OK")
