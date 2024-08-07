import time
from Entidades.Vendedor import Vendedor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_cadastro_vendedor(servicos, navegador):      
    try:


        sucess = False

        navegador.get("http://localhost:51265/Vendedor")

        time.sleep(1)

        servicos.clicar_elemento_por_id('btnIncluirVendedor')
        time.sleep(1)     
                     
        Vendedor.nome = servicos.preenche_input_dev("#txtnomevend")
        Vendedor.ddd = servicos.preenche_input_dev("#txtdddvendedor", 11)
        Vendedor.telvendedor = servicos.preenche_input_dev("#txttelefonevendedor", 25419006)
        Vendedor.salario = servicos.preenche_input_dev("#txtsalariovend", 4.000)
        Vendedor.rg = servicos.preenche_input_dev("#txtrgvend", 505201471)
        Vendedor.email = servicos.preenche_input_dev("#txtemailvend", "GABRIEL@DESEMPENHO.COM.BR")
        Vendedor.pis = servicos.preenche_input_dev("#txtpisvend", 123456)
        Vendedor.telcontato = servicos.preenche_input_dev("#txtcontatovend", "GABRIEL")
        Vendedor.dddcontato = servicos.preenche_input_dev("#txtdddcontatovend", 11)
        Vendedor.dddrecado = servicos.preenche_input_dev("#txtdddrecadovend", 11)
        Vendedor.telrecado = servicos.preenche_input_dev("#txtrecadovend", 25419006)
        Vendedor.dddcel = servicos.preenche_input_dev("#txtdddcelularvend", 11)
        Vendedor.celvendedor = servicos.preenche_input_dev("#txtcelularvend", 983270236)
        Vendedor.descvalor = servicos.preenche_input_dev("#txtdescvalorvend", 10)
        Vendedor.descpercentual = servicos.preenche_input_dev("#txtdescpercenvend", 10)
        Vendedor.tipocomissao = servicos.seleciona_selectbox('txtcomissaovend')
        servicos.marcar_checkbox("#chkDefaultWeb")
        servicos.marcar_checkbox("#chkNaoEntraComissaoGerente")
        servicos.marcar_checkbox("#chkNaoEntraMetaLoja")
        servicos.marcar_checkbox("#chkVendedorExterno")       
        
    
        servicos.clicar_elemento_por_id('btnGravarVendedor')

        time.sleep(1)
        servicos.clicar_elemento_por_id("#bodyLayout > div.jconfirm.jconfirm-light.jconfirm-open > div.jconfirm-scrollpane > div > div > div > div > div > div > div > div.jconfirm-buttons > button.btn.btn-danger", True)
        time.sleep(1)
        servicos.clicar_elemento_por_id("#bodyLayout > div.jconfirm.jconfirm-light.jconfirm-open > div.jconfirm-scrollpane > div > div > div > div > div > div > div > div.jconfirm-buttons > button.btn.btn-danger", True)

         
        time.sleep(2)
        
        navegador.get("http://localhost:51265/Vendedor")
                  
        vendedor2 =  retorna_dados(servicos, Vendedor.nome)


        sucess = True     
         
      
    except Exception as e:
        try:
            error_message = f'test_cadastro_vendedor: NOTOK - {str(e)}'
            servicos.gerar_log(error_message) 
        except Exception as log_error:
            print("Failed to generate log:", log_error)
    finally:

        if sucess:
            servicos.gerar_log('test_cadastro_vendedor: OK')
        



def retorna_dados(servicos, nome):
    
    servicos.click_grid(nome)     
    
    nome = servicos.retorna_atributo("#txtnomevend")
    ddd = servicos.retorna_atributo("#txtdddvendedor")
    telvendedor = servicos.retorna_atributo("#txttelefonevendedor")
    salario = servicos.retorna_atributo("#txtsalariovend")
    rg = servicos.retorna_atributo("#txtrgvend")
    email = servicos.retorna_atributo("#txtemailvend")
    telcontato = servicos.retorna_atributo("#txtcontatovend")
    dddcontato = servicos.retorna_atributo("#txtdddcontatovend")
    dddrecado = servicos.retorna_atributo("#txtdddrecadovend")
    telrecado = servicos.retorna_atributo("#txtrecadovend")
    dddcel = servicos.retorna_atributo("#txtdddcelularvend")
    celvendedor = servicos.retorna_atributo("#txtcelularvend")
    descvalor = servicos.retorna_atributo("#txtdescvalorvend")
    descpercentual = servicos.retorna_atributo("#txtdescpercenvend")
    defaultweb = servicos.retorna_valor_checkbox("#chkDefaultWeb")
    comissaogerente = servicos.retorna_valor_checkbox("#chkDefaultWeb")
    metaloja = servicos.retorna_valor_checkbox("#chkDefaultWeb")
    vendedorexterno = servicos.retorna_valor_checkbox("#chkDefaultWeb")
    pis = servicos.retorna_atributo("#txtpisvend")
    tipocomissao = servicos.retorna_valor_selectbox("#txtcomissaovend")

    
    return Vendedor(nome, 
                    ddd, 
                    telvendedor, 
                    salario, 
                    rg, 
                    email, 
                    telcontato, 
                    dddcontato, 
                    dddrecado, 
                    telrecado, 
                    dddcel, 
                    celvendedor, 
                    descvalor, 
                    descpercentual, 
                    defaultweb, 
                    comissaogerente, 
                    metaloja, 
                    vendedorexterno,
                    pis,
                    tipocomissao)




    


    
    