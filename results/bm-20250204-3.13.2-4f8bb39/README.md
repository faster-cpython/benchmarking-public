# Results

- fork: python/v3.13.2
- version: 3.13.2
- config: 
- commit hash: [4f8bb39](https://github.com/python/cpython/commit/4f8bb39)
- commit date: 2025-02-04T15:51:09+01:00
- ref: v3.13.2

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13184564150)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39.json)

### vs. 3.10.4

- Geometric mean: 1.278x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.md)
- [📈time plot](bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x slower (HPT: reliability of 53.71%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.md)
- [📈time plot](bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x faster (HPT: reliability of 71.44%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.md)
- [📈time plot](bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13184564150)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39.json)

### vs. 3.10.4

- Geometric mean: 1.393x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.md)
- [📈time plot](bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.056x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.md)
- [📈time plot](bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.md)
- [📈time plot](bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13184564150)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39.json)

### vs. 3.10.4

- Geometric mean: 1.284x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.md)
- [📈time plot](bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x slower (HPT: reliability of 75.64%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.md)
- [📈time plot](bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 99.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.md)
- [📈time plot](bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13184564150)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39.json)

### vs. 3.10.4

- Geometric mean: 1.230x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.md)
- [📈time plot](bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.md)
- [📈time plot](bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x faster (HPT: reliability of 88.96%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.md)
- [📈time plot](bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13184564150)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39.json)

### vs. 3.10.4

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.md)
- [📈time plot](bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.140x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.md)
- [📈time plot](bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.md)
- [📈time plot](bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13184564150)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39.json)

### vs. 3.10.4

- Geometric mean: 1.260x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.11x
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, gunicorn
- [📄table](bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.md)
- [📈time plot](bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 97.30%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [📄table](bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.md)
- [📈time plot](bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x slower (HPT: reliability of 98.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- [📄table](bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.md)
- [📈time plot](bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39-vs-3.13.0.svg)

