# Results

- fork: Fidget-Spinner/lto_fix
- version: 3.14.0a6+
- config: 
- commit hash: [8891cd2](https://github.com/Fidget%2dSpinner/cpython/commit/8891cd2)
- commit date: 2025-04-07T22:07:18+08:00
- commit merge base: [7bb1e1a23634bae81bf76fdb34e9f9f7e59b3793](https://github.com/python/cpython/commit/7bb1e1a23634bae81bf76fdb34e9f9f7e59b3793)
- ref: lto_fix

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14315687962)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2.json)

### vs. 3.10.4

- Geometric mean: 1.474x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.10.4.md)
- [📈time plot](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.137x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.12.0.md)
- [📈time plot](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.13.0.md)
- [📈time plot](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-base-mem.svg)
- [📄table](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-base.md)
- [📈time plot](bm-20250407-linux-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14315692379)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2.json)

### vs. 3.10.4

- Geometric mean: 1.367x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.10.4.md)
- [📈time plot](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.12.0.md)
- [📈time plot](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.074x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.13.0.md)
- [📈time plot](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 91.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-base-mem.svg)
- [📄table](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-base.md)
- [📈time plot](bm-20250407-pythonperf2-x86_64-Fidget%252dSpinner-lto_fix-3.14.0a6%2B-8891cd2-vs-base.svg)

