# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [8b9b14d](https://github.com/brandtbucher/cpython/commit/8b9b14d)
- commit date: 2024-09-03T17:57:17-07:00
- commit merge base: [5fce482c9a9d18d36c8177bdd0028cd2fef9f09f](https://github.com/brandtbucher/cpython/commit/5fce482c9a9d18d36c8177bdd0028cd2fef9f09f)
- ref: ujb0_project

## linux x86_64 (azure)

- [pystats raw](bm-20240903-azure-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-pystats.json)
- [pystats table](bm-20240903-azure-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-pystats.md)

### vs. base

- [pystats diff](bm-20240903-azure-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10693150856)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d.json)

### vs. 3.10.4

- Geometric mean: 1.359x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-3.10.4.md)
- [📈time plot](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 95.53%, 1.00x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-3.12.0.md)
- [📈time plot](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x slower (HPT: reliability of 94.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-3.13.0.md)
- [📈time plot](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-base-mem.svg)
- [📄table](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-base.md)
- [📈time plot](bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d-vs-base.svg)

