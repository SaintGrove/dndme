from attr import attrib
import pytest

from dndme.loaders import EncounterLoader


@pytest.fixture
def encounter_loader():
    """Create a testing encounter loader"""
    return EncounterLoader(
        base_dir='tests/test_data/test_encounter_loader_encounters',
        monster_loader=None
    )


def test_get_avaoilable_encounters(encounter_loader):
    available_encounters = encounter_loader.get_available_encounters()

    print(available_encounters)
    assert len(available_encounters) == 1
    assert available_encounters[0].name == 'LMoP 1.1.1: Goblin Ambush'
    assert 'goblins' in available_encounters[0].groups
    assert available_encounters[0].groups['goblins']['count'] == 4

