from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from datetime import datetime
from os import sep


class Storage(FileSystemStorage):
    def _save(self, name, content):
        name_parts = name.split(sep)
        file_name = name_parts.pop()
        name = sep.join(name_parts) + sep + str(datetime.today().date()).replace('-', sep) + sep + file_name
        return default_storage.save(name, content)
