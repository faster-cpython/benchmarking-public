# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: darwin-arm64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.082x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 167 ms: 1.01x faster                                                          |
| sphinx         | 613 ms                                                 | 574 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.86x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.83x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 380 ms: 1.77x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 368 ms: 1.68x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 191 ms: 1.67x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.61x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 193 ms: 1.61x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 412 ms: 1.28x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 417 ms: 1.26x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                          |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                         |
| async_generators                 | 299 ms                                                 | 286 ms: 1.04x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                          |
| async_tree_eager                 | 65.8 ms                                                | 63.2 ms: 1.04x faster                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                          |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 128 ms: 2.74x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                | 60.3 ms: 1.12x faster                                                         |
| float          | 54.1 ms                                                | 51.5 ms: 1.05x faster                                                         |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.13 ms: 1.15x faster                                                         |
| regex_compile  | 75.9 ms                                                | 71.6 ms: 1.06x faster                                                         |
| regex_dna      | 143 ms                                                 | 138 ms: 1.04x faster                                                          |
| regex_v8       | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 118 us: 1.23x faster                                                          |
| tomli_loads          | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                        |
| xml_etree_process    | 38.9 ms                                                | 33.6 ms: 1.16x faster                                                         |
| xml_etree_generate   | 55.4 ms                                                | 48.2 ms: 1.15x faster                                                         |
| xml_etree_iterparse  | 75.5 ms                                                | 72.2 ms: 1.05x faster                                                         |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                          |
| json_loads           | 17.0 us                                                | 16.9 us: 1.01x faster                                                         |
| pickle_pure_python   | 197 us                                                 | 202 us: 1.02x slower                                                          |
| json_dumps           | 6.19 ms                                                | 6.60 ms: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 16.5 ms: 1.07x faster                                                         |
| python_startup_no_site | 13.2 ms                                                | 12.4 ms: 1.07x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.44 ms: 1.16x faster                                                         |
| genshi_text     | 14.7 ms                                                | 15.2 ms: 1.03x slower                                                         |
| genshi_xml      | 30.5 ms                                                | 32.7 ms: 1.07x slower                                                         |
| django_template | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 745 ms: 2.00x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 359 ms: 1.86x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.83x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 380 ms: 1.77x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 368 ms: 1.68x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 191 ms: 1.67x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.61x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 193 ms: 1.61x faster                                                          |
| deepcopy                         | 226 us                                                 | 173 us: 1.31x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 58.8 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 412 ms: 1.28x faster                                                          |
| subparsers                       | 32.1 ms                                                | 25.2 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 417 ms: 1.26x faster                                                          |
| comprehensions                   | 14.0 us                                                | 11.2 us: 1.25x faster                                                         |
| unpickle_pure_python             | 145 us                                                 | 118 us: 1.23x faster                                                          |
| generators                       | 29.4 ms                                                | 24.3 ms: 1.21x faster                                                         |
| deepcopy_memo                    | 26.0 us                                                | 21.6 us: 1.20x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                          |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                         |
| raytrace                         | 204 ms                                                 | 172 ms: 1.19x faster                                                          |
| tomli_loads                      | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                        |
| bpe_tokeniser                    | 3.28 sec                                               | 2.80 sec: 1.17x faster                                                        |
| dulwich_log                      | 29.2 ms                                                | 25.1 ms: 1.17x faster                                                         |
| xml_etree_process                | 38.9 ms                                                | 33.6 ms: 1.16x faster                                                         |
| mako                             | 7.44 ms                                                | 6.44 ms: 1.16x faster                                                         |
| go                               | 98.5 ms                                                | 85.4 ms: 1.15x faster                                                         |
| xml_etree_generate               | 55.4 ms                                                | 48.2 ms: 1.15x faster                                                         |
| pyflate                          | 311 ms                                                 | 270 ms: 1.15x faster                                                          |
| regex_effbot                     | 2.44 ms                                                | 2.13 ms: 1.15x faster                                                         |
| deepcopy_reduce                  | 2.01 us                                                | 1.78 us: 1.13x faster                                                         |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                          |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.12x faster                                                        |
| nbody                            | 67.6 ms                                                | 60.3 ms: 1.12x faster                                                         |
| chaos                            | 41.6 ms                                                | 38.3 ms: 1.09x faster                                                         |
| pprint_safe_repr                 | 483 ms                                                 | 447 ms: 1.08x faster                                                          |
| scimark_fft                      | 194 ms                                                 | 180 ms: 1.08x faster                                                          |
| logging_simple                   | 3.60 us                                                | 3.35 us: 1.07x faster                                                         |
| pathlib                          | 24.7 ms                                                | 23.0 ms: 1.07x faster                                                         |
| python_startup                   | 17.8 ms                                                | 16.5 ms: 1.07x faster                                                         |
| logging_format                   | 3.90 us                                                | 3.63 us: 1.07x faster                                                         |
| pprint_pformat                   | 986 ms                                                 | 921 ms: 1.07x faster                                                          |
| sphinx                           | 613 ms                                                 | 574 ms: 1.07x faster                                                          |
| python_startup_no_site           | 13.2 ms                                                | 12.4 ms: 1.07x faster                                                         |
| deltablue                        | 2.57 ms                                                | 2.42 ms: 1.06x faster                                                         |
| regex_compile                    | 75.9 ms                                                | 71.6 ms: 1.06x faster                                                         |
| hexiom                           | 4.38 ms                                                | 4.15 ms: 1.05x faster                                                         |
| float                            | 54.1 ms                                                | 51.5 ms: 1.05x faster                                                         |
| crypto_pyaes                     | 51.4 ms                                                | 49.2 ms: 1.05x faster                                                         |
| xml_etree_iterparse              | 75.5 ms                                                | 72.2 ms: 1.05x faster                                                         |
| async_generators                 | 299 ms                                                 | 286 ms: 1.04x faster                                                          |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                          |
| async_tree_eager                 | 65.8 ms                                                | 63.2 ms: 1.04x faster                                                         |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.04x faster                                                          |
| fannkuch                         | 250 ms                                                 | 243 ms: 1.03x faster                                                          |
| thrift                           | 468 us                                                 | 456 us: 1.02x faster                                                          |
| scimark_sor                      | 85.8 ms                                                | 83.8 ms: 1.02x faster                                                         |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.02x faster                                                         |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                          |
| json                             | 3.00 ms                                                | 2.98 ms: 1.01x faster                                                         |
| 2to3                             | 168 ms                                                 | 167 ms: 1.01x faster                                                          |
| json_loads                       | 17.0 us                                                | 16.9 us: 1.01x faster                                                         |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| scimark_monte_carlo              | 44.5 ms                                                | 44.7 ms: 1.01x slower                                                         |
| scimark_lu                       | 73.5 ms                                                | 74.2 ms: 1.01x slower                                                         |
| logging_silent                   | 72.5 ns                                                | 73.6 ns: 1.01x slower                                                         |
| meteor_contest                   | 69.1 ms                                                | 70.1 ms: 1.01x slower                                                         |
| pickle_pure_python               | 197 us                                                 | 202 us: 1.02x slower                                                          |
| regex_v8                         | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                         |
| pycparser                        | 673 ms                                                 | 692 ms: 1.03x slower                                                          |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                         |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                          |
| genshi_text                      | 14.7 ms                                                | 15.2 ms: 1.03x slower                                                         |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.28 ms: 1.04x slower                                                         |
| connected_components             | 300 ms                                                 | 313 ms: 1.04x slower                                                          |
| typing_runtime_protocols         | 91.5 us                                                | 95.9 us: 1.05x slower                                                         |
| sympy_expand                     | 233 ms                                                 | 245 ms: 1.05x slower                                                          |
| json_dumps                       | 6.19 ms                                                | 6.60 ms: 1.07x slower                                                         |
| genshi_xml                       | 30.5 ms                                                | 32.7 ms: 1.07x slower                                                         |
| gc_traversal                     | 2.95 ms                                                | 3.21 ms: 1.09x slower                                                         |
| richards_super                   | 34.6 ms                                                | 37.8 ms: 1.09x slower                                                         |
| richards                         | 30.6 ms                                                | 33.4 ms: 1.09x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                          |
| telco                            | 3.92 ms                                                | 4.42 ms: 1.13x slower                                                         |
| django_template                  | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                                          |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                         |
| coverage                         | 38.5 ms                                                | 47.1 ms: 1.22x slower                                                         |
| many_optionals                   | 403 us                                                 | 595 us: 1.48x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 128 ms: 2.74x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                  |

Benchmark hidden because not significant (6): html5lib, sympy_sum, asyncio_websockets, docutils, nqueens, sympy_str
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250722-3.15.0a0-a4de1bf-JIT/bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.15x