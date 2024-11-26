# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: darwin-arm64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 196 ms: 1.05x slower                                                            |
| docutils       | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                          |
| html5lib       | 36.6 ms                                                | 32.0 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                                           |
| async_tree_memoization_tg        | 288 ms                                                 | 245 ms: 1.18x faster                                                            |
| async_tree_eager                 | 70.1 ms                                                | 59.7 ms: 1.17x faster                                                           |
| async_tree_eager_tg              | 47.8 ms                                                | 41.9 ms: 1.14x faster                                                           |
| async_tree_none                  | 215 ms                                                 | 192 ms: 1.12x faster                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 251 ms: 1.07x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 158 ms: 1.07x faster                                                            |
| async_generators                 | 295 ms                                                 | 279 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 459 ms: 1.02x slower                                                            |
| async_tree_io_tg                 | 497 ms                                                 | 563 ms: 1.13x slower                                                            |
| async_tree_io                    | 507 ms                                                 | 593 ms: 1.17x slower                                                            |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 711 ms: 1.49x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 49.0 ms: 1.14x faster                                                           |
| nbody          | 74.0 ms                                                | 65.6 ms: 1.13x faster                                                           |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 68.3 ms: 1.15x faster                                                           |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                           |
| regex_dna      | 149 ms                                                 | 146 ms: 1.02x faster                                                            |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 183 us: 1.17x faster                                                            |
| unpickle_pure_python | 164 us                                                 | 142 us: 1.15x faster                                                            |
| xml_etree_process    | 41.0 ms                                                | 37.4 ms: 1.10x faster                                                           |
| xml_etree_generate   | 57.0 ms                                                | 52.4 ms: 1.09x faster                                                           |
| tomli_loads          | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                          |
| json_loads           | 17.0 us                                                | 16.4 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 73.6 ms                                                | 73.1 ms: 1.01x faster                                                           |
| xml_etree_parse      | 107 ms                                                 | 108 ms: 1.01x slower                                                            |
| json_dumps           | 6.52 ms                                                | 7.25 ms: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 19.0 ms: 1.01x slower                                                           |
| python_startup_no_site | 14.5 ms                                                | 15.9 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.24x faster                                                           |
| genshi_xml      | 34.4 ms                                                | 29.9 ms: 1.15x faster                                                           |
| django_template | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                           |
| mako            | 7.68 ms                                                | 7.00 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 147 us: 1.61x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 17.3 us: 1.59x faster                                                           |
| generators                       | 31.5 ms                                                | 20.3 ms: 1.55x faster                                                           |
| go                               | 115 ms                                                 | 81.8 ms: 1.41x faster                                                           |
| deepcopy_reduce                  | 2.07 us                                                | 1.53 us: 1.35x faster                                                           |
| create_gc_cycles                 | 1.17 ms                                                | 929 us: 1.26x faster                                                            |
| bench_mp_pool                    | 62.5 ms                                                | 50.5 ms: 1.24x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.24x faster                                                           |
| deltablue                        | 2.68 ms                                                | 2.22 ms: 1.20x faster                                                           |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                                           |
| logging_simple                   | 3.60 us                                                | 3.05 us: 1.18x faster                                                           |
| async_tree_memoization_tg        | 288 ms                                                 | 245 ms: 1.18x faster                                                            |
| hexiom                           | 4.86 ms                                                | 4.14 ms: 1.17x faster                                                           |
| async_tree_eager                 | 70.1 ms                                                | 59.7 ms: 1.17x faster                                                           |
| raytrace                         | 181 ms                                                 | 154 ms: 1.17x faster                                                            |
| pickle_pure_python               | 214 us                                                 | 183 us: 1.17x faster                                                            |
| logging_format                   | 3.89 us                                                | 3.34 us: 1.17x faster                                                           |
| gc_traversal                     | 2.91 ms                                                | 2.50 ms: 1.16x faster                                                           |
| logging_silent                   | 70.1 ns                                                | 60.6 ns: 1.16x faster                                                           |
| pprint_safe_repr                 | 533 ms                                                 | 461 ms: 1.16x faster                                                            |
| nqueens                          | 62.5 ms                                                | 54.2 ms: 1.15x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 43.7 ms: 1.15x faster                                                           |
| unpickle_pure_python             | 164 us                                                 | 142 us: 1.15x faster                                                            |
| sqlglot_parse                    | 856 us                                                 | 743 us: 1.15x faster                                                            |
| regex_compile                    | 78.6 ms                                                | 68.3 ms: 1.15x faster                                                           |
| pprint_pformat                   | 1.08 sec                                               | 943 ms: 1.15x faster                                                            |
| genshi_xml                       | 34.4 ms                                                | 29.9 ms: 1.15x faster                                                           |
| float                            | 56.0 ms                                                | 49.0 ms: 1.14x faster                                                           |
| scimark_lu                       | 76.7 ms                                                | 67.0 ms: 1.14x faster                                                           |
| html5lib                         | 36.6 ms                                                | 32.0 ms: 1.14x faster                                                           |
| async_tree_eager_tg              | 47.8 ms                                                | 41.9 ms: 1.14x faster                                                           |
| sqlglot_transpile                | 1.02 ms                                                | 898 us: 1.14x faster                                                            |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                                            |
| richards                         | 35.2 ms                                                | 31.2 ms: 1.13x faster                                                           |
| nbody                            | 74.0 ms                                                | 65.6 ms: 1.13x faster                                                           |
| sqlglot_optimize                 | 34.9 ms                                                | 31.0 ms: 1.13x faster                                                           |
| async_tree_none                  | 215 ms                                                 | 192 ms: 1.12x faster                                                            |
| richards_super                   | 39.1 ms                                                | 34.8 ms: 1.12x faster                                                           |
| thrift                           | 466 us                                                 | 419 us: 1.11x faster                                                            |
| comprehensions                   | 12.3 us                                                | 11.0 us: 1.11x faster                                                           |
| django_template                  | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                           |
| bench_thread_pool                | 505 us                                                 | 455 us: 1.11x faster                                                            |
| pycparser                        | 705 ms                                                 | 638 ms: 1.11x faster                                                            |
| chaos                            | 41.2 ms                                                | 37.4 ms: 1.10x faster                                                           |
| scimark_sor                      | 105 ms                                                 | 95.9 ms: 1.10x faster                                                           |
| mako                             | 7.68 ms                                                | 7.00 ms: 1.10x faster                                                           |
| xml_etree_process                | 41.0 ms                                                | 37.4 ms: 1.10x faster                                                           |
| sympy_expand                     | 246 ms                                                 | 225 ms: 1.09x faster                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                            |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.09x faster                                                            |
| typing_runtime_protocols         | 101 us                                                 | 92.9 us: 1.09x faster                                                           |
| sympy_sum                        | 75.4 ms                                                | 69.3 ms: 1.09x faster                                                           |
| xml_etree_generate               | 57.0 ms                                                | 52.4 ms: 1.09x faster                                                           |
| spectral_norm                    | 76.3 ms                                                | 70.8 ms: 1.08x faster                                                           |
| json                             | 3.03 ms                                                | 2.82 ms: 1.07x faster                                                           |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                                            |
| fannkuch                         | 284 ms                                                 | 266 ms: 1.07x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 251 ms: 1.07x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 158 ms: 1.07x faster                                                            |
| pathlib                          | 23.4 ms                                                | 22.0 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.82 ms: 1.06x faster                                                           |
| crypto_pyaes                     | 54.2 ms                                                | 51.2 ms: 1.06x faster                                                           |
| async_generators                 | 295 ms                                                 | 279 ms: 1.06x faster                                                            |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.05x faster                                                            |
| bpe_tokeniser                    | 3.25 sec                                               | 3.08 sec: 1.05x faster                                                          |
| coverage                         | 46.0 ms                                                | 43.6 ms: 1.05x faster                                                           |
| tomli_loads                      | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                          |
| telco                            | 4.76 ms                                                | 4.57 ms: 1.04x faster                                                           |
| dulwich_log                      | 28.5 ms                                                | 27.4 ms: 1.04x faster                                                           |
| meteor_contest                   | 74.0 ms                                                | 71.5 ms: 1.03x faster                                                           |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.03x faster                                                           |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                            |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                           |
| docutils                         | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                          |
| mdp                              | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                          |
| regex_dna                        | 149 ms                                                 | 146 ms: 1.02x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                           |
| xml_etree_iterparse              | 73.6 ms                                                | 73.1 ms: 1.01x faster                                                           |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| python_startup                   | 18.9 ms                                                | 19.0 ms: 1.01x slower                                                           |
| xml_etree_parse                  | 107 ms                                                 | 108 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 459 ms: 1.02x slower                                                            |
| 2to3                             | 187 ms                                                 | 196 ms: 1.05x slower                                                            |
| python_startup_no_site           | 14.5 ms                                                | 15.9 ms: 1.10x slower                                                           |
| json_dumps                       | 6.52 ms                                                | 7.25 ms: 1.11x slower                                                           |
| async_tree_io_tg                 | 497 ms                                                 | 563 ms: 1.13x slower                                                            |
| async_tree_io                    | 507 ms                                                 | 593 ms: 1.17x slower                                                            |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 711 ms: 1.49x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (5): tornado_http, pylint, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.086x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.55x