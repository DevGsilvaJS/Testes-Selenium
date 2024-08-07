from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException


class Servicos:
    def __init__(self, navegador):
        self.navegador = navegador

    def gerar_texto(self, tamanho=3):
        letras = string.ascii_uppercase
        return ''.join(random.choice(letras) for _ in range(tamanho))
    

   
    def preenche_input(self, elemento_id, texto):
        input_element = self.navegador.find_element(By.ID, elemento_id)
        input_element.send_keys(texto)

    def clicar_elemento_por_id(self, elemento_id, pesquisaCSS=False):
                
        
        if pesquisaCSS:
                
            wait = WebDriverWait(self.navegador, 10)
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento_id)))
            button.click()
            
        else:
            try:
                button_element = self.navegador.find_element(By.ID, elemento_id)
                button_element.click()
            except Exception as e:
                wait = WebDriverWait(self.navegador, 10)
                button_element = wait.until(EC.element_to_be_clickable((By.ID, elemento_id)))
                button_element.click()  

    def preenche_input_dev(self, elemento_id, valor=""):      
        
        dxnumber = False          
        try:
            
            if isinstance(valor, (int, float)):
                dxnumber = True            
            
            if valor == "":
                texto_aleatorio = self.gerar_texto()
            else:
                texto_aleatorio = valor

            campo = WebDriverWait(self.navegador, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, elemento_id)))
            
            
            if dxnumber == True:
                seletor_css = f"{elemento_id} .dx-texteditor-input"
                input_element = campo.find_element(By.CSS_SELECTOR,seletor_css)
                
            else:
                input_element = campo.find_element(By.TAG_NAME, "input")   
                                  
            input_element.clear()
            time.sleep(1)  # Pequena pausa após limpar o campo

            actions = ActionChains(self.navegador)
            actions.move_to_element(input_element)
            actions.click(input_element)
            actions.send_keys(texto_aleatorio)
            actions.perform()
 
            
            
            substring = "collapseAtrinutosProduto"
            
            if substring in elemento_id:
                time.sleep(3) 
                

                count = 0
                while count < 2:
                    try:
                        modal = WebDriverWait(self.navegador, 2).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "#mdOpcaoCadastroAtributo > div > div > div.modal-footer")))

                        botao_sim = modal.find_element(By.ID, "btnSalvarDescricaoAtributo")
                        botao_sim.click()
                        time.sleep(2)
                        count += 1#
                    except Exception as e:
                        count += 1
                        time.sleep(1)

            return texto_aleatorio
        except Exception as e:
            return None        
                
    
    def preenche_input_obrigatorio(self, elemento, valor):
        try:
            script = f"""var widget = $("{elemento}").dxTextBox("instance");widget.option("value", "{valor}");"""
            self.navegador.execute_script(script)
        except Exception as e1:
            try:
                script = f"""var widget = $("{elemento}").dxNumberBox("instance");widget.option("value", "{valor}");"""
                self.navegador.execute_script(script)
            except Exception as e2:
                print(f"Erro na primeira tentativa: {e1}")
                print(f"Erro na segunda tentativa: {e2}")
        
    def clicar_botao_pesquisa(self, elemento_id):
        try:
            campo = WebDriverWait(self.navegador, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, elemento_id)))

            botao_pesquisa = campo.find_element(By.CSS_SELECTOR, "div[role='button'][aria-label='Pesquisar ...']")
        
            botao_pesquisa.click()

        except Exception as e:
            print(f"Erro ao clicar no botão de pesquisa: {e}")   



    def gerar_log(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('log.txt', 'a') as file:
            file.write(f'[{timestamp}] {message}\n')





    def seleciona_selectbox(self, seletor_base, opcao=1):        
        
        valor = f'//*[@id="{seletor_base}"]/div[1]/div'        
        
        try:
            dropdown = WebDriverWait(self.navegador, 10).until(
                EC.visibility_of_element_located((By.XPATH, valor))
            )
            self.navegador.execute_script("arguments[0].scrollIntoView(true);", dropdown)
            dropdown.click()
            
            
            if opcao == 1:
        
                primeira_opcao = WebDriverWait(self.navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".dx-list .dx-list-item")))
                primeira_opcao.click()
            else:
                segunda_opcao = WebDriverWait(self.navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".dx-list .dx-list-item:nth-child(2)")))
                segunda_opcao.click()
                    
      
        
            time.sleep(3)
        except Exception as e:
            print(f"Erro ao selecionar a opção: {e}")


    


    def preenche_valor(self, elemento_id, valor):
        
        elemento = elemento_id + " div.dx-texteditor-container > div.dx-texteditor-input-container"
        
        campo = WebDriverWait(self.navegador, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, elemento)))
        self.navegador.execute_script(f"arguments[0].value = '{valor}';", campo)
        self.navegador.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", campo)
        self.navegador.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", campo)
        
        valor_atualizado = self.navegador.execute_script("return arguments[0].value;", campo)

    def preenche_data(self, id_elemento, data):

        try:
 
            wait = WebDriverWait(self.navegador, 10)
            date_box_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f"#{id_elemento} > div.dx-dropdowneditor-input-wrapper > div > div.dx-texteditor-input-container"))
            )

        # Script para configurar e definir a data no dxDateBox
            script = f"""
            var _Data = "{data}"; // Data específica que você deseja definir

        function toDate(dateStr) {{
            var parts = dateStr.split("/");
            return new Date(parts[2], parts[1] - 1, parts[0]);
        }}

        var dateBoxElement = $('#{id_elemento}');
        if (dateBoxElement.length) {{
            dateBoxElement.dxDateBox({{
                label: "Data de:",
                labelMode: "static",
                type: "date",
                pickerType: "calendar",
                value: toDate(_Data),
                dateSerializationFormat: "yyyyMMdd",
                displayFormat: "dd/MM/yyyy"
            }});

            var dateBox = dateBoxElement.dxDateBox("instance");
            dateBox.option("value", toDate(_Data));
        }}
        """
            self.navegador.execute_script(script)
    
        except Exception as e:
            print(f"Erro ao configurar a data no dxDateBox: {e}")
            
            
            
    def seleciona_all_dxgrid(self):
         
        wait = WebDriverWait(self.navegador, 10)

        while True:
            try:
                element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.dx-select-checkbox")))
                element.click()
                break
            except StaleElementReferenceException:
                continue      
            
            
            
    def click_grid(self, valor):     
      
        self.preenche_input("Valor", valor)
        
        self.clicar_elemento_por_id('btmPesquisaListaGeral')
        
        time.sleep(3)
               
        grid_element = self.navegador.find_element(By.CSS_SELECTOR, "#gridContainerListaGeral > div > div.dx-datagrid-rowsview.dx-datagrid-nowrap.dx-scrollable.dx-visibility-change-handler.dx-scrollable-both.dx-scrollable-simulated.dx-fixed-columns > div.dx-scrollable-wrapper > div > div.dx-scrollable-content > div > table > tbody > tr:nth-child(1) > td:nth-child(1)")

        actions = ActionChains(self.navegador)
        time.sleep(1)

        actions.double_click(grid_element).perform()
        time.sleep(1)
        
        
    def retorna_valor_checkbox(self, componente):
        checkbox = WebDriverWait(self.navegador, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, componente))
    )

        aria_checked = checkbox.get_attribute('aria-checked')
    
        if aria_checked == 'true':
            return 1
        else:
            return 0  
        

    def retorna_valor_selectbox(self, componente):
        hidden_input = self.navegador.find_element(By.CSS_SELECTOR, '#txtcomissaovend input[type="hidden"]')

        value = hidden_input.get_attribute('value')

        return value   





    def retorna_atributo(self, componente):       
        
        try:
            input_element = WebDriverWait(self.navegador, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f"{componente} .dx-texteditor-input"))
            )
            return input_element.get_attribute("value")
        except Exception as e:
            return None
        
   
        
    def comparar_objetos(self, obj1, obj2):
        try:
            atributos_obj1 = {k: v for k, v in obj1.__dict__.items() if not k.startswith('__')}
            atributos_obj2 = {k: v for k, v in obj2.__dict__.items() if not k.startswith('__')}

            diferencas = []

            for chave, valor1 in atributos_obj1.items():
                if chave in atributos_obj2:
                    valor2 = atributos_obj2[chave]                  
            
                    
                    if not(str(valor1) == str(valor2)):
                        diferenca = {
                        'atributo': chave,
                        'valor_obj1': valor1,
                        'valor_obj2': valor2
                        }
                        diferencas.append(diferenca)
                        
            if diferencas:            
                diferencas_str = "\n".join(
                    [f"Atributo: {d['atributo']}, Valor Objeto 1: {d['valor_obj1']}, Valor Objeto 2: {d['valor_obj2']}" 
                    for d in diferencas]
            )            
        
            return diferencas_str
    
        except Exception as e:
            print(f"Erro ao comparar objetos: {e}")
            return None
        
    def marcar_checkbox(self,elemento_id):
        try:
            checkbox = WebDriverWait(self.navegador, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, elemento_id))
        )
       
            
            checkbox.click()
        
        except Exception as e:
            print(f"Erro ao marcar o checkbox: {e}")    
        
            




        
            


