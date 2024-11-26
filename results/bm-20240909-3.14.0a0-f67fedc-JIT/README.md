# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [f67fedc](https://github.com/brandtbucher/cpython/commit/f67fedc)
- commit date: 2024-09-09T20:31:20-07:00
- commit merge base: [5fce482c9a9d18d36c8177bdd0028cd2fef9f09f](https://github.com/brandtbucher/cpython/commit/5fce482c9a9d18d36c8177bdd0028cd2fef9f09f)
- ref: ujb0_project_warmup

## linux x86_64 (azure)

- [pystats raw](bm-20240909-azure-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-pystats.json)
- [pystats table](bm-20240909-azure-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-pystats.md)

### vs. base

- [pystats diff](bm-20240909-azure-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10785489442)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc.json)

### vs. 3.10.4

- Geometric mean: 1.353x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-3.10.4.md)
- [📈time plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 88.26%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-3.12.0.md)
- [📈time plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 94.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-3.13.0.md)
- [📈time plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-base-mem.svg)
- [📄table](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-base.md)
- [📈time plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc-vs-base.svg)

