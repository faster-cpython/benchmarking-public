# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [cae9e43](https://github.com/brandtbucher/cpython/commit/cae9e43)
- commit date: 2024-09-19T13:05:48-07:00
- commit merge base: [6e06e01881dcffbeef5baac0c112ffb14cfa0b27](https://github.com/brandtbucher/cpython/commit/6e06e01881dcffbeef5baac0c112ffb14cfa0b27)
- ref: justin_compact_exits

## linux x86_64 (azure)

- [pystats raw](bm-20240919-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-pystats.json)
- [pystats table](bm-20240919-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-pystats.md)

### vs. base

- [pystats diff](bm-20240919-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10948501573)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43.json)

### vs. 3.10.4

- Geometric mean: 1.39x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, html5lib, mypy2, pycparser, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-3.10.4.md)
- [📈time plot](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pycparser, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, pylint, thrift
- [📄table](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-3.12.0.md)
- [📈time plot](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 94.12%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, html5lib, mypy2, pycparser
- [📄table](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-3.13.0.md)
- [📈time plot](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 html5lib, pycparser
- [🧠memory plot](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-base-mem.svg)
- [📄table](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-base.md)
- [📈time plot](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-3.13.0b2.md)
- [📈time plot](bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43-vs-3.13.0b2.svg)

