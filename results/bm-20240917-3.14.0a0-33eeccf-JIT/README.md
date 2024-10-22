# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [33eeccf](https://github.com/python/cpython/commit/33eeccf)
- commit date: 2024-09-17T16:02:14+03:00
- commit merge base: [4d0971934145698bc57d287bb9fe9112bd325899](https://github.com/python/cpython/commit/4d0971934145698bc57d287bb9fe9112bd325899)
- ref: 33eeccf6d4f16e483b4c

## linux x86_64 (azure)

- [pystats raw](bm-20240917-azure-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-pystats.json)
- [pystats table](bm-20240917-azure-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10976400379)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-vs-3.10.4.md)
- [📈time plot](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-vs-3.12.0.md)
- [📈time plot](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x slower (HPT: reliability of 59.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-vs-3.13.0.md)
- [📈time plot](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-vs-3.13.0b2.md)
- [📈time plot](bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf-vs-3.13.0b2.svg)

