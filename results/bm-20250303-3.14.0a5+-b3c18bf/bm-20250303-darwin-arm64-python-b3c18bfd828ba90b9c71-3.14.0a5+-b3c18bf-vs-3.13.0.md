# Results vs. 3.13.0

- fork: python
- ref: b3c18bfd828ba90b9c71
- machine: darwin-arm64
- commit hash: b3c18bf
- commit date: 2025-03-03
- overall geometric mean: 1.012x slower
- HPT reliability: 77.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                 |
| html5lib       | 36.7 ms                                                | 33.2 ms: 1.10x faster                                                  |
| sphinx         | 602 ms                                                 | 609 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 212 ms: 1.36x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 395 ms: 1.29x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 401 ms: 1.25x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 414 ms: 1.23x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 406 ms: 1.18x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.15x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 268 ms: 1.09x faster                                                   |
| coroutines                       | 20.0 ms                                                | 18.6 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 435 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 428 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 366 ms: 1.02x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 69.0 ms: 1.01x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 191 ms: 1.38x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.01x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 54.4 ms: 1.03x faster                                                  |
| nbody          | 73.6 ms                                                | 92.1 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.32 ms: 1.13x faster                                                  |
| regex_dna      | 149 ms                                                 | 146 ms: 1.02x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                  |
| regex_compile  | 78.3 ms                                                | 78.1 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 75.1 ms: 1.01x slower                                                  |
| xml_etree_generate   | 57.1 ms                                                | 58.2 ms: 1.02x slower                                                  |
| unpickle_pure_python | 165 us                                                 | 169 us: 1.02x slower                                                   |
| xml_etree_process    | 41.3 ms                                                | 42.8 ms: 1.04x slower                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 230 us: 1.07x slower                                                   |
| json_dumps           | 6.47 ms                                                | 7.49 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.5 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 33.9 ms: 1.01x faster                                                  |
| mako            | 7.75 ms                                                | 8.32 ms: 1.07x slower                                                  |
| django_template | 20.5 ms                                                | 24.2 ms: 1.18x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-darwin-arm64-python-b3c18bfd828ba90b9c71-3.14.0a5+-b3c18bf |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 168 us: 1.40x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 212 ms: 1.36x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 21.0 us: 1.31x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 395 ms: 1.29x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 401 ms: 1.25x faster                                                   |
| go                               | 117 ms                                                 | 94.8 ms: 1.23x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 414 ms: 1.23x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.76 us: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 406 ms: 1.18x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.15x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 92.8 ms: 1.14x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.32 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                   |
| generators                       | 31.9 ms                                                | 28.9 ms: 1.11x faster                                                  |
| html5lib                         | 36.7 ms                                                | 33.2 ms: 1.10x faster                                                  |
| async_generators                 | 294 ms                                                 | 268 ms: 1.09x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.6 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 435 ms: 1.05x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 61.5 ms: 1.05x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.05x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 428 ms: 1.05x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                  |
| float                            | 55.8 ms                                                | 54.4 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 366 ms: 1.02x faster                                                   |
| shortest_path                    | 345 ms                                                 | 339 ms: 1.02x faster                                                   |
| regex_dna                        | 149 ms                                                 | 146 ms: 1.02x faster                                                   |
| connected_components             | 319 ms                                                 | 314 ms: 1.01x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 69.0 ms: 1.01x faster                                                  |
| telco                            | 4.84 ms                                                | 4.79 ms: 1.01x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 49.9 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.24 sec: 1.01x faster                                                 |
| thrift                           | 466 us                                                 | 463 us: 1.01x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 33.9 ms: 1.01x faster                                                  |
| pyflate                          | 352 ms                                                 | 351 ms: 1.00x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 78.1 ms: 1.00x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 545 ms: 1.01x slower                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 75.1 ms: 1.01x slower                                                  |
| sphinx                           | 602 ms                                                 | 609 ms: 1.01x slower                                                   |
| xml_etree_generate               | 57.1 ms                                                | 58.2 ms: 1.02x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 78.1 ms: 1.02x slower                                                  |
| unpickle_pure_python             | 165 us                                                 | 169 us: 1.02x slower                                                   |
| pathlib                          | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 73.1 ns: 1.03x slower                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 35.7 ms: 1.03x slower                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 1.07 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.08 ms: 1.03x slower                                                  |
| coverage                         | 46.2 ms                                                | 47.8 ms: 1.03x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 256 ms: 1.04x slower                                                   |
| xml_etree_process                | 41.3 ms                                                | 42.8 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| deltablue                        | 2.65 ms                                                | 2.75 ms: 1.04x slower                                                  |
| dulwich_log                      | 28.7 ms                                                | 29.9 ms: 1.04x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                 |
| sqlglot_normalize                | 188 ms                                                 | 196 ms: 1.04x slower                                                   |
| python_startup                   | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 524 us: 1.04x slower                                                   |
| mdp                              | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                 |
| sqlglot_parse                    | 852 us                                                 | 891 us: 1.05x slower                                                   |
| fannkuch                         | 279 ms                                                 | 292 ms: 1.05x slower                                                   |
| sympy_str                        | 146 ms                                                 | 153 ms: 1.05x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.08 ms: 1.05x slower                                                  |
| nqueens                          | 61.8 ms                                                | 65.2 ms: 1.05x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.5 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.26 ms: 1.06x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.77 us: 1.06x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.08 us: 1.06x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.09 ms: 1.06x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 62.6 ms: 1.06x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 78.7 ms: 1.06x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 79.9 ms: 1.06x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 59.0 ms: 1.07x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 230 us: 1.07x slower                                                   |
| mako                             | 7.75 ms                                                | 8.32 ms: 1.07x slower                                                  |
| chaos                            | 41.1 ms                                                | 44.1 ms: 1.07x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.28 ms: 1.08x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 12.3 ms: 1.09x slower                                                  |
| comprehensions                   | 12.0 us                                                | 13.1 us: 1.09x slower                                                  |
| richards_super                   | 39.2 ms                                                | 42.9 ms: 1.09x slower                                                  |
| richards                         | 36.2 ms                                                | 40.0 ms: 1.10x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 84.7 ms: 1.12x slower                                                  |
| many_optionals                   | 409 us                                                 | 465 us: 1.14x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.49 ms: 1.16x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                   |
| django_template                  | 20.5 ms                                                | 24.2 ms: 1.18x slower                                                  |
| nbody                            | 73.6 ms                                                | 92.1 ms: 1.25x slower                                                  |
| subparsers                       | 9.44 ms                                                | 12.8 ms: 1.36x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 191 ms: 1.38x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.01x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (10): pylint, typing_runtime_protocols, dask, pprint_pformat, sqlite_synth, pidigits, 2to3, scimark_fft, json, pycparser
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 77.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x