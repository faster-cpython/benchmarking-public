# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: darwin-arm64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.035x faster
- HPT reliability: 98.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 183 ms: 1.02x faster                                                    |
| docutils       | 1.44 sec                                               | 1.58 sec: 1.10x slower                                                  |
| html5lib       | 36.6 ms                                                | 34.0 ms: 1.08x faster                                                   |
| sphinx         | 603 ms                                                 | 668 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.23x faster                                                    |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 42.4 ms: 1.13x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 63.4 ms: 1.11x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                    |
| async_tree_memoization           | 268 ms                                                 | 245 ms: 1.10x faster                                                    |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                                    |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.06x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 471 ms: 1.05x slower                                                    |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                    |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                    |
| async_tree_io_tg                 | 497 ms                                                 | 613 ms: 1.23x slower                                                    |
| async_tree_eager_io              | 514 ms                                                 | 671 ms: 1.31x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 715 ms: 1.50x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.4 ms: 1.16x faster                                                   |
| nbody          | 74.0 ms                                                | 65.5 ms: 1.13x faster                                                   |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 75.8 ms: 1.04x faster                                                   |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                    |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 132 us: 1.25x faster                                                    |
| tomli_loads          | 1.57 sec                                               | 1.26 sec: 1.25x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 180 us: 1.19x faster                                                    |
| xml_etree_process    | 41.0 ms                                                | 35.0 ms: 1.17x faster                                                   |
| xml_etree_generate   | 57.0 ms                                                | 50.8 ms: 1.12x faster                                                   |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 73.6 ms                                                | 72.9 ms: 1.01x faster                                                   |
| json_dumps           | 6.52 ms                                                | 7.14 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 19.2 ms: 1.01x slower                                                   |
| python_startup_no_site | 14.5 ms                                                | 14.8 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.48 ms: 1.18x faster                                                   |
| genshi_text     | 16.9 ms                                                | 17.0 ms: 1.00x slower                                                   |
| django_template | 22.2 ms                                                | 22.8 ms: 1.02x slower                                                   |
| genshi_xml      | 34.4 ms                                                | 42.9 ms: 1.25x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.9 us: 1.62x faster                                                   |
| deepcopy                         | 237 us                                                 | 156 us: 1.52x faster                                                    |
| deepcopy_reduce                  | 2.07 us                                                | 1.56 us: 1.33x faster                                                   |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                   |
| unpickle_pure_python             | 164 us                                                 | 132 us: 1.25x faster                                                    |
| tomli_loads                      | 1.57 sec                                               | 1.26 sec: 1.25x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.23x faster                                                    |
| scimark_sor                      | 105 ms                                                 | 86.1 ms: 1.22x faster                                                   |
| pickle_pure_python               | 214 us                                                 | 180 us: 1.19x faster                                                    |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                   |
| scimark_lu                       | 76.7 ms                                                | 64.6 ms: 1.19x faster                                                   |
| mako                             | 7.68 ms                                                | 6.48 ms: 1.18x faster                                                   |
| xml_etree_process                | 41.0 ms                                                | 35.0 ms: 1.17x faster                                                   |
| go                               | 115 ms                                                 | 98.2 ms: 1.17x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.10 us: 1.16x faster                                                   |
| float                            | 56.0 ms                                                | 48.4 ms: 1.16x faster                                                   |
| logging_format                   | 3.89 us                                                | 3.40 us: 1.15x faster                                                   |
| nbody                            | 74.0 ms                                                | 65.5 ms: 1.13x faster                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 42.4 ms: 1.13x faster                                                   |
| xml_etree_generate               | 57.0 ms                                                | 50.8 ms: 1.12x faster                                                   |
| deltablue                        | 2.68 ms                                                | 2.41 ms: 1.11x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 63.4 ms: 1.11x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                    |
| scimark_monte_carlo              | 50.4 ms                                                | 45.9 ms: 1.10x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 245 ms: 1.10x faster                                                    |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                    |
| spectral_norm                    | 76.3 ms                                                | 69.8 ms: 1.09x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                                    |
| html5lib                         | 36.6 ms                                                | 34.0 ms: 1.08x faster                                                   |
| pprint_safe_repr                 | 533 ms                                                 | 496 ms: 1.08x faster                                                    |
| nqueens                          | 62.5 ms                                                | 58.2 ms: 1.07x faster                                                   |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                                    |
| fannkuch                         | 284 ms                                                 | 266 ms: 1.07x faster                                                    |
| pprint_pformat                   | 1.08 sec                                               | 1.02 sec: 1.07x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 475 us: 1.06x faster                                                    |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.06x faster                                                    |
| coverage                         | 46.0 ms                                                | 43.5 ms: 1.06x faster                                                   |
| json                             | 3.03 ms                                                | 2.88 ms: 1.05x faster                                                   |
| bpe_tokeniser                    | 3.25 sec                                               | 3.09 sec: 1.05x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                    |
| raytrace                         | 181 ms                                                 | 173 ms: 1.05x faster                                                    |
| pathlib                          | 23.4 ms                                                | 22.4 ms: 1.04x faster                                                   |
| regex_compile                    | 78.6 ms                                                | 75.8 ms: 1.04x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 97.9 us: 1.03x faster                                                   |
| pycparser                        | 705 ms                                                 | 683 ms: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                    |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                                   |
| 2to3                             | 187 ms                                                 | 183 ms: 1.02x faster                                                    |
| telco                            | 4.76 ms                                                | 4.67 ms: 1.02x faster                                                   |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.01x faster                                                    |
| bench_mp_pool                    | 62.5 ms                                                | 61.8 ms: 1.01x faster                                                   |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                    |
| richards_super                   | 39.1 ms                                                | 38.7 ms: 1.01x faster                                                   |
| xml_etree_iterparse              | 73.6 ms                                                | 72.9 ms: 1.01x faster                                                   |
| logging_silent                   | 70.1 ns                                                | 69.9 ns: 1.00x faster                                                   |
| crypto_pyaes                     | 54.2 ms                                                | 54.1 ms: 1.00x faster                                                   |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                    |
| regex_effbot                     | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                   |
| sympy_expand                     | 246 ms                                                 | 247 ms: 1.00x slower                                                    |
| genshi_text                      | 16.9 ms                                                | 17.0 ms: 1.00x slower                                                   |
| meteor_contest                   | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                   |
| dulwich_log                      | 28.5 ms                                                | 28.8 ms: 1.01x slower                                                   |
| gc_traversal                     | 2.91 ms                                                | 2.95 ms: 1.01x slower                                                   |
| python_startup                   | 18.9 ms                                                | 19.2 ms: 1.01x slower                                                   |
| chaos                            | 41.2 ms                                                | 41.8 ms: 1.02x slower                                                   |
| hexiom                           | 4.86 ms                                                | 4.95 ms: 1.02x slower                                                   |
| sqlglot_parse                    | 856 us                                                 | 873 us: 1.02x slower                                                    |
| python_startup_no_site           | 14.5 ms                                                | 14.8 ms: 1.02x slower                                                   |
| django_template                  | 22.2 ms                                                | 22.8 ms: 1.02x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                  |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                                    |
| sqlglot_transpile                | 1.02 ms                                                | 1.07 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 471 ms: 1.05x slower                                                    |
| sympy_sum                        | 75.4 ms                                                | 79.3 ms: 1.05x slower                                                   |
| comprehensions                   | 12.3 us                                                | 12.9 us: 1.06x slower                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.19 ms: 1.07x slower                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 37.5 ms: 1.07x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                    |
| json_dumps                       | 6.52 ms                                                | 7.14 ms: 1.09x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.58 sec: 1.10x slower                                                  |
| sphinx                           | 603 ms                                                 | 668 ms: 1.11x slower                                                    |
| sympy_integrate                  | 11.3 ms                                                | 12.6 ms: 1.12x slower                                                   |
| create_gc_cycles                 | 1.17 ms                                                | 1.31 ms: 1.12x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                    |
| async_tree_io_tg                 | 497 ms                                                 | 613 ms: 1.23x slower                                                    |
| genshi_xml                       | 34.4 ms                                                | 42.9 ms: 1.25x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 671 ms: 1.31x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 715 ms: 1.50x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, regex_v8, asyncio_websockets, richards, async_generators, xml_etree_parse, tornado_http, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 98.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x