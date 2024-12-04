# Results

- fork: faster-cpython
- version: 3.14.0a1+
- config: 
- commit hash: [3c18fc8](https://github.com/faster%2dcpython/cpython/commit/3c18fc8)
- commit date: 2024-11-06T11:42:21+00:00
- commit merge base: [bfc1d2504c183a9464e65c290e48516d176ea41f](https://github.com/faster%2dcpython/cpython/commit/bfc1d2504c183a9464e65c290e48516d176ea41f)
- ref: mark_first_gc

## linux x86_64 (azure)

- [pystats raw](bm-20241106-azure-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-pystats.json)
- [pystats table](bm-20241106-azure-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-pystats.md)

### vs. base

- [pystats diff](bm-20241106-azure-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11702967947)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8.json)

### vs. 3.10.4

- Geometric mean: 1.446x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-3.10.4.md)
- [📈time plot](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.112x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-3.12.0.md)
- [📈time plot](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-3.13.0.md)
- [📈time plot](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.046x faster (HPT: reliability of 96.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-base-mem.svg)
- [📄table](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-base.md)
- [📈time plot](bm-20241106-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-3c18fc8-vs-base.svg)

