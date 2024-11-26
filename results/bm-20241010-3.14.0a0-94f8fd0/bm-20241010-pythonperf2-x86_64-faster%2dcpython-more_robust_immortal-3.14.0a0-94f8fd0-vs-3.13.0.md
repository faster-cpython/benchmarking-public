# Results vs. 3.13.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 280 ms: 1.04x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.87 sec: 1.02x slower                                                                |
| html5lib       | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                                 |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                                  |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                                  |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                                  |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 571 ms: 1.04x faster                                                                  |
| async_tree_io_tg           | 823 ms                                                       | 795 ms: 1.03x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                                 |
| async_tree_io              | 832 ms                                                       | 812 ms: 1.02x faster                                                                  |
| async_generators           | 364 ms                                                       | 358 ms: 1.02x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 89.2 ms: 1.03x faster                                                                 |
| float          | 81.6 ms                                                      | 79.7 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                                  |
| regex_effbot   | 3.51 ms                                                      | 3.57 ms: 1.02x slower                                                                 |
| regex_dna      | 238 ms                                                       | 247 ms: 1.04x slower                                                                  |
| regex_v8       | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads           | 24.7 us                                                      | 23.4 us: 1.06x faster                                                                 |
| pickle_pure_python   | 322 us                                                       | 312 us: 1.03x faster                                                                  |
| xml_etree_process    | 60.7 ms                                                      | 59.6 ms: 1.02x faster                                                                 |
| unpickle_pure_python | 216 us                                                       | 213 us: 1.01x faster                                                                  |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| xml_etree_generate   | 85.2 ms                                                      | 84.7 ms: 1.01x faster                                                                 |
| json_dumps           | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                                 |
| tomli_loads          | 2.43 sec                                                     | 2.52 sec: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                                 |
| python_startup_no_site | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                                 |
| genshi_xml      | 58.0 ms                                                      | 52.3 ms: 1.11x faster                                                                 |
| mako            | 10.3 ms                                                      | 10.6 ms: 1.03x slower                                                                 |
| django_template | 38.9 ms                                                      | 41.8 ms: 1.08x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 284 us: 1.37x faster                                                                  |
| deepcopy_memo              | 38.9 us                                                      | 28.9 us: 1.35x faster                                                                 |
| create_gc_cycles           | 2.65 ms                                                      | 2.02 ms: 1.31x faster                                                                 |
| go                         | 167 ms                                                       | 133 ms: 1.25x faster                                                                  |
| generators                 | 33.9 ms                                                      | 28.0 ms: 1.21x faster                                                                 |
| deepcopy_reduce            | 3.49 us                                                      | 2.90 us: 1.21x faster                                                                 |
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                                  |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                                 |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                                  |
| scimark_sor                | 125 ms                                                       | 108 ms: 1.16x faster                                                                  |
| genshi_text                | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                                 |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                                  |
| telco                      | 8.77 ms                                                      | 7.87 ms: 1.11x faster                                                                 |
| genshi_xml                 | 58.0 ms                                                      | 52.3 ms: 1.11x faster                                                                 |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                                  |
| json                       | 5.62 ms                                                      | 5.10 ms: 1.10x faster                                                                 |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 4.74 sec: 1.07x faster                                                                |
| fannkuch                   | 384 ms                                                       | 358 ms: 1.07x faster                                                                  |
| richards_super             | 60.2 ms                                                      | 56.8 ms: 1.06x faster                                                                 |
| nqueens                    | 92.3 ms                                                      | 87.2 ms: 1.06x faster                                                                 |
| json_loads                 | 24.7 us                                                      | 23.4 us: 1.06x faster                                                                 |
| pprint_pformat             | 1.70 sec                                                     | 1.61 sec: 1.06x faster                                                                |
| bench_thread_pool          | 929 us                                                       | 881 us: 1.05x faster                                                                  |
| pprint_safe_repr           | 835 ms                                                       | 792 ms: 1.05x faster                                                                  |
| pycparser                  | 1.28 sec                                                     | 1.22 sec: 1.05x faster                                                                |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                                  |
| thrift                     | 918 us                                                       | 878 us: 1.05x faster                                                                  |
| hexiom                     | 6.47 ms                                                      | 6.20 ms: 1.04x faster                                                                 |
| 2to3                       | 293 ms                                                       | 280 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 571 ms: 1.04x faster                                                                  |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                                  |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.04x faster                                                                  |
| async_tree_io_tg           | 823 ms                                                       | 795 ms: 1.03x faster                                                                  |
| richards                   | 52.5 ms                                                      | 50.8 ms: 1.03x faster                                                                 |
| coverage                   | 84.5 ms                                                      | 81.9 ms: 1.03x faster                                                                 |
| nbody                      | 92.1 ms                                                      | 89.2 ms: 1.03x faster                                                                 |
| html5lib                   | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                                 |
| pickle_pure_python         | 322 us                                                       | 312 us: 1.03x faster                                                                  |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                                  |
| scimark_lu                 | 97.4 ms                                                      | 94.8 ms: 1.03x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                                 |
| sympy_str                  | 297 ms                                                       | 289 ms: 1.02x faster                                                                  |
| async_tree_io              | 832 ms                                                       | 812 ms: 1.02x faster                                                                  |
| float                      | 81.6 ms                                                      | 79.7 ms: 1.02x faster                                                                 |
| pyflate                    | 493 ms                                                       | 481 ms: 1.02x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 95.3 ms: 1.02x faster                                                                 |
| comprehensions             | 17.3 us                                                      | 16.9 us: 1.02x faster                                                                 |
| sympy_expand               | 506 ms                                                       | 497 ms: 1.02x faster                                                                  |
| mdp                        | 2.53 sec                                                     | 2.48 sec: 1.02x faster                                                                |
| xml_etree_process          | 60.7 ms                                                      | 59.6 ms: 1.02x faster                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.14 ms: 1.02x faster                                                                 |
| typing_runtime_protocols   | 176 us                                                       | 173 us: 1.02x faster                                                                  |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                                  |
| async_generators           | 364 ms                                                       | 358 ms: 1.02x faster                                                                  |
| unpickle_pure_python       | 216 us                                                       | 213 us: 1.01x faster                                                                  |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| scimark_fft                | 298 ms                                                       | 294 ms: 1.01x faster                                                                  |
| scimark_monte_carlo        | 65.2 ms                                                      | 64.4 ms: 1.01x faster                                                                 |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                                                 |
| crypto_pyaes               | 73.5 ms                                                      | 72.9 ms: 1.01x faster                                                                 |
| deltablue                  | 3.38 ms                                                      | 3.36 ms: 1.01x faster                                                                 |
| xml_etree_generate         | 85.2 ms                                                      | 84.7 ms: 1.01x faster                                                                 |
| raytrace                   | 267 ms                                                       | 266 ms: 1.00x faster                                                                  |
| python_startup_no_site     | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                                 |
| sqlglot_optimize           | 58.7 ms                                                      | 59.5 ms: 1.01x slower                                                                 |
| regex_effbot               | 3.51 ms                                                      | 3.57 ms: 1.02x slower                                                                 |
| sqlglot_transpile          | 1.76 ms                                                      | 1.79 ms: 1.02x slower                                                                 |
| logging_format             | 6.95 us                                                      | 7.09 us: 1.02x slower                                                                 |
| chaos                      | 60.6 ms                                                      | 61.9 ms: 1.02x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.87 sec: 1.02x slower                                                                |
| json_dumps                 | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                                 |
| mako                       | 10.3 ms                                                      | 10.6 ms: 1.03x slower                                                                 |
| tomli_loads                | 2.43 sec                                                     | 2.52 sec: 1.03x slower                                                                |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                                                 |
| logging_simple             | 6.28 us                                                      | 6.50 us: 1.04x slower                                                                 |
| regex_dna                  | 238 ms                                                       | 247 ms: 1.04x slower                                                                  |
| regex_v8                   | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                                 |
| gc_traversal               | 4.48 ms                                                      | 4.74 ms: 1.06x slower                                                                 |
| django_template            | 38.9 ms                                                      | 41.8 ms: 1.08x slower                                                                 |
| bench_mp_pool              | 4.82 ms                                                      | 1.92 sec: 398.96x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                          |

Benchmark hidden because not significant (7): asyncio_websockets, pidigits, dulwich_log, pylint, sqlglot_normalize, xml_etree_iterparse, logging_silent
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x