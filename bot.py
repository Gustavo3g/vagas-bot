from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date


browser = Chrome()

# Função responsavel pelo login no site do Trabalha Brasilf
def loginTrabalha(cpf, nascimento):
    print("######\033[1;32m BUSCANDO VAGAS \033[0;0m ######")
    browser.get('https://www.trabalhabrasil.com.br/')
    browser.implicitly_wait(10)
    browser.find_element_by_id('footer-access-link').click()
    browser.find_element_by_id("txtLoginCPF").send_keys(cpf)
    browser.find_element_by_id("txtLoginNascimento").send_keys(nascimento)
    sleep(3)
    browser.find_element_by_id("txtLoginName").click()
    sleep(2)


# Função resposavel pela listagem das vagas
def listJobs():
    browser.get('https://www.trabalhabrasil.com.br/vagas-empregos-em-imperatriz-ma')
    data_atual = date.today().strftime("%d/%m/%Y")
    print(f"###### \033[1;41mLISTANDO VAGAS\033[0;0m ######\n         {data_atual}")
    sleep(1)
    jobs = browser.find_elements_by_class_name('job__container')
    for job in jobs:
        print(job.text)
        print('\033[1;34m###########################\033[0;0m')


decisao = int(input("Você tem um curriculo cadastrado no site Trabalha Brasil ?\n1- Sim \n2- Quero listar vagas sem fazer login\n>>> "))

if decisao == 1:
    try:
        cpf = str(input("Digite seu cpf:\n> "))
        nasc = str(input("Digite sua data de nascimento:\n> "))
        loginTrabalha(cpf, nasc)
        listJobs()
    except:
        print("Desculpe, algo deu errado!\nTente Novamente")
        exit()
else:
    print("dica:\nAlgumas vagas só aparecem para pessoas cadastradas")
    sleep(3)
    listJobs()
