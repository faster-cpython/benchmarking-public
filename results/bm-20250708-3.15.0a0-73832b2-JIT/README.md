# Results

- fork: faster-cpython/fast_side_exits
- version: 3.15.0a0
- config: JIT
- commit hash: [73832b2](https://github.com/faster%2dcpython/cpython/commit/73832b2)
- commit date: 2025-07-08T10:26:43+01:00
- commit merge base: [cb99d992774b67761441e122965ed056bac09241](https://github.com/python/cpython/commit/cb99d992774b67761441e122965ed056bac09241)
- ref: fast_side_exits

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16139562343)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2.json)

### vs. 3.10.4

- Geometric mean: 1.329x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.10.4.md)
- [📈time plot](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.12.0.md)
- [📈time plot](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.13.0.md)
- [📈time plot](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 pycparser
- [🧠memory plot](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-base-mem.svg)
- [📄table](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-base.md)
- [📈time plot](bm-20250708-pythonperf2-x86_64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16139581600)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2.json)

### vs. 3.10.4

- Geometric mean: 1.317x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.10.4.md)
- [📈time plot](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.120x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.12.0.md)
- [📈time plot](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.087x faster (HPT: reliability of 85.08%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.13.0.md)
- [📈time plot](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 61.01%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-base.md)
- [📈time plot](bm-20250708-pythonperf1-amd64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16139571637)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2.json)

### vs. 3.10.4

- Geometric mean: 1.344x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.10.4.md)
- [📈time plot](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 96.11%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.12.0.md)
- [📈time plot](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.13.0.md)
- [📈time plot](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 95.44%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-base-mem.svg)
- [📄table](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-base.md)
- [📈time plot](bm-20250708-darwin-arm64-faster%252dcpython-fast_side_exits-3.15.0a0-73832b2-vs-base.svg)

