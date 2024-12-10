# Results

- fork: faster-cpython/refactor_refcnt_mort
- version: 3.14.0a0
- config: 
- commit hash: [2fbc12f](https://github.com/faster%2dcpython/cpython/commit/2fbc12f)
- commit date: 2024-10-10T20:09:52+01:00
- commit merge base: [c9014374c50d6ef64786d3e7d9c7e99053d5c9e2](https://github.com/python/cpython/commit/c9014374c50d6ef64786d3e7d9c7e99053d5c9e2)
- ref: refactor_refcnt_mort

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11280469906)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f.json)

### vs. 3.10.4

- Geometric mean: 1.402x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-3.10.4.md)
- [📈time plot](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-3.12.0.md)
- [📈time plot](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x faster (HPT: reliability of 91.45%, 1.00x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-3.13.0.md)
- [📈time plot](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.019x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-base-mem.svg)
- [📄table](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-base.md)
- [📈time plot](bm-20241010-linux-x86_64-faster%252dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f-vs-base.svg)

