from django.conf import settings


class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


def pytest_configure():
    settings.MIGRATION_MODULES = DisableMigrations()
