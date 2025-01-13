# Results

- fork: python/v3.13.0
- version: 3.13.0
- config: 
- commit hash: [60403a5](https://github.com/python/cpython/commit/60403a5)
- commit date: 2024-10-07T07:02:14+02:00
- ref: v3.13.0

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12166812176)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.274x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x slower (HPT: reliability of 70.16%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12166812176)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.397x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12166812176)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.278x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x slower (HPT: reliability of 84.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12166812176)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.222x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12166812176)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.114x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.153x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12751214999)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.258x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.11x
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, gunicorn
- [📄table](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.002x faster (HPT: reliability of 91.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [📄table](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

