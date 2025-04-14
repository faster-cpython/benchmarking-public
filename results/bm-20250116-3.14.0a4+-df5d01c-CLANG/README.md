# Results

- fork: Fidget-Spinner/tail_call
- version: 3.14.0a4+
- config: CLANG
- commit hash: [df5d01c](https://github.com/Fidget%2dSpinner/cpython/commit/df5d01c)
- commit date: 2025-01-16T20:44:01+08:00
- commit merge base: [313b96eb8b8d0ad3bac58d633822a0a3705ce60b](https://github.com/python/cpython/commit/313b96eb8b8d0ad3bac58d633822a0a3705ce60b)
- ref: tail_call

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12811335920)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c.json)

### vs. 3.10.4

- Geometric mean: 1.355x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.md)
- [📈time plot](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.md)
- [📈time plot](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.md)
- [📈time plot](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base-mem.svg)
- [📄table](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.md)
- [📈time plot](bm-20250116-arminc-aarch64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12811326822)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c.json)

### vs. 3.10.4

- Geometric mean: 1.397x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.082x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.093x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base-mem.svg)
- [📄table](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12811331877)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c.json)

### vs. 3.10.4

- Geometric mean: 1.466x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.md)
- [📈time plot](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.170x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.md)
- [📈time plot](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.173x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.md)
- [📈time plot](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.117x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base-mem.svg)
- [📄table](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.md)
- [📈time plot](bm-20250116-darwin-arm64-Fidget%252dSpinner-tail_call-3.14.0a4%2B-df5d01c-vs-base.svg)

