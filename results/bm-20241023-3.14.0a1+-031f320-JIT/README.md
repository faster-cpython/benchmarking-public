# Results

- fork: faster-cpython
- version: 3.14.0a1+
- config: JIT
- commit hash: [031f320](https://github.com/faster%2dcpython/cpython/commit/031f320)
- commit date: 2024-10-23T11:28:35+01:00
- commit merge base: [759a54d28ffe7eac8c23917f5d3dfad8309856be](https://github.com/faster%2dcpython/cpython/commit/759a54d28ffe7eac8c23917f5d3dfad8309856be)
- ref: load_const_return_re

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11478043352)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320.json)

### vs. 3.10.4

- Geometric mean: 1.281x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-3.10.4.md)
- [📈time plot](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 72.25%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-3.12.0.md)
- [📈time plot](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x slower (HPT: reliability of 59.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-3.13.0.md)
- [📈time plot](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.63%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-base-mem.svg)
- [📄table](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-base.md)
- [📈time plot](bm-20241023-pythonperf2-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-031f320-vs-base.svg)

