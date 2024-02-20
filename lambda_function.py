
from page import manipulate_html_file

def lambda_handler():

    return manipulate_html_file(['Belford Roxo', 'Mesquita', 'Nova Iguaçu', 'Nilópolis', 'Irajá'])


lambda_handler()