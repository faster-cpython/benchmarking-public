# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [ec9d12b](https://github.com/python/cpython/commit/ec9d12b)
- commit date: 2024-05-10T16:55:49+00:00
- commit merge base: [f5c6b9977a561fcf9c2a803fb08652fd39b13d3b](https://github.com/python/cpython/commit/f5c6b9977a561fcf9c2a803fb08652fd39b13d3b)
- ref: ec9d12be9648ee60a2eb

## linux x86_64 (azure)

- [pystats raw](bm-20240510-azure-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-pystats.json)
- [pystats table](bm-20240510-azure-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038114880)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-3.10.4.md)
- [📈time plot](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 95.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-3.12.0.md)
- [📈time plot](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 75.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-3.13.0b2.md)
- [📈time plot](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 77.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-base-mem.svg)
- [📄table](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-base.md)
- [📈time plot](bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b-vs-base.svg)

