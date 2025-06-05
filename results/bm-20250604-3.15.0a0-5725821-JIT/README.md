# Results

- fork: faster-cpython/fix_tier2_for_iter
- version: 3.15.0a0
- config: JIT
- commit hash: [5725821](https://github.com/faster%2dcpython/cpython/commit/5725821)
- commit date: 2025-06-04T13:20:30+01:00
- commit merge base: [ec12559ebafca01ded22c9013de64abe535c838d](https://github.com/python/cpython/commit/ec12559ebafca01ded22c9013de64abe535c838d)
- ref: fix_tier2_for_iter

## linux x86_64 (azure)

- [pystats raw](bm-20250604-azure-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-pystats.json)
- [pystats table](bm-20250604-azure-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-pystats.md)

### vs. base

- [pystats diff](bm-20250604-azure-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15458694911)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821.json)

### vs. 3.10.4

- Geometric mean: 1.330x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-3.10.4.md)
- [📈time plot](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.099x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-3.12.0.md)
- [📈time plot](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x slower (HPT: reliability of 98.87%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-3.13.0.md)
- [📈time plot](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.273x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- new benchmarks: regex_compile
- [🧠memory plot](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-base-mem.svg)
- [📄table](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-base.md)
- [📈time plot](bm-20250604-linux-x86_64-faster%252dcpython-fix_tier2_for_iter-3.15.0a0-5725821-vs-base.svg)

