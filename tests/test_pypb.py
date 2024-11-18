import sys
sys.path.append('.')

from datetime import datetime

from pypb import PathBuilder


def test_pypb():
    data_dir = PathBuilder(".")
    assert "." == str(data_dir)

    data_dir.add_path("data").add_path("v1")
    assert "data/v1" == str(data_dir)

    data_dir.add_date()
    ymd = datetime.today().strftime("%Y-%m-%d")
    assert f"data/v1/{ymd}" == str(data_dir)

    params = dict(n_epochs=100, n_batch_size=32, lr=0.01)
    data_dir.add_params(params)
    assert f"data/v1/{ymd}/n_epochs=100-n_batch_size=32-lr=0.01" == str(data_dir)
