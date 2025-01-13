# Results

- fork: brandtbucher/jit_off
- version: 3.14.0a3+
- config: 
- commit hash: [1f40ea4](https://github.com/brandtbucher/cpython/commit/1f40ea4)
- commit date: 2025-01-08T13:37:57-08:00
- commit merge base: [7363476b6405e3d288a61282aa7bc6aca9c2114d](https://github.com/python/cpython/commit/7363476b6405e3d288a61282aa7bc6aca9c2114d)
- ref: jit_off

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679534027)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.10.4.md)
- [📈time plot](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.12.0.md)
- [📈time plot](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.13.0.md)
- [📈time plot](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 59.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base-mem.svg)
- [📄table](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base.md)
- [📈time plot](bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250108-azure-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-pystats.json)
- [pystats table](bm-20250108-azure-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-pystats.md)

### vs. base

- [pystats diff](bm-20250108-azure-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679534027)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4.json)

### vs. 3.10.4

- Geometric mean: 1.436x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.10.4.md)
- [📈time plot](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.106x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.12.0.md)
- [📈time plot](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.13.0.md)
- [📈time plot](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 89.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base-mem.svg)
- [📄table](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base.md)
- [📈time plot](bm-20250108-linux-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679534027)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4.json)

### vs. 3.10.4

- Geometric mean: 1.355x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.10.4.md)
- [📈time plot](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x faster (HPT: reliability of 99.90%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.12.0.md)
- [📈time plot](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.13.0.md)
- [📈time plot](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 96.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base-mem.svg)
- [📄table](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base.md)
- [📈time plot](bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679534027)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.10.4.md)
- [📈time plot](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.12.0.md)
- [📈time plot](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.122x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.13.0.md)
- [📈time plot](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 98.17%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base-mem.svg)
- [📄table](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base.md)
- [📈time plot](bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3%2B-1f40ea4-vs-base.svg)

