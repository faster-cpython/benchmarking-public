# Results

- fork: Fidget-Spinner/trace_function_entry
- version: 3.14.0a5+
- config: JIT
- commit hash: [553888a](https://github.com/Fidget%2dSpinner/cpython/commit/553888a)
- commit date: 2025-03-07T15:54:15+08:00
- commit merge base: [052cb717f5f97d08d2074f4118fd2c21224d3015](https://github.com/python/cpython/commit/052cb717f5f97d08d2074f4118fd2c21224d3015)
- ref: trace_function_entry

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13720004889)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a.json)

### vs. 3.10.4

- Geometric mean: 1.325x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.10.4.md)
- [📈time plot](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.12.0.md)
- [📈time plot](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, docutils, gevent_hub, gunicorn, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.13.0.md)
- [📈time plot](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 79.78%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 docutils, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize
- [🧠memory plot](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base-mem.svg)
- [📄table](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base.md)
- [📈time plot](bm-20250307-arminc-aarch64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13720004889)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a.json)

### vs. 3.10.4

- Geometric mean: 1.447x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, docutils, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.10.4.md)
- [📈time plot](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.12.0.md)
- [📈time plot](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, docutils, gevent_hub, gunicorn, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http
- [📄table](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.13.0.md)
- [📈time plot](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 82.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 docutils, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize
- [🧠memory plot](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base-mem.svg)
- [📄table](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base.md)
- [📈time plot](bm-20250307-linux-x86_64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13720004889)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a.json)

### vs. 3.10.4

- Geometric mean: 1.254x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.10.4.md)
- [📈time plot](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 98.51%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.12.0.md)
- [📈time plot](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 82.97%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, docutils, gevent_hub, pprint_pformat, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, tornado_http
- [📄table](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.13.0.md)
- [📈time plot](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 docutils, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize
- [📄table](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base.md)
- [📈time plot](bm-20250307-pythonperf1-amd64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13720004889)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a.json)

### vs. 3.10.4

- Geometric mean: 1.360x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, docutils, gevent_hub, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.10.4.md)
- [📈time plot](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, docutils, gevent_hub, gunicorn, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http
- [📄table](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.12.0.md)
- [📈time plot](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, docutils, gevent_hub, gunicorn, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http
- [📄table](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.13.0.md)
- [📈time plot](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 docutils, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize
- [🧠memory plot](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base-mem.svg)
- [📄table](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base.md)
- [📈time plot](bm-20250307-darwin-arm64-Fidget%252dSpinner-trace_function_entry-3.14.0a5%2B-553888a-vs-base.svg)

