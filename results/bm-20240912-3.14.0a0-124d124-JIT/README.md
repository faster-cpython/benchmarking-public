# Results

- fork: brandtbucher/deopt_tracing_16
- version: 3.14.0a0
- config: JIT
- commit hash: [124d124](https://github.com/brandtbucher/cpython/commit/124d124)
- commit date: 2024-09-12T14:46:37-07:00
- commit merge base: [6e06e01881dcffbeef5baac0c112ffb14cfa0b27](https://github.com/python/cpython/commit/6e06e01881dcffbeef5baac0c112ffb14cfa0b27)
- ref: deopt_tracing_16

## linux x86_64 (azure)

- [pystats raw](bm-20240912-azure-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-pystats.json)
- [pystats table](bm-20240912-azure-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-pystats.md)

### vs. base

- [pystats diff](bm-20240912-azure-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10843289466)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124.json)

### vs. 3.10.4

- Geometric mean: 1.411x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-3.10.4.md)
- [📈time plot](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.080x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-3.12.0.md)
- [📈time plot](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x faster (HPT: reliability of 75.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-3.13.0.md)
- [📈time plot](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 88.12%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-base-mem.svg)
- [📄table](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-base.md)
- [📈time plot](bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124-vs-base.svg)

