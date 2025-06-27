# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.017x slower
- HPT reliability: 75.27%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 187 ms: 1.04x slower                                                            |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.06x slower                                                          |
| html5lib       | 36.7 ms                                                | 34.3 ms: 1.07x faster                                                           |
| sphinx         | 602 ms                                                 | 618 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 209 ms: 1.38x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 398 ms: 1.28x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 216 ms: 1.24x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 411 ms: 1.24x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 413 ms: 1.21x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 405 ms: 1.18x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 179 ms: 1.18x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.15x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                            |
| async_generators                 | 294 ms                                                 | 274 ms: 1.07x faster                                                            |
| coroutines                       | 20.0 ms                                                | 18.8 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 433 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.05x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 367 ms: 1.02x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 76.5 ms: 1.09x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 3.00x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 57.2 ms: 1.02x slower                                                           |
| nbody          | 73.6 ms                                                | 85.1 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.42 ms: 1.09x faster                                                           |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                            |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.03x faster                                                           |
| regex_compile  | 78.3 ms                                                | 81.4 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.43 sec: 1.09x faster                                                          |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                           |
| xml_etree_generate   | 57.1 ms                                                | 59.0 ms: 1.03x slower                                                           |
| xml_etree_process    | 41.3 ms                                                | 43.5 ms: 1.05x slower                                                           |
| json_dumps           | 6.47 ms                                                | 6.81 ms: 1.05x slower                                                           |
| unpickle_pure_python | 165 us                                                 | 180 us: 1.09x slower                                                            |
| pickle_pure_python   | 215 us                                                 | 243 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.7 ms: 1.06x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.2 ms: 1.07x slower                                                           |
| genshi_xml      | 34.1 ms                                                | 36.6 ms: 1.07x slower                                                           |
| mako            | 7.75 ms                                                | 9.33 ms: 1.20x slower                                                           |
| django_template | 20.5 ms                                                | 25.3 ms: 1.23x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 823 ms: 1.82x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 209 ms: 1.38x faster                                                            |
| deepcopy                         | 236 us                                                 | 177 us: 1.34x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 398 ms: 1.28x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 22.0 us: 1.24x faster                                                           |
| async_tree_memoization           | 268 ms                                                 | 216 ms: 1.24x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 411 ms: 1.24x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 413 ms: 1.21x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 405 ms: 1.18x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 179 ms: 1.18x faster                                                            |
| go                               | 117 ms                                                 | 99.7 ms: 1.17x faster                                                           |
| scimark_sor                      | 106 ms                                                 | 90.4 ms: 1.17x faster                                                           |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.15x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.91 us: 1.09x faster                                                           |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.09x faster                                                          |
| tomli_loads                      | 1.57 sec                                               | 1.43 sec: 1.09x faster                                                          |
| regex_effbot                     | 2.63 ms                                                | 2.42 ms: 1.09x faster                                                           |
| async_generators                 | 294 ms                                                 | 274 ms: 1.07x faster                                                            |
| html5lib                         | 36.7 ms                                                | 34.3 ms: 1.07x faster                                                           |
| coroutines                       | 20.0 ms                                                | 18.8 ms: 1.07x faster                                                           |
| python_startup                   | 18.8 ms                                                | 17.7 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 433 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.05x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 72.5 ms: 1.05x faster                                                           |
| connected_components             | 319 ms                                                 | 305 ms: 1.05x faster                                                            |
| dulwich_log                      | 28.7 ms                                                | 27.5 ms: 1.05x faster                                                           |
| shortest_path                    | 345 ms                                                 | 332 ms: 1.04x faster                                                            |
| pyflate                          | 352 ms                                                 | 339 ms: 1.04x faster                                                            |
| python_startup_no_site           | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| json                             | 3.04 ms                                                | 2.95 ms: 1.03x faster                                                           |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                           |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                            |
| pathlib                          | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                           |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.03x faster                                                           |
| telco                            | 4.84 ms                                                | 4.73 ms: 1.02x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 367 ms: 1.02x faster                                                            |
| generators                       | 31.9 ms                                                | 31.5 ms: 1.02x faster                                                           |
| bpe_tokeniser                    | 3.26 sec                                               | 3.27 sec: 1.00x slower                                                          |
| thrift                           | 466 us                                                 | 472 us: 1.01x slower                                                            |
| scimark_fft                      | 200 ms                                                 | 203 ms: 1.02x slower                                                            |
| meteor_contest                   | 74.0 ms                                                | 75.3 ms: 1.02x slower                                                           |
| float                            | 55.8 ms                                                | 57.2 ms: 1.02x slower                                                           |
| sphinx                           | 602 ms                                                 | 618 ms: 1.03x slower                                                            |
| xml_etree_generate               | 57.1 ms                                                | 59.0 ms: 1.03x slower                                                           |
| deltablue                        | 2.65 ms                                                | 2.73 ms: 1.03x slower                                                           |
| regex_compile                    | 78.3 ms                                                | 81.4 ms: 1.04x slower                                                           |
| richards                         | 36.2 ms                                                | 37.7 ms: 1.04x slower                                                           |
| 2to3                             | 179 ms                                                 | 187 ms: 1.04x slower                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.63 us: 1.05x slower                                                           |
| xml_etree_process                | 41.3 ms                                                | 43.5 ms: 1.05x slower                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 53.1 ms: 1.05x slower                                                           |
| typing_runtime_protocols         | 101 us                                                 | 106 us: 1.05x slower                                                            |
| json_dumps                       | 6.47 ms                                                | 6.81 ms: 1.05x slower                                                           |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.06x slower                                                          |
| hexiom                           | 4.87 ms                                                | 5.14 ms: 1.06x slower                                                           |
| richards_super                   | 39.2 ms                                                | 41.5 ms: 1.06x slower                                                           |
| fannkuch                         | 279 ms                                                 | 296 ms: 1.06x slower                                                            |
| pycparser                        | 701 ms                                                 | 744 ms: 1.06x slower                                                            |
| coverage                         | 46.2 ms                                                | 49.1 ms: 1.06x slower                                                           |
| sympy_expand                     | 248 ms                                                 | 263 ms: 1.06x slower                                                            |
| sympy_str                        | 146 ms                                                 | 155 ms: 1.07x slower                                                            |
| genshi_text                      | 16.9 ms                                                | 18.2 ms: 1.07x slower                                                           |
| genshi_xml                       | 34.1 ms                                                | 36.6 ms: 1.07x slower                                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.22 ms: 1.08x slower                                                           |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                           |
| unpickle_pure_python             | 165 us                                                 | 180 us: 1.09x slower                                                            |
| async_tree_eager                 | 69.9 ms                                                | 76.5 ms: 1.09x slower                                                           |
| sympy_sum                        | 75.1 ms                                                | 82.1 ms: 1.09x slower                                                           |
| crypto_pyaes                     | 55.3 ms                                                | 61.3 ms: 1.11x slower                                                           |
| comprehensions                   | 12.0 us                                                | 13.3 us: 1.11x slower                                                           |
| chaos                            | 41.1 ms                                                | 46.1 ms: 1.12x slower                                                           |
| scimark_lu                       | 75.9 ms                                                | 85.3 ms: 1.12x slower                                                           |
| pickle_pure_python               | 215 us                                                 | 243 us: 1.13x slower                                                            |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                            |
| nqueens                          | 61.8 ms                                                | 71.3 ms: 1.15x slower                                                           |
| nbody                            | 73.6 ms                                                | 85.1 ms: 1.16x slower                                                           |
| pprint_pformat                   | 1.10 sec                                               | 1.28 sec: 1.16x slower                                                          |
| pprint_safe_repr                 | 541 ms                                                 | 629 ms: 1.16x slower                                                            |
| raytrace                         | 181 ms                                                 | 211 ms: 1.17x slower                                                            |
| logging_format                   | 3.85 us                                                | 4.53 us: 1.18x slower                                                           |
| logging_simple                   | 3.56 us                                                | 4.22 us: 1.19x slower                                                           |
| mako                             | 7.75 ms                                                | 9.33 ms: 1.20x slower                                                           |
| many_optionals                   | 409 us                                                 | 503 us: 1.23x slower                                                            |
| django_template                  | 20.5 ms                                                | 25.3 ms: 1.23x slower                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                            |
| subparsers                       | 9.44 ms                                                | 15.1 ms: 1.60x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 3.00x slower                                                            |
| logging_silent                   | 71.0 ns                                                | 346 ns: 4.88x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                                    |

Benchmark hidden because not significant (6): pylint, dask, xml_etree_iterparse, asyncio_websockets, pidigits, sympy_integrate
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 75.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x