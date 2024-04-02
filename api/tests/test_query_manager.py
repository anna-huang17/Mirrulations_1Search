"""
Module to test the query manager
"""

from mirrsearch.api.mock_database_manager import MockMongoDatabase
from mirrsearch.api.query_manager import MongoQueryManager

def test_search_dockets():
    """
    Function to test the search_dockets function in the MongoQueryManager class
    """
    manager = MockMongoDatabase()
    query_manager = MongoQueryManager(manager)
    response = query_manager.search_dockets('test')
    assert response['data']['search_term'] == 'test'

def test_search_comments():
    """
    Function to test the search_comments function in the MongoQueryManager class
    """
    manager = MockMongoDatabase()
    query_manager = MongoQueryManager(manager)
    response = query_manager.search_comments('test', 'test')
    assert response['data']['search_term'] == 'test'
    assert response['data']['docket_id'] == 'test'
    assert response['data']['comments'][0]['author'] == 'pass'
    assert response['data']['comments'][0]['date_posted'] == 'pass'
    assert response['data']['comments'][0]['link'] == 'pass'
    assert response['data']['comments'][0]['docket_id'] == 'test'
