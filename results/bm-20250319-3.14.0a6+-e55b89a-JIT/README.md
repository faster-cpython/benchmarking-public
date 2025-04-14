# Results

- fork: Fidget-Spinner/baseline_jit
- version: 3.14.0a6+
- config: JIT
- commit hash: [e55b89a](https://github.com/Fidget%2dSpinner/cpython/commit/e55b89a)
- commit date: 2025-03-19T22:51:20+08:00
- commit merge base: [295b53df2aa18deb625a7da41f7e4babfe6ef34b](https://github.com/python/cpython/commit/295b53df2aa18deb625a7da41f7e4babfe6ef34b)
- ref: baseline_jit

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13950825369)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a.json)

### vs. 3.10.4

- Geometric mean: 1.279x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.10.4.md)
- [📈time plot](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x faster (HPT: reliability of 80.36%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.12.0.md)
- [📈time plot](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x faster (HPT: reliability of 65.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.13.0.md)
- [📈time plot](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x faster (HPT: reliability of 99.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-base-mem.svg)
- [📄table](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-base.md)
- [📈time plot](bm-20250319-arminc-aarch64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13950825369)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a.json)

### vs. 3.10.4

- Geometric mean: 1.416x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.10.4.md)
- [📈time plot](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.093x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.12.0.md)
- [📈time plot](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 91.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.13.0.md)
- [📈time plot](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x slower (HPT: reliability of 72.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-base-mem.svg)
- [📄table](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-base.md)
- [📈time plot](bm-20250319-linux-x86_64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13950825369)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a.json)

### vs. 3.10.4

- Geometric mean: 1.191x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.10.4.md)
- [📈time plot](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 83.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.12.0.md)
- [📈time plot](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x slower (HPT: reliability of 99.94%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.13.0.md)
- [📈time plot](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.034x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-base.md)
- [📈time plot](bm-20250319-pythonperf1-amd64-Fidget%252dSpinner-baseline_jit-3.14.0a6%2B-e55b89a-vs-base.svg)

