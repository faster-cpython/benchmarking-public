# Results vs. 3.13.0

- fork: faster-cpython
- ref: more_untracking
- machine: linux-x86_64
- commit hash: 1746ca4
- commit date: 2024-10-29
- overall geometric mean: 1.016x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                              |
| docutils       | 2.81 sec                                                     | 2.93 sec: 1.04x slower                                                            |
| html5lib       | 72.9 ms                                                      | 71.7 ms: 1.02x faster                                                             |
| sphinx         | 1.11 sec                                                     | 1.13 sec: 1.02x slower                                                            |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 378 ms: 1.21x faster                                                              |
| async_tree_none            | 370 ms                                                       | 340 ms: 1.09x faster                                                              |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.08x faster                                                              |
| async_tree_none_tg         | 342 ms                                                       | 325 ms: 1.05x faster                                                              |
| async_generators           | 364 ms                                                       | 352 ms: 1.03x faster                                                              |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 578 ms: 1.03x faster                                                              |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                              |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 565 ms: 1.02x faster                                                              |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                             |
| async_tree_io_tg           | 823 ms                                                       | 866 ms: 1.05x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 83.1 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                              |
| regex_effbot   | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                             |
| regex_v8       | 24.9 ms                                                      | 25.4 ms: 1.02x slower                                                             |
| regex_dna      | 238 ms                                                       | 243 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 24.7 us                                                      | 24.4 us: 1.01x faster                                                             |
| unpickle_pure_python | 216 us                                                       | 215 us: 1.00x faster                                                              |
| xml_etree_generate   | 85.2 ms                                                      | 86.0 ms: 1.01x slower                                                             |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                              |
| pickle_pure_python   | 322 us                                                       | 328 us: 1.02x slower                                                              |
| tomli_loads          | 2.43 sec                                                     | 2.49 sec: 1.02x slower                                                            |
| xml_etree_iterparse  | 99.8 ms                                                      | 104 ms: 1.04x slower                                                              |
| json_dumps           | 10.8 ms                                                      | 11.6 ms: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 8.91 ms: 1.00x faster                                                             |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.6 ms: 1.10x faster                                                             |
| genshi_xml      | 58.0 ms                                                      | 53.9 ms: 1.08x faster                                                             |
| django_template | 38.9 ms                                                      | 40.0 ms: 1.03x slower                                                             |
| mako            | 10.3 ms                                                      | 10.8 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 300 us: 1.29x faster                                                              |
| deepcopy_memo              | 38.9 us                                                      | 30.4 us: 1.28x faster                                                             |
| go                         | 167 ms                                                       | 136 ms: 1.23x faster                                                              |
| async_tree_memoization_tg  | 458 ms                                                       | 378 ms: 1.21x faster                                                              |
| deepcopy_reduce            | 3.49 us                                                      | 2.99 us: 1.17x faster                                                             |
| generators                 | 33.9 ms                                                      | 29.4 ms: 1.16x faster                                                             |
| genshi_text                | 27.2 ms                                                      | 24.6 ms: 1.10x faster                                                             |
| scimark_sor                | 125 ms                                                       | 113 ms: 1.10x faster                                                              |
| telco                      | 8.77 ms                                                      | 7.98 ms: 1.10x faster                                                             |
| json                       | 5.62 ms                                                      | 5.13 ms: 1.10x faster                                                             |
| async_tree_none            | 370 ms                                                       | 340 ms: 1.09x faster                                                              |
| richards_super             | 60.2 ms                                                      | 55.4 ms: 1.09x faster                                                             |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.08x faster                                                              |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                             |
| genshi_xml                 | 58.0 ms                                                      | 53.9 ms: 1.08x faster                                                             |
| richards                   | 52.5 ms                                                      | 49.1 ms: 1.07x faster                                                             |
| fannkuch                   | 384 ms                                                       | 361 ms: 1.06x faster                                                              |
| bpe_tokeniser              | 5.09 sec                                                     | 4.81 sec: 1.06x faster                                                            |
| pprint_safe_repr           | 835 ms                                                       | 791 ms: 1.06x faster                                                              |
| async_tree_none_tg         | 342 ms                                                       | 325 ms: 1.05x faster                                                              |
| sqlalchemy_declarative     | 148 ms                                                       | 141 ms: 1.05x faster                                                              |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                            |
| thrift                     | 918 us                                                       | 874 us: 1.05x faster                                                              |
| shortest_path              | 477 ms                                                       | 457 ms: 1.05x faster                                                              |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                              |
| nqueens                    | 92.3 ms                                                      | 89.4 ms: 1.03x faster                                                             |
| async_generators           | 364 ms                                                       | 352 ms: 1.03x faster                                                              |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 578 ms: 1.03x faster                                                              |
| pycparser                  | 1.28 sec                                                     | 1.24 sec: 1.03x faster                                                            |
| connected_components       | 443 ms                                                       | 430 ms: 1.03x faster                                                              |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                              |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                              |
| bench_thread_pool          | 929 us                                                       | 905 us: 1.03x faster                                                              |
| hexiom                     | 6.47 ms                                                      | 6.30 ms: 1.03x faster                                                             |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.02x faster                                                              |
| scimark_fft                | 298 ms                                                       | 292 ms: 1.02x faster                                                              |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                              |
| html5lib                   | 72.9 ms                                                      | 71.7 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 565 ms: 1.02x faster                                                              |
| typing_runtime_protocols   | 176 us                                                       | 173 us: 1.02x faster                                                              |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                              |
| json_loads                 | 24.7 us                                                      | 24.4 us: 1.01x faster                                                             |
| sympy_expand               | 506 ms                                                       | 501 ms: 1.01x faster                                                              |
| scimark_monte_carlo        | 65.2 ms                                                      | 64.5 ms: 1.01x faster                                                             |
| sympy_str                  | 297 ms                                                       | 294 ms: 1.01x faster                                                              |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                             |
| coverage                   | 84.5 ms                                                      | 83.8 ms: 1.01x faster                                                             |
| scimark_lu                 | 97.4 ms                                                      | 96.5 ms: 1.01x faster                                                             |
| unpickle_pure_python       | 216 us                                                       | 215 us: 1.00x faster                                                              |
| python_startup_no_site     | 8.93 ms                                                      | 8.91 ms: 1.00x faster                                                             |
| mdp                        | 2.53 sec                                                     | 2.52 sec: 1.00x faster                                                            |
| xml_etree_generate         | 85.2 ms                                                      | 86.0 ms: 1.01x slower                                                             |
| logging_format             | 6.95 us                                                      | 7.03 us: 1.01x slower                                                             |
| logging_simple             | 6.28 us                                                      | 6.35 us: 1.01x slower                                                             |
| regex_effbot               | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                             |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                              |
| comprehensions             | 17.3 us                                                      | 17.6 us: 1.02x slower                                                             |
| regex_v8                   | 24.9 ms                                                      | 25.4 ms: 1.02x slower                                                             |
| regex_dna                  | 238 ms                                                       | 243 ms: 1.02x slower                                                              |
| float                      | 81.6 ms                                                      | 83.1 ms: 1.02x slower                                                             |
| sphinx                     | 1.11 sec                                                     | 1.13 sec: 1.02x slower                                                            |
| deltablue                  | 3.38 ms                                                      | 3.45 ms: 1.02x slower                                                             |
| dulwich_log                | 65.5 ms                                                      | 66.8 ms: 1.02x slower                                                             |
| pickle_pure_python         | 322 us                                                       | 328 us: 1.02x slower                                                              |
| logging_silent             | 97.5 ns                                                      | 99.6 ns: 1.02x slower                                                             |
| sqlglot_normalize          | 119 ms                                                       | 122 ms: 1.02x slower                                                              |
| tomli_loads                | 2.43 sec                                                     | 2.49 sec: 1.02x slower                                                            |
| sqlglot_optimize           | 58.7 ms                                                      | 60.1 ms: 1.02x slower                                                             |
| spectral_norm              | 97.4 ms                                                      | 99.9 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.32 ms: 1.03x slower                                                             |
| sqlglot_transpile          | 1.76 ms                                                      | 1.81 ms: 1.03x slower                                                             |
| django_template            | 38.9 ms                                                      | 40.0 ms: 1.03x slower                                                             |
| create_gc_cycles           | 2.65 ms                                                      | 2.73 ms: 1.03x slower                                                             |
| chaos                      | 60.6 ms                                                      | 62.7 ms: 1.03x slower                                                             |
| xml_etree_iterparse        | 99.8 ms                                                      | 104 ms: 1.04x slower                                                              |
| docutils                   | 2.81 sec                                                     | 2.93 sec: 1.04x slower                                                            |
| mako                       | 10.3 ms                                                      | 10.8 ms: 1.04x slower                                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.43 ms: 1.05x slower                                                             |
| async_tree_io_tg           | 823 ms                                                       | 866 ms: 1.05x slower                                                              |
| raytrace                   | 267 ms                                                       | 282 ms: 1.05x slower                                                              |
| json_dumps                 | 10.8 ms                                                      | 11.6 ms: 1.07x slower                                                             |
| gc_traversal               | 4.48 ms                                                      | 5.52 ms: 1.23x slower                                                             |
| k_core                     | 2.18 sec                                                     | 3.08 sec: 1.42x slower                                                            |
| bench_mp_pool              | 4.82 ms                                                      | 1.47 sec: 305.53x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                      |

Benchmark hidden because not significant (10): nbody, xml_etree_process, crypto_pyaes, sympy_integrate, pidigits, pyflate, python_startup, sqlalchemy_imperative, async_tree_io, pylint
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x