# Results

- fork: brandtbucher/jit_recursion
- version: 3.14.0a5+
- config: JIT
- commit hash: [91d0090](https://github.com/brandtbucher/cpython/commit/91d0090)
- commit date: 2025-02-25T11:58:56-08:00
- commit merge base: [f963239ff1f986742d4c6bab2ab7b73f5a4047f6](https://github.com/python/cpython/commit/f963239ff1f986742d4c6bab2ab7b73f5a4047f6)
- ref: jit_recursion

## linux x86_64 (azure)

- [pystats raw](bm-20250225-azure-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-pystats.json)
- [pystats table](bm-20250225-azure-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-pystats.md)

### vs. base

- [pystats diff](bm-20250225-azure-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13529874895)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090.json)

### vs. 3.10.4

- Geometric mean: 1.432x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-3.10.4.md)
- [📈time plot](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-3.12.0.md)
- [📈time plot](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 99.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-3.13.0.md)
- [📈time plot](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 98.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-base-mem.svg)
- [📄table](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-base.md)
- [📈time plot](bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5%2B-91d0090-vs-base.svg)

