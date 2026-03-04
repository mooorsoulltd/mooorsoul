class NameGenerator:
    def __init__(self):
        self.names = []

    def create_name_from_objects(self, objects):
        """
        Generate a name based on detected objects.
        :param objects: List of detected objects.
        :return: A generated name.
        """
        name = "Video featuring: " + ", ".join(objects)
        self.names.append(name)
        return name

    def create_name_from_scenes(self, scenes):
        """
        Generate a name based on scenes.
        :param scenes: List of detected scenes.
        :return: A generated name.
        """
        name = "Captured in: " + ", ".join(scenes)
        self.names.append(name)
        return name

    def create_name_from_audio(self, audio_features):
        """
        Generate a name based on audio features.
        :param audio_features: List of audio features detected.
        :return: A generated name.
        """
        name = "Audio features: " + ", ".join(audio_features)
        self.names.append(name)
        return name

    def get_names(self):
        """
        Retrieve all generated names.
        :return: List of generated names.
        """
        return self.names
