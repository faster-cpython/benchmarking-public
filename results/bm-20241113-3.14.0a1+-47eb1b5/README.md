# Results

- fork: faster-cpython/faster_marking
- version: 3.14.0a1+
- config: 
- commit hash: [47eb1b5](https://github.com/faster%2dcpython/cpython/commit/47eb1b5)
- commit date: 2024-11-13T20:02:38+00:00
- commit merge base: [6293d00e7201f3f28b1f4512e57dc4f03855cabd](https://github.com/python/cpython/commit/6293d00e7201f3f28b1f4512e57dc4f03855cabd)
- ref: faster_marking

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11834908494)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5.json)

### vs. 3.10.4

- Geometric mean: 1.440x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.10.4.md)
- [📈time plot](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.12.0.md)
- [📈time plot](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 99.20%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.13.0.md)
- [📈time plot](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.044x faster (HPT: reliability of 96.44%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-base-mem.svg)
- [📄table](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-base.md)
- [📈time plot](bm-20241113-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11897376333)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5.json)

### vs. 3.10.4

- Geometric mean: 1.333x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.10.4.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x faster (HPT: reliability of 57.42%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.12.0.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.13.0.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.023x faster (HPT: reliability of 89.59%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-base-mem.svg)
- [📄table](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-base.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-47eb1b5-vs-base.svg)

