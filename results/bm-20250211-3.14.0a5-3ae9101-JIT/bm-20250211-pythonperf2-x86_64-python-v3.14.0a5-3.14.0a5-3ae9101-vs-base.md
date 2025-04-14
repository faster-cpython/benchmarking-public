# Results vs. base

- fork: python
- ref: v3.14.0a5
- machine: linux-x86_64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.002x faster
- HPT reliability: 94.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| docutils       | 2.98 sec                                                                     | 2.94 sec: 1.01x faster                                           |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg       | 657 ms                                                                       | 644 ms: 1.02x faster                                             |
| asyncio_websockets     | 389 ms                                                                       | 384 ms: 1.01x faster                                             |
| async_generators       | 426 ms                                                                       | 428 ms: 1.00x slower                                             |
| coroutines             | 21.0 ms                                                                      | 21.1 ms: 1.01x slower                                            |
| async_tree_memoization | 356 ms                                                                       | 359 ms: 1.01x slower                                             |
| async_tree_none        | 292 ms                                                                       | 296 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 104 ms                                                                       | 101 ms: 1.04x faster                                             |
| pidigits       | 254 ms                                                                       | 253 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 25.2 ms                                                                      | 24.5 ms: 1.03x faster                                            |
| regex_compile  | 137 ms                                                                       | 136 ms: 1.01x faster                                             |
| regex_effbot   | 3.10 ms                                                                      | 3.14 ms: 1.02x slower                                            |
| regex_dna      | 234 ms                                                                       | 244 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|---------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse | 98.4 ms                                                                      | 95.5 ms: 1.03x faster                                            |
| json_dumps          | 11.8 ms                                                                      | 11.6 ms: 1.02x faster                                            |
| xml_etree_generate  | 79.8 ms                                                                      | 79.0 ms: 1.01x faster                                            |
| xml_etree_parse     | 137 ms                                                                       | 136 ms: 1.01x faster                                             |
| pickle_pure_python  | 337 us                                                                       | 335 us: 1.01x faster                                             |
| json_loads          | 26.8 us                                                                      | 26.9 us: 1.01x slower                                            |
| Geometric mean      | (ref)                                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 9.00 ms: 1.00x faster                                            |
| python_startup         | 16.1 ms                                                                      | 16.0 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml     | 56.0 ms                                                                      | 55.5 ms: 1.01x faster                                            |
| mako           | 9.66 ms                                                                      | 9.74 ms: 1.01x slower                                            |
| genshi_text    | 24.3 ms                                                                      | 24.8 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|--------------------------|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
| scimark_lu               | 100 ms                                                                       | 94.3 ms: 1.06x faster                                            |
| scimark_fft              | 306 ms                                                                       | 294 ms: 1.04x faster                                             |
| nbody                    | 104 ms                                                                       | 101 ms: 1.04x faster                                             |
| gc_traversal             | 6.50 ms                                                                      | 6.29 ms: 1.03x faster                                            |
| xml_etree_iterparse      | 98.4 ms                                                                      | 95.5 ms: 1.03x faster                                            |
| regex_v8                 | 25.2 ms                                                                      | 24.5 ms: 1.03x faster                                            |
| scimark_sor              | 109 ms                                                                       | 106 ms: 1.03x faster                                             |
| comprehensions           | 19.4 us                                                                      | 18.9 us: 1.02x faster                                            |
| create_gc_cycles         | 2.73 ms                                                                      | 2.68 ms: 1.02x faster                                            |
| async_tree_io_tg         | 657 ms                                                                       | 644 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult  | 4.84 ms                                                                      | 4.75 ms: 1.02x faster                                            |
| mdp                      | 2.60 sec                                                                     | 2.55 sec: 1.02x faster                                           |
| telco                    | 7.76 ms                                                                      | 7.63 ms: 1.02x faster                                            |
| json_dumps               | 11.8 ms                                                                      | 11.6 ms: 1.02x faster                                            |
| deltablue                | 3.53 ms                                                                      | 3.47 ms: 1.02x faster                                            |
| nqueens                  | 100.0 ms                                                                     | 98.6 ms: 1.01x faster                                            |
| many_optionals           | 1.03 ms                                                                      | 1.01 ms: 1.01x faster                                            |
| docutils                 | 2.98 sec                                                                     | 2.94 sec: 1.01x faster                                           |
| asyncio_websockets       | 389 ms                                                                       | 384 ms: 1.01x faster                                             |
| pathlib                  | 16.7 ms                                                                      | 16.6 ms: 1.01x faster                                            |
| coverage                 | 82.8 ms                                                                      | 82.0 ms: 1.01x faster                                            |
| crypto_pyaes             | 77.4 ms                                                                      | 76.6 ms: 1.01x faster                                            |
| xml_etree_generate       | 79.8 ms                                                                      | 79.0 ms: 1.01x faster                                            |
| meteor_contest           | 134 ms                                                                       | 132 ms: 1.01x faster                                             |
| spectral_norm            | 83.9 ms                                                                      | 83.1 ms: 1.01x faster                                            |
| xml_etree_parse          | 137 ms                                                                       | 136 ms: 1.01x faster                                             |
| genshi_xml               | 56.0 ms                                                                      | 55.5 ms: 1.01x faster                                            |
| scimark_monte_carlo      | 61.1 ms                                                                      | 60.6 ms: 1.01x faster                                            |
| logging_simple           | 6.41 us                                                                      | 6.37 us: 1.01x faster                                            |
| pickle_pure_python       | 337 us                                                                       | 335 us: 1.01x faster                                             |
| regex_compile            | 137 ms                                                                       | 136 ms: 1.01x faster                                             |
| pidigits                 | 254 ms                                                                       | 253 ms: 1.01x faster                                             |
| bpe_tokeniser            | 4.59 sec                                                                     | 4.57 sec: 1.01x faster                                           |
| connected_components     | 404 ms                                                                       | 402 ms: 1.00x faster                                             |
| python_startup_no_site   | 9.02 ms                                                                      | 9.00 ms: 1.00x faster                                            |
| python_startup           | 16.1 ms                                                                      | 16.0 ms: 1.00x faster                                            |
| shortest_path            | 437 ms                                                                       | 438 ms: 1.00x slower                                             |
| sympy_integrate          | 23.6 ms                                                                      | 23.7 ms: 1.00x slower                                            |
| async_generators         | 426 ms                                                                       | 428 ms: 1.00x slower                                             |
| sqlalchemy_declarative   | 145 ms                                                                       | 146 ms: 1.00x slower                                             |
| json_loads               | 26.8 us                                                                      | 26.9 us: 1.01x slower                                            |
| deepcopy_memo            | 29.0 us                                                                      | 29.2 us: 1.01x slower                                            |
| coroutines               | 21.0 ms                                                                      | 21.1 ms: 1.01x slower                                            |
| dulwich_log              | 67.6 ms                                                                      | 68.0 ms: 1.01x slower                                            |
| sympy_str                | 298 ms                                                                       | 300 ms: 1.01x slower                                             |
| pyflate                  | 425 ms                                                                       | 428 ms: 1.01x slower                                             |
| logging_silent           | 96.8 ns                                                                      | 97.5 ns: 1.01x slower                                            |
| sqlglot_normalize        | 118 ms                                                                       | 119 ms: 1.01x slower                                             |
| mako                     | 9.66 ms                                                                      | 9.74 ms: 1.01x slower                                            |
| async_tree_memoization   | 356 ms                                                                       | 359 ms: 1.01x slower                                             |
| sqlglot_optimize         | 59.9 ms                                                                      | 60.5 ms: 1.01x slower                                            |
| pprint_pformat           | 1.65 sec                                                                     | 1.67 sec: 1.01x slower                                           |
| deepcopy_reduce          | 2.88 us                                                                      | 2.91 us: 1.01x slower                                            |
| sympy_expand             | 508 ms                                                                       | 514 ms: 1.01x slower                                             |
| pprint_safe_repr         | 803 ms                                                                       | 812 ms: 1.01x slower                                             |
| richards_super           | 50.8 ms                                                                      | 51.4 ms: 1.01x slower                                            |
| async_tree_none          | 292 ms                                                                       | 296 ms: 1.01x slower                                             |
| typing_runtime_protocols | 174 us                                                                       | 176 us: 1.01x slower                                             |
| chaos                    | 62.0 ms                                                                      | 62.9 ms: 1.02x slower                                            |
| regex_effbot             | 3.10 ms                                                                      | 3.14 ms: 1.02x slower                                            |
| deepcopy                 | 278 us                                                                       | 283 us: 1.02x slower                                             |
| genshi_text              | 24.3 ms                                                                      | 24.8 ms: 1.02x slower                                            |
| richards                 | 44.9 ms                                                                      | 46.0 ms: 1.03x slower                                            |
| generators               | 28.5 ms                                                                      | 29.8 ms: 1.05x slower                                            |
| regex_dna                | 234 ms                                                                       | 244 ms: 1.05x slower                                             |
| Geometric mean           | (ref)                                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (31): raytrace, tomli_loads, sphinx, html5lib, async_tree_io, async_tree_memoization_tg, pylint, float, django_template, async_tree_cpu_io_mixed_tg, async_tree_none_tg, sqlglot_transpile, sqlite_synth, fannkuch, 2to3, thrift, sqlglot_parse, logging_format, async_tree_cpu_io_mixed, pycparser, json, hexiom, subparsers, sqlalchemy_imperative, xml_etree_process, unpickle_pure_python, sympy_sum, go, k_core, bench_thread_pool, bench_mp_pool

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 94.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x