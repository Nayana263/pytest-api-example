from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, is_

def test_pet_schema():
    endpoint = "/pets/1"
    response = api_helpers.get_api_data(endpoint)

    assert response.status_code == 200

    pet_data = response.json()
    validate(instance=pet_data, schema=schemas.pet)


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_by_status(status):
    endpoint = "/pets/findByStatus"
    params = {"status": status}

    response = api_helpers.get_api_data(endpoint, params)

    assert response.status_code == 200

    pets = response.json()
    assert isinstance(pets, list)

    for pet in pets:
        validate(instance=pet, schema=schemas.pet)
        assert_that(pet["status"], is_(status))


@pytest.mark.parametrize("pet_id", [-1, 9999])
def test_get_invalid_pet_id(pet_id):
    endpoint = f"/pets/{pet_id}"
    response = api_helpers.get_api_data(endpoint)

    assert response.status_code == 404