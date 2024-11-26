# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: darwin-arm64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.099x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.46x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 162 ms: 1.16x faster                                                  |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                |
| html5lib       | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 60.8 ms: 1.15x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.8 ms: 1.14x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 256 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 123 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.06x faster                                                  |
| async_generators                 | 295 ms                                                 | 278 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 548 ms: 1.10x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 675 ms: 1.31x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 60.0 ms: 1.23x faster                                                 |
| float          | 56.0 ms                                                | 48.5 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 67.0 ms: 1.17x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 180 us: 1.19x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 140 us: 1.17x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 37.5 ms: 1.09x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 52.9 ms: 1.08x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| json_dumps           | 6.52 ms                                                | 6.30 ms: 1.04x faster                                                 |
| json_loads           | 17.0 us                                                | 16.8 us: 1.01x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 109 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.0 ms: 1.18x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.1 ms: 1.11x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| django_template | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                 |
| mako            | 7.68 ms                                                | 7.12 ms: 1.08x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.6 us: 1.65x faster                                                 |
| deepcopy                         | 237 us                                                 | 144 us: 1.64x faster                                                  |
| generators                       | 31.5 ms                                                | 21.1 ms: 1.49x faster                                                 |
| go                               | 115 ms                                                 | 79.2 ms: 1.45x faster                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 892 us: 1.31x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 48.0 ms: 1.30x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.13 ms: 1.26x faster                                                 |
| nbody                            | 74.0 ms                                                | 60.0 ms: 1.23x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| raytrace                         | 181 ms                                                 | 149 ms: 1.21x faster                                                  |
| hexiom                           | 4.86 ms                                                | 4.04 ms: 1.20x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.00 us: 1.20x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 180 us: 1.19x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 42.4 ms: 1.19x faster                                                 |
| gc_traversal                     | 2.91 ms                                                | 2.45 ms: 1.19x faster                                                 |
| logging_format                   | 3.89 us                                                | 3.28 us: 1.19x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 64.6 ms: 1.19x faster                                                 |
| python_startup                   | 18.9 ms                                                | 16.0 ms: 1.18x faster                                                 |
| nqueens                          | 62.5 ms                                                | 53.2 ms: 1.18x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 67.0 ms: 1.17x faster                                                 |
| unpickle_pure_python             | 164 us                                                 | 140 us: 1.17x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 457 ms: 1.17x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 930 ms: 1.17x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 736 us: 1.16x faster                                                  |
| 2to3                             | 187 ms                                                 | 162 ms: 1.16x faster                                                  |
| chaos                            | 41.2 ms                                                | 35.6 ms: 1.16x faster                                                 |
| float                            | 56.0 ms                                                | 48.5 ms: 1.16x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 66.0 ms: 1.15x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 60.8 ns: 1.15x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 60.8 ms: 1.15x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.8 ms: 1.14x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 898 us: 1.14x faster                                                  |
| scimark_sor                      | 105 ms                                                 | 92.7 ms: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 448 us: 1.13x faster                                                  |
| comprehensions                   | 12.3 us                                                | 10.9 us: 1.13x faster                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 31.1 ms: 1.12x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 256 ms: 1.12x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 179 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 123 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                  |
| django_template                  | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                 |
| pycparser                        | 705 ms                                                 | 637 ms: 1.11x faster                                                  |
| python_startup_no_site           | 14.5 ms                                                | 13.1 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.70 ms: 1.10x faster                                                 |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 320 ms: 1.10x faster                                                  |
| sympy_sum                        | 75.4 ms                                                | 68.7 ms: 1.10x faster                                                 |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 37.5 ms: 1.09x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                  |
| fannkuch                         | 284 ms                                                 | 261 ms: 1.09x faster                                                  |
| richards                         | 35.2 ms                                                | 32.4 ms: 1.09x faster                                                 |
| crypto_pyaes                     | 54.2 ms                                                | 50.0 ms: 1.09x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.08x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 93.6 us: 1.08x faster                                                 |
| richards_super                   | 39.1 ms                                                | 36.2 ms: 1.08x faster                                                 |
| mako                             | 7.68 ms                                                | 7.12 ms: 1.08x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 52.9 ms: 1.08x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.06x faster                                                  |
| async_generators                 | 295 ms                                                 | 278 ms: 1.06x faster                                                  |
| dulwich_log                      | 28.5 ms                                                | 27.3 ms: 1.04x faster                                                 |
| json                             | 3.03 ms                                                | 2.91 ms: 1.04x faster                                                 |
| mdp                              | 1.49 sec                                               | 1.44 sec: 1.04x faster                                                |
| bpe_tokeniser                    | 3.25 sec                                               | 3.13 sec: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 71.3 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                                  |
| json_dumps                       | 6.52 ms                                                | 6.30 ms: 1.04x faster                                                 |
| coverage                         | 46.0 ms                                                | 44.4 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.03x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.8 us: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                |
| telco                            | 4.76 ms                                                | 4.81 ms: 1.01x slower                                                 |
| xml_etree_parse                  | 107 ms                                                 | 109 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 548 ms: 1.10x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 675 ms: 1.31x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (5): pylint, async_tree_cpu_io_mixed, xml_etree_iterparse, pathlib, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.099x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.46x