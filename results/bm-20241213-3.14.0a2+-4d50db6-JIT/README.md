# Results

- fork: Fidget-Spinner/lower_jit_tier1
- version: 3.14.0a2+
- config: JIT
- commit hash: [4d50db6](https://github.com/Fidget%2dSpinner/cpython/commit/4d50db6)
- commit date: 2024-12-13T01:29:10+08:00
- commit merge base: [487fdbed40734fd7721457c6f6ffeca03da0b0e7](https://github.com/python/cpython/commit/487fdbed40734fd7721457c6f6ffeca03da0b0e7)
- ref: lower_jit_tier1

## linux x86_64 (azure)

- [pystats raw](bm-20241213-azure-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-pystats.json)
- [pystats table](bm-20241213-azure-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-pystats.md)

### vs. base

- [pystats diff](bm-20241213-azure-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12305706643)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6.json)

### vs. 3.10.4

- Geometric mean: 1.426x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-3.10.4.md)
- [📈time plot](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.100x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-3.12.0.md)
- [📈time plot](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 95.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-3.13.0.md)
- [📈time plot](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 97.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-base-mem.svg)
- [📄table](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-base.md)
- [📈time plot](bm-20241213-linux-x86_64-Fidget%252dSpinner-lower_jit_tier1-3.14.0a2%2B-4d50db6-vs-base.svg)

