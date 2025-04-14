# Results

- fork: python/v3.13.0b4
- version: 3.13.0b4
- config: 
- commit hash: [567c38b](https://github.com/python/cpython/commit/567c38b)
- commit date: 2024-07-18T11:41:38+02:00
- ref: v3.13.0b4

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9994110031)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.10.4.md)
- [📈time plot](bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 87.35%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.12.0.md)
- [📈time plot](bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 55.49%, 1.00x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, mypy2
- [📄table](bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.13.0.md)
- [📈time plot](bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9994110031)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b.json)

### vs. 3.10.4

- Geometric mean: 1.395x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.10.4.md)
- [📈time plot](bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.12.0.md)
- [📈time plot](bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 57.77%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, mypy2
- [📄table](bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.13.0.md)
- [📈time plot](bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9994110031)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.10.4.md)
- [📈time plot](bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.000x faster (HPT: reliability of 75.63%, 1.00x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.12.0.md)
- [📈time plot](bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 80.01%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, mypy2
- [📄table](bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.13.0.md)
- [📈time plot](bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9994110031)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b.json)

### vs. 3.10.4

- Geometric mean: 1.303x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, mypy2
- [📄table](bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.10.4.md)
- [📈time plot](bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, mypy2
- [📄table](bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.12.0.md)
- [📈time plot](bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, mypy2
- [📄table](bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.13.0.md)
- [📈time plot](bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b-vs-3.13.0.svg)

