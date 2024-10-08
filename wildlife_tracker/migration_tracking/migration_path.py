from typing import Optional
from wildlife_tracker.migration_tracker.migration_path import MigrationPath
from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:


   def __init__(self,
               destination: Habitat,
               start_location: Habitat,
               start_date: str,
               duration: Optional[int] ,
               path_id: int,
               species: str) -> None:
       self.destination = destination
       self.start_location = start_location
       self.duration = duration
       self.start_date  = start_date
       self.path_id = path_id
       self.species = species






   def create_migration_path(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
       pass


   def get_migration_path_by_id(self, path_id: int) -> MigrationPath:
       pass


   def get_migration_paths(self) -> list[MigrationPath]:
       pass


   def get_migration_paths_by_destination(self, destination: Habitat) -> list[MigrationPath]:
       pass


   def get_migration_paths_by_species(self, species: str) -> list[MigrationPath]:
       pass


   def get_migration_paths_by_start_location(self, start_location: Habitat) -> list[MigrationPath]:
       pass


   def get_migration_path_details(self, path_id) -> dict:
       pass
  
   def remove_migration_path(self, path_id: int) -> None:
       pass


   def update_migration_path_details(self, path_id: int, **kwargs) -> None:
       pass



