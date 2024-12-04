# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [c5de9e3](https://github.com/brandtbucher/cpython/commit/c5de9e3)
- commit date: 2024-09-05T11:53:43-07:00
- commit merge base: [cfbc841ef3c27b3e65d1223bf8fedf1f652137bc](https://github.com/brandtbucher/cpython/commit/cfbc841ef3c27b3e65d1223bf8fedf1f652137bc)
- ref: tier_two_constants

## linux x86_64 (azure)

- [pystats raw](bm-20240905-azure-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-pystats.json)
- [pystats table](bm-20240905-azure-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-pystats.md)

### vs. base

- [pystats diff](bm-20240905-azure-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10726580133)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-3.10.4.md)
- [📈time plot](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-3.12.0.md)
- [📈time plot](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x faster (HPT: reliability of 94.43%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-3.13.0.md)
- [📈time plot](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 92.39%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-base-mem.svg)
- [📄table](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-base.md)
- [📈time plot](bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3-vs-base.svg)

