# Results vs. base

- fork: Fidget-Spinner
- ref: eliminate_func_guard
- machine: linux-x86_64
- commit hash: 6d6263c
- commit date: 2024-11-04
- overall geometric mean: 1.002x faster
- HPT reliability: 86.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1+-9441993 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 280 ms: 1.00x faster                                                             |
| docutils       | 2.94 sec                                                               | 2.95 sec: 1.00x slower                                                           |
| html5lib       | 65.9 ms                                                                | 67.0 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1+-9441993 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines       | 23.7 ms                                                                | 23.3 ms: 1.02x faster                                                            |
| async_generators | 452 ms                                                                 | 448 ms: 1.01x faster                                                             |
| async_tree_io_tg | 978 ms                                                                 | 983 ms: 1.01x slower                                                             |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1+-9441993 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.5 ms                                                                | 76.1 ms: 1.01x faster                                                            |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1+-9441993 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                                | 25.3 ms: 1.01x faster                                                            |
| regex_effbot   | 3.79 ms                                                                | 3.81 ms: 1.00x slower                                                            |
| regex_dna      | 219 ms                                                                 | 220 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1+-9441993 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python | 320 us                                                                 | 325 us: 1.02x slower                                                             |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (8): tomli_loads, json_dumps, xml_etree_iterparse, unpickle_pure_python, xml_etree_parse, json_loads, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1+-9441993 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                                | 7.11 ms: 1.00x faster                                                            |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1+-9441993 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml     | 60.8 ms                                                                | 58.6 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (3): django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20241103-linux-x86_64-python-9441993f272f42e4a97d-3.14.0a1+-9441993 | bm-20241104-linux-x86_64-Fidget%2dSpinner-eliminate_func_guard-3.14.0a1+-6d6263c |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml               | 60.8 ms                                                                | 58.6 ms: 1.04x faster                                                            |
| pycparser                | 1.20 sec                                                               | 1.16 sec: 1.04x faster                                                           |
| gc_traversal             | 4.71 ms                                                                | 4.57 ms: 1.03x faster                                                            |
| pprint_safe_repr         | 740 ms                                                                 | 721 ms: 1.03x faster                                                             |
| coroutines               | 23.7 ms                                                                | 23.3 ms: 1.02x faster                                                            |
| generators               | 36.0 ms                                                                | 35.4 ms: 1.02x faster                                                            |
| shortest_path            | 485 ms                                                                 | 480 ms: 1.01x faster                                                             |
| sqlite_synth             | 2.83 us                                                                | 2.80 us: 1.01x faster                                                            |
| telco                    | 7.75 ms                                                                | 7.68 ms: 1.01x faster                                                            |
| async_generators         | 452 ms                                                                 | 448 ms: 1.01x faster                                                             |
| logging_format           | 6.18 us                                                                | 6.13 us: 1.01x faster                                                            |
| create_gc_cycles         | 2.69 ms                                                                | 2.67 ms: 1.01x faster                                                            |
| bpe_tokeniser            | 4.49 sec                                                               | 4.46 sec: 1.01x faster                                                           |
| regex_v8                 | 25.5 ms                                                                | 25.3 ms: 1.01x faster                                                            |
| sqlglot_optimize         | 60.1 ms                                                                | 59.7 ms: 1.01x faster                                                            |
| sqlglot_transpile        | 1.70 ms                                                                | 1.69 ms: 1.01x faster                                                            |
| sympy_expand             | 508 ms                                                                 | 504 ms: 1.01x faster                                                             |
| connected_components     | 440 ms                                                                 | 437 ms: 1.01x faster                                                             |
| sqlglot_parse            | 1.34 ms                                                                | 1.34 ms: 1.01x faster                                                            |
| go                       | 134 ms                                                                 | 133 ms: 1.01x faster                                                             |
| float                    | 76.5 ms                                                                | 76.1 ms: 1.01x faster                                                            |
| sqlglot_normalize        | 115 ms                                                                 | 115 ms: 1.00x faster                                                             |
| hexiom                   | 7.10 ms                                                                | 7.06 ms: 1.00x faster                                                            |
| scimark_fft              | 321 ms                                                                 | 320 ms: 1.00x faster                                                             |
| sympy_str                | 304 ms                                                                 | 303 ms: 1.00x faster                                                             |
| 2to3                     | 280 ms                                                                 | 280 ms: 1.00x faster                                                             |
| python_startup_no_site   | 7.12 ms                                                                | 7.11 ms: 1.00x faster                                                            |
| sqlalchemy_declarative   | 147 ms                                                                 | 147 ms: 1.00x faster                                                             |
| python_startup           | 12.8 ms                                                                | 12.7 ms: 1.00x faster                                                            |
| docutils                 | 2.94 sec                                                               | 2.95 sec: 1.00x slower                                                           |
| regex_effbot             | 3.79 ms                                                                | 3.81 ms: 1.00x slower                                                            |
| meteor_contest           | 107 ms                                                                 | 108 ms: 1.00x slower                                                             |
| pidigits                 | 187 ms                                                                 | 187 ms: 1.00x slower                                                             |
| async_tree_io_tg         | 978 ms                                                                 | 983 ms: 1.01x slower                                                             |
| deltablue                | 3.28 ms                                                                | 3.30 ms: 1.01x slower                                                            |
| dulwich_log              | 67.2 ms                                                                | 67.7 ms: 1.01x slower                                                            |
| sympy_integrate          | 23.4 ms                                                                | 23.5 ms: 1.01x slower                                                            |
| pyflate                  | 454 ms                                                                 | 458 ms: 1.01x slower                                                             |
| pathlib                  | 16.1 ms                                                                | 16.2 ms: 1.01x slower                                                            |
| regex_dna                | 219 ms                                                                 | 220 ms: 1.01x slower                                                             |
| typing_runtime_protocols | 165 us                                                                 | 167 us: 1.01x slower                                                             |
| bench_thread_pool        | 878 us                                                                 | 888 us: 1.01x slower                                                             |
| deepcopy                 | 267 us                                                                 | 271 us: 1.01x slower                                                             |
| richards_super           | 47.5 ms                                                                | 48.2 ms: 1.02x slower                                                            |
| richards                 | 41.3 ms                                                                | 41.9 ms: 1.02x slower                                                            |
| pickle_pure_python       | 320 us                                                                 | 325 us: 1.02x slower                                                             |
| html5lib                 | 65.9 ms                                                                | 67.0 ms: 1.02x slower                                                            |
| deepcopy_memo            | 29.1 us                                                                | 29.6 us: 1.02x slower                                                            |
| scimark_sparse_mat_mult  | 4.68 ms                                                                | 4.78 ms: 1.02x slower                                                            |
| logging_silent           | 97.8 ns                                                                | 101 ns: 1.03x slower                                                             |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (45): k_core, pprint_pformat, django_template, genshi_text, thrift, crypto_pyaes, tomli_loads, raytrace, deepcopy_reduce, bench_mp_pool, json, comprehensions, sphinx, json_dumps, xml_etree_iterparse, sympy_sum, async_tree_cpu_io_mixed_tg, mako, nbody, unpickle_pure_python, mdp, scimark_monte_carlo, logging_simple, sqlalchemy_imperative, async_tree_io, xml_etree_parse, scimark_sor, asyncio_websockets, pylint, json_loads, tornado_http, chaos, spectral_norm, nqueens, scimark_lu, async_tree_memoization_tg, xml_etree_generate, async_tree_cpu_io_mixed, xml_etree_process, async_tree_none, coverage, regex_compile, async_tree_none_tg, fannkuch, async_tree_memoization

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 86.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x