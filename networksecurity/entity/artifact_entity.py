from dataclasses import dataclass
## Acts like a decorator which create variable of empty class

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str