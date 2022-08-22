#BancoMySql
from database.config import *;

#Cpu
from controller.CpuController import *;

#Memória
from controller.MemoriaController import *;

#Disco
from controller.DiscoController import *;


class App:

    informacao_hardware = '';


    @staticmethod 
    def perguntar_usuario():
        print("Digite o número do que deseja acessar\n");
        print(
            "(1) Cpu\n"+
            "(2) Memória\n"+
            "(3) Disco\n"
        );
        resposta_usuario = int(input("Resposta: "));

        if resposta_usuario != 1 and resposta_usuario != 2 and resposta_usuario != 3:
            raise Exception;
        
        return resposta_usuario;


    def escolher_componente_hardware(self):
        
        try : 
            pergunta_usuario = App.perguntar_usuario();

            if(pergunta_usuario == 1):
                self.informacao_hardware = CpuController(Cpu(), CpuView(), BancoMySql(), CpuDao());

            elif(pergunta_usuario == 2):
                self.informacao_hardware = MemoriaController(Memoria(), MemoriaView(), BancoMySql(), MemoriaDao());

            else:
                self.informacao_hardware = DiscoController(Disco(), DiscoView(), BancoMySql(), DiscoDao())

        
        except:
            print("Escolha inválida");

        


    
    def iniciar_programa(self):
        self.escolher_componente_hardware();
        try:
            self.informacao_hardware.iniciar();
        
        except:
            print("Não foi possível iniciar o programa");

programa = App();
programa.iniciar_programa();
