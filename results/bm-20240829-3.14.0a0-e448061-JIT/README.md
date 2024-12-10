# Results

- fork: brandtbucher/underflow_jump_backw
- version: 3.14.0a0
- config: JIT
- commit hash: [e448061](https://github.com/brandtbucher/cpython/commit/e448061)
- commit date: 2024-08-29T16:38:24-07:00
- commit merge base: [5fce482c9a9d18d36c8177bdd0028cd2fef9f09f](https://github.com/python/cpython/commit/5fce482c9a9d18d36c8177bdd0028cd2fef9f09f)
- ref: underflow_jump_backw

## linux x86_64 (azure)

- [pystats raw](bm-20240829-azure-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-pystats.json)
- [pystats table](bm-20240829-azure-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-pystats.md)

### vs. base

- [pystats diff](bm-20240829-azure-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10624214447)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-3.10.4.md)
- [📈time plot](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 92.06%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-3.12.0.md)
- [📈time plot](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x slower (HPT: reliability of 99.03%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-3.13.0.md)
- [📈time plot](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-base-mem.svg)
- [📄table](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-base.md)
- [📈time plot](bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061-vs-base.svg)

