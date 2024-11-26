# Results vs. 3.12.0

- fork: faster-cpython
- ref: more_untracking
- machine: linux-x86_64
- commit hash: 1746ca4
- commit date: 2024-10-29
- overall geometric mean: 1.012x faster
- HPT reliability: 88.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                              |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                            |
| tornado_http   | 121 ms                                                       | 116 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 378 ms: 1.43x faster                                                              |
| async_tree_none            | 452 ms                                                       | 340 ms: 1.33x faster                                                              |
| async_tree_none_tg         | 431 ms                                                       | 325 ms: 1.33x faster                                                              |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 839 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 565 ms: 1.23x faster                                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 866 ms: 1.22x faster                                                              |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                              |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                              |
| nbody          | 88.0 ms                                                      | 91.1 ms: 1.04x slower                                                             |
| float          | 76.6 ms                                                      | 83.1 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                              |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                             |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                              |
| regex_v8       | 23.6 ms                                                      | 25.4 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                                              |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                              |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.03x slower                                                              |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                              |
| xml_etree_process    | 58.4 ms                                                      | 60.5 ms: 1.04x slower                                                             |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                             |
| tomli_loads          | 2.16 sec                                                     | 2.49 sec: 1.15x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.91 ms: 1.03x slower                                                             |
| python_startup         | 11.6 ms                                                      | 15.7 ms: 1.35x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 40.0 ms: 1.05x slower                                                             |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                             |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 378 ms: 1.43x faster                                                              |
| async_tree_none            | 452 ms                                                       | 340 ms: 1.33x faster                                                              |
| async_tree_none_tg         | 431 ms                                                       | 325 ms: 1.33x faster                                                              |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                              |
| generators                 | 37.4 ms                                                      | 29.4 ms: 1.28x faster                                                             |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.25x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 839 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 565 ms: 1.23x faster                                                              |
| deepcopy                   | 368 us                                                       | 300 us: 1.23x faster                                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 866 ms: 1.22x faster                                                              |
| deepcopy_memo              | 36.8 us                                                      | 30.4 us: 1.21x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                              |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.18x faster                                                             |
| sqlalchemy_declarative     | 159 ms                                                       | 141 ms: 1.13x faster                                                              |
| deepcopy_reduce            | 3.37 us                                                      | 2.99 us: 1.13x faster                                                             |
| async_generators           | 390 ms                                                       | 352 ms: 1.11x faster                                                              |
| go                         | 150 ms                                                       | 136 ms: 1.10x faster                                                              |
| crypto_pyaes               | 80.3 ms                                                      | 73.4 ms: 1.10x faster                                                             |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.08x faster                                                             |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                              |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.5 ms: 1.07x faster                                                             |
| logging_format             | 7.48 us                                                      | 7.03 us: 1.06x faster                                                             |
| raytrace                   | 298 ms                                                       | 282 ms: 1.06x faster                                                              |
| logging_simple             | 6.71 us                                                      | 6.35 us: 1.06x faster                                                             |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                              |
| bench_thread_pool          | 950 us                                                       | 905 us: 1.05x faster                                                              |
| tornado_http               | 121 ms                                                       | 116 ms: 1.05x faster                                                              |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                              |
| scimark_fft                | 301 ms                                                       | 292 ms: 1.03x faster                                                              |
| sympy_str                  | 302 ms                                                       | 294 ms: 1.03x faster                                                              |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.03x faster                                                             |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                             |
| scimark_lu                 | 98.8 ms                                                      | 96.5 ms: 1.02x faster                                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                            |
| chaos                      | 64.0 ms                                                      | 62.7 ms: 1.02x faster                                                             |
| pprint_safe_repr           | 807 ms                                                       | 791 ms: 1.02x faster                                                              |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                            |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                              |
| nqueens                    | 89.9 ms                                                      | 89.4 ms: 1.01x faster                                                             |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                             |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                              |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                                              |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                              |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                              |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                             |
| dulwich_log                | 65.4 ms                                                      | 66.8 ms: 1.02x slower                                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.32 ms: 1.03x slower                                                             |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.03x slower                                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.91 ms: 1.03x slower                                                             |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                              |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                              |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.03x slower                                                              |
| nbody                      | 88.0 ms                                                      | 91.1 ms: 1.04x slower                                                             |
| xml_etree_process          | 58.4 ms                                                      | 60.5 ms: 1.04x slower                                                             |
| scimark_sor                | 109 ms                                                       | 113 ms: 1.04x slower                                                              |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 60.1 ms: 1.05x slower                                                             |
| django_template            | 38.2 ms                                                      | 40.0 ms: 1.05x slower                                                             |
| sqlglot_normalize          | 116 ms                                                       | 122 ms: 1.05x slower                                                              |
| logging_silent             | 94.4 ns                                                      | 99.6 ns: 1.06x slower                                                             |
| hexiom                     | 5.96 ms                                                      | 6.30 ms: 1.06x slower                                                             |
| deltablue                  | 3.24 ms                                                      | 3.45 ms: 1.07x slower                                                             |
| regex_v8                   | 23.6 ms                                                      | 25.4 ms: 1.07x slower                                                             |
| richards                   | 45.7 ms                                                      | 49.1 ms: 1.07x slower                                                             |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                             |
| richards_super             | 51.3 ms                                                      | 55.4 ms: 1.08x slower                                                             |
| float                      | 76.6 ms                                                      | 83.1 ms: 1.08x slower                                                             |
| spectral_norm              | 91.6 ms                                                      | 99.9 ms: 1.09x slower                                                             |
| pyflate                    | 439 ms                                                       | 492 ms: 1.12x slower                                                              |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                             |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                              |
| telco                      | 6.96 ms                                                      | 7.98 ms: 1.15x slower                                                             |
| tomli_loads                | 2.16 sec                                                     | 2.49 sec: 1.15x slower                                                            |
| coverage                   | 66.7 ms                                                      | 83.8 ms: 1.26x slower                                                             |
| python_startup             | 11.6 ms                                                      | 15.7 ms: 1.35x slower                                                             |
| gc_traversal               | 3.48 ms                                                      | 5.52 ms: 1.59x slower                                                             |
| create_gc_cycles           | 1.59 ms                                                      | 2.73 ms: 1.72x slower                                                             |
| bench_mp_pool              | 4.76 ms                                                      | 1.47 sec: 308.99x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                      |

Benchmark hidden because not significant (5): xml_etree_generate, asyncio_websockets, json, json_loads, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241029-3.14.0a1+-1746ca4/bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.012x faster
# HPT report

- Reliability score: 88.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x