from django.apps import AppConfig


class DebtorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Debtor'
    
    def ready(self):
        import Debtor.signals
