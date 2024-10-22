# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.32x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x slower
- Memory change: 6.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 250 ms: 1.41x slower                                                  |
| docutils       | 1.44 sec                                               | 1.80 sec: 1.25x slower                                                |
| html5lib       | 36.6 ms                                                | 52.4 ms: 1.43x slower                                                 |
| tornado_http   | 77.2 ms                                                | 96.0 ms: 1.24x slower                                                 |
| Geometric mean | (ref)                                                  | 1.33x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                      | 457 ms                                                 | 353 ms: 1.30x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 265 ms: 1.10x faster                                                  |
| async_tree_eager_io              | 513 ms                                                 | 493 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.24 sec: 1.02x faster                                                |
| async_tree_eager_io_tg           | 477 ms                                                 | 468 ms: 1.02x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 507 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 465 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 208 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 367 ms: 1.05x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 538 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 398 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 491 ms: 1.07x slower                                                  |
| async_tree_memoization           | 270 ms                                                 | 292 ms: 1.08x slower                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 185 ms: 1.10x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 235 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 158 ms: 1.14x slower                                                  |
| async_generators                 | 294 ms                                                 | 343 ms: 1.17x slower                                                  |
| coroutines                       | 19.8 ms                                                | 23.1 ms: 1.17x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 106 ms: 1.50x slower                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 74.0 ms: 1.53x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 406 ms: 1.68x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 56.2 ms                                                | 96.6 ms: 1.72x slower                                                 |
| nbody          | 73.9 ms                                                | 159 ms: 2.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.54x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.43 ms: 1.08x faster                                                 |
| regex_dna      | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| regex_v8       | 16.9 ms                                                | 17.5 ms: 1.04x slower                                                 |
| regex_compile  | 78.5 ms                                                | 125 ms: 1.59x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                 | 98.9 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 76.8 ms: 1.04x slower                                                 |
| json_loads           | 16.9 us                                                | 19.3 us: 1.15x slower                                                 |
| json_dumps           | 6.56 ms                                                | 8.14 ms: 1.24x slower                                                 |
| xml_etree_generate   | 56.6 ms                                                | 70.7 ms: 1.25x slower                                                 |
| tomli_loads          | 1.56 sec                                               | 2.06 sec: 1.32x slower                                                |
| xml_etree_process    | 40.9 ms                                                | 60.9 ms: 1.49x slower                                                 |
| pickle_pure_python   | 213 us                                                 | 346 us: 1.63x slower                                                  |
| unpickle_pure_python | 163 us                                                 | 269 us: 1.65x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.27x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 17.3 ms: 1.02x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.0 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 51.6 ms: 1.50x slower                                                 |
| genshi_text     | 16.9 ms                                                | 25.8 ms: 1.53x slower                                                 |
| django_template | 22.2 ms                                                | 35.9 ms: 1.62x slower                                                 |
| mako            | 7.68 ms                                                | 13.4 ms: 1.74x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.59x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize                | 189 ms                                                 | 109 ms: 1.73x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 353 ms: 1.30x faster                                                  |
| create_gc_cycles                 | 803 us                                                 | 665 us: 1.21x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.11 ms: 1.18x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 98.9 ms: 1.10x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 265 ms: 1.10x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.43 ms: 1.08x faster                                                 |
| regex_dna                        | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| async_tree_eager_io              | 513 ms                                                 | 493 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.24 sec: 1.02x faster                                                |
| async_tree_eager_io_tg           | 477 ms                                                 | 468 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 507 ms: 1.01x slower                                                  |
| python_startup                   | 17.0 ms                                                | 17.3 ms: 1.02x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 14.0 ms: 1.02x slower                                                 |
| regex_v8                         | 16.9 ms                                                | 17.5 ms: 1.04x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 76.8 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 465 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 208 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 367 ms: 1.05x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 538 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 398 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 491 ms: 1.07x slower                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 54.6 ms: 1.07x slower                                                 |
| async_tree_memoization           | 270 ms                                                 | 292 ms: 1.08x slower                                                  |
| deepcopy                         | 232 us                                                 | 252 us: 1.08x slower                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 185 ms: 1.10x slower                                                  |
| async_tree_none                  | 212 ms                                                 | 235 ms: 1.11x slower                                                  |
| pathlib                          | 22.8 ms                                                | 25.9 ms: 1.14x slower                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 158 ms: 1.14x slower                                                  |
| deepcopy_memo                    | 27.2 us                                                | 30.9 us: 1.14x slower                                                 |
| json_loads                       | 16.9 us                                                | 19.3 us: 1.15x slower                                                 |
| telco                            | 4.80 ms                                                | 5.53 ms: 1.15x slower                                                 |
| json                             | 2.94 ms                                                | 3.42 ms: 1.16x slower                                                 |
| async_generators                 | 294 ms                                                 | 343 ms: 1.17x slower                                                  |
| coroutines                       | 19.8 ms                                                | 23.1 ms: 1.17x slower                                                 |
| generators                       | 31.5 ms                                                | 37.0 ms: 1.17x slower                                                 |
| pylint                           | 181 ms                                                 | 218 ms: 1.21x slower                                                  |
| coverage                         | 46.1 ms                                                | 56.5 ms: 1.23x slower                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 2.55 us: 1.24x slower                                                 |
| meteor_contest                   | 73.8 ms                                                | 91.5 ms: 1.24x slower                                                 |
| json_dumps                       | 6.56 ms                                                | 8.14 ms: 1.24x slower                                                 |
| tornado_http                     | 77.2 ms                                                | 96.0 ms: 1.24x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.80 sec: 1.25x slower                                                |
| xml_etree_generate               | 56.6 ms                                                | 70.7 ms: 1.25x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.88 sec: 1.25x slower                                                |
| nqueens                          | 62.9 ms                                                | 79.2 ms: 1.26x slower                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 4.12 sec: 1.27x slower                                                |
| fannkuch                         | 282 ms                                                 | 359 ms: 1.27x slower                                                  |
| tomli_loads                      | 1.56 sec                                               | 2.06 sec: 1.32x slower                                                |
| pycparser                        | 706 ms                                                 | 955 ms: 1.35x slower                                                  |
| pyflate                          | 351 ms                                                 | 482 ms: 1.37x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 277 ms: 1.38x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 15.8 ms: 1.39x slower                                                 |
| 2to3                             | 178 ms                                                 | 250 ms: 1.41x slower                                                  |
| html5lib                         | 36.6 ms                                                | 52.4 ms: 1.43x slower                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.35 ms: 1.45x slower                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 79.5 ms: 1.47x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 149 us: 1.47x slower                                                  |
| xml_etree_process                | 40.9 ms                                                | 60.9 ms: 1.49x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 51.6 ms: 1.50x slower                                                 |
| async_tree_eager                 | 70.5 ms                                                | 106 ms: 1.50x slower                                                  |
| scimark_sor                      | 106 ms                                                 | 160 ms: 1.51x slower                                                  |
| thrift                           | 466 us                                                 | 706 us: 1.52x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 25.8 ms: 1.53x slower                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 74.0 ms: 1.53x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 54.4 ms: 1.56x slower                                                 |
| bench_thread_pool                | 506 us                                                 | 790 us: 1.56x slower                                                  |
| spectral_norm                    | 77.3 ms                                                | 122 ms: 1.57x slower                                                  |
| comprehensions                   | 12.2 us                                                | 19.3 us: 1.58x slower                                                 |
| regex_compile                    | 78.5 ms                                                | 125 ms: 1.59x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 80.5 ms: 1.60x slower                                                 |
| richards                         | 35.4 ms                                                | 56.8 ms: 1.60x slower                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 851 ms: 1.60x slower                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.73 sec: 1.61x slower                                                |
| django_template                  | 22.2 ms                                                | 35.9 ms: 1.62x slower                                                 |
| pickle_pure_python               | 213 us                                                 | 346 us: 1.63x slower                                                  |
| sympy_str                        | 145 ms                                                 | 238 ms: 1.64x slower                                                  |
| unpickle_pure_python             | 163 us                                                 | 269 us: 1.65x slower                                                  |
| hexiom                           | 4.85 ms                                                | 8.02 ms: 1.65x slower                                                 |
| asyncio_websockets               | 241 ms                                                 | 406 ms: 1.68x slower                                                  |
| richards_super                   | 39.1 ms                                                | 66.5 ms: 1.70x slower                                                 |
| float                            | 56.2 ms                                                | 96.6 ms: 1.72x slower                                                 |
| logging_simple                   | 3.57 us                                                | 6.16 us: 1.72x slower                                                 |
| go                               | 115 ms                                                 | 200 ms: 1.74x slower                                                  |
| logging_format                   | 3.85 us                                                | 6.72 us: 1.74x slower                                                 |
| mako                             | 7.68 ms                                                | 13.4 ms: 1.74x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 444 ms: 1.80x slower                                                  |
| chaos                            | 41.3 ms                                                | 76.5 ms: 1.85x slower                                                 |
| sympy_sum                        | 75.6 ms                                                | 141 ms: 1.86x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.95 ms: 1.90x slower                                                 |
| logging_silent                   | 69.9 ns                                                | 135 ns: 1.93x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 1.71 ms: 1.99x slower                                                 |
| raytrace                         | 182 ms                                                 | 373 ms: 2.05x slower                                                  |
| scimark_lu                       | 76.5 ms                                                | 159 ms: 2.08x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.76 ms: 2.15x slower                                                 |
| nbody                            | 73.9 ms                                                | 159 ms: 2.15x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.32x slower                                                          |
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.23x
- 99% likely to have a slowdown of 1.20x

# Memory
- memory change: 6.33x