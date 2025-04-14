# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: darwin-arm64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.011x slower
- HPT reliability: 69.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| docutils       | 1.44 sec                                               | 1.51 sec: 1.04x slower                                                           |
| html5lib       | 36.7 ms                                                | 32.6 ms: 1.13x faster                                                            |
| sphinx         | 602 ms                                                 | 614 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 213 ms: 1.35x faster                                                             |
| async_tree_eager_io              | 511 ms                                                 | 395 ms: 1.29x faster                                                             |
| async_tree_io_tg                 | 500 ms                                                 | 395 ms: 1.27x faster                                                             |
| async_tree_memoization           | 268 ms                                                 | 218 ms: 1.23x faster                                                             |
| async_tree_io                    | 508 ms                                                 | 416 ms: 1.22x faster                                                             |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                             |
| async_tree_eager_io_tg           | 479 ms                                                 | 406 ms: 1.18x faster                                                             |
| async_tree_none_tg               | 198 ms                                                 | 170 ms: 1.17x faster                                                             |
| async_generators                 | 294 ms                                                 | 264 ms: 1.11x faster                                                             |
| coroutines                       | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 430 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 428 ms: 1.05x faster                                                             |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 366 ms: 1.02x faster                                                             |
| async_tree_eager                 | 69.9 ms                                                | 70.3 ms: 1.00x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                             |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 191 ms: 1.39x slower                                                             |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.02x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 56.4 ms: 1.01x slower                                                            |
| nbody          | 73.6 ms                                                | 90.5 ms: 1.23x slower                                                            |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.29 ms: 1.15x faster                                                            |
| regex_dna      | 149 ms                                                 | 141 ms: 1.05x faster                                                             |
| regex_v8       | 17.0 ms                                                | 17.0 ms: 1.00x faster                                                            |
| regex_compile  | 78.3 ms                                                | 78.5 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.35 sec: 1.16x faster                                                           |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                             |
| xml_etree_generate   | 57.1 ms                                                | 58.1 ms: 1.02x slower                                                            |
| xml_etree_process    | 41.3 ms                                                | 42.0 ms: 1.02x slower                                                            |
| unpickle_pure_python | 165 us                                                 | 173 us: 1.05x slower                                                             |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                            |
| pickle_pure_python   | 215 us                                                 | 237 us: 1.11x slower                                                             |
| json_dumps           | 6.47 ms                                                | 7.54 ms: 1.17x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                            |
| python_startup_no_site | 13.7 ms                                                | 14.4 ms: 1.05x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                            |
| genshi_xml      | 34.1 ms                                                | 33.5 ms: 1.02x faster                                                            |
| mako            | 7.75 ms                                                | 8.64 ms: 1.11x slower                                                            |
| django_template | 20.5 ms                                                | 23.4 ms: 1.14x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 172 us: 1.37x faster                                                             |
| async_tree_memoization_tg        | 288 ms                                                 | 213 ms: 1.35x faster                                                             |
| async_tree_eager_io              | 511 ms                                                 | 395 ms: 1.29x faster                                                             |
| async_tree_io_tg                 | 500 ms                                                 | 395 ms: 1.27x faster                                                             |
| async_tree_memoization           | 268 ms                                                 | 218 ms: 1.23x faster                                                             |
| async_tree_io                    | 508 ms                                                 | 416 ms: 1.22x faster                                                             |
| deepcopy_memo                    | 27.4 us                                                | 22.7 us: 1.21x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                             |
| deepcopy_reduce                  | 2.09 us                                                | 1.78 us: 1.18x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 406 ms: 1.18x faster                                                             |
| async_tree_none_tg               | 198 ms                                                 | 170 ms: 1.17x faster                                                             |
| tomli_loads                      | 1.57 sec                                               | 1.35 sec: 1.16x faster                                                           |
| go                               | 117 ms                                                 | 101 ms: 1.16x faster                                                             |
| generators                       | 31.9 ms                                                | 27.8 ms: 1.15x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.29 ms: 1.15x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 92.3 ms: 1.14x faster                                                            |
| html5lib                         | 36.7 ms                                                | 32.6 ms: 1.13x faster                                                            |
| async_generators                 | 294 ms                                                 | 264 ms: 1.11x faster                                                             |
| coroutines                       | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 430 ms: 1.07x faster                                                             |
| bench_mp_pool                    | 64.7 ms                                                | 61.3 ms: 1.06x faster                                                            |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.05x faster                                                             |
| spectral_norm                    | 76.5 ms                                                | 72.8 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 428 ms: 1.05x faster                                                             |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                             |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                            |
| pyflate                          | 352 ms                                                 | 340 ms: 1.03x faster                                                             |
| k_core                           | 1.61 sec                                               | 1.57 sec: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 366 ms: 1.02x faster                                                             |
| telco                            | 4.84 ms                                                | 4.75 ms: 1.02x faster                                                            |
| genshi_xml                       | 34.1 ms                                                | 33.5 ms: 1.02x faster                                                            |
| pprint_pformat                   | 1.10 sec                                               | 1.08 sec: 1.02x faster                                                           |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                            |
| shortest_path                    | 345 ms                                                 | 342 ms: 1.01x faster                                                             |
| connected_components             | 319 ms                                                 | 315 ms: 1.01x faster                                                             |
| scimark_monte_carlo              | 50.4 ms                                                | 49.9 ms: 1.01x faster                                                            |
| pprint_safe_repr                 | 541 ms                                                 | 535 ms: 1.01x faster                                                             |
| bpe_tokeniser                    | 3.26 sec                                               | 3.24 sec: 1.00x faster                                                           |
| regex_v8                         | 17.0 ms                                                | 17.0 ms: 1.00x faster                                                            |
| regex_compile                    | 78.3 ms                                                | 78.5 ms: 1.00x slower                                                            |
| async_tree_eager                 | 69.9 ms                                                | 70.3 ms: 1.00x slower                                                            |
| thrift                           | 466 us                                                 | 469 us: 1.01x slower                                                             |
| scimark_fft                      | 200 ms                                                 | 201 ms: 1.01x slower                                                             |
| float                            | 55.8 ms                                                | 56.4 ms: 1.01x slower                                                            |
| coverage                         | 46.2 ms                                                | 47.0 ms: 1.02x slower                                                            |
| xml_etree_generate               | 57.1 ms                                                | 58.1 ms: 1.02x slower                                                            |
| xml_etree_process                | 41.3 ms                                                | 42.0 ms: 1.02x slower                                                            |
| typing_runtime_protocols         | 101 us                                                 | 103 us: 1.02x slower                                                             |
| sphinx                           | 602 ms                                                 | 614 ms: 1.02x slower                                                             |
| richards                         | 36.2 ms                                                | 36.9 ms: 1.02x slower                                                            |
| sqlglot_optimize                 | 34.7 ms                                                | 35.5 ms: 1.02x slower                                                            |
| dulwich_log                      | 28.7 ms                                                | 29.5 ms: 1.03x slower                                                            |
| sympy_expand                     | 248 ms                                                 | 255 ms: 1.03x slower                                                             |
| pathlib                          | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                            |
| bench_thread_pool                | 503 us                                                 | 519 us: 1.03x slower                                                             |
| python_startup                   | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                            |
| pycparser                        | 701 ms                                                 | 728 ms: 1.04x slower                                                             |
| mdp                              | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.11 ms: 1.04x slower                                                            |
| logging_simple                   | 3.56 us                                                | 3.71 us: 1.04x slower                                                            |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.04x slower                                                           |
| sqlglot_normalize                | 188 ms                                                 | 197 ms: 1.05x slower                                                             |
| unpickle_pure_python             | 165 us                                                 | 173 us: 1.05x slower                                                             |
| logging_format                   | 3.85 us                                                | 4.04 us: 1.05x slower                                                            |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                            |
| python_startup_no_site           | 13.7 ms                                                | 14.4 ms: 1.05x slower                                                            |
| scimark_lu                       | 75.9 ms                                                | 80.0 ms: 1.05x slower                                                            |
| sympy_str                        | 146 ms                                                 | 153 ms: 1.05x slower                                                             |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.06 ms: 1.06x slower                                                            |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.06x slower                                                            |
| sympy_sum                        | 75.1 ms                                                | 79.4 ms: 1.06x slower                                                            |
| sqlglot_transpile                | 1.04 ms                                                | 1.10 ms: 1.06x slower                                                            |
| meteor_contest                   | 74.0 ms                                                | 78.3 ms: 1.06x slower                                                            |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                            |
| sqlglot_parse                    | 852 us                                                 | 912 us: 1.07x slower                                                             |
| deltablue                        | 2.65 ms                                                | 2.83 ms: 1.07x slower                                                            |
| sqlalchemy_declarative           | 59.0 ms                                                | 63.7 ms: 1.08x slower                                                            |
| nqueens                          | 61.8 ms                                                | 66.8 ms: 1.08x slower                                                            |
| richards_super                   | 39.2 ms                                                | 42.6 ms: 1.09x slower                                                            |
| sympy_integrate                  | 11.3 ms                                                | 12.3 ms: 1.09x slower                                                            |
| hexiom                           | 4.87 ms                                                | 5.29 ms: 1.09x slower                                                            |
| fannkuch                         | 279 ms                                                 | 304 ms: 1.09x slower                                                             |
| raytrace                         | 181 ms                                                 | 199 ms: 1.10x slower                                                             |
| logging_silent                   | 71.0 ns                                                | 78.4 ns: 1.11x slower                                                            |
| pickle_pure_python               | 215 us                                                 | 237 us: 1.11x slower                                                             |
| chaos                            | 41.1 ms                                                | 45.6 ms: 1.11x slower                                                            |
| crypto_pyaes                     | 55.3 ms                                                | 61.5 ms: 1.11x slower                                                            |
| mako                             | 7.75 ms                                                | 8.64 ms: 1.11x slower                                                            |
| comprehensions                   | 12.0 us                                                | 13.3 us: 1.11x slower                                                            |
| django_template                  | 20.5 ms                                                | 23.4 ms: 1.14x slower                                                            |
| many_optionals                   | 409 us                                                 | 472 us: 1.16x slower                                                             |
| json_dumps                       | 6.47 ms                                                | 7.54 ms: 1.17x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                             |
| nbody                            | 73.6 ms                                                | 90.5 ms: 1.23x slower                                                            |
| subparsers                       | 9.44 ms                                                | 12.8 ms: 1.35x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 191 ms: 1.39x slower                                                             |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.02x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (7): pylint, xml_etree_iterparse, dask, asyncio_websockets, pidigits, json, 2to3
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 69.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x