import time

def saida_estoque(servicos, navegador, sequencial):
    

    try:

        navegador.get("http://localhost:51265/SaidaEstoque")

        time.sleep(4)

        servicos.clicar_elemento_por_id('btnIncluir')

        time.sleep(4)  
        
        servicos.clicar_elemento_por_id('.clsbtnMaisFiltro',True)
        
        servicos.preenche_input_dev('#txtMVNNUMNOTA > div.dx-texteditor-container', 12345)
        
        time.sleep(2)  
        
        servicos.seleciona_selectbox('ddlCFOP')
        
        servicos.preenche_input_dev("#txtCodProduto", sequencial)
        
    
        servicos.clicar_elemento_por_id("btnBuscaProduto");   
        
        time.sleep(1)
            
        servicos.clicar_elemento_por_id("#btnSalvaProduto", True)
        
        script = """
            var widget = $("#ddlMOMID").dxSelectBox("instance");
            widget.option("value", "1");
            """
        navegador.execute_script(script)
        
        time.sleep(1)
        servicos.clicar_elemento_por_id("#btnSalvar", True)   
        time.sleep(1)                      
            
        servicos.clicar_elemento_por_id("#btnSimConfirmacao", True)   
        time.sleep(5)         
       

    finally:
        servicos.gerar_log('Saída Estoque: OK')
