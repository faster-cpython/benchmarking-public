# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [4ed7d1d](https://github.com/python/cpython/commit/4ed7d1d)
- commit date: 2024-09-12T15:32:45+01:00
- commit merge base: [3ea51fa2e33797c772af6eaf6ede76d2dc6082ba](https://github.com/python/cpython/commit/3ea51fa2e33797c772af6eaf6ede76d2dc6082ba)
- ref: 4ed7d1d6acc22807bfb5

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10903585502)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d-vs-3.10.4.md)
- [📈time plot](bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d-vs-3.12.0.md)
- [📈time plot](bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d-vs-3.13.0b2.md)
- [📈time plot](bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d-vs-3.13.0b2.svg)

