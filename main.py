from experta import Fact, KnowledgeEngine, Rule, P, AS, Field


class Weather(Fact):
    pass


class WeatherExpert(KnowledgeEngine):
    result = ""

    @Rule(Weather(temperature=P(lambda t: t > 30), humidity=P(lambda h: h < 50), wind_speed=P(lambda w: w < 30)))
    def caluroso(self):
        self.result = "El clima es caluroso"

    @Rule(Weather(temperature=P(lambda t: t < 10), humidity=P(lambda h: h > 50), wind_speed=P(lambda w: w < 30)))
    def frio(self):
        self.result = "El clima es frío"

    @Rule(Weather(temperature=P(lambda t: t >= 15 and t <= 25), humidity=P(lambda h: h > 70), wind_speed=P(lambda w: w < 15)))
    def nublado(self):
        self.result = "El clima es nublado"

    @Rule(Weather(temperature=P(lambda t: t > 20 and t < 30), humidity=P(lambda h: h > 80), wind_speed=P(lambda w: w > 100)))
    def huracan(self):
        self.result = "El clima es huracán"

    @Rule(Weather(temperature=P(lambda t: t > 10 and t < 20), humidity=P(lambda h: h > 60), wind_speed=P(lambda w: w >= 30)))
    def lluvioso(self):
        self.result = "El clima es lluvioso"

    @Rule(Weather(temperature=P(lambda t: t >= 20 and t <= 30), humidity=P(lambda h: h < 50), wind_speed=P(lambda w: w >= 30)))
    def ventoso(self):
        self.result = "El clima es ventoso"

    # Regla para clima extraño
    @Rule(AS.w << Weather())
    def clima_extrano(self, w):
        self.result = "El clima es extraño"