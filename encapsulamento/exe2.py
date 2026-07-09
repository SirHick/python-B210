class Termostato:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    '''
    get_temperatura() - retorna a temperatura atual
    set_temperatura(valor) - define a temperatura, mas apenas se estiver entre
    16 e 30 graus (fora desse intervalo, exibe aviso e não altera)
    exibir_status() - exibe a temperatura atual
    '''

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, valor):

        if 16 <= valor <= 30:
            self.__temperatura = valor
            print("Temperatura alterada com sucesso.")
        else:
            print("Aviso: Temperatura inválida! Escolha um valor entre 16 e 30.")

    def exibir_info(self):
        print(f"="* 30)
        print(f"Temperatura atual: {self.get_temperatura()}")
        print(f"="* 30)

t1 = Termostato(18)
t1.set_temperatura(27)
t1.exibir_info()