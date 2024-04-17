class RemoteUserRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'remote_users':
            return 'db_old'

        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'remote_users':
            return 'db_old'

        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'remote_users' or obj2._meta.app_label == 'remote_users':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'remote_users':
            return False
        return True
