# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: JIT
- commit hash: [e5d0e67](https://github.com/faster%2dcpython/cpython/commit/e5d0e67)
- commit date: 2024-09-17T15:38:54+01:00
- commit merge base: [4ed7d1d6acc22807bfb5983c98fd59f7cb5061db](https://github.com/faster%2dcpython/cpython/commit/4ed7d1d6acc22807bfb5983c98fd59f7cb5061db)
- ref: spill_before_escapin

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10905380218)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67.json)

### vs. 3.10.4

- Geometric mean: 1.313x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-3.10.4.md)
- [📈time plot](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x faster (HPT: reliability of 69.26%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-3.12.0.md)
- [📈time plot](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x faster (HPT: reliability of 94.92%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-3.13.0.md)
- [📈time plot](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 66.06%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-base-mem.svg)
- [📄table](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-base.md)
- [📈time plot](bm-20240917-pythonperf2-x86_64-faster%252dcpython-spill_before_escapin-3.14.0a0-e5d0e67-vs-base.svg)

