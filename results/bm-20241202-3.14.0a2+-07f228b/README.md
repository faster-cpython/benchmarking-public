# Results

- fork: faster-cpython/faster_marking
- version: 3.14.0a2+
- config: 
- commit hash: [07f228b](https://github.com/faster%2dcpython/cpython/commit/07f228b)
- commit date: 2024-12-02T15:45:47+00:00
- commit merge base: [7c2bd9b2266665ff4010b6c6c175bab18e08e4f8](https://github.com/python/cpython/commit/7c2bd9b2266665ff4010b6c6c175bab18e08e4f8)
- ref: faster_marking

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12122901979)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b.json)

### vs. 3.10.4

- Geometric mean: 1.423x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-3.10.4.md)
- [📈time plot](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-3.12.0.md)
- [📈time plot](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 99.79%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-3.13.0.md)
- [📈time plot](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 99.96%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-base-mem.svg)
- [📄table](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-base.md)
- [📈time plot](bm-20241202-linux-x86_64-faster%252dcpython-faster_marking-3.14.0a2%2B-07f228b-vs-base.svg)

