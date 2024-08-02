# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [99d62f9](https://github.com/python/cpython/commit/99d62f9)
- commit date: 2024-06-15T12:51:58+00:00
- commit merge base: [c501261c919ceb97c850ef9427a93326f06a8f2e](https://github.com/python/cpython/commit/c501261c919ceb97c850ef9427a93326f06a8f2e)
- ref: 99d62f902e43c08ebec5

## linux x86_64 (azure)

- [pystats raw](bm-20240615-azure-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9-pystats.json)
- [pystats table](bm-20240615-azure-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9576601818)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9-vs-3.10.4.md)
- [📈time plot](bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 95.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9-vs-3.12.0.md)
- [📈time plot](bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 52.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9-vs-3.13.0b2.md)
- [📈time plot](bm-20240615-linux-x86_64-python-99d62f902e43c08ebec5-3.14.0a0-99d62f9-vs-3.13.0b2.svg)

