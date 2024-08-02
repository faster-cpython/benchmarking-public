# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [548a11d](https://github.com/python/cpython/commit/548a11d)
- commit date: 2024-05-28T16:42:23-06:00
- commit merge base: [606be663622c6784aed4ffa55b877adbd6fe8e54](https://github.com/python/cpython/commit/606be663622c6784aed4ffa55b877adbd6fe8e54)
- ref: 548a11d5cf1dbb32d86c

## linux x86_64 (azure)

- [pystats raw](bm-20240528-azure-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d-pystats.json)
- [pystats table](bm-20240528-azure-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9278899214)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d-vs-3.10.4.md)
- [📈time plot](bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 96.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d-vs-3.12.0.md)
- [📈time plot](bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 68.65%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d-vs-3.13.0b2.md)
- [📈time plot](bm-20240528-linux-x86_64-python-548a11d5cf1dbb32d86c-3.14.0a0-548a11d-vs-3.13.0b2.svg)

