# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.070x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 202 ms: 1.13x slower                                                   |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                 |
| sphinx         | 602 ms                                                 | 636 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 200 ms: 1.44x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 351 ms: 1.42x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 336 ms: 1.42x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.41x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 374 ms: 1.36x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 164 ms: 1.21x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 228 ms: 1.18x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 182 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 406 ms: 1.10x faster                                                   |
| coroutines                       | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 435 ms: 1.06x faster                                                   |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 383 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 385 ms: 1.11x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 93.3 ms: 1.33x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 135 ms: 2.86x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| float          | 55.8 ms                                                | 56.2 ms: 1.01x slower                                                  |
| nbody          | 73.6 ms                                                | 106 ms: 1.43x slower                                                   |
| Geometric mean | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.16 ms: 1.22x faster                                                  |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.1 ms: 1.06x faster                                                  |
| regex_compile  | 78.3 ms                                                | 92.9 ms: 1.19x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 96.7 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 67.4 ms: 1.10x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 60.9 ms: 1.07x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 45.9 ms: 1.11x slower                                                  |
| json_loads           | 17.0 us                                                | 19.1 us: 1.12x slower                                                  |
| unpickle_pure_python | 165 us                                                 | 189 us: 1.14x slower                                                   |
| json_dumps           | 6.47 ms                                                | 7.98 ms: 1.23x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 270 us: 1.26x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 20.5 ms: 1.09x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 15.8 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 39.2 ms: 1.15x slower                                                  |
| genshi_text     | 16.9 ms                                                | 20.1 ms: 1.19x slower                                                  |
| django_template | 20.5 ms                                                | 27.1 ms: 1.32x slower                                                  |
| mako            | 7.75 ms                                                | 11.0 ms: 1.41x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.26x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.40 ms: 2.10x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 764 us: 1.56x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 200 ms: 1.44x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 351 ms: 1.42x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 336 ms: 1.42x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.41x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 374 ms: 1.36x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.16 ms: 1.22x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 164 ms: 1.21x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.32 us: 1.18x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 228 ms: 1.18x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 182 ms: 1.16x faster                                                   |
| deepcopy                         | 236 us                                                 | 204 us: 1.16x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 96.7 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 406 ms: 1.10x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 67.4 ms: 1.10x faster                                                  |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                   |
| coroutines                       | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.1 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 435 ms: 1.06x faster                                                   |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| go                               | 117 ms                                                 | 115 ms: 1.02x faster                                                   |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| float                            | 55.8 ms                                                | 56.2 ms: 1.01x slower                                                  |
| scimark_sor                      | 106 ms                                                 | 107 ms: 1.01x slower                                                   |
| pathlib                          | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 2.12 us: 1.01x slower                                                  |
| pycparser                        | 701 ms                                                 | 716 ms: 1.02x slower                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 3.33 sec: 1.02x slower                                                 |
| generators                       | 31.9 ms                                                | 32.8 ms: 1.03x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 383 ms: 1.03x slower                                                   |
| json                             | 3.04 ms                                                | 3.16 ms: 1.04x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                 |
| pyflate                          | 352 ms                                                 | 369 ms: 1.05x slower                                                   |
| k_core                           | 1.61 sec                                               | 1.69 sec: 1.05x slower                                                 |
| deepcopy_memo                    | 27.4 us                                                | 28.8 us: 1.05x slower                                                  |
| sphinx                           | 602 ms                                                 | 636 ms: 1.06x slower                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                 |
| telco                            | 4.84 ms                                                | 5.15 ms: 1.06x slower                                                  |
| connected_components             | 319 ms                                                 | 340 ms: 1.07x slower                                                   |
| xml_etree_generate               | 57.1 ms                                                | 60.9 ms: 1.07x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 82.1 ms: 1.07x slower                                                  |
| shortest_path                    | 345 ms                                                 | 371 ms: 1.07x slower                                                   |
| python_startup                   | 18.8 ms                                                | 20.5 ms: 1.09x slower                                                  |
| dulwich_log                      | 28.7 ms                                                | 31.7 ms: 1.10x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.66 sec: 1.11x slower                                                 |
| sqlglot_optimize                 | 34.7 ms                                                | 38.5 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 385 ms: 1.11x slower                                                   |
| xml_etree_process                | 41.3 ms                                                | 45.9 ms: 1.11x slower                                                  |
| sqlglot_normalize                | 188 ms                                                 | 210 ms: 1.12x slower                                                   |
| json_loads                       | 17.0 us                                                | 19.1 us: 1.12x slower                                                  |
| thrift                           | 466 us                                                 | 522 us: 1.12x slower                                                   |
| meteor_contest                   | 74.0 ms                                                | 83.5 ms: 1.13x slower                                                  |
| 2to3                             | 179 ms                                                 | 202 ms: 1.13x slower                                                   |
| unpickle_pure_python             | 165 us                                                 | 189 us: 1.14x slower                                                   |
| nqueens                          | 61.8 ms                                                | 71.0 ms: 1.15x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 285 ms: 1.15x slower                                                   |
| python_startup_no_site           | 13.7 ms                                                | 15.8 ms: 1.15x slower                                                  |
| genshi_xml                       | 34.1 ms                                                | 39.2 ms: 1.15x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 87.0 ms: 1.16x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 232 ms: 1.16x slower                                                   |
| richards                         | 36.2 ms                                                | 42.0 ms: 1.16x slower                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 1.21 ms: 1.17x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.29 sec: 1.17x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 632 ms: 1.17x slower                                                   |
| sympy_str                        | 146 ms                                                 | 171 ms: 1.17x slower                                                   |
| fannkuch                         | 279 ms                                                 | 329 ms: 1.18x slower                                                   |
| coverage                         | 46.2 ms                                                | 54.7 ms: 1.18x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.93 ms: 1.19x slower                                                  |
| regex_compile                    | 78.3 ms                                                | 92.9 ms: 1.19x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 20.1 ms: 1.19x slower                                                  |
| logging_simple                   | 3.56 us                                                | 4.25 us: 1.20x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 70.6 ms: 1.20x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 66.3 ms: 1.20x slower                                                  |
| richards_super                   | 39.2 ms                                                | 47.3 ms: 1.21x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 13.8 ms: 1.22x slower                                                  |
| many_optionals                   | 409 us                                                 | 499 us: 1.22x slower                                                   |
| logging_format                   | 3.85 us                                                | 4.72 us: 1.23x slower                                                  |
| comprehensions                   | 12.0 us                                                | 14.7 us: 1.23x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 87.3 ns: 1.23x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.98 ms: 1.23x slower                                                  |
| hexiom                           | 4.87 ms                                                | 6.02 ms: 1.24x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 62.5 ms: 1.24x slower                                                  |
| sqlglot_parse                    | 852 us                                                 | 1.06 ms: 1.24x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 126 us: 1.25x slower                                                   |
| pickle_pure_python               | 215 us                                                 | 270 us: 1.26x slower                                                   |
| chaos                            | 41.1 ms                                                | 53.4 ms: 1.30x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 98.8 ms: 1.30x slower                                                  |
| deltablue                        | 2.65 ms                                                | 3.46 ms: 1.31x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.92 ms: 1.32x slower                                                  |
| django_template                  | 20.5 ms                                                | 27.1 ms: 1.32x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 93.3 ms: 1.33x slower                                                  |
| raytrace                         | 181 ms                                                 | 243 ms: 1.34x slower                                                   |
| mako                             | 7.75 ms                                                | 11.0 ms: 1.41x slower                                                  |
| nbody                            | 73.6 ms                                                | 106 ms: 1.43x slower                                                   |
| subparsers                       | 9.44 ms                                                | 14.1 ms: 1.49x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 802 us: 1.59x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 135 ms: 2.86x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                           |

Benchmark hidden because not significant (4): pylint, html5lib, async_tree_eager_memoization, bench_mp_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.070x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.21x