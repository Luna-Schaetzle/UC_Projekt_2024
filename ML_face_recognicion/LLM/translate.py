

# Importiere die notwendigen Module
from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging

# Lade ein vortrainiertes Modell
predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bert-base-srl-2020.03.24.tar.gz")

# Verwende das Modell zur Vorhersage
prediction = predictor.predict(sentence="Once upon a time")

# Zeige die Vorhersage an
print(prediction)
