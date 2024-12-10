# Results

- fork: brandtbucher/justin_frame_pointer
- version: 3.14.0a1+
- config: JIT
- commit hash: [68190be](https://github.com/brandtbucher/cpython/commit/68190be)
- commit date: 2024-11-20T07:23:20-08:00
- commit merge base: [4cd10762b06ec57252e3c7373e74240b4d0c5ed8](https://github.com/python/cpython/commit/4cd10762b06ec57252e3c7373e74240b4d0c5ed8)
- ref: justin_frame_pointer

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11936426410)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be.json)

### vs. 3.10.4

- Geometric mean: 1.162x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-3.10.4.md)
- [📈time plot](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-3.12.0.md)
- [📈time plot](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-3.13.0.md)
- [📈time plot](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.031x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-base-mem.svg)
- [📄table](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-base.md)
- [📈time plot](bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-68190be-vs-base.svg)

