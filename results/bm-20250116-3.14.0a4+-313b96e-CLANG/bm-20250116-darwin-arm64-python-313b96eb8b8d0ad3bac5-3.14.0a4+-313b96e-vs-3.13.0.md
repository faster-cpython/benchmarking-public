# Results vs. 3.13.0

- fork: python
- ref: 313b96eb8b8d0ad3bac5
- machine: darwin-arm64
- commit hash: 313b96e
- commit date: 2025-01-16
- overall geometric mean: 1.051x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 169 ms: 1.06x faster                                                   |
| html5lib       | 36.7 ms                                                | 32.9 ms: 1.11x faster                                                  |
| sphinx         | 602 ms                                                 | 577 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 365 ms: 1.37x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 373 ms: 1.37x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 379 ms: 1.34x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 209 ms: 1.28x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 158 ms: 1.26x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.24x faster                                                   |
| coroutines                       | 20.0 ms                                                | 16.9 ms: 1.18x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.15x faster                                                   |
| async_generators                 | 294 ms                                                 | 266 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 422 ms: 1.09x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 69.6 ms: 1.01x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 49.0 ms: 1.03x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.5 ms: 1.08x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 73.6 ms                                                | 83.0 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.05 ms: 1.28x faster                                                  |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                   |
| regex_compile  | 78.3 ms                                                | 77.5 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                  |
| unpickle_pure_python | 165 us                                                 | 160 us: 1.03x faster                                                   |
| xml_etree_generate   | 57.1 ms                                                | 55.5 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.5 ms: 1.02x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 41.1 ms: 1.00x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.59 sec: 1.01x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 220 us: 1.02x slower                                                   |
| json_dumps           | 6.47 ms                                                | 7.41 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 12.2 ms: 1.13x faster                                                  |
| python_startup         | 18.8 ms                                                | 16.7 ms: 1.12x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.8 ms: 1.07x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 33.2 ms: 1.03x faster                                                  |
| mako            | 7.75 ms                                                | 8.07 ms: 1.04x slower                                                  |
| django_template | 20.5 ms                                                | 22.7 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 365 ms: 1.37x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 373 ms: 1.37x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 379 ms: 1.34x faster                                                   |
| deepcopy                         | 236 us                                                 | 177 us: 1.34x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 209 ms: 1.28x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.05 ms: 1.28x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 21.7 us: 1.26x faster                                                  |
| go                               | 117 ms                                                 | 92.6 ms: 1.26x faster                                                  |
| generators                       | 31.9 ms                                                | 25.4 ms: 1.26x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 158 ms: 1.26x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.24x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.76 us: 1.19x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.9 ms: 1.18x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 90.3 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.15x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 67.7 ms: 1.13x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 12.2 ms: 1.13x faster                                                  |
| python_startup                   | 18.8 ms                                                | 16.7 ms: 1.12x faster                                                  |
| html5lib                         | 36.7 ms                                                | 32.9 ms: 1.11x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.39 ms: 1.11x faster                                                  |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 266 ms: 1.10x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 59.2 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 422 ms: 1.09x faster                                                   |
| pyflate                          | 352 ms                                                 | 324 ms: 1.09x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.48 sec: 1.09x faster                                                 |
| richards                         | 36.2 ms                                                | 33.4 ms: 1.08x faster                                                  |
| float                            | 55.8 ms                                                | 51.5 ms: 1.08x faster                                                  |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                   |
| connected_components             | 319 ms                                                 | 297 ms: 1.07x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 15.8 ms: 1.07x faster                                                  |
| json                             | 3.04 ms                                                | 2.85 ms: 1.07x faster                                                  |
| shortest_path                    | 345 ms                                                 | 324 ms: 1.07x faster                                                   |
| richards_super                   | 39.2 ms                                                | 36.9 ms: 1.06x faster                                                  |
| 2to3                             | 179 ms                                                 | 169 ms: 1.06x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 47.7 ms: 1.06x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 52.8 ms: 1.05x faster                                                  |
| sphinx                           | 602 ms                                                 | 577 ms: 1.04x faster                                                   |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.71 us: 1.04x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 192 ms: 1.04x faster                                                   |
| logging_simple                   | 3.56 us                                                | 3.43 us: 1.04x faster                                                  |
| raytrace                         | 181 ms                                                 | 175 ms: 1.04x faster                                                   |
| thrift                           | 466 us                                                 | 450 us: 1.04x faster                                                   |
| coverage                         | 46.2 ms                                                | 44.7 ms: 1.03x faster                                                  |
| telco                            | 4.84 ms                                                | 4.69 ms: 1.03x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 160 us: 1.03x faster                                                   |
| sqlglot_transpile                | 1.04 ms                                                | 1.01 ms: 1.03x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 55.5 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 33.2 ms: 1.03x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 72.5 ms: 1.02x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.76 ms: 1.02x faster                                                  |
| nqueens                          | 61.8 ms                                                | 60.6 ms: 1.02x faster                                                  |
| pathlib                          | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.20 sec: 1.02x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                                  |
| sqlglot_parse                    | 852 us                                                 | 837 us: 1.02x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 74.9 ms: 1.01x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 28.4 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| pycparser                        | 701 ms                                                 | 692 ms: 1.01x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 498 us: 1.01x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 77.5 ms: 1.01x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 246 ms: 1.01x faster                                                   |
| sqlglot_optimize                 | 34.7 ms                                                | 34.4 ms: 1.01x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 69.6 ms: 1.01x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 41.1 ms: 1.00x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 71.3 ns: 1.00x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.11 sec: 1.00x slower                                                 |
| sympy_str                        | 146 ms                                                 | 147 ms: 1.01x slower                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 547 ms: 1.01x slower                                                   |
| mdp                              | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.59 sec: 1.01x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 220 us: 1.02x slower                                                   |
| typing_runtime_protocols         | 101 us                                                 | 104 us: 1.03x slower                                                   |
| sympy_sum                        | 75.1 ms                                                | 77.3 ms: 1.03x slower                                                  |
| chaos                            | 41.1 ms                                                | 42.4 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.08 ms: 1.03x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 49.0 ms: 1.03x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 76.7 ms: 1.04x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.2 ms: 1.04x slower                                                  |
| mako                             | 7.75 ms                                                | 8.07 ms: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.06x slower                                                  |
| comprehensions                   | 12.0 us                                                | 13.1 us: 1.10x slower                                                  |
| django_template                  | 20.5 ms                                                | 22.7 ms: 1.11x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.45 ms: 1.11x slower                                                  |
| nbody                            | 73.6 ms                                                | 83.0 ms: 1.13x slower                                                  |
| fannkuch                         | 279 ms                                                 | 315 ms: 1.13x slower                                                   |
| many_optionals                   | 409 us                                                 | 467 us: 1.14x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.41 ms: 1.15x slower                                                  |
| subparsers                       | 9.44 ms                                                | 12.7 ms: 1.35x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (5): docutils, dask, sqlglot_normalize, sqlite_synth, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x