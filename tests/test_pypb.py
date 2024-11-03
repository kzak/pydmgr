from pypb import PathBuilder
from datetime import datetime


def test_pypb():
    data_dir = PathBuilder(".")
    assert "." == str(data_dir)

    data_dir.add_path("data")
    assert "data" == str(data_dir)

    data_dir.add_date()
    ymd = datetime.today().strftime("%Y-%m-%d")
    assert f"data/{ymd}" == str(data_dir)

    params = dict(n_epochs=100, n_batch_size=32, lr=0.01)
    data_dir.add_params(params)
    assert f"data/{ymd}/n_epochs=100-n_batch_size=32-lr=0.01" == str(data_dir)
