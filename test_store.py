from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

def test_patch_order_by_id():

    create_endpoint = "/store/order"

    create_payload = {
        "pet_id": 0
    }

    create_response = api_helpers.post_api_data(create_endpoint, create_payload)

    assert create_response.status_code == 201

    order_data = create_response.json()
    order_id = order_data["id"]

    patch_endpoint = f"/store/order/{order_id}"

    patch_payload = {
        "status": "sold"
    }

    response = api_helpers.patch_api_data(patch_endpoint, patch_payload)

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["message"] == "Order and pet status updated successfully"