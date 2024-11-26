# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.010x faster
- HPT reliability: 58.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 191 ms: 1.02x slower                                                      |
| docutils       | 1.44 sec                                               | 1.58 sec: 1.10x slower                                                    |
| html5lib       | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                     |
| sphinx         | 603 ms                                                 | 670 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.22x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 42.4 ms: 1.13x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                      |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                      |
| async_tree_eager                 | 70.1 ms                                                | 65.9 ms: 1.06x faster                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                      |
| async_generators                 | 295 ms                                                 | 298 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 468 ms: 1.04x slower                                                      |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 586 ms: 1.16x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 614 ms: 1.24x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 717 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 49.8 ms: 1.13x faster                                                     |
| nbody          | 74.0 ms                                                | 66.1 ms: 1.12x faster                                                     |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                     |
| regex_dna      | 149 ms                                                 | 142 ms: 1.05x faster                                                      |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                     |
| regex_compile  | 78.6 ms                                                | 79.4 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 137 us: 1.20x faster                                                      |
| pickle_pure_python   | 214 us                                                 | 181 us: 1.18x faster                                                      |
| tomli_loads          | 1.57 sec                                               | 1.33 sec: 1.18x faster                                                    |
| xml_etree_process    | 41.0 ms                                                | 35.7 ms: 1.15x faster                                                     |
| xml_etree_generate   | 57.0 ms                                                | 51.2 ms: 1.11x faster                                                     |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                                     |
| json_dumps           | 6.52 ms                                                | 7.23 ms: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 18.0 ms: 1.05x faster                                                     |
| python_startup_no_site | 14.5 ms                                                | 14.0 ms: 1.03x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 7.03 ms: 1.09x faster                                                     |
| genshi_text     | 16.9 ms                                                | 16.8 ms: 1.00x faster                                                     |
| django_template | 22.2 ms                                                | 25.0 ms: 1.13x slower                                                     |
| genshi_xml      | 34.4 ms                                                | 45.7 ms: 1.33x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 18.1 us: 1.51x faster                                                     |
| deepcopy                         | 237 us                                                 | 163 us: 1.45x faster                                                      |
| deepcopy_reduce                  | 2.07 us                                                | 1.54 us: 1.35x faster                                                     |
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.22x faster                                                      |
| generators                       | 31.5 ms                                                | 26.0 ms: 1.21x faster                                                     |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                     |
| unpickle_pure_python             | 164 us                                                 | 137 us: 1.20x faster                                                      |
| pickle_pure_python               | 214 us                                                 | 181 us: 1.18x faster                                                      |
| tomli_loads                      | 1.57 sec                                               | 1.33 sec: 1.18x faster                                                    |
| scimark_lu                       | 76.7 ms                                                | 66.1 ms: 1.16x faster                                                     |
| scimark_sor                      | 105 ms                                                 | 91.6 ms: 1.15x faster                                                     |
| xml_etree_process                | 41.0 ms                                                | 35.7 ms: 1.15x faster                                                     |
| logging_simple                   | 3.60 us                                                | 3.18 us: 1.13x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 42.4 ms: 1.13x faster                                                     |
| float                            | 56.0 ms                                                | 49.8 ms: 1.13x faster                                                     |
| nbody                            | 74.0 ms                                                | 66.1 ms: 1.12x faster                                                     |
| logging_format                   | 3.89 us                                                | 3.48 us: 1.12x faster                                                     |
| xml_etree_generate               | 57.0 ms                                                | 51.2 ms: 1.11x faster                                                     |
| html5lib                         | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                     |
| thrift                           | 466 us                                                 | 422 us: 1.11x faster                                                      |
| mako                             | 7.68 ms                                                | 7.03 ms: 1.09x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                      |
| go                               | 115 ms                                                 | 106 ms: 1.08x faster                                                      |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                      |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                     |
| deltablue                        | 2.68 ms                                                | 2.51 ms: 1.07x faster                                                     |
| telco                            | 4.76 ms                                                | 4.47 ms: 1.07x faster                                                     |
| async_tree_eager                 | 70.1 ms                                                | 65.9 ms: 1.06x faster                                                     |
| json                             | 3.03 ms                                                | 2.87 ms: 1.06x faster                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                                      |
| coverage                         | 46.0 ms                                                | 43.5 ms: 1.06x faster                                                     |
| scimark_monte_carlo              | 50.4 ms                                                | 47.9 ms: 1.05x faster                                                     |
| python_startup                   | 18.9 ms                                                | 18.0 ms: 1.05x faster                                                     |
| regex_dna                        | 149 ms                                                 | 142 ms: 1.05x faster                                                      |
| bench_thread_pool                | 505 us                                                 | 481 us: 1.05x faster                                                      |
| pathlib                          | 23.4 ms                                                | 22.4 ms: 1.04x faster                                                     |
| spectral_norm                    | 76.3 ms                                                | 73.6 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.03x faster                                                      |
| bpe_tokeniser                    | 3.25 sec                                               | 3.14 sec: 1.03x faster                                                    |
| python_startup_no_site           | 14.5 ms                                                | 14.0 ms: 1.03x faster                                                     |
| fannkuch                         | 284 ms                                                 | 275 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                      |
| pyflate                          | 351 ms                                                 | 343 ms: 1.02x faster                                                      |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                                     |
| raytrace                         | 181 ms                                                 | 178 ms: 1.02x faster                                                      |
| typing_runtime_protocols         | 101 us                                                 | 99.5 us: 1.02x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                     |
| bench_mp_pool                    | 62.5 ms                                                | 61.6 ms: 1.01x faster                                                     |
| nqueens                          | 62.5 ms                                                | 61.6 ms: 1.01x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 16.8 ms: 1.00x faster                                                     |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.73 ms: 1.01x slower                                                     |
| async_generators                 | 295 ms                                                 | 298 ms: 1.01x slower                                                      |
| regex_compile                    | 78.6 ms                                                | 79.4 ms: 1.01x slower                                                     |
| scimark_fft                      | 201 ms                                                 | 203 ms: 1.01x slower                                                      |
| gc_traversal                     | 2.91 ms                                                | 2.94 ms: 1.01x slower                                                     |
| 2to3                             | 187 ms                                                 | 191 ms: 1.02x slower                                                      |
| richards                         | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                     |
| crypto_pyaes                     | 54.2 ms                                                | 55.6 ms: 1.02x slower                                                     |
| richards_super                   | 39.1 ms                                                | 40.1 ms: 1.03x slower                                                     |
| sqlglot_normalize                | 189 ms                                                 | 195 ms: 1.03x slower                                                      |
| sympy_expand                     | 246 ms                                                 | 256 ms: 1.04x slower                                                      |
| meteor_contest                   | 74.0 ms                                                | 76.8 ms: 1.04x slower                                                     |
| mdp                              | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                    |
| pprint_pformat                   | 1.08 sec                                               | 1.13 sec: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 468 ms: 1.04x slower                                                      |
| dulwich_log                      | 28.5 ms                                                | 29.8 ms: 1.05x slower                                                     |
| sqlalchemy_declarative           | 58.9 ms                                                | 62.4 ms: 1.06x slower                                                     |
| chaos                            | 41.2 ms                                                | 43.7 ms: 1.06x slower                                                     |
| logging_silent                   | 70.1 ns                                                | 74.8 ns: 1.07x slower                                                     |
| sqlglot_parse                    | 856 us                                                 | 916 us: 1.07x slower                                                      |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                      |
| sympy_str                        | 145 ms                                                 | 158 ms: 1.08x slower                                                      |
| sympy_sum                        | 75.4 ms                                                | 82.6 ms: 1.10x slower                                                     |
| docutils                         | 1.44 sec                                               | 1.58 sec: 1.10x slower                                                    |
| sqlglot_transpile                | 1.02 ms                                                | 1.12 ms: 1.10x slower                                                     |
| json_dumps                       | 6.52 ms                                                | 7.23 ms: 1.11x slower                                                     |
| sphinx                           | 603 ms                                                 | 670 ms: 1.11x slower                                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 39.1 ms: 1.12x slower                                                     |
| django_template                  | 22.2 ms                                                | 25.0 ms: 1.13x slower                                                     |
| hexiom                           | 4.86 ms                                                | 5.52 ms: 1.14x slower                                                     |
| create_gc_cycles                 | 1.17 ms                                                | 1.33 ms: 1.14x slower                                                     |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.42 ms: 1.15x slower                                                     |
| async_tree_io                    | 507 ms                                                 | 586 ms: 1.16x slower                                                      |
| comprehensions                   | 12.3 us                                                | 14.3 us: 1.17x slower                                                     |
| sympy_integrate                  | 11.3 ms                                                | 13.2 ms: 1.17x slower                                                     |
| pylint                           | 180 ms                                                 | 217 ms: 1.21x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 614 ms: 1.24x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                                      |
| genshi_xml                       | 34.4 ms                                                | 45.7 ms: 1.33x slower                                                     |
| async_tree_eager_io_tg           | 477 ms                                                 | 717 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (7): tornado_http, async_tree_cpu_io_mixed, pycparser, pprint_safe_repr, asyncio_websockets, xml_etree_parse, xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 58.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x