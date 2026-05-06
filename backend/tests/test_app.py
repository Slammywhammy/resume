import json
import os
from unittest.mock import patch, MagicMock

os.environ.setdefault('TABLE_NAME', 'visitor-count')

with patch('boto3.resource'):
    from visitor_counter import app


def _mock_table(count=10):
    mock = MagicMock()
    mock.update_item.return_value = {
        'Attributes': {'count': count}
    }
    return mock


def test_returns_200():
    with patch.object(app, 'table', _mock_table()):
        result = app.lambda_handler({}, {})
    assert result['statusCode'] == 200


def test_body_contains_count():
    with patch.object(app, 'table', _mock_table(42)):
        result = app.lambda_handler({}, {})
    assert json.loads(result['body']) == {'count': 42}


def test_cors_header_present():
    with patch.object(app, 'table', _mock_table()):
        result = app.lambda_handler({}, {})
    assert 'Access-Control-Allow-Origin' in result['headers']


def test_cors_restricted_to_domain():
    with patch.object(app, 'table', _mock_table()):
        result = app.lambda_handler({}, {})
    assert result['headers']['Access-Control-Allow-Origin'] == 'https://sam-gardner.com'


def test_calls_dynamodb_update():
    mock_table = _mock_table()
    with patch.object(app, 'table', mock_table):
        app.lambda_handler({}, {})
    mock_table.update_item.assert_called_once()
