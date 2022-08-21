class DiscoDao:

    @staticmethod
    def inserir_dados_disco(cursor, dados_disco):
        query = "INSERT INTO Disco VALUES (null, %s, %s, %s, %s)";
        cursor.execute(
            query, 
            (dados_disco["total"],
             dados_disco["usado"] ,
             dados_disco["porcentagem_disco_usado"],
             dados_disco["livre"])
        )

