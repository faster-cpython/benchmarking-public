# Results

- fork: python/v3.10.4
- version: 3.10.4
- config: 
- commit hash: [9d38120](https://github.com/python/cpython/commit/9d38120)
- commit date: 2022-03-23T20:12:04+00:00
- fork: python/9d38120e335357a3b294
- ref: 9d38120e335357a3b294, v3.10.4

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8924024762)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.223x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 0.83x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging
- [📄table](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.226x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 0.81x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.13.0.md)
- [📈time plot](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.244x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.275x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 0.83x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.md)
- [📈time plot](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.236x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 0.84x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.224x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 0.82x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.md)
- [📈time plot](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: missing
- platform: Windows-10-10.0.22621-SP0
- [raw results](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.169x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.165x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.md)
- [📈time plot](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: missing
- platform: Windows-10-10.0.22621-SP0
- [raw results](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.002x slower (HPT: reliability of 96.47%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.091x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.md)
- [📈time plot](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12751204569)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit
- [raw results](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.172x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, gunicorn
- [📄table](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.135x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 0.80x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, gunicorn
- [📄table](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.md)
- [📈time plot](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0.svg)

