# Results

- fork: python/v3.13.0a1
- version: 3.13.0a1
- config: NOGIL
- commit hash: [ad056f0](https://github.com/python/cpython/commit/ad056f0)
- commit date: 2023-10-13T10:52:10+02:00
- commit merge base: [b7f9661bc12fdfec98684c89f03177ae5d3d74c1](https://github.com/python/cpython/commit/b7f9661bc12fdfec98684c89f03177ae5d3d74c1)
- ref: v3.13.0a1

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9036771738)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json)

### vs. 3.10.4

- Geometric mean: 1.254x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 0.65x
- missing benchmarks: djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x slower (HPT: reliability of 71.33%, 1.00x faster at 99th %ile)
- Memory usage: 0.55x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.52x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.045x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.58x
- missing benchmarks: 🔴 unpack_sequence
- new benchmarks: aiohttp, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, thrift
- [🧠memory plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-base-mem.svg)
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-base.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-base.svg)

