# Results

- fork: python/2a66dd33dfc0b845042d
- version: 3.14.0a3+
- config: NOGIL
- commit hash: [2a66dd3](https://github.com/python/cpython/commit/2a66dd3)
- commit date: 2024-12-20T11:40:58-08:00
- commit merge base: [3879ca0100942ae15a09ac22889cbe3e46d424eb](https://github.com/python/cpython/commit/3879ca0100942ae15a09ac22889cbe3e46d424eb)
- ref: 2a66dd33dfc0b845042d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12449454953)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3.json)

### vs. 3.10.4

- Geometric mean: 1.076x slower (HPT: reliability of 99.99%, 1.04x slower at 99th %ile)
- Memory usage: 1.54x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.md)
- [📈time plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.267x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.md)
- [📈time plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.259x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.md)
- [📈time plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.282x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base-mem.svg)
- [📄table](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.md)
- [📈time plot](bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12449454953)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3.json)

### vs. 3.10.4

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.md)
- [📈time plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.145x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.md)
- [📈time plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.190x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.md)
- [📈time plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.221x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base-mem.svg)
- [📄table](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.md)
- [📈time plot](bm-20241220-linux-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12449454953)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3.json)

### vs. 3.10.4

- Geometric mean: 1.037x faster (HPT: reliability of 97.14%, 1.00x faster at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.md)
- [📈time plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.191x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.md)
- [📈time plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.174x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.md)
- [📈time plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.216x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base-mem.svg)
- [📄table](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.md)
- [📈time plot](bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3%2B-2a66dd3-vs-base.svg)

