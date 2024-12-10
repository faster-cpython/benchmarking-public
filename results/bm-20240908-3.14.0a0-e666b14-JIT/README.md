# Results

- fork: brandtbucher/underflow_known_dyna
- version: 3.14.0a0
- config: JIT
- commit hash: [e666b14](https://github.com/brandtbucher/cpython/commit/e666b14)
- commit date: 2024-09-08T08:47:33-07:00
- commit merge base: [cfbc841ef3c27b3e65d1223bf8fedf1f652137bc](https://github.com/python/cpython/commit/cfbc841ef3c27b3e65d1223bf8fedf1f652137bc)
- ref: underflow_known_dyna

## linux x86_64 (azure)

- [pystats raw](bm-20240908-azure-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-pystats.json)
- [pystats table](bm-20240908-azure-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-pystats.md)

### vs. base

- [pystats diff](bm-20240908-azure-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10761221378)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14.json)

### vs. 3.10.4

- Geometric mean: 1.393x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-3.10.4.md)
- [📈time plot](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-3.12.0.md)
- [📈time plot](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x faster (HPT: reliability of 65.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-3.13.0.md)
- [📈time plot](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- new benchmarks: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-base-mem.svg)
- [📄table](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-base.md)
- [📈time plot](bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14-vs-base.svg)

