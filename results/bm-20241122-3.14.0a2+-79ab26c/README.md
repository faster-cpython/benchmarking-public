# Results

- fork: faster-cpython/mark_first_2
- version: 3.14.0a2+
- config: 
- commit hash: [79ab26c](https://github.com/faster%2dcpython/cpython/commit/79ab26c)
- commit date: 2024-11-22T12:16:26+00:00
- commit merge base: [1629d2ca56014beb2d46c42cc199a43ac97e3b97](https://github.com/python/cpython/commit/1629d2ca56014beb2d46c42cc199a43ac97e3b97)
- ref: mark_first_2

## linux x86_64 (azure)

- [pystats raw](bm-20241122-azure-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-pystats.json)
- [pystats table](bm-20241122-azure-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-pystats.md)

### vs. base

- [pystats diff](bm-20241122-azure-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11974349921)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.10.4.md)
- [📈time plot](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.12.0.md)
- [📈time plot](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.13.0.md)
- [📈time plot](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.036x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-base-mem.svg)
- [📄table](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-base.md)
- [📈time plot](bm-20241122-linux-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11981680184)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241122-pythonperf2-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c.json)

### vs. 3.10.4

- Geometric mean: 1.312x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-pythonperf2-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.10.4.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 86.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-pythonperf2-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.12.0.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-pythonperf2-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.13.0.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-faster%252dcpython-mark_first_2-3.14.0a2%2B-79ab26c-vs-3.13.0.svg)

