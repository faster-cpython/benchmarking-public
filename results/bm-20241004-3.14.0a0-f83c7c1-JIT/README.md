# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [f83c7c1](https://github.com/brandtbucher/cpython/commit/f83c7c1)
- commit date: 2024-10-04T16:25:10-07:00
- commit merge base: [6f4d64b048133c60d40705fb5ef776f78c7dd710](https://github.com/brandtbucher/cpython/commit/6f4d64b048133c60d40705fb5ef776f78c7dd710)
- ref: underflow

## linux x86_64 (azure)

- [pystats raw](bm-20241004-azure-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-pystats.json)
- [pystats table](bm-20241004-azure-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-pystats.md)

### vs. base

- [pystats diff](bm-20241004-azure-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11188343736)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-3.10.4.md)
- [📈time plot](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-3.12.0.md)
- [📈time plot](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x slower (HPT: reliability of 62.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-3.13.0.md)
- [📈time plot](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.96%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-base-mem.svg)
- [📄table](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-base.md)
- [📈time plot](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-3.13.0b2.md)
- [📈time plot](bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1-vs-3.13.0b2.svg)

