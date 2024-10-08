# Results

- fork: savannahostrowski
- version: 3.14.0a0
- config: JIT
- commit hash: [17ece50](https://github.com/savannahostrowski/cpython/commit/17ece50)
- commit date: 2024-09-23T15:55:04-07:00
- commit merge base: [33eeccf6d4f16e483b4c8a180bad718545aeaeaf](https://github.com/savannahostrowski/cpython/commit/33eeccf6d4f16e483b4c8a180bad718545aeaeaf)
- ref: jit_inv_mem_100k

## linux x86_64 (azure)

- [pystats raw](bm-20240923-azure-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-pystats.json)
- [pystats table](bm-20240923-azure-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-pystats.md)

### vs. base

- [pystats diff](bm-20240923-azure-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11003928763)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-3.10.4.md)
- [📈time plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-3.12.0.md)
- [📈time plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-3.13.0b2.md)
- [📈time plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-base-mem.svg)
- [📄table](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-base.md)
- [📈time plot](bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50-vs-base.svg)

