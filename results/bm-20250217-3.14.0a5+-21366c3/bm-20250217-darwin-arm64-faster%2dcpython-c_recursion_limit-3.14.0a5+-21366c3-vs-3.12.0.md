# Results vs. 3.12.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: darwin-arm64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.015x slower
- HPT reliability: 99.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 205 ms: 1.21x slower                                                          |
| docutils       | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                        |
| html5lib       | 33.4 ms                                                | 32.9 ms: 1.01x faster                                                         |
| sphinx         | 613 ms                                                 | 608 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 404 ms: 1.67x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 409 ms: 1.63x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 424 ms: 1.58x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 405 ms: 1.52x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 215 ms: 1.48x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 173 ms: 1.48x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 184 ms: 1.43x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 221 ms: 1.40x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 431 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.20x faster                                                          |
| async_generators                 | 299 ms                                                 | 269 ms: 1.11x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                          |
| coroutines                       | 19.7 ms                                                | 18.6 ms: 1.06x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 370 ms: 1.01x faster                                                          |
| async_tree_eager                 | 65.8 ms                                                | 74.2 ms: 1.13x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 190 ms: 1.34x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| nbody          | 67.6 ms                                                | 91.9 ms: 1.36x slower                                                         |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.30 ms: 1.06x faster                                                         |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                          |
| regex_compile  | 75.9 ms                                                | 77.5 ms: 1.02x slower                                                         |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 74.6 ms: 1.01x faster                                                         |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                         |
| xml_etree_generate   | 55.4 ms                                                | 58.4 ms: 1.05x slower                                                         |
| tomli_loads          | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                        |
| xml_etree_process    | 38.9 ms                                                | 43.0 ms: 1.11x slower                                                         |
| unpickle_pure_python | 145 us                                                 | 170 us: 1.17x slower                                                          |
| pickle_pure_python   | 197 us                                                 | 232 us: 1.18x slower                                                          |
| json_dumps           | 6.19 ms                                                | 7.53 ms: 1.22x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.4 ms: 1.01x slower                                                         |
| python_startup         | 17.8 ms                                                | 18.1 ms: 1.02x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 8.18 ms: 1.10x slower                                                         |
| genshi_xml      | 30.5 ms                                                | 33.8 ms: 1.11x slower                                                         |
| genshi_text     | 14.7 ms                                                | 16.3 ms: 1.11x slower                                                         |
| django_template | 19.7 ms                                                | 24.1 ms: 1.22x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-darwin-arm64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.9 ms: 2.50x faster                                                         |
| async_tree_io_tg                 | 673 ms                                                 | 404 ms: 1.67x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 409 ms: 1.63x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 424 ms: 1.58x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 405 ms: 1.52x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 215 ms: 1.48x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 173 ms: 1.48x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 184 ms: 1.43x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 221 ms: 1.40x faster                                                          |
| deepcopy                         | 226 us                                                 | 167 us: 1.36x faster                                                          |
| deepcopy_memo                    | 26.0 us                                                | 20.9 us: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 431 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.20x faster                                                          |
| deepcopy_reduce                  | 2.01 us                                                | 1.76 us: 1.14x faster                                                         |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                        |
| async_generators                 | 299 ms                                                 | 269 ms: 1.11x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                          |
| bench_mp_pool                    | 65.5 ms                                                | 59.7 ms: 1.10x faster                                                         |
| comprehensions                   | 14.0 us                                                | 13.0 us: 1.08x faster                                                         |
| pylint                           | 182 ms                                                 | 170 ms: 1.07x faster                                                          |
| pathlib                          | 24.7 ms                                                | 23.2 ms: 1.06x faster                                                         |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                          |
| regex_effbot                     | 2.44 ms                                                | 2.30 ms: 1.06x faster                                                         |
| coroutines                       | 19.7 ms                                                | 18.6 ms: 1.06x faster                                                         |
| go                               | 98.5 ms                                                | 94.6 ms: 1.04x faster                                                         |
| bpe_tokeniser                    | 3.28 sec                                               | 3.20 sec: 1.02x faster                                                        |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.08 ms: 1.02x faster                                                         |
| html5lib                         | 33.4 ms                                                | 32.9 ms: 1.01x faster                                                         |
| xml_etree_iterparse              | 75.5 ms                                                | 74.6 ms: 1.01x faster                                                         |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 370 ms: 1.01x faster                                                          |
| sphinx                           | 613 ms                                                 | 608 ms: 1.01x faster                                                          |
| generators                       | 29.4 ms                                                | 29.1 ms: 1.01x faster                                                         |
| thrift                           | 468 us                                                 | 465 us: 1.01x faster                                                          |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| sqlalchemy_declarative           | 61.9 ms                                                | 62.5 ms: 1.01x slower                                                         |
| logging_silent                   | 72.5 ns                                                | 73.4 ns: 1.01x slower                                                         |
| python_startup_no_site           | 13.2 ms                                                | 13.4 ms: 1.01x slower                                                         |
| spectral_norm                    | 76.5 ms                                                | 77.9 ms: 1.02x slower                                                         |
| scimark_fft                      | 194 ms                                                 | 198 ms: 1.02x slower                                                          |
| regex_compile                    | 75.9 ms                                                | 77.5 ms: 1.02x slower                                                         |
| python_startup                   | 17.8 ms                                                | 18.1 ms: 1.02x slower                                                         |
| dulwich_log                      | 29.2 ms                                                | 30.0 ms: 1.03x slower                                                         |
| shortest_path                    | 331 ms                                                 | 343 ms: 1.04x slower                                                          |
| docutils                         | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                        |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                          |
| logging_simple                   | 3.60 us                                                | 3.75 us: 1.04x slower                                                         |
| logging_format                   | 3.90 us                                                | 4.07 us: 1.04x slower                                                         |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                        |
| pycparser                        | 673 ms                                                 | 703 ms: 1.04x slower                                                          |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                         |
| sympy_sum                        | 76.2 ms                                                | 80.1 ms: 1.05x slower                                                         |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.05x slower                                                         |
| xml_etree_generate               | 55.4 ms                                                | 58.4 ms: 1.05x slower                                                         |
| connected_components             | 300 ms                                                 | 316 ms: 1.06x slower                                                          |
| tomli_loads                      | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                        |
| chaos                            | 41.6 ms                                                | 44.5 ms: 1.07x slower                                                         |
| sqlglot_optimize                 | 33.2 ms                                                | 35.6 ms: 1.07x slower                                                         |
| sympy_str                        | 144 ms                                                 | 154 ms: 1.07x slower                                                          |
| deltablue                        | 2.57 ms                                                | 2.76 ms: 1.08x slower                                                         |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.10 ms: 1.08x slower                                                         |
| scimark_sor                      | 85.8 ms                                                | 92.7 ms: 1.08x slower                                                         |
| bench_thread_pool                | 483 us                                                 | 522 us: 1.08x slower                                                          |
| sympy_expand                     | 233 ms                                                 | 255 ms: 1.09x slower                                                          |
| sqlglot_normalize                | 180 ms                                                 | 196 ms: 1.09x slower                                                          |
| sqlglot_parse                    | 808 us                                                 | 888 us: 1.10x slower                                                          |
| mako                             | 7.44 ms                                                | 8.18 ms: 1.10x slower                                                         |
| nqueens                          | 59.5 ms                                                | 65.7 ms: 1.10x slower                                                         |
| typing_runtime_protocols         | 91.5 us                                                | 101 us: 1.10x slower                                                          |
| sqlglot_transpile                | 973 us                                                 | 1.08 ms: 1.11x slower                                                         |
| xml_etree_process                | 38.9 ms                                                | 43.0 ms: 1.11x slower                                                         |
| sympy_integrate                  | 11.1 ms                                                | 12.3 ms: 1.11x slower                                                         |
| genshi_xml                       | 30.5 ms                                                | 33.8 ms: 1.11x slower                                                         |
| genshi_text                      | 14.7 ms                                                | 16.3 ms: 1.11x slower                                                         |
| pprint_pformat                   | 986 ms                                                 | 1.10 sec: 1.12x slower                                                        |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                         |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                         |
| pprint_safe_repr                 | 483 ms                                                 | 542 ms: 1.12x slower                                                          |
| scimark_monte_carlo              | 44.5 ms                                                | 50.1 ms: 1.13x slower                                                         |
| async_tree_eager                 | 65.8 ms                                                | 74.2 ms: 1.13x slower                                                         |
| meteor_contest                   | 69.1 ms                                                | 78.0 ms: 1.13x slower                                                         |
| pyflate                          | 311 ms                                                 | 351 ms: 1.13x slower                                                          |
| scimark_lu                       | 73.5 ms                                                | 83.4 ms: 1.14x slower                                                         |
| crypto_pyaes                     | 51.4 ms                                                | 58.6 ms: 1.14x slower                                                         |
| many_optionals                   | 403 us                                                 | 468 us: 1.16x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| unpickle_pure_python             | 145 us                                                 | 170 us: 1.17x slower                                                          |
| fannkuch                         | 250 ms                                                 | 294 ms: 1.18x slower                                                          |
| pickle_pure_python               | 197 us                                                 | 232 us: 1.18x slower                                                          |
| hexiom                           | 4.38 ms                                                | 5.26 ms: 1.20x slower                                                         |
| 2to3                             | 168 ms                                                 | 205 ms: 1.21x slower                                                          |
| json_dumps                       | 6.19 ms                                                | 7.53 ms: 1.22x slower                                                         |
| telco                            | 3.92 ms                                                | 4.78 ms: 1.22x slower                                                         |
| django_template                  | 19.7 ms                                                | 24.1 ms: 1.22x slower                                                         |
| richards_super                   | 34.6 ms                                                | 42.7 ms: 1.23x slower                                                         |
| coverage                         | 38.5 ms                                                | 47.6 ms: 1.24x slower                                                         |
| richards                         | 30.6 ms                                                | 39.8 ms: 1.30x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 190 ms: 1.34x slower                                                          |
| nbody                            | 67.6 ms                                                | 91.9 ms: 1.36x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                                  |

Benchmark hidden because not significant (4): asyncio_websockets, sqlite_synth, json, float
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 99.30% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x