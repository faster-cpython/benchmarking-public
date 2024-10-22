# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [8ca892b](https://github.com/mdboom/cpython/commit/8ca892b)
- commit date: 2024-09-26T13:36:04-04:00
- commit merge base: [b4d0d7de0f6d938128bf525e119c18af5632b804](https://github.com/mdboom/cpython/commit/b4d0d7de0f6d938128bf525e119c18af5632b804)
- ref: cmq_mdboom

## linux x86_64 (azure)

- [pystats raw](bm-20240926-azure-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-pystats.json)
- [pystats table](bm-20240926-azure-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-pystats.md)

### vs. base

- [pystats diff](bm-20240926-azure-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11057377176)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-3.10.4.md)
- [📈time plot](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-3.12.0.md)
- [📈time plot](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-3.13.0.md)
- [📈time plot](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 93.58%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-base-mem.svg)
- [📄table](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-base.md)
- [📈time plot](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-3.13.0b2.md)
- [📈time plot](bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b-vs-3.13.0b2.svg)

