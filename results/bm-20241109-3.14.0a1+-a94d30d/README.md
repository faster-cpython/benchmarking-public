# Results

- fork: faster-cpython/faster_marking
- version: 3.14.0a1+
- config: 
- commit hash: [a94d30d](https://github.com/faster%2dcpython/cpython/commit/a94d30d)
- commit date: 2024-11-09T11:30:49+00:00
- commit merge base: [6293d00e7201f3f28b1f4512e57dc4f03855cabd](https://github.com/python/cpython/commit/6293d00e7201f3f28b1f4512e57dc4f03855cabd)
- ref: faster_marking

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11755880064)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d.json)

### vs. 3.10.4

- Geometric mean: 1.449x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-3.10.4.md)
- [📈time plot](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.113x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-3.12.0.md)
- [📈time plot](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-3.13.0.md)
- [📈time plot](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.052x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-base-mem.svg)
- [📄table](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-base.md)
- [📈time plot](bm-20241109-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a1%2B-a94d30d-vs-base.svg)

