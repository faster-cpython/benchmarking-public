# Results

- fork: faster-cpython
- version: 3.14.0a1+
- config: 
- commit hash: [5e813c5](https://github.com/faster%2dcpython/cpython/commit/5e813c5)
- commit date: 2024-11-04T12:27:51+00:00
- commit merge base: [bfc1d2504c183a9464e65c290e48516d176ea41f](https://github.com/faster%2dcpython/cpython/commit/bfc1d2504c183a9464e65c290e48516d176ea41f)
- ref: mark_first_gc

## linux x86_64 (azure)

- [pystats raw](bm-20241104-azure-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-pystats.json)
- [pystats table](bm-20241104-azure-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-pystats.md)

### vs. base

- [pystats diff](bm-20241104-azure-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11664284848)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5.json)

### vs. 3.10.4

- Geometric mean: 1.412x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-3.10.4.md)
- [📈time plot](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-3.12.0.md)
- [📈time plot](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, mypy2, tornado_http
- new benchmarks: sqlite_synth
- [📄table](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-3.13.0.md)
- [📈time plot](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x faster (HPT: reliability of 54.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-base-mem.svg)
- [📄table](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-base.md)
- [📈time plot](bm-20241104-linux-x86_64-faster%252dcpython-mark_first_gc-3.14.0a1%2B-5e813c5-vs-base.svg)

