class Relogio:
    def __init__(self, horas, minutos, segundos):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def set_hora(self, h, m, s):

        if (0 <= h <= 23) and (0 <= m <= 59) and (0 <= s <= 59):
            self.__horas = h
            self.__minutos = m
            self.__segundos = s
        else:
            print("Erro: horário fora do padrão aceitável.")

    def get_hora(self):
        return f"{self.__horas:02d}:{self.__minutos:02d}:{self.__segundos:02d}"

    def avancar_segundo(self):
        self.__segundos += 1

        # Cascata lógica de verificação
        if self.__segundos == 60:
            self.__segundos = 0
            self.__minutos += 1

        if self.__minutos == 60:
            self.__minutos = 0
            self.__horas += 1

        if self.__horas == 24:
            self.__horas = 0

    def exibir(self):
        print(self.get_hora())


# --- Testando o funcionamento ---
r1 = Relogio(20, 39, 19)
r1.set_hora(23, 59, 58)
r1.avancar_segundo()
r1.exibir()
r1.avancar_segundo()
r1.exibir()
