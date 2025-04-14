# Results

- fork: nelhage/computed_goto_nomerg
- version: 3.14.0a4+
- config: 
- commit hash: [4603470](https://github.com/nelhage/cpython/commit/4603470)
- commit date: 2025-02-10T18:10:11-08:00
- commit merge base: [c1f352bf0813803bb795b796c16040a5cd4115f2](https://github.com/python/cpython/commit/c1f352bf0813803bb795b796c16040a5cd4115f2)
- ref: computed_goto_nomerg

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13286286073)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470.json)

### vs. 3.10.4

- Geometric mean: 1.325x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.10.4.md)
- [📈time plot](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.12.0.md)
- [📈time plot](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.13.0.md)
- [📈time plot](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 99.64%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base-mem.svg)
- [📄table](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base.md)
- [📈time plot](bm-20250210-arminc-aarch64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13286281600)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470.json)

### vs. 3.10.4

- Geometric mean: 1.463x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.10.4.md)
- [📈time plot](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.12.0.md)
- [📈time plot](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.13.0.md)
- [📈time plot](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 66.44%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base-mem.svg)
- [📄table](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base.md)
- [📈time plot](bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13290078422)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470.json)

### vs. 3.10.4

- Geometric mean: 1.391x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.10.4.md)
- [📈time plot](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.12.0.md)
- [📈time plot](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.13.0.md)
- [📈time plot](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 99.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base-mem.svg)
- [📄table](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base.md)
- [📈time plot](bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4%2B-4603470-vs-base.svg)

