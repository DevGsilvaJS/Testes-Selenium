import time




def estorno_movimentacao(servicos, navegador):
    
    
        navegador.get("http://localhost:51265/EstornoMovimentacao")
        
        servicos.preenche_data("txtESTORNODE", "29/07/2024")
        servicos.preenche_data("txtESTORNOATE", "29/07/2024")

        servicos.seleciona_selectbox('//*[@id="txtLojas"]/div[1]/div/div[1]')

        servicos.preenche_input_dev("#txtNOTASDE > div.dx-texteditor-container > div.dx-texteditor-input-container", 323771)
        servicos.preenche_input_dev("#txtNOTASATE > div.dx-texteditor-container > div.dx-texteditor-input-container", 323771)

        time.sleep(5)
        servicos.clicar_elemento_por_id("#btnPesquisa", True)


        servicos.seleciona_all_dxgrid() 
           

        servicos.clicar_elemento_por_id("#btnConfirmar", True)
        servicos.clicar_elemento_por_id("#btnSimConfirmacao", True)
        servicos.clicar_elemento_por_id("#btnSimConfirmacao", True)
