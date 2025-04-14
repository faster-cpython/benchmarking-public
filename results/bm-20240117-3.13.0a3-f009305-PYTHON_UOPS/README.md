# Results

- fork: python/v3.13.0a3
- version: 3.13.0a3
- config: T2
- commit hash: [f009305](https://github.com/python/cpython/commit/f009305)
- commit date: 2024-01-17T13:14:40+01:00
- commit merge base: [b204c4beb44c1a9013f8da16984c9129374ed8c5](https://github.com/python/cpython/commit/b204c4beb44c1a9013f8da16984c9129374ed8c5)
- fork: python/f009305a7d635f86440c
- ref: f009305a7d635f86440c, v3.13.0a3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575581884)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.271x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 0.87x
- missing benchmarks: bpe_tokeniser, connected_components, django_template, djangocms, genshi_text, genshi_xml, gevent_hub, gunicorn, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, thrift
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.063x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base-mem.svg)
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575581884)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.171x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.096x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: bpe_tokeniser, connected_components, django_template, djangocms, genshi_text, genshi_xml, gevent_hub, gunicorn, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, thrift
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.092x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base-mem.svg)
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575581884)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.203x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.003x faster (HPT: reliability of 95.48%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, django_template, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, thrift
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.047x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7583593375)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.157x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.155x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x faster (HPT: reliability of 60.61%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, django_template, djangocms, dulwich_log, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, thrift
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.058x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10778755675)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit
- [raw results](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.185x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 0.47x
- missing benchmarks: connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 90.81%, 1.00x slower at 99th %ile)
- Memory usage: 0.50x
- missing benchmarks: connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x faster (HPT: reliability of 69.27%, 1.00x faster at 99th %ile)
- Memory usage: 0.35x
- missing benchmarks: connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 64.94%, 1.00x slower at 99th %ile)
- Memory usage: 0.26x
- new benchmarks: bpe_tokeniser, unpack_sequence
- [🧠memory plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-base-mem.svg)
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

