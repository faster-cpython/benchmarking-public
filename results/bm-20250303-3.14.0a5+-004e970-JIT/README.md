# Results

- fork: brandtbucher/jit_warmup_2048
- version: 3.14.0a5+
- config: JIT
- commit hash: [004e970](https://github.com/brandtbucher/cpython/commit/004e970)
- commit date: 2025-03-03T22:09:48-08:00
- commit merge base: [7afa476874b9a432ad6dbe9fb3e65d62f2999f88](https://github.com/python/cpython/commit/7afa476874b9a432ad6dbe9fb3e65d62f2999f88)
- ref: jit_warmup_2048

## linux x86_64 (azure)

- [pystats raw](bm-20250303-azure-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-pystats.json)
- [pystats table](bm-20250303-azure-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-pystats.md)

### vs. base

- [pystats diff](bm-20250303-azure-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13647470332)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970.json)

### vs. 3.10.4

- Geometric mean: 1.448x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-3.10.4.md)
- [📈time plot](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-3.12.0.md)
- [📈time plot](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-3.13.0.md)
- [📈time plot](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-base-mem.svg)
- [📄table](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-base.md)
- [📈time plot](bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5%2B-004e970-vs-base.svg)

