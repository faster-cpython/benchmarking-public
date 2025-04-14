# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: darwin-arm64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.017x faster
- HPT reliability: 53.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 173 ms: 1.03x slower                                                            |
| docutils       | 1.45 sec                                               | 1.49 sec: 1.03x slower                                                          |
| html5lib       | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                           |
| sphinx         | 613 ms                                                 | 601 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 387 ms: 1.74x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 389 ms: 1.71x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 401 ms: 1.67x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 395 ms: 1.56x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 165 ms: 1.55x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 206 ms: 1.54x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 175 ms: 1.51x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 212 ms: 1.46x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 425 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 426 ms: 1.24x faster                                                            |
| async_generators                 | 299 ms                                                 | 265 ms: 1.13x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.12x faster                                                            |
| coroutines                       | 19.7 ms                                                | 17.6 ms: 1.12x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 365 ms: 1.02x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 67.3 ms: 1.02x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 185 ms: 1.30x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 137 ms: 2.91x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 52.1 ms: 1.04x faster                                                           |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                            |
| nbody          | 67.6 ms                                                | 80.1 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                           |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                            |
| regex_v8       | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                            |
| tomli_loads          | 1.36 sec                                               | 1.32 sec: 1.03x faster                                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 74.0 ms: 1.02x faster                                                           |
| xml_etree_generate   | 55.4 ms                                                | 56.9 ms: 1.03x slower                                                           |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                           |
| xml_etree_process    | 38.9 ms                                                | 41.3 ms: 1.06x slower                                                           |
| unpickle_pure_python | 145 us                                                 | 166 us: 1.14x slower                                                            |
| pickle_pure_python   | 197 us                                                 | 229 us: 1.16x slower                                                            |
| json_dumps           | 6.19 ms                                                | 7.50 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.4 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 32.5 ms: 1.07x slower                                                           |
| genshi_text     | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                           |
| mako            | 7.44 ms                                                | 8.11 ms: 1.09x slower                                                           |
| django_template | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.10x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.8 ms: 2.51x faster                                                           |
| async_tree_io_tg                 | 673 ms                                                 | 387 ms: 1.74x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 389 ms: 1.71x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 401 ms: 1.67x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 395 ms: 1.56x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 165 ms: 1.55x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 206 ms: 1.54x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 175 ms: 1.51x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 212 ms: 1.46x faster                                                            |
| deepcopy                         | 226 us                                                 | 166 us: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 425 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 426 ms: 1.24x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 21.4 us: 1.21x faster                                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.72 us: 1.17x faster                                                           |
| dulwich_log                      | 29.2 ms                                                | 25.6 ms: 1.14x faster                                                           |
| async_generators                 | 299 ms                                                 | 265 ms: 1.13x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.12x faster                                                            |
| coroutines                       | 19.7 ms                                                | 17.6 ms: 1.12x faster                                                           |
| k_core                           | 1.72 sec                                               | 1.56 sec: 1.11x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 70.2 ms: 1.09x faster                                                           |
| bench_mp_pool                    | 65.5 ms                                                | 60.4 ms: 1.09x faster                                                           |
| comprehensions                   | 14.0 us                                                | 13.0 us: 1.08x faster                                                           |
| raytrace                         | 204 ms                                                 | 189 ms: 1.08x faster                                                            |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                           |
| pylint                           | 182 ms                                                 | 170 ms: 1.07x faster                                                            |
| generators                       | 29.4 ms                                                | 27.8 ms: 1.06x faster                                                           |
| html5lib                         | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                           |
| go                               | 98.5 ms                                                | 94.2 ms: 1.04x faster                                                           |
| pathlib                          | 24.7 ms                                                | 23.7 ms: 1.04x faster                                                           |
| float                            | 54.1 ms                                                | 52.1 ms: 1.04x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                            |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.05 ms: 1.03x faster                                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 3.19 sec: 1.03x faster                                                          |
| tomli_loads                      | 1.36 sec                                               | 1.32 sec: 1.03x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 365 ms: 1.02x faster                                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 74.0 ms: 1.02x faster                                                           |
| sphinx                           | 613 ms                                                 | 601 ms: 1.02x faster                                                            |
| thrift                           | 468 us                                                 | 460 us: 1.02x faster                                                            |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                            |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                            |
| scimark_fft                      | 194 ms                                                 | 193 ms: 1.01x faster                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                           |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.5 ms: 1.01x faster                                                           |
| logging_simple                   | 3.60 us                                                | 3.59 us: 1.00x faster                                                           |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                            |
| logging_silent                   | 72.5 ns                                                | 73.0 ns: 1.01x slower                                                           |
| python_startup_no_site           | 13.2 ms                                                | 13.4 ms: 1.02x slower                                                           |
| scimark_sor                      | 85.8 ms                                                | 87.5 ms: 1.02x slower                                                           |
| async_tree_eager                 | 65.8 ms                                                | 67.3 ms: 1.02x slower                                                           |
| 2to3                             | 168 ms                                                 | 173 ms: 1.03x slower                                                            |
| sympy_sum                        | 76.2 ms                                                | 78.2 ms: 1.03x slower                                                           |
| shortest_path                    | 331 ms                                                 | 339 ms: 1.03x slower                                                            |
| xml_etree_generate               | 55.4 ms                                                | 56.9 ms: 1.03x slower                                                           |
| docutils                         | 1.45 sec                                               | 1.49 sec: 1.03x slower                                                          |
| mdp                              | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                          |
| pycparser                        | 673 ms                                                 | 698 ms: 1.04x slower                                                            |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.87 ms: 1.04x slower                                                           |
| connected_components             | 300 ms                                                 | 312 ms: 1.04x slower                                                            |
| sympy_str                        | 144 ms                                                 | 150 ms: 1.04x slower                                                            |
| chaos                            | 41.6 ms                                                | 43.7 ms: 1.05x slower                                                           |
| pprint_pformat                   | 986 ms                                                 | 1.04 sec: 1.05x slower                                                          |
| pyflate                          | 311 ms                                                 | 327 ms: 1.05x slower                                                            |
| regex_v8                         | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                           |
| json                             | 3.00 ms                                                | 3.17 ms: 1.05x slower                                                           |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                           |
| gc_traversal                     | 2.95 ms                                                | 3.13 ms: 1.06x slower                                                           |
| scimark_lu                       | 73.5 ms                                                | 77.9 ms: 1.06x slower                                                           |
| xml_etree_process                | 38.9 ms                                                | 41.3 ms: 1.06x slower                                                           |
| pprint_safe_repr                 | 483 ms                                                 | 513 ms: 1.06x slower                                                            |
| bench_thread_pool                | 483 us                                                 | 514 us: 1.07x slower                                                            |
| genshi_xml                       | 30.5 ms                                                | 32.5 ms: 1.07x slower                                                           |
| sympy_expand                     | 233 ms                                                 | 251 ms: 1.07x slower                                                            |
| deltablue                        | 2.57 ms                                                | 2.76 ms: 1.08x slower                                                           |
| scimark_monte_carlo              | 44.5 ms                                                | 47.8 ms: 1.08x slower                                                           |
| genshi_text                      | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                           |
| mako                             | 7.44 ms                                                | 8.11 ms: 1.09x slower                                                           |
| sympy_integrate                  | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                           |
| meteor_contest                   | 69.1 ms                                                | 75.6 ms: 1.09x slower                                                           |
| typing_runtime_protocols         | 91.5 us                                                | 101 us: 1.10x slower                                                            |
| nqueens                          | 59.5 ms                                                | 66.4 ms: 1.12x slower                                                           |
| create_gc_cycles                 | 1.15 ms                                                | 1.30 ms: 1.13x slower                                                           |
| richards                         | 30.6 ms                                                | 34.9 ms: 1.14x slower                                                           |
| unpickle_pure_python             | 145 us                                                 | 166 us: 1.14x slower                                                            |
| crypto_pyaes                     | 51.4 ms                                                | 59.2 ms: 1.15x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                            |
| hexiom                           | 4.38 ms                                                | 5.05 ms: 1.15x slower                                                           |
| many_optionals                   | 403 us                                                 | 466 us: 1.16x slower                                                            |
| pickle_pure_python               | 197 us                                                 | 229 us: 1.16x slower                                                            |
| richards_super                   | 34.6 ms                                                | 40.2 ms: 1.16x slower                                                           |
| django_template                  | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                           |
| fannkuch                         | 250 ms                                                 | 296 ms: 1.18x slower                                                            |
| nbody                            | 67.6 ms                                                | 80.1 ms: 1.19x slower                                                           |
| telco                            | 3.92 ms                                                | 4.66 ms: 1.19x slower                                                           |
| json_dumps                       | 6.19 ms                                                | 7.50 ms: 1.21x slower                                                           |
| coverage                         | 38.5 ms                                                | 46.7 ms: 1.21x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 185 ms: 1.30x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 137 ms: 2.91x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (4): python_startup, asyncio_websockets, logging_format, regex_compile
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 53.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x