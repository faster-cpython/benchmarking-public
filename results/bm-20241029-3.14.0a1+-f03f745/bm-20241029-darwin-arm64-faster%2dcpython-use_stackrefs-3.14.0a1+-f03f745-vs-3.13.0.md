# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.020x faster
- HPT reliability: 98.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 171 ms: 1.10x faster                                                      |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                                    |
| html5lib       | 36.6 ms                                                | 33.5 ms: 1.09x faster                                                     |
| sphinx         | 603 ms                                                 | 611 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 244 ms: 1.18x faster                                                      |
| coroutines                       | 19.8 ms                                                | 18.1 ms: 1.09x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                      |
| async_tree_eager                 | 70.1 ms                                                | 66.3 ms: 1.06x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 45.5 ms: 1.05x faster                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 134 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                      |
| async_generators                 | 295 ms                                                 | 289 ms: 1.02x faster                                                      |
| async_tree_none                  | 215 ms                                                 | 213 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 478 ms: 1.07x slower                                                      |
| async_tree_none_tg               | 198 ms                                                 | 224 ms: 1.13x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 596 ms: 1.18x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 640 ms: 1.29x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 695 ms: 1.35x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 740 ms: 1.55x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 64.9 ms: 1.14x faster                                                     |
| float          | 56.0 ms                                                | 51.4 ms: 1.09x faster                                                     |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                     |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                      |
| regex_compile  | 78.6 ms                                                | 74.2 ms: 1.06x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 209 us: 1.03x faster                                                      |
| xml_etree_process    | 41.0 ms                                                | 40.8 ms: 1.01x faster                                                     |
| unpickle_pure_python | 164 us                                                 | 167 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 74.8 ms: 1.02x slower                                                     |
| xml_etree_generate   | 57.0 ms                                                | 58.6 ms: 1.03x slower                                                     |
| tomli_loads          | 1.57 sec                                               | 1.64 sec: 1.04x slower                                                    |
| json_dumps           | 6.52 ms                                                | 7.37 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 12.4 ms: 1.16x faster                                                     |
| python_startup         | 18.9 ms                                                | 17.1 ms: 1.10x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.8 ms: 1.07x faster                                                     |
| mako            | 7.68 ms                                                | 7.35 ms: 1.04x faster                                                     |
| genshi_xml      | 34.4 ms                                                | 32.9 ms: 1.04x faster                                                     |
| django_template | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 17.8 us: 1.54x faster                                                     |
| deepcopy                         | 237 us                                                 | 155 us: 1.53x faster                                                      |
| generators                       | 31.5 ms                                                | 22.8 ms: 1.38x faster                                                     |
| deepcopy_reduce                  | 2.07 us                                                | 1.65 us: 1.26x faster                                                     |
| go                               | 115 ms                                                 | 96.4 ms: 1.19x faster                                                     |
| async_tree_memoization_tg        | 288 ms                                                 | 244 ms: 1.18x faster                                                      |
| python_startup_no_site           | 14.5 ms                                                | 12.4 ms: 1.16x faster                                                     |
| nbody                            | 74.0 ms                                                | 64.9 ms: 1.14x faster                                                     |
| pprint_safe_repr                 | 533 ms                                                 | 480 ms: 1.11x faster                                                      |
| pprint_pformat                   | 1.08 sec                                               | 979 ms: 1.11x faster                                                      |
| raytrace                         | 181 ms                                                 | 164 ms: 1.10x faster                                                      |
| python_startup                   | 18.9 ms                                                | 17.1 ms: 1.10x faster                                                     |
| 2to3                             | 187 ms                                                 | 171 ms: 1.10x faster                                                      |
| comprehensions                   | 12.3 us                                                | 11.2 us: 1.10x faster                                                     |
| coroutines                       | 19.8 ms                                                | 18.1 ms: 1.09x faster                                                     |
| scimark_monte_carlo              | 50.4 ms                                                | 46.2 ms: 1.09x faster                                                     |
| float                            | 56.0 ms                                                | 51.4 ms: 1.09x faster                                                     |
| html5lib                         | 36.6 ms                                                | 33.5 ms: 1.09x faster                                                     |
| nqueens                          | 62.5 ms                                                | 57.6 ms: 1.09x faster                                                     |
| sqlglot_parse                    | 856 us                                                 | 792 us: 1.08x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                      |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 15.8 ms: 1.07x faster                                                     |
| sqlglot_normalize                | 189 ms                                                 | 177 ms: 1.07x faster                                                      |
| bench_thread_pool                | 505 us                                                 | 474 us: 1.07x faster                                                      |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                      |
| sqlglot_transpile                | 1.02 ms                                                | 962 us: 1.06x faster                                                      |
| regex_compile                    | 78.6 ms                                                | 74.2 ms: 1.06x faster                                                     |
| deltablue                        | 2.68 ms                                                | 2.53 ms: 1.06x faster                                                     |
| bench_mp_pool                    | 62.5 ms                                                | 59.1 ms: 1.06x faster                                                     |
| async_tree_eager                 | 70.1 ms                                                | 66.3 ms: 1.06x faster                                                     |
| thrift                           | 466 us                                                 | 442 us: 1.05x faster                                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 45.5 ms: 1.05x faster                                                     |
| logging_simple                   | 3.60 us                                                | 3.44 us: 1.05x faster                                                     |
| sqlglot_optimize                 | 34.9 ms                                                | 33.3 ms: 1.05x faster                                                     |
| mako                             | 7.68 ms                                                | 7.35 ms: 1.04x faster                                                     |
| genshi_xml                       | 34.4 ms                                                | 32.9 ms: 1.04x faster                                                     |
| pycparser                        | 705 ms                                                 | 678 ms: 1.04x faster                                                      |
| coverage                         | 46.0 ms                                                | 44.2 ms: 1.04x faster                                                     |
| django_template                  | 22.2 ms                                                | 21.5 ms: 1.03x faster                                                     |
| hexiom                           | 4.86 ms                                                | 4.72 ms: 1.03x faster                                                     |
| json                             | 3.03 ms                                                | 2.94 ms: 1.03x faster                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 134 ms: 1.03x faster                                                      |
| sympy_sum                        | 75.4 ms                                                | 73.2 ms: 1.03x faster                                                     |
| logging_format                   | 3.89 us                                                | 3.78 us: 1.03x faster                                                     |
| chaos                            | 41.2 ms                                                | 40.0 ms: 1.03x faster                                                     |
| pickle_pure_python               | 214 us                                                 | 209 us: 1.03x faster                                                      |
| pathlib                          | 23.4 ms                                                | 22.8 ms: 1.03x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                      |
| scimark_sor                      | 105 ms                                                 | 103 ms: 1.02x faster                                                      |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.02x faster                                                      |
| async_generators                 | 295 ms                                                 | 289 ms: 1.02x faster                                                      |
| scimark_lu                       | 76.7 ms                                                | 75.3 ms: 1.02x faster                                                     |
| sympy_expand                     | 246 ms                                                 | 242 ms: 1.02x faster                                                      |
| logging_silent                   | 70.1 ns                                                | 69.0 ns: 1.02x faster                                                     |
| meteor_contest                   | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                     |
| telco                            | 4.76 ms                                                | 4.69 ms: 1.02x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 213 ms: 1.01x faster                                                      |
| pyflate                          | 351 ms                                                 | 347 ms: 1.01x faster                                                      |
| xml_etree_process                | 41.0 ms                                                | 40.8 ms: 1.01x faster                                                     |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| richards_super                   | 39.1 ms                                                | 39.2 ms: 1.00x slower                                                     |
| richards                         | 35.2 ms                                                | 35.3 ms: 1.00x slower                                                     |
| mdp                              | 1.49 sec                                               | 1.50 sec: 1.01x slower                                                    |
| dulwich_log                      | 28.5 ms                                                | 28.8 ms: 1.01x slower                                                     |
| gc_traversal                     | 2.91 ms                                                | 2.94 ms: 1.01x slower                                                     |
| shortest_path                    | 347 ms                                                 | 351 ms: 1.01x slower                                                      |
| sqlalchemy_declarative           | 58.9 ms                                                | 59.6 ms: 1.01x slower                                                     |
| scimark_fft                      | 201 ms                                                 | 203 ms: 1.01x slower                                                      |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.01x slower                                                     |
| sphinx                           | 603 ms                                                 | 611 ms: 1.01x slower                                                      |
| unpickle_pure_python             | 164 us                                                 | 167 us: 1.02x slower                                                      |
| xml_etree_iterparse              | 73.6 ms                                                | 74.8 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                                      |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                                    |
| spectral_norm                    | 76.3 ms                                                | 78.0 ms: 1.02x slower                                                     |
| connected_components             | 319 ms                                                 | 327 ms: 1.02x slower                                                      |
| xml_etree_generate               | 57.0 ms                                                | 58.6 ms: 1.03x slower                                                     |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.88 ms: 1.03x slower                                                     |
| bpe_tokeniser                    | 3.25 sec                                               | 3.35 sec: 1.03x slower                                                    |
| tomli_loads                      | 1.57 sec                                               | 1.64 sec: 1.04x slower                                                    |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.13 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 478 ms: 1.07x slower                                                      |
| crypto_pyaes                     | 54.2 ms                                                | 58.6 ms: 1.08x slower                                                     |
| json_dumps                       | 6.52 ms                                                | 7.37 ms: 1.13x slower                                                     |
| async_tree_none_tg               | 198 ms                                                 | 224 ms: 1.13x slower                                                      |
| create_gc_cycles                 | 1.17 ms                                                | 1.33 ms: 1.14x slower                                                     |
| async_tree_io                    | 507 ms                                                 | 596 ms: 1.18x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 640 ms: 1.29x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 695 ms: 1.35x slower                                                      |
| k_core                           | 1.61 sec                                               | 2.32 sec: 1.45x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 740 ms: 1.55x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (8): async_tree_memoization, xml_etree_parse, typing_runtime_protocols, fannkuch, json_loads, asyncio_websockets, pylint, tornado_http
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2
Ignored benchmarks (1) of results/bm-20241029-3.14.0a1+-f03f745/bm-20241029-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745.json: sqlite_synth

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 98.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x