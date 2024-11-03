# pypb

`pypb` is a path builder designed specifically for people involved in data science projects.
It offers a simple and effective way to build paths.
Please see the "Usage" section below for more details.

---

## Installation

```sh
pip install git+https://github.com/kzak/pypb
```

## Usage

```py
from pypb import PathBuilder

params = dict(n_epochs=1000, n_batch_size=256, lr=0.01)
data_dir = PathBuilder(".").add_path("data").add_date().add_params(params).mkdir()
# => Create: "./data/yyyy-mm-dd/n_epochs=1000-n_batch_size=256-lr=0.01/"
```
