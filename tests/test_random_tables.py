import randomtable2026 as rt

# test load_table function

def test_column_names():
    
    # Arrange 
    data_path = "./data/example-table.csv"
    expected_output = ['Weather', 'Time of Day', 'Environment', 'Environmental Hazard', 'NPCs']
    
    # Act 
    table = rt.load_table(data_path)
    output = table.columns.to_list()
    # Assert
    assert output == expected_output, f"Expected {expected_output} but got {output}"

def test_categories():

    # Arrange
    data_path = "./data/example-table.csv"
    expected_output = ['Weather', 'Time of Day', 'Environment', 'Environmental Hazard', 'NPCs']
    
    # Act

    actual_output = rt.categories(data_path)

    # Assert

    assert actual_output == expected_output
    