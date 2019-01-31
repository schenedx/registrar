# Serializers that can be shared across multiple versions of the API
# should be created here. As the API evolves, serializers may become more
# specific to a particular version of the API. In this case, the serializers
# in question should be moved to versioned sub-package.
from rest_framework import serializers


class ProgramSerializer(serializers.Serializer):
    discovery_uuid = serializers.CharField()
    title = serializers.CharField()
