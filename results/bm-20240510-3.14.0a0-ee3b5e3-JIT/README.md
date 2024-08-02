# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [ee3b5e3](https://github.com/brandtbucher/cpython/commit/ee3b5e3)
- commit date: 2024-05-10T12:20:26-07:00
- commit merge base: [ec9d12be9648ee60a2eb02d67069d74f8b314df9](https://github.com/brandtbucher/cpython/commit/ec9d12be9648ee60a2eb02d67069d74f8b314df9)
- ref: peel

## linux x86_64 (azure)

- [pystats raw](bm-20240510-azure-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-pystats.json)
- [pystats table](bm-20240510-azure-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-pystats.md)

### vs. base

- [pystats diff](bm-20240510-azure-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038114880)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, djangocms, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-3.10.4.md)
- [📈time plot](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 98.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-3.12.0.md)
- [📈time plot](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 70.10%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, docutils, gunicorn, mypy2
- [📄table](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-3.13.0b2.md)
- [📈time plot](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 69.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 docutils
- [🧠memory plot](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-base-mem.svg)
- [📄table](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-base.md)
- [📈time plot](bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3-vs-base.svg)

