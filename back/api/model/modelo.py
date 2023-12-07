import numpy as np
import pickle
import joblib

class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um cliente com base no modelo treinado
        """
        # Função auxiliar para mapear "sim" e "não" para 1 e 0
        if form.chronic_diseases.lower() == "sim":
            chronic_diseases = 1
        elif form.chronic_diseases.lower() == "não":
            chronic_diseases = 0

        if form.graduate_or_not.lower() == "sim":
            graduate_or_not = 1
        elif form.graduate_or_not.lower() == "não":
            graduate_or_not = 0
    
        if form.frequent_flyer.lower() == "sim":
            frequent_flyer = 1
        elif form.frequent_flyer.lower() == "não":
            frequent_flyer = 0

        if form.ever_travelled_abroad.lower() == "sim":
            ever_travelled_abroad = 1
        elif form.ever_travelled_abroad.lower() == "não":
            ever_travelled_abroad = 0

        # Mapeando "Setor Governamental" e "Setor Privado/Autônomo" para 1 e 0
        if form.employment_type.lower() == "setor governamental":
            employment_type = 0
        elif form.employment_type.lower() == "setor privado/autônomo":
            employment_type = 1

        X_input = np.array([form.age, 
                            employment_type, 
                            graduate_or_not, 
                            form.annual_income, 
                            form.family_members, 
                            chronic_diseases, 
                            frequent_flyer, 
                            ever_travelled_abroad
                        ])
        
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])