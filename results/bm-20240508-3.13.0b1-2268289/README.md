# Results

- fork: python/v3.13.0b1
- version: 3.13.0b1
- config: 
- commit hash: [2268289](https://github.com/python/cpython/commit/2268289)
- commit date: 2024-05-08T11:21:00+02:00
- commit merge base: [c4f9823be277b2e3de2315526612276626217743](https://github.com/python/cpython/commit/c4f9823be277b2e3de2315526612276626217743)
- fork: python/2268289a47c6e3c9a220
- ref: 2268289a47c6e3c9a220, v3.13.0b1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- [raw results](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.245x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- Geometric mean: 1.243x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.14x
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x slower (HPT: reliability of 81.23%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- Geometric mean: 1.025x slower (HPT: reliability of 59.21%, 1.00x slower at 99th %ile)
- Memory usage: 0.94x
- new benchmarks: bpe_tokeniser, flaskblogging, unpack_sequence
- [📄table](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x slower (HPT: reliability of 99.86%, 1.00x slower at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- Geometric mean: 1.029x slower (HPT: reliability of 96.47%, 1.00x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.svg)
- [📄table](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- Geometric mean: 1.329x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.004x slower (HPT: reliability of 99.87%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- Geometric mean: 1.019x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- Geometric mean: 1.027x slower (HPT: reliability of 97.86%, 1.00x slower at 99th %ile)
- missing benchmarks: connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-linux-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.svg)
- [📄table](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- [raw results](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.234x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- Geometric mean: 1.242x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x slower (HPT: reliability of 97.64%, 1.00x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- Geometric mean: 1.041x slower (HPT: reliability of 94.40%, 1.00x slower at 99th %ile)
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x slower (HPT: reliability of 98.78%, 1.00x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- Geometric mean: 1.028x slower (HPT: reliability of 84.57%, 1.00x slower at 99th %ile)
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.svg)
- [📄table](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9768323837)
- [raw results](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.242x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- Geometric mean: 1.245x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- missing benchmarks: aiohttp, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- missing benchmarks: aiohttp, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- Geometric mean: 1.036x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, mypy2
- [📄table](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.svg)
- [📄table](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.172x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.216x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-pythonperf1_win32-x86-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9021430016)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289.json)
- [raw results](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289.json)

### vs. 3.10.4

- Geometric mean: 1.276x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- Geometric mean: 1.268x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.10.4.svg)
- [📄table](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.md)
- [📈time plot](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- Geometric mean: 1.069x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.51x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.12.0.svg)
- [📄table](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.md)
- [📈time plot](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.46x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-darwin-arm64-python-2268289a47c6e3c9a220-3.13.0b1-2268289-vs-3.13.0.svg)
- [📄table](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.md)
- [📈time plot](bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289-vs-3.13.0.svg)

