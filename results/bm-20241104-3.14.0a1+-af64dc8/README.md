# Results

- fork: faster-cpython
- version: 3.14.0a1+
- config: 
- commit hash: [af64dc8](https://github.com/faster%2dcpython/cpython/commit/af64dc8)
- commit date: 2024-11-04T14:38:23+00:00
- commit merge base: [bfc1d2504c183a9464e65c290e48516d176ea41f](https://github.com/faster%2dcpython/cpython/commit/bfc1d2504c183a9464e65c290e48516d176ea41f)
- ref: gc_visit_by_type_sta

## linux x86_64 (azure)

- [pystats raw](bm-20241104-azure-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-pystats.json)
- [pystats table](bm-20241104-azure-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-pystats.md)

### vs. base

- [pystats diff](bm-20241104-azure-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11666458667)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241104-pythonperf2-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8.json)

### vs. 3.10.4

- Geometric mean: 1.317x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241104-pythonperf2-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-vs-3.10.4.md)
- [📈time plot](bm-20241104-pythonperf2-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x faster (HPT: reliability of 97.54%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241104-pythonperf2-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-vs-3.12.0.md)
- [📈time plot](bm-20241104-pythonperf2-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, mypy2, tornado_http
- new benchmarks: sqlite_synth
- [📄table](bm-20241104-pythonperf2-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-vs-3.13.0.md)
- [📈time plot](bm-20241104-pythonperf2-x86_64-faster%252dcpython-gc_visit_by_type_sta-3.14.0a1%2B-af64dc8-vs-3.13.0.svg)

