# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [406ffb5](https://github.com/python/cpython/commit/406ffb5)
- commit date: 2024-05-23T11:06:10+01:00
- commit merge base: [c85e3526736d1cf8226686fdf4f5117e105a7b13](https://github.com/python/cpython/commit/c85e3526736d1cf8226686fdf4f5117e105a7b13)
- ref: 406ffb5293a8c9ca315b

## linux x86_64 (azure)

- [pystats raw](bm-20240523-azure-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5-pystats.json)
- [pystats table](bm-20240523-azure-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9222927979)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5-vs-3.10.4.md)
- [📈time plot](bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5-vs-3.12.0.md)
- [📈time plot](bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5-vs-3.13.0b2.md)
- [📈time plot](bm-20240523-linux-x86_64-python-406ffb5293a8c9ca315b-3.14.0a0-406ffb5-vs-3.13.0b2.svg)

