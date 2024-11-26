# Results vs. base

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.002x faster
- HPT reliability: 54.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-pythonperf2-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.93 sec                                                                     | 2.92 sec: 1.00x faster                                                   |
| html5lib       | 71.9 ms                                                                      | 71.0 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241116-pythonperf2-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators | 446 ms                                                                       | 436 ms: 1.02x faster                                                     |
| Geometric mean   | (ref)                                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_io, async_tree_io_tg, asyncio_websockets, async_tree_none, async_tree_none_tg, coroutines, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-pythonperf2-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 82.2 ms                                                                      | 80.5 ms: 1.02x faster                                                    |
| nbody          | 89.6 ms                                                                      | 91.3 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-pythonperf2-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 248 ms                                                                       | 242 ms: 1.02x faster                                                     |
| regex_compile  | 139 ms                                                                       | 139 ms: 1.01x faster                                                     |
| regex_v8       | 26.3 ms                                                                      | 26.2 ms: 1.00x faster                                                    |
| regex_effbot   | 3.57 ms                                                                      | 3.61 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241116-pythonperf2-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.48 sec                                                                     | 2.42 sec: 1.03x faster                                                   |
| unpickle_pure_python | 218 us                                                                       | 215 us: 1.01x faster                                                     |
| xml_etree_process    | 60.5 ms                                                                      | 59.9 ms: 1.01x faster                                                    |
| json_dumps           | 11.4 ms                                                                      | 11.5 ms: 1.00x slower                                                    |
| xml_etree_iterparse  | 103 ms                                                                       | 104 ms: 1.01x slower                                                     |
| xml_etree_generate   | 85.8 ms                                                                      | 87.3 ms: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20241116-pythonperf2-x86_64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|--------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| spectral_norm            | 96.5 ms                                                                      | 87.3 ms: 1.11x faster                                                    |
| gc_traversal             | 6.59 ms                                                                      | 6.15 ms: 1.07x faster                                                    |
| richards_super           | 57.3 ms                                                                      | 55.6 ms: 1.03x faster                                                    |
| generators               | 30.1 ms                                                                      | 29.3 ms: 1.03x faster                                                    |
| logging_format           | 7.22 us                                                                      | 7.03 us: 1.03x faster                                                    |
| scimark_sparse_mat_mult  | 4.74 ms                                                                      | 4.61 ms: 1.03x faster                                                    |
| tomli_loads              | 2.48 sec                                                                     | 2.42 sec: 1.03x faster                                                   |
| telco                    | 8.09 ms                                                                      | 7.88 ms: 1.03x faster                                                    |
| richards                 | 50.6 ms                                                                      | 49.3 ms: 1.03x faster                                                    |
| pycparser                | 1.24 sec                                                                     | 1.21 sec: 1.02x faster                                                   |
| dulwich_log              | 68.2 ms                                                                      | 66.7 ms: 1.02x faster                                                    |
| regex_dna                | 248 ms                                                                       | 242 ms: 1.02x faster                                                     |
| async_generators         | 446 ms                                                                       | 436 ms: 1.02x faster                                                     |
| float                    | 82.2 ms                                                                      | 80.5 ms: 1.02x faster                                                    |
| sqlite_synth             | 2.87 us                                                                      | 2.81 us: 1.02x faster                                                    |
| deepcopy                 | 291 us                                                                       | 286 us: 1.02x faster                                                     |
| logging_simple           | 6.63 us                                                                      | 6.54 us: 1.01x faster                                                    |
| unpickle_pure_python     | 218 us                                                                       | 215 us: 1.01x faster                                                     |
| k_core                   | 3.08 sec                                                                     | 3.03 sec: 1.01x faster                                                   |
| create_gc_cycles         | 3.04 ms                                                                      | 3.00 ms: 1.01x faster                                                    |
| html5lib                 | 71.9 ms                                                                      | 71.0 ms: 1.01x faster                                                    |
| nqueens                  | 89.6 ms                                                                      | 88.6 ms: 1.01x faster                                                    |
| comprehensions           | 17.7 us                                                                      | 17.5 us: 1.01x faster                                                    |
| mdp                      | 2.50 sec                                                                     | 2.47 sec: 1.01x faster                                                   |
| xml_etree_process        | 60.5 ms                                                                      | 59.9 ms: 1.01x faster                                                    |
| thrift                   | 865 us                                                                       | 858 us: 1.01x faster                                                     |
| deepcopy_memo            | 29.7 us                                                                      | 29.5 us: 1.01x faster                                                    |
| sqlglot_optimize         | 59.4 ms                                                                      | 59.0 ms: 1.01x faster                                                    |
| regex_compile            | 139 ms                                                                       | 139 ms: 1.01x faster                                                     |
| regex_v8                 | 26.3 ms                                                                      | 26.2 ms: 1.00x faster                                                    |
| sqlglot_transpile        | 1.80 ms                                                                      | 1.79 ms: 1.00x faster                                                    |
| docutils                 | 2.93 sec                                                                     | 2.92 sec: 1.00x faster                                                   |
| hexiom                   | 6.27 ms                                                                      | 6.28 ms: 1.00x slower                                                    |
| logging_silent           | 99.7 ns                                                                      | 100.0 ns: 1.00x slower                                                   |
| json_dumps               | 11.4 ms                                                                      | 11.5 ms: 1.00x slower                                                    |
| sympy_str                | 293 ms                                                                       | 294 ms: 1.00x slower                                                     |
| meteor_contest           | 124 ms                                                                       | 125 ms: 1.01x slower                                                     |
| xml_etree_iterparse      | 103 ms                                                                       | 104 ms: 1.01x slower                                                     |
| pprint_pformat           | 1.61 sec                                                                     | 1.62 sec: 1.01x slower                                                   |
| subparsers               | 23.0 ms                                                                      | 23.2 ms: 1.01x slower                                                    |
| pathlib                  | 16.2 ms                                                                      | 16.3 ms: 1.01x slower                                                    |
| sympy_expand             | 499 ms                                                                       | 504 ms: 1.01x slower                                                     |
| deepcopy_reduce          | 2.92 us                                                                      | 2.95 us: 1.01x slower                                                    |
| deltablue                | 3.48 ms                                                                      | 3.52 ms: 1.01x slower                                                    |
| scimark_lu               | 97.4 ms                                                                      | 98.4 ms: 1.01x slower                                                    |
| regex_effbot             | 3.57 ms                                                                      | 3.61 ms: 1.01x slower                                                    |
| connected_components     | 428 ms                                                                       | 433 ms: 1.01x slower                                                     |
| shortest_path            | 450 ms                                                                       | 457 ms: 1.02x slower                                                     |
| xml_etree_generate       | 85.8 ms                                                                      | 87.3 ms: 1.02x slower                                                    |
| bpe_tokeniser            | 4.83 sec                                                                     | 4.91 sec: 1.02x slower                                                   |
| nbody                    | 89.6 ms                                                                      | 91.3 ms: 1.02x slower                                                    |
| go                       | 134 ms                                                                       | 136 ms: 1.02x slower                                                     |
| pyflate                  | 478 ms                                                                       | 488 ms: 1.02x slower                                                     |
| typing_runtime_protocols | 173 us                                                                       | 177 us: 1.03x slower                                                     |
| crypto_pyaes             | 72.0 ms                                                                      | 75.1 ms: 1.04x slower                                                    |
| scimark_monte_carlo      | 63.6 ms                                                                      | 66.5 ms: 1.05x slower                                                    |
| fannkuch                 | 350 ms                                                                       | 376 ms: 1.07x slower                                                     |
| scimark_sor              | 117 ms                                                                       | 126 ms: 1.08x slower                                                     |
| coverage                 | 76.8 ms                                                                      | 83.7 ms: 1.09x slower                                                    |
| Geometric mean           | (ref)                                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (38): bench_mp_pool, sqlalchemy_imperative, mako, raytrace, async_tree_memoization, pickle_pure_python, async_tree_io, async_tree_io_tg, pidigits, django_template, 2to3, many_optionals, asyncio_websockets, xml_etree_parse, sphinx, json_loads, djangocms, sqlalchemy_declarative, async_tree_none, python_startup_no_site, python_startup, sympy_integrate, chaos, pylint, async_tree_none_tg, coroutines, scimark_fft, sqlglot_parse, sqlglot_normalize, sympy_sum, genshi_text, async_tree_cpu_io_mixed, pprint_safe_repr, async_tree_memoization_tg, json, async_tree_cpu_io_mixed_tg, genshi_xml, bench_thread_pool

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 54.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x