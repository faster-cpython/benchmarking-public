# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [3df2022](https://github.com/python/cpython/commit/3df2022)
- commit date: 2024-06-17T09:44:13+03:00
- commit merge base: [bac4edad69bb20dd9460766e062637cae999e1e0](https://github.com/python/cpython/commit/bac4edad69bb20dd9460766e062637cae999e1e0)
- ref: 3df2022931f77c5cadb3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9544495349)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022-vs-3.10.4.md)
- [📈time plot](bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022-vs-3.12.0.md)
- [📈time plot](bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022-vs-3.13.0b2.md)
- [📈time plot](bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022-vs-3.13.0b2.svg)

