# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [8763a2d](https://github.com/brandtbucher/cpython/commit/8763a2d)
- commit date: 2024-09-07T13:46:40-07:00
- commit merge base: [cfbc841ef3c27b3e65d1223bf8fedf1f652137bc](https://github.com/brandtbucher/cpython/commit/cfbc841ef3c27b3e65d1223bf8fedf1f652137bc)
- ref: underflow_known

## linux x86_64 (azure)

- [pystats raw](bm-20240907-azure-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-pystats.json)
- [pystats table](bm-20240907-azure-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-pystats.md)

### vs. base

- [pystats diff](bm-20240907-azure-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10754353847)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d.json)

### vs. 3.10.4

- Geometric mean: 1.416x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-3.10.4.md)
- [📈time plot](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.079x faster (HPT: reliability of 99.89%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-3.12.0.md)
- [📈time plot](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 60.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-3.13.0.md)
- [📈time plot](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x slower (HPT: reliability of 99.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- new benchmarks: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-base-mem.svg)
- [📄table](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-base.md)
- [📈time plot](bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d-vs-base.svg)

