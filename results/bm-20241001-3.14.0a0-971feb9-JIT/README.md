# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [971feb9](https://github.com/brandtbucher/cpython/commit/971feb9)
- commit date: 2024-10-01T22:14:56-07:00
- commit merge base: [6f4d64b048133c60d40705fb5ef776f78c7dd710](https://github.com/brandtbucher/cpython/commit/6f4d64b048133c60d40705fb5ef776f78c7dd710)
- ref: justin_compact_exits

## linux x86_64 (azure)

- [pystats raw](bm-20241001-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-pystats.json)
- [pystats table](bm-20241001-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-pystats.md)

### vs. base

- [pystats diff](bm-20241001-azure-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11138286652)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9.json)

### vs. 3.10.4

- Geometric mean: 1.448x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, docutils, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_optimize
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-3.10.4.md)
- [📈time plot](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_optimize
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-3.12.0.md)
- [📈time plot](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 98.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: chameleon, connected_components, docutils, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_optimize
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-3.13.0.md)
- [📈time plot](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 docutils, sqlglot_optimize
- [🧠memory plot](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-base-mem.svg)
- [📄table](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-base.md)
- [📈time plot](bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9-vs-base.svg)

