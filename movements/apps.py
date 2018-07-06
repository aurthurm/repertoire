from django.apps import AppConfig


class MovementsConfig(AppConfig):
    name = 'movements'

    def ready(self):
        import movements.signals
