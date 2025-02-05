# Results

- fork: faster-cpython/fix_decref_and_reuse
- version: 3.14.0a0
- config: 
- commit hash: [07df2d0](https://github.com/faster%2dcpython/cpython/commit/07df2d0)
- commit date: 2024-10-14T10:37:30+01:00
- commit merge base: [5217328f93f599755bd70418952392c54f705a71](https://github.com/python/cpython/commit/5217328f93f599755bd70418952392c54f705a71)
- ref: fix_decref_and_reuse

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11325536521)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json)

### vs. 3.10.4

- Geometric mean: 1.391x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.10.4.md)
- [📈time plot](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.048x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.12.0.md)
- [📈time plot](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 96.92%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.13.0.md)
- [📈time plot](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 99.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-base-mem.svg)
- [📄table](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-base.md)
- [📈time plot](bm-20241014-linux-x86_64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11325548685)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json)

### vs. 3.10.4

- Geometric mean: 1.140x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.10.4.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.049x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.12.0.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.13.0.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 96.69%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-base.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-faster%252dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0-vs-base.svg)

