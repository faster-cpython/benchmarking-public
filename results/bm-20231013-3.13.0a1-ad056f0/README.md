# Results

- fork: python/v3.13.0a1
- version: 3.13.0a1
- config: 
- commit hash: [ad056f0](https://github.com/python/cpython/commit/ad056f0)
- commit date: 2023-10-13T10:52:10+02:00
- commit merge base: [b7f9661bc12fdfec98684c89f03177ae5d3d74c1](https://github.com/python/cpython/commit/b7f9661bc12fdfec98684c89f03177ae5d3d74c1)
- ref: v3.13.0a1

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/6855745543)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json)

### vs. 3.10.4

- Geometric mean: 1.365x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, dask, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.022x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: aiohttp, dask, django_template, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: bpe_tokeniser, connected_components, django_template, djangocms, genshi_text, genshi_xml, gevent_hub, gunicorn, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, thrift
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/6855745543)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json)

### vs. 3.10.4

- Geometric mean: 1.268x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.md)
- [📈time plot](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.87x
- missing benchmarks: aiohttp, dask, django_template, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.md)
- [📈time plot](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x slower (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: 0.85x
- missing benchmarks: bpe_tokeniser, connected_components, django_template, djangocms, genshi_text, genshi_xml, gevent_hub, gunicorn, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, thrift
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0.md)
- [📈time plot](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/6855745543)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0.json)

### vs. 3.10.4

- Geometric mean: 1.210x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.md)
- [📈time plot](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.006x faster (HPT: reliability of 99.63%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, django_template, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.md)
- [📈time plot](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, django_template, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, thrift
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0.md)
- [📈time plot](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0.svg)

