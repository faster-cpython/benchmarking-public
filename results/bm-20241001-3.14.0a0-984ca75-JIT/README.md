# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [984ca75](https://github.com/brandtbucher/cpython/commit/984ca75)
- commit date: 2024-10-01T14:59:58-07:00
- commit merge base: [6f4d64b048133c60d40705fb5ef776f78c7dd710](https://github.com/brandtbucher/cpython/commit/6f4d64b048133c60d40705fb5ef776f78c7dd710)
- ref: tier_two_exit_leaks

## linux x86_64 (azure)

- [pystats raw](bm-20241001-azure-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-pystats.json)
- [pystats table](bm-20241001-azure-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-pystats.md)

### vs. base

- [pystats diff](bm-20241001-azure-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11134116722)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75.json)

### vs. 3.10.4

- Geometric mean: 1.418x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-3.10.4.md)
- [📈time plot](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-3.12.0.md)
- [📈time plot](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 82.09%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-3.13.0.md)
- [📈time plot](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 85.80%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-base-mem.svg)
- [📄table](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-base.md)
- [📈time plot](bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75-vs-base.svg)

