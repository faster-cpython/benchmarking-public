# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [e213475](https://github.com/python/cpython/commit/e213475)
- commit date: 2024-06-22T17:25:55+02:00
- commit merge base: [a046c848c1df0cf98092e9696594d3fb836e3530](https://github.com/python/cpython/commit/a046c848c1df0cf98092e9696594d3fb836e3530)
- ref: e21347549535b16f51a3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9646892753)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240622-linux-x86_64-python-e21347549535b16f51a3-3.14.0a0-e213475.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-linux-x86_64-python-e21347549535b16f51a3-3.14.0a0-e213475-vs-3.10.4.md)
- [📈time plot](bm-20240622-linux-x86_64-python-e21347549535b16f51a3-3.14.0a0-e213475-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-linux-x86_64-python-e21347549535b16f51a3-3.14.0a0-e213475-vs-3.12.0.md)
- [📈time plot](bm-20240622-linux-x86_64-python-e21347549535b16f51a3-3.14.0a0-e213475-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-linux-x86_64-python-e21347549535b16f51a3-3.14.0a0-e213475-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-linux-x86_64-python-e21347549535b16f51a3-3.14.0a0-e213475-vs-3.13.0b2.svg)

