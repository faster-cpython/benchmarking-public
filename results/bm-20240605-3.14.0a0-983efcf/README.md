# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [983efcf](https://github.com/python/cpython/commit/983efcf)
- commit date: 2024-06-05T07:25:47+01:00
- commit merge base: [b6b0dcbfc054f581b6f78602e4c2e9474e3efe21](https://github.com/python/cpython/commit/b6b0dcbfc054f581b6f78602e4c2e9474e3efe21)
- ref: 983efcf15b2503fe0c05

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9423172789)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf-vs-3.10.4.md)
- [📈time plot](bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.83%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf-vs-3.12.0.md)
- [📈time plot](bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 99.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf-vs-3.13.0b2.md)
- [📈time plot](bm-20240605-linux-x86_64-python-983efcf15b2503fe0c05-3.14.0a0-983efcf-vs-3.13.0b2.svg)

