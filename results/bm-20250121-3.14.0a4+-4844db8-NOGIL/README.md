# Results

- fork: mdboom/aa_test_2025
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [4844db8](https://github.com/mdboom/cpython/commit/4844db8)
- commit date: 2025-01-21T15:13:39-05:00
- commit merge base: [f18b2264929c56360c868d7ad77508035d751352](https://github.com/python/cpython/commit/f18b2264929c56360c868d7ad77508035d751352)
- ref: aa_test_2025

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12909106070)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8.json)

### vs. 3.10.4

- Geometric mean: 1.084x faster (HPT: reliability of 99.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.56x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.10.4.md)
- [📈time plot](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.138x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.12.0.md)
- [📈time plot](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.140x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.13.0.md)
- [📈time plot](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 85.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base-mem.svg)
- [📄table](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base.md)
- [📈time plot](bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12909106070)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8.json)

### vs. 3.10.4

- Geometric mean: 1.232x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.10.4.md)
- [📈time plot](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x slower (HPT: reliability of 99.97%, 1.03x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.12.0.md)
- [📈time plot](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.103x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.13.0.md)
- [📈time plot](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 95.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base-mem.svg)
- [📄table](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base.md)
- [📈time plot](bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12909106070)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8.json)

### vs. 3.10.4

- Geometric mean: 1.188x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.54x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.10.4.md)
- [📈time plot](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.069x slower (HPT: reliability of 99.96%, 1.04x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.12.0.md)
- [📈time plot](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x slower (HPT: reliability of 99.96%, 1.02x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.13.0.md)
- [📈time plot](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 56.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base-mem.svg)
- [📄table](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base.md)
- [📈time plot](bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12909106070)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8.json)

### vs. 3.10.4

- Geometric mean: 1.258x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.10.4.md)
- [📈time plot](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.002x faster (HPT: reliability of 93.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.12.0.md)
- [📈time plot](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 57.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.13.0.md)
- [📈time plot](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 98.06%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base-mem.svg)
- [📄table](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base.md)
- [📈time plot](bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4%2B-4844db8-vs-base.svg)

