# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [1e48156](https://github.com/python/cpython/commit/1e48156)
- commit date: 2024-06-19T21:35:11+01:00
- commit merge base: [ed5ae6c4d76feaff06c2104c8ff864553b000253](https://github.com/python/cpython/commit/ed5ae6c4d76feaff06c2104c8ff864553b000253)
- ref: 1e4815692f6c8a37a397

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9613281399)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156-vs-3.10.4.md)
- [📈time plot](bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156-vs-3.12.0.md)
- [📈time plot](bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156-vs-3.13.0b2.md)
- [📈time plot](bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156-vs-3.13.0b2.svg)

