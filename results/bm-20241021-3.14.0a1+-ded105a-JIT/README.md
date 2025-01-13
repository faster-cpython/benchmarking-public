# Results

- fork: python/ded105a62b9d78717f8d
- version: 3.14.0a1+
- config: JIT
- commit hash: [ded105a](https://github.com/python/cpython/commit/ded105a)
- commit date: 2024-10-21T10:44:18+02:00
- commit merge base: [c5c21fee7ae1ea689a351caa454c98e716a6e537](https://github.com/python/cpython/commit/c5c21fee7ae1ea689a351caa454c98e716a6e537)
- ref: ded105a62b9d78717f8d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.161x faster (HPT: reliability of 99.96%, 1.02x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.097x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: dulwich_log
- [📄table](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.396x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.063x faster (HPT: reliability of 99.96%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 60.45%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.283x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 71.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x slower (HPT: reliability of 53.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.194x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x faster (HPT: reliability of 75.11%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 99.84%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.175x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.184x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 54.52%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472488447)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a.json)

### vs. 3.10.4

- Geometric mean: 1.241x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.md)
- [📈time plot](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.20%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.md)
- [📈time plot](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.md)
- [📈time plot](bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1%2B-ded105a-vs-3.13.0.svg)

