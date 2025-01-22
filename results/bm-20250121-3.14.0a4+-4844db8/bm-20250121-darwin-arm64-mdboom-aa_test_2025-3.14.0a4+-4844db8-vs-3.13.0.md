# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: darwin-arm64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 197 ms: 1.10x slower                                           |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.05x slower                                         |
| html5lib       | 36.7 ms                                                | 31.2 ms: 1.17x faster                                          |
| sphinx         | 602 ms                                                 | 582 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 191 ms: 1.51x faster                                           |
| async_tree_eager_io              | 511 ms                                                 | 377 ms: 1.36x faster                                           |
| async_tree_io_tg                 | 500 ms                                                 | 373 ms: 1.34x faster                                           |
| async_tree_io                    | 508 ms                                                 | 379 ms: 1.34x faster                                           |
| async_tree_memoization           | 268 ms                                                 | 201 ms: 1.33x faster                                           |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.33x faster                                           |
| async_tree_none_tg               | 198 ms                                                 | 153 ms: 1.29x faster                                           |
| coroutines                       | 20.0 ms                                                | 16.0 ms: 1.25x faster                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 389 ms: 1.23x faster                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                           |
| async_generators                 | 294 ms                                                 | 250 ms: 1.18x faster                                           |
| async_tree_eager                 | 69.9 ms                                                | 61.4 ms: 1.14x faster                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 416 ms: 1.10x faster                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 410 ms: 1.09x faster                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 126 ms: 2.67x slower                                           |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.6 ms: 1.15x faster                                          |
| nbody          | 73.6 ms                                                | 68.6 ms: 1.07x faster                                          |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 67.0 ms: 1.17x faster                                          |
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                          |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                           |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.20 sec: 1.30x faster                                         |
| unpickle_pure_python | 165 us                                                 | 147 us: 1.12x faster                                           |
| pickle_pure_python   | 215 us                                                 | 197 us: 1.09x faster                                           |
| xml_etree_generate   | 57.1 ms                                                | 53.4 ms: 1.07x faster                                          |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                           |
| xml_etree_iterparse  | 74.2 ms                                                | 71.1 ms: 1.04x faster                                          |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                          |
| xml_etree_process    | 41.3 ms                                                | 41.1 ms: 1.00x faster                                          |
| json_dumps           | 6.47 ms                                                | 7.49 ms: 1.16x slower                                          |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.7 ms: 1.01x faster                                          |
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 28.8 ms: 1.18x faster                                          |
| genshi_text     | 16.9 ms                                                | 14.5 ms: 1.16x faster                                          |
| mako            | 7.75 ms                                                | 7.19 ms: 1.08x faster                                          |
| django_template | 20.5 ms                                                | 21.3 ms: 1.04x slower                                          |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 148 us: 1.59x faster                                           |
| deepcopy_memo                    | 27.4 us                                                | 18.0 us: 1.52x faster                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 191 ms: 1.51x faster                                           |
| generators                       | 31.9 ms                                                | 22.5 ms: 1.42x faster                                          |
| async_tree_eager_io              | 511 ms                                                 | 377 ms: 1.36x faster                                           |
| async_tree_io_tg                 | 500 ms                                                 | 373 ms: 1.34x faster                                           |
| async_tree_io                    | 508 ms                                                 | 379 ms: 1.34x faster                                           |
| deepcopy_reduce                  | 2.09 us                                                | 1.57 us: 1.34x faster                                          |
| async_tree_memoization           | 268 ms                                                 | 201 ms: 1.33x faster                                           |
| go                               | 117 ms                                                 | 87.8 ms: 1.33x faster                                          |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.33x faster                                           |
| tomli_loads                      | 1.57 sec                                               | 1.20 sec: 1.30x faster                                         |
| async_tree_none_tg               | 198 ms                                                 | 153 ms: 1.29x faster                                           |
| spectral_norm                    | 76.5 ms                                                | 60.7 ms: 1.26x faster                                          |
| coroutines                       | 20.0 ms                                                | 16.0 ms: 1.25x faster                                          |
| scimark_sor                      | 106 ms                                                 | 85.6 ms: 1.23x faster                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 389 ms: 1.23x faster                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                           |
| pprint_pformat                   | 1.10 sec                                               | 929 ms: 1.18x faster                                           |
| genshi_xml                       | 34.1 ms                                                | 28.8 ms: 1.18x faster                                          |
| async_generators                 | 294 ms                                                 | 250 ms: 1.18x faster                                           |
| html5lib                         | 36.7 ms                                                | 31.2 ms: 1.17x faster                                          |
| pyflate                          | 352 ms                                                 | 300 ms: 1.17x faster                                           |
| regex_compile                    | 78.3 ms                                                | 67.0 ms: 1.17x faster                                          |
| pprint_safe_repr                 | 541 ms                                                 | 464 ms: 1.17x faster                                           |
| genshi_text                      | 16.9 ms                                                | 14.5 ms: 1.16x faster                                          |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                          |
| scimark_fft                      | 200 ms                                                 | 173 ms: 1.15x faster                                           |
| float                            | 55.8 ms                                                | 48.6 ms: 1.15x faster                                          |
| hexiom                           | 4.87 ms                                                | 4.25 ms: 1.15x faster                                          |
| async_tree_eager                 | 69.9 ms                                                | 61.4 ms: 1.14x faster                                          |
| fannkuch                         | 279 ms                                                 | 247 ms: 1.13x faster                                           |
| unpickle_pure_python             | 165 us                                                 | 147 us: 1.12x faster                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.69 ms: 1.11x faster                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 416 ms: 1.10x faster                                           |
| pylint                           | 180 ms                                                 | 163 ms: 1.10x faster                                           |
| bpe_tokeniser                    | 3.26 sec                                               | 2.95 sec: 1.10x faster                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 410 ms: 1.09x faster                                           |
| pickle_pure_python               | 215 us                                                 | 197 us: 1.09x faster                                           |
| mako                             | 7.75 ms                                                | 7.19 ms: 1.08x faster                                          |
| connected_components             | 319 ms                                                 | 296 ms: 1.08x faster                                           |
| bench_mp_pool                    | 64.7 ms                                                | 60.2 ms: 1.08x faster                                          |
| pycparser                        | 701 ms                                                 | 653 ms: 1.07x faster                                           |
| nbody                            | 73.6 ms                                                | 68.6 ms: 1.07x faster                                          |
| nqueens                          | 61.8 ms                                                | 57.7 ms: 1.07x faster                                          |
| telco                            | 4.84 ms                                                | 4.52 ms: 1.07x faster                                          |
| xml_etree_generate               | 57.1 ms                                                | 53.4 ms: 1.07x faster                                          |
| shortest_path                    | 345 ms                                                 | 324 ms: 1.07x faster                                           |
| logging_format                   | 3.85 us                                                | 3.61 us: 1.07x faster                                          |
| k_core                           | 1.61 sec                                               | 1.51 sec: 1.06x faster                                         |
| logging_simple                   | 3.56 us                                                | 3.35 us: 1.06x faster                                          |
| json                             | 3.04 ms                                                | 2.87 ms: 1.06x faster                                          |
| richards                         | 36.2 ms                                                | 34.2 ms: 1.06x faster                                          |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                           |
| sympy_expand                     | 248 ms                                                 | 235 ms: 1.05x faster                                           |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                           |
| sympy_str                        | 146 ms                                                 | 139 ms: 1.05x faster                                           |
| sqlglot_optimize                 | 34.7 ms                                                | 33.1 ms: 1.05x faster                                          |
| scimark_lu                       | 75.9 ms                                                | 72.5 ms: 1.05x faster                                          |
| dulwich_log                      | 28.7 ms                                                | 27.5 ms: 1.04x faster                                          |
| xml_etree_iterparse              | 74.2 ms                                                | 71.1 ms: 1.04x faster                                          |
| sqlglot_normalize                | 188 ms                                                 | 180 ms: 1.04x faster                                           |
| chaos                            | 41.1 ms                                                | 39.4 ms: 1.04x faster                                          |
| crypto_pyaes                     | 55.3 ms                                                | 53.1 ms: 1.04x faster                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                           |
| typing_runtime_protocols         | 101 us                                                 | 96.9 us: 1.04x faster                                          |
| bench_thread_pool                | 503 us                                                 | 486 us: 1.04x faster                                           |
| sphinx                           | 602 ms                                                 | 582 ms: 1.03x faster                                           |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                          |
| richards_super                   | 39.2 ms                                                | 38.0 ms: 1.03x faster                                          |
| meteor_contest                   | 74.0 ms                                                | 71.7 ms: 1.03x faster                                          |
| sqlglot_transpile                | 1.04 ms                                                | 1.01 ms: 1.03x faster                                          |
| thrift                           | 466 us                                                 | 457 us: 1.02x faster                                           |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                          |
| scimark_monte_carlo              | 50.4 ms                                                | 49.8 ms: 1.01x faster                                          |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                          |
| sympy_sum                        | 75.1 ms                                                | 74.3 ms: 1.01x faster                                          |
| sqlglot_parse                    | 852 us                                                 | 845 us: 1.01x faster                                           |
| coverage                         | 46.2 ms                                                | 46.0 ms: 1.01x faster                                          |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.01x faster                                          |
| python_startup                   | 18.8 ms                                                | 18.7 ms: 1.01x faster                                          |
| xml_etree_process                | 41.3 ms                                                | 41.1 ms: 1.00x faster                                          |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                           |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.74 ms: 1.01x slower                                          |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.01x slower                                          |
| mdp                              | 1.50 sec                                               | 1.52 sec: 1.02x slower                                         |
| deltablue                        | 2.65 ms                                                | 2.70 ms: 1.02x slower                                          |
| sqlalchemy_declarative           | 59.0 ms                                                | 60.8 ms: 1.03x slower                                          |
| django_template                  | 20.5 ms                                                | 21.3 ms: 1.04x slower                                          |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.05x slower                                         |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.06x slower                                          |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.07x slower                                          |
| comprehensions                   | 12.0 us                                                | 12.9 us: 1.07x slower                                          |
| many_optionals                   | 409 us                                                 | 444 us: 1.09x slower                                           |
| logging_silent                   | 71.0 ns                                                | 77.7 ns: 1.10x slower                                          |
| 2to3                             | 179 ms                                                 | 197 ms: 1.10x slower                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                           |
| raytrace                         | 181 ms                                                 | 204 ms: 1.12x slower                                           |
| json_dumps                       | 6.47 ms                                                | 7.49 ms: 1.16x slower                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                           |
| subparsers                       | 9.44 ms                                                | 12.3 ms: 1.30x slower                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 126 ms: 2.67x slower                                           |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                   |

Benchmark hidden because not significant (3): pathlib, asyncio_websockets, dask
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x