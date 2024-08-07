from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Servicos.utils import Servicos
from Autenticacao.login import login
from Estoque.cadastro_entrada import cadastro_entrada
from Estoque.transferencia_lote import transferencia_lote
from Estoque.transferencia import transferencia
from Estoque.importacao_xml import importacao_estorno
from Estoque.estorno_movimentacao import estorno_movimentacao
from Estoque.saida_estoque import saida_estoque
from Estoque.inventario import inventario
from Estoque.tabelas_auxiliares.Caracteristicas.cor import test_cadastro_cor
from Estoque.tabelas_auxiliares.Caracteristicas.grife import test_cadastro_grife
from Estoque.tabelas_auxiliares.Caracteristicas.base import test_cadastro_base
from Estoque.tabelas_auxiliares.Caracteristicas.cor_numerica import test_cadastro_cornumerica
from Estoque.tabelas_auxiliares.Caracteristicas.fabricante import test_cadastro_fabricante
from Estoque.tabelas_auxiliares.Caracteristicas.grife import test_cadastro_grife
from Estoque.tabelas_auxiliares.Caracteristicas.grupo import test_cadastro_grupo
from Estoque.tabelas_auxiliares.Caracteristicas.linha import test_cadastro_linha
from Estoque.tabelas_auxiliares.Caracteristicas.modelo import test_cadastro_modelo
from Estoque.tabelas_auxiliares.Caracteristicas.sublinha1 import test_cadastro_sublinha1
from Estoque.tabelas_auxiliares.Caracteristicas.sublinha2 import test_cadastro_sublinha2
from Vendas.tabelas_auxiliares.grupo_loja import test_cadastro_grupo_loja
from Vendas.tabelas_auxiliares.vendedor import test_cadastro_vendedor
from Vendas.tabelas_auxiliares.tipo_venda import test_cadastro_tipo_venda
from Vendas.tabelas_auxiliares.tipo_lente import test_cadastro_tipo_lente
from Vendas.tabelas_auxiliares.tipo_cliente import test_cadastro_tipo_cliente
from Vendas.tabelas_auxiliares.pronome_tratamento import test_cadastro_pronome_tratamento
from Vendas.tabelas_auxiliares.motivo_cancelamento import test_cadastro_motivo_cancelamento
from Vendas.tabelas_auxiliares.justificativa_desconto import test_cadastro_justificativa_desconto
from Vendas.tabelas_auxiliares.indicacao import test_cadastro_indicacao
from Vendas.tabelas_auxiliares.departamento import test_cadastro_departamento
from Vendas.tabelas_auxiliares.convenio import test_cadastro_convenio



class TesteAutomatizado:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome()
        self.servicos = Servicos(self.navegador)

    
    def run_tests(self):
        
        login(self.servicos, self.navegador)
        test_cadastro_vendedor(self.servicos, self.navegador)  
        #self.run_test_tabelas_auxiliares_vendas()           
        #self.run_test_cadastro_atributos()
        #self.run_test_modulo_produtos()     
          
        
    def run_test_modulo_produtos(self):
        sequencial = cadastro_entrada(self.servicos, self.navegador)         
        saida_estoque(self.servicos, self.navegador, sequencial)
        transferencia_lote(self.servicos, self.navegador, sequencial) 
        transferencia(self.servicos, self.navegador, sequencial) 
        inventario(self.servicos, self.navegador, sequencial)
                  
        
    def run_test_cadastro_atributos(self):
        test_cadastro_cornumerica(self.servicos, self.navegador) 
        test_cadastro_cor(self.servicos, self.navegador) 
        test_cadastro_fabricante(self.servicos, self.navegador)         
        test_cadastro_grife(self.servicos, self.navegador) 
        test_cadastro_base(self.servicos, self.navegador) 
        test_cadastro_grife(self.servicos, self.navegador) 
        test_cadastro_grupo(self.servicos, self.navegador) 
        test_cadastro_linha(self.servicos, self.navegador) 
        test_cadastro_modelo(self.servicos, self.navegador) 
        test_cadastro_sublinha1(self.servicos, self.navegador) 
        test_cadastro_sublinha2(self.servicos, self.navegador) 
        
              
    def run_test_tabelas_auxiliares_vendas(self):
        test_cadastro_vendedor(self.servicos, self.navegador)
        test_cadastro_tipo_venda(self.servicos, self.navegador)
        test_cadastro_tipo_lente(self.servicos, self.navegador)
        test_cadastro_tipo_cliente(self.servicos, self.navegador)
        test_cadastro_pronome_tratamento(self.servicos, self.navegador)
        test_cadastro_motivo_cancelamento(self.servicos, self.navegador)
        test_cadastro_justificativa_desconto(self.servicos, self.navegador)
        test_cadastro_indicacao(self.servicos, self.navegador)
        test_cadastro_departamento(self.servicos, self.navegador)
        test_cadastro_convenio(self.servicos, self.navegador)    
        
                  
        
if __name__ == "__main__":
    teste = TesteAutomatizado()
    teste.run_tests()   