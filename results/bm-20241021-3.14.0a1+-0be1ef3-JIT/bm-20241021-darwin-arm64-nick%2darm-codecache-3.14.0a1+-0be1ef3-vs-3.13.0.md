# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 171 ms: 1.09x faster                                            |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                          |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.17x faster                                           |
| sphinx         | 603 ms                                                 | 618 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                            |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                           |
| async_tree_eager                 | 70.1 ms                                                | 61.9 ms: 1.13x faster                                           |
| async_tree_eager_tg              | 47.8 ms                                                | 42.5 ms: 1.12x faster                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                            |
| async_tree_none                  | 215 ms                                                 | 197 ms: 1.10x faster                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                            |
| async_generators                 | 295 ms                                                 | 291 ms: 1.01x faster                                            |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 454 ms: 1.01x faster                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 468 ms: 1.04x slower                                            |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                            |
| async_tree_io                    | 507 ms                                                 | 578 ms: 1.14x slower                                            |
| async_tree_io_tg                 | 497 ms                                                 | 608 ms: 1.22x slower                                            |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                            |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.1 ms: 1.17x faster                                           |
| nbody          | 74.0 ms                                                | 65.5 ms: 1.13x faster                                           |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 71.0 ms: 1.11x faster                                           |
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                           |
| regex_dna      | 149 ms                                                 | 143 ms: 1.05x faster                                            |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.23 sec: 1.27x faster                                          |
| unpickle_pure_python | 164 us                                                 | 132 us: 1.24x faster                                            |
| pickle_pure_python   | 214 us                                                 | 179 us: 1.20x faster                                            |
| xml_etree_process    | 41.0 ms                                                | 34.3 ms: 1.19x faster                                           |
| xml_etree_generate   | 57.0 ms                                                | 50.3 ms: 1.13x faster                                           |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                           |
| xml_etree_iterparse  | 73.6 ms                                                | 72.5 ms: 1.01x faster                                           |
| json_dumps           | 6.52 ms                                                | 7.12 ms: 1.09x slower                                           |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.8 ms: 1.13x faster                                           |
| python_startup_no_site | 14.5 ms                                                | 12.9 ms: 1.12x faster                                           |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.44 ms: 1.19x faster                                           |
| genshi_text     | 16.9 ms                                                | 14.5 ms: 1.16x faster                                           |
| genshi_xml      | 34.4 ms                                                | 31.4 ms: 1.10x faster                                           |
| django_template | 22.2 ms                                                | 20.3 ms: 1.09x faster                                           |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.7 us: 1.64x faster                                           |
| deepcopy                         | 237 us                                                 | 148 us: 1.60x faster                                            |
| deepcopy_reduce                  | 2.07 us                                                | 1.52 us: 1.36x faster                                           |
| generators                       | 31.5 ms                                                | 24.1 ms: 1.31x faster                                           |
| go                               | 115 ms                                                 | 90.0 ms: 1.28x faster                                           |
| tomli_loads                      | 1.57 sec                                               | 1.23 sec: 1.27x faster                                          |
| unpickle_pure_python             | 164 us                                                 | 132 us: 1.24x faster                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                            |
| scimark_sor                      | 105 ms                                                 | 85.7 ms: 1.23x faster                                           |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                           |
| pickle_pure_python               | 214 us                                                 | 179 us: 1.20x faster                                            |
| xml_etree_process                | 41.0 ms                                                | 34.3 ms: 1.19x faster                                           |
| mako                             | 7.68 ms                                                | 6.44 ms: 1.19x faster                                           |
| logging_simple                   | 3.60 us                                                | 3.03 us: 1.19x faster                                           |
| logging_format                   | 3.89 us                                                | 3.31 us: 1.18x faster                                           |
| scimark_lu                       | 76.7 ms                                                | 65.3 ms: 1.17x faster                                           |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.17x faster                                           |
| float                            | 56.0 ms                                                | 48.1 ms: 1.17x faster                                           |
| genshi_text                      | 16.9 ms                                                | 14.5 ms: 1.16x faster                                           |
| pprint_safe_repr                 | 533 ms                                                 | 459 ms: 1.16x faster                                            |
| deltablue                        | 2.68 ms                                                | 2.32 ms: 1.15x faster                                           |
| xml_etree_generate               | 57.0 ms                                                | 50.3 ms: 1.13x faster                                           |
| async_tree_eager                 | 70.1 ms                                                | 61.9 ms: 1.13x faster                                           |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                           |
| nbody                            | 74.0 ms                                                | 65.5 ms: 1.13x faster                                           |
| richards                         | 35.2 ms                                                | 31.2 ms: 1.13x faster                                           |
| pyflate                          | 351 ms                                                 | 312 ms: 1.13x faster                                            |
| python_startup                   | 18.9 ms                                                | 16.8 ms: 1.13x faster                                           |
| pprint_pformat                   | 1.08 sec                                               | 961 ms: 1.13x faster                                            |
| async_tree_eager_tg              | 47.8 ms                                                | 42.5 ms: 1.12x faster                                           |
| python_startup_no_site           | 14.5 ms                                                | 12.9 ms: 1.12x faster                                           |
| thrift                           | 466 us                                                 | 417 us: 1.12x faster                                            |
| pylint                           | 180 ms                                                 | 161 ms: 1.11x faster                                            |
| raytrace                         | 181 ms                                                 | 162 ms: 1.11x faster                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                            |
| scimark_monte_carlo              | 50.4 ms                                                | 45.4 ms: 1.11x faster                                           |
| regex_compile                    | 78.6 ms                                                | 71.0 ms: 1.11x faster                                           |
| fannkuch                         | 284 ms                                                 | 257 ms: 1.10x faster                                            |
| spectral_norm                    | 76.3 ms                                                | 69.4 ms: 1.10x faster                                           |
| genshi_xml                       | 34.4 ms                                                | 31.4 ms: 1.10x faster                                           |
| async_tree_none                  | 215 ms                                                 | 197 ms: 1.10x faster                                            |
| 2to3                             | 187 ms                                                 | 171 ms: 1.09x faster                                            |
| sqlglot_normalize                | 189 ms                                                 | 173 ms: 1.09x faster                                            |
| django_template                  | 22.2 ms                                                | 20.3 ms: 1.09x faster                                           |
| hexiom                           | 4.86 ms                                                | 4.49 ms: 1.08x faster                                           |
| nqueens                          | 62.5 ms                                                | 57.9 ms: 1.08x faster                                           |
| pycparser                        | 705 ms                                                 | 653 ms: 1.08x faster                                            |
| bench_thread_pool                | 505 us                                                 | 470 us: 1.07x faster                                            |
| bpe_tokeniser                    | 3.25 sec                                               | 3.02 sec: 1.07x faster                                          |
| json                             | 3.03 ms                                                | 2.84 ms: 1.07x faster                                           |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                            |
| coverage                         | 46.0 ms                                                | 43.5 ms: 1.06x faster                                           |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                            |
| pathlib                          | 23.4 ms                                                | 22.3 ms: 1.05x faster                                           |
| typing_runtime_protocols         | 101 us                                                 | 96.7 us: 1.05x faster                                           |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.05x faster                                            |
| bench_mp_pool                    | 62.5 ms                                                | 59.9 ms: 1.04x faster                                           |
| telco                            | 4.76 ms                                                | 4.57 ms: 1.04x faster                                           |
| sympy_expand                     | 246 ms                                                 | 237 ms: 1.04x faster                                            |
| sqlglot_parse                    | 856 us                                                 | 823 us: 1.04x faster                                            |
| sqlglot_optimize                 | 34.9 ms                                                | 33.7 ms: 1.04x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                            |
| sqlglot_transpile                | 1.02 ms                                                | 992 us: 1.03x faster                                            |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                           |
| chaos                            | 41.2 ms                                                | 40.3 ms: 1.02x faster                                           |
| meteor_contest                   | 74.0 ms                                                | 72.5 ms: 1.02x faster                                           |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.02x faster                                            |
| xml_etree_iterparse              | 73.6 ms                                                | 72.5 ms: 1.01x faster                                           |
| async_generators                 | 295 ms                                                 | 291 ms: 1.01x faster                                            |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 454 ms: 1.01x faster                                            |
| logging_silent                   | 70.1 ns                                                | 69.3 ns: 1.01x faster                                           |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                           |
| sympy_sum                        | 75.4 ms                                                | 75.0 ms: 1.01x faster                                           |
| crypto_pyaes                     | 54.2 ms                                                | 54.0 ms: 1.01x faster                                           |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                            |
| gc_traversal                     | 2.91 ms                                                | 2.93 ms: 1.01x slower                                           |
| mdp                              | 1.49 sec                                               | 1.51 sec: 1.01x slower                                          |
| sphinx                           | 603 ms                                                 | 618 ms: 1.03x slower                                            |
| comprehensions                   | 12.3 us                                                | 12.7 us: 1.03x slower                                           |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.04x slower                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 468 ms: 1.04x slower                                            |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                          |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.17 ms: 1.06x slower                                           |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                            |
| json_dumps                       | 6.52 ms                                                | 7.12 ms: 1.09x slower                                           |
| create_gc_cycles                 | 1.17 ms                                                | 1.32 ms: 1.13x slower                                           |
| async_tree_io                    | 507 ms                                                 | 578 ms: 1.14x slower                                            |
| async_tree_io_tg                 | 497 ms                                                 | 608 ms: 1.22x slower                                            |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                            |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                    |

Benchmark hidden because not significant (5): async_tree_memoization, xml_etree_parse, asyncio_websockets, dulwich_log, tornado_http
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.072x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x