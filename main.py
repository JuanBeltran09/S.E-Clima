from experta import Fact, KnowledgeEngine, Rule, P

# Definición de los hechos:
class Weather(Fact):
    """Representa los hechos sobre las condiciones atmosféricas."""
    pass

# Definición del motor de inferencia:
class WeatherExpert(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.result = ""

    @Rule(Weather(temperature=P(lambda t: t >= 30), humidity=P(lambda h: h < 60)))
    def hot_weather(self):
        self.result = "El clima es caluroso"

    @Rule(Weather(temperature=P(lambda t: t <= 15)))
    def cold_weather(self):
        self.result = "El clima es frío"

    @Rule(Weather(temperature=P(lambda t: 15 < t < 30), humidity=P(lambda h: h > 70)))
    def rainy_weather(self):
        self.result = "El clima es lluvioso"

    @Rule(Weather(wind_speed=P(lambda w: w >= 50)))
    def windy_weather(self):
        self.result = "El clima es ventoso"
