import os


defaultValues = {
    "ELASTICSEARCH_HOST": "",
    "ELASTICSEARCH_PORT": "9200",
    "ELASTICSEARCH_USERNAME": "elastic",
    "ELASTICSEARCH_PASSWORD": "changeme"
}


class AbstractConfig(object):
    """
    Parent class containing get_property to return the ENV variable of
    default value if not found.
    """

    def __init__(self):
        self._defaultValues = defaultValues

    def get_property(self, property_name):
        if os.getenv(property_name) is not None:
            return os.getenv(property_name)
        return self._defaultValues.get(property_name)


class Config(AbstractConfig):
    """
    Class providing hard-coded values to the application, first using
    environment variables, and if not found, defaulting to those values
    provided in the defaultValues dictionary above.
    """

    @property
    def elasticsearch_host(self):
        return self.get_property('ELASTICSEARCH_HOST')

    @property
    def elasticsearch_port(self):
        return self.get_property('ELASTICSEARCH_PORT')

    @property
    def elasticsearch_username(self):
        return self.get_property('ELASTICSEARCH_USERNAME')

    @property
    def elasticsearch_password(self):
        return self.get_property('ELASTICSEARCH_PASSWORD')

    @property
    def elasticsearch_indices(self):
        return {
            'csbc_pson_computational_tools':'csbc-pson-computational-tools-20211209'
        }


config = Config()
