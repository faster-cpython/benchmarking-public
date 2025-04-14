# Results

- fork: python/v3.12.0
- version: 3.12.0
- config: 
- commit hash: [0fb18b0](https://github.com/python/cpython/commit/0fb18b0)
- commit date: 2023-10-02T13:48:14+02:00
- fork: python/0fb18b02c8ad56299d6a
- ref: 0fb18b02c8ad56299d6a, v3.12.0

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8924024991)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.288x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: flaskblogging
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.006x slower (HPT: reliability of 95.45%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.323x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.047x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.309x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 57.24%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.204x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.003x faster (HPT: reliability of 96.47%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.123x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12751211058)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit
- [raw results](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.209x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.11x
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, gunicorn
- [📄table](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 87.37%, 1.00x faster at 99th %ile)
- Memory usage: 0.88x
- [📄table](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

