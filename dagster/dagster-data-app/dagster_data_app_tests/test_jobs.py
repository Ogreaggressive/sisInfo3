from dagster_data_app.jobs.sample_job import get_total_size, complex_job


# We can test an operation
def test_get_total_size():
    file_sizes = {"file1": 400, "file2": 50}
    result = get_total_size(file_sizes)
    assert result == 450


# We can also test a job
def test_complex_job():
    res = complex_job.execute_in_process()
    assert res.success
    assert res.output_for_node("get_total_size") > 0
    
