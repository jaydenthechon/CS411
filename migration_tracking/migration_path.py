from typing import Optional

from habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self, path):
        self.path = path

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    
    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass
