# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [35b5eaa](https://github.com/python/cpython/commit/35b5eaa)
- commit date: 2024-05-09T13:52:08+00:00
- commit merge base: [82acc5f2113bffd0ed902851f4ccf5b9be8980b2](https://github.com/python/cpython/commit/82acc5f2113bffd0ed902851f4ccf5b9be8980b2)
- ref: 35b5eaa176a5bae8a0ca

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9034646637)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa-vs-3.10.4.md)
- [📈time plot](bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 99.87%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa-vs-3.12.0.md)
- [📈time plot](bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa-vs-3.13.0b2.svg)

