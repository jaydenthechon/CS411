from typing import Any

class Migration:

    def __init__(self, migration):
        self.migration = migration

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
    