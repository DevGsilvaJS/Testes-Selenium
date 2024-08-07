import time

def transferencia_lote(servicos, navegador, sequencial):
    
    
    try:


        navegador.get("http://localhost:51265/TransferenciaPorLote")

        time.sleep(3)

        servicos.clicar_elemento_por_id('btnIncluirTransLote')

        time.sleep(1)   
    
    
        servicos.seleciona_selectbox('ddlLojaDestinoTransLote', 2)
    
        script = """
            var widget = $("#ddlCfopTransLote").dxSelectBox("instance");
            widget.option("value", "6");
            """
        navegador.execute_script(script)
    
        servicos.preenche_input_dev("#txtProdutoTransLote", sequencial)
        
    
        servicos.clicar_elemento_por_id("btnPesquisaProdTrans");    
    
        time.sleep(1)
    
        servicos.clicar_elemento_por_id("btnSalvaProdutoTransLote");
    
        time.sleep(1)
        servicos.clicar_elemento_por_id('btnGravarTransLote')
        time.sleep(2)
        servicos.gerar_log('Transferência por lote: OK')  
    finally:
        servicos.gerar_log('Transferência por lote: NOTOK')    
    