# Results vs. base

- fork: tomasr8
- ref: jit_contains_op_set_
- machine: linux-x86_64
- commit hash: 52c1a54
- commit date: 2025-04-03
- overall geometric mean: 1.002x slower
- HPT reliability: 80.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250402-linux-x86_64-python-06822bfbf625e9777813-3.14.0a6+-06822bf | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 253 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250402-linux-x86_64-python-06822bfbf625e9777813-3.14.0a6+-06822bf | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 483 ms                                                                 | 477 ms: 1.01x faster                                                    |
| coroutines              | 23.1 ms                                                                | 24.3 ms: 1.05x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (9): async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_generators, async_tree_memoization, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250402-linux-x86_64-python-06822bfbf625e9777813-3.14.0a6+-06822bf | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 86.2 ms                                                                | 89.2 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250402-linux-x86_64-python-06822bfbf625e9777813-3.14.0a6+-06822bf | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                 | 126 ms: 1.01x faster                                                    |
| regex_dna      | 208 ms                                                                 | 216 ms: 1.04x slower                                                    |
| regex_v8       | 23.0 ms                                                                | 24.0 ms: 1.04x slower                                                   |
| regex_effbot   | 3.21 ms                                                                | 3.36 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250402-linux-x86_64-python-06822bfbf625e9777813-3.14.0a6+-06822bf | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|---------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 98.4 ms                                                                | 97.2 ms: 1.01x faster                                                   |
| xml_etree_process   | 55.7 ms                                                                | 55.4 ms: 1.01x faster                                                   |
| pickle_pure_python  | 320 us                                                                 | 324 us: 1.01x slower                                                    |
| json_dumps          | 11.4 ms                                                                | 11.6 ms: 1.02x slower                                                   |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (5): tomli_loads, xml_etree_parse, json_loads, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250402-linux-x86_64-python-06822bfbf625e9777813-3.14.0a6+-06822bf | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.21 ms                                                                | 8.20 ms: 1.00x faster                                                   |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250402-linux-x86_64-python-06822bfbf625e9777813-3.14.0a6+-06822bf | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 32.8 ms                                                                | 31.9 ms: 1.03x faster                                                   |
| mako            | 10.9 ms                                                                | 10.9 ms: 1.00x faster                                                   |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250402-linux-x86_64-python-06822bfbf625e9777813-3.14.0a6+-06822bf | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal             | 4.98 ms                                                                | 4.76 ms: 1.05x faster                                                   |
| pyflate                  | 445 ms                                                                 | 432 ms: 1.03x faster                                                    |
| django_template          | 32.8 ms                                                                | 31.9 ms: 1.03x faster                                                   |
| logging_silent           | 99.6 ns                                                                | 97.5 ns: 1.02x faster                                                   |
| deepcopy_memo            | 29.2 us                                                                | 28.6 us: 1.02x faster                                                   |
| typing_runtime_protocols | 167 us                                                                 | 164 us: 1.02x faster                                                    |
| sqlglot_v2_normalize     | 109 ms                                                                 | 107 ms: 1.01x faster                                                    |
| scimark_fft              | 311 ms                                                                 | 307 ms: 1.01x faster                                                    |
| sympy_expand             | 478 ms                                                                 | 472 ms: 1.01x faster                                                    |
| xml_etree_iterparse      | 98.4 ms                                                                | 97.2 ms: 1.01x faster                                                   |
| sympy_str                | 275 ms                                                                 | 272 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed  | 483 ms                                                                 | 477 ms: 1.01x faster                                                    |
| deepcopy                 | 252 us                                                                 | 250 us: 1.01x faster                                                    |
| regex_compile            | 127 ms                                                                 | 126 ms: 1.01x faster                                                    |
| sqlglot_v2_optimize      | 54.1 ms                                                                | 53.6 ms: 1.01x faster                                                   |
| scimark_lu               | 116 ms                                                                 | 115 ms: 1.01x faster                                                    |
| fannkuch                 | 417 ms                                                                 | 414 ms: 1.01x faster                                                    |
| dulwich_log              | 61.3 ms                                                                | 60.8 ms: 1.01x faster                                                   |
| bpe_tokeniser            | 4.52 sec                                                               | 4.48 sec: 1.01x faster                                                  |
| richards                 | 38.6 ms                                                                | 38.4 ms: 1.01x faster                                                   |
| sympy_integrate          | 19.7 ms                                                                | 19.6 ms: 1.01x faster                                                   |
| xml_etree_process        | 55.7 ms                                                                | 55.4 ms: 1.01x faster                                                   |
| mdp                      | 1.22 sec                                                               | 1.21 sec: 1.00x faster                                                  |
| raytrace                 | 262 ms                                                                 | 261 ms: 1.00x faster                                                    |
| deltablue                | 3.03 ms                                                                | 3.02 ms: 1.00x faster                                                   |
| mako                     | 10.9 ms                                                                | 10.9 ms: 1.00x faster                                                   |
| bench_thread_pool        | 887 us                                                                 | 885 us: 1.00x faster                                                    |
| python_startup_no_site   | 8.21 ms                                                                | 8.20 ms: 1.00x faster                                                   |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| python_startup           | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                                   |
| shortest_path            | 485 ms                                                                 | 486 ms: 1.00x slower                                                    |
| 2to3                     | 253 ms                                                                 | 253 ms: 1.00x slower                                                    |
| comprehensions           | 18.2 us                                                                | 18.3 us: 1.00x slower                                                   |
| connected_components     | 449 ms                                                                 | 452 ms: 1.01x slower                                                    |
| spectral_norm            | 100 ms                                                                 | 101 ms: 1.01x slower                                                    |
| hexiom                   | 6.64 ms                                                                | 6.71 ms: 1.01x slower                                                   |
| pickle_pure_python       | 320 us                                                                 | 324 us: 1.01x slower                                                    |
| subparsers               | 20.7 ms                                                                | 21.0 ms: 1.02x slower                                                   |
| json_dumps               | 11.4 ms                                                                | 11.6 ms: 1.02x slower                                                   |
| pathlib                  | 16.7 ms                                                                | 17.1 ms: 1.02x slower                                                   |
| generators               | 28.8 ms                                                                | 29.6 ms: 1.03x slower                                                   |
| logging_simple           | 5.52 us                                                                | 5.71 us: 1.03x slower                                                   |
| nbody                    | 86.2 ms                                                                | 89.2 ms: 1.03x slower                                                   |
| regex_dna                | 208 ms                                                                 | 216 ms: 1.04x slower                                                    |
| regex_v8                 | 23.0 ms                                                                | 24.0 ms: 1.04x slower                                                   |
| coverage                 | 84.6 ms                                                                | 88.4 ms: 1.04x slower                                                   |
| logging_format           | 6.06 us                                                                | 6.33 us: 1.05x slower                                                   |
| regex_effbot             | 3.21 ms                                                                | 3.36 ms: 1.05x slower                                                   |
| coroutines               | 23.1 ms                                                                | 24.3 ms: 1.05x slower                                                   |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (46): pprint_safe_repr, async_tree_io, json, scimark_monte_carlo, tomli_loads, async_tree_cpu_io_mixed_tg, nqueens, scimark_sor, scimark_sparse_mat_mult, genshi_xml, crypto_pyaes, sqlglot_v2_parse, asyncio_websockets, sqlglot_v2_transpile, deepcopy_reduce, sqlalchemy_declarative, create_gc_cycles, go, bench_mp_pool, xml_etree_parse, sympy_sum, sqlalchemy_imperative, json_loads, many_optionals, sphinx, docutils, genshi_text, xml_etree_generate, k_core, telco, async_generators, pylint, chaos, async_tree_memoization, meteor_contest, pprint_pformat, float, html5lib, async_tree_none, async_tree_io_tg, richards_super, sqlite_synth, async_tree_none_tg, pycparser, async_tree_memoization_tg, unpickle_pure_python

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 80.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x