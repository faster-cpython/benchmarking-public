# Results vs. base

- fork: faster-cpython
- ref: fast_side_exits
- machine: linux-x86_64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.004x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines       | 22.4 ms                                                                     | 22.3 ms: 1.01x faster                                                            |
| async_generators | 442 ms                                                                      | 444 ms: 1.00x slower                                                             |
| Geometric mean   | (ref)                                                                       | 1.00x faster                                                                     |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 101 ms                                                                      | 99.7 ms: 1.02x faster                                                            |
| float          | 64.0 ms                                                                     | 63.6 ms: 1.01x faster                                                            |
| pidigits       | 255 ms                                                                      | 255 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.74 ms                                                                     | 3.67 ms: 1.02x faster                                                            |
| regex_compile  | 134 ms                                                                      | 133 ms: 1.01x faster                                                             |
| regex_dna      | 222 ms                                                                      | 225 ms: 1.01x slower                                                             |
| regex_v8       | 23.2 ms                                                                     | 23.6 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|---------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps          | 11.4 ms                                                                     | 11.1 ms: 1.02x faster                                                            |
| xml_etree_generate  | 80.3 ms                                                                     | 78.9 ms: 1.02x faster                                                            |
| xml_etree_process   | 56.0 ms                                                                     | 55.4 ms: 1.01x faster                                                            |
| xml_etree_parse     | 135 ms                                                                      | 134 ms: 1.01x faster                                                             |
| xml_etree_iterparse | 96.1 ms                                                                     | 96.9 ms: 1.01x slower                                                            |
| json_loads          | 25.0 us                                                                     | 25.2 us: 1.01x slower                                                            |
| Geometric mean      | (ref)                                                                       | 1.01x faster                                                                     |

Benchmark hidden because not significant (3): pickle_pure_python, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                                     | 15.4 ms: 1.00x slower                                                            |
| python_startup_no_site | 8.82 ms                                                                     | 8.86 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 55.2 ms                                                                     | 54.2 ms: 1.02x faster                                                            |
| django_template | 35.7 ms                                                                     | 35.4 ms: 1.01x faster                                                            |
| mako            | 9.95 ms                                                                     | 10.1 ms: 1.01x slower                                                            |
| genshi_text     | 22.9 ms                                                                     | 23.2 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|--------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators               | 30.6 ms                                                                     | 28.2 ms: 1.09x faster                                                            |
| coverage                 | 84.1 ms                                                                     | 80.3 ms: 1.05x faster                                                            |
| go                       | 132 ms                                                                      | 127 ms: 1.04x faster                                                             |
| richards_super           | 41.6 ms                                                                     | 40.3 ms: 1.03x faster                                                            |
| scimark_fft              | 310 ms                                                                      | 303 ms: 1.02x faster                                                             |
| json_dumps               | 11.4 ms                                                                     | 11.1 ms: 1.02x faster                                                            |
| regex_effbot             | 3.74 ms                                                                     | 3.67 ms: 1.02x faster                                                            |
| logging_silent           | 95.2 ns                                                                     | 93.3 ns: 1.02x faster                                                            |
| genshi_xml               | 55.2 ms                                                                     | 54.2 ms: 1.02x faster                                                            |
| spectral_norm            | 82.9 ms                                                                     | 81.3 ms: 1.02x faster                                                            |
| xml_etree_generate       | 80.3 ms                                                                     | 78.9 ms: 1.02x faster                                                            |
| nbody                    | 101 ms                                                                      | 99.7 ms: 1.02x faster                                                            |
| mdp                      | 1.31 sec                                                                    | 1.29 sec: 1.02x faster                                                           |
| comprehensions           | 17.7 us                                                                     | 17.5 us: 1.02x faster                                                            |
| chaos                    | 61.2 ms                                                                     | 60.4 ms: 1.01x faster                                                            |
| thrift                   | 847 us                                                                      | 835 us: 1.01x faster                                                             |
| meteor_contest           | 122 ms                                                                      | 121 ms: 1.01x faster                                                             |
| pyflate                  | 411 ms                                                                      | 405 ms: 1.01x faster                                                             |
| pprint_pformat           | 1.56 sec                                                                    | 1.54 sec: 1.01x faster                                                           |
| xml_etree_process        | 56.0 ms                                                                     | 55.4 ms: 1.01x faster                                                            |
| scimark_sparse_mat_mult  | 5.06 ms                                                                     | 5.00 ms: 1.01x faster                                                            |
| deepcopy_memo            | 28.3 us                                                                     | 28.1 us: 1.01x faster                                                            |
| django_template          | 35.7 ms                                                                     | 35.4 ms: 1.01x faster                                                            |
| scimark_monte_carlo      | 63.8 ms                                                                     | 63.3 ms: 1.01x faster                                                            |
| coroutines               | 22.4 ms                                                                     | 22.3 ms: 1.01x faster                                                            |
| create_gc_cycles         | 2.87 ms                                                                     | 2.84 ms: 1.01x faster                                                            |
| float                    | 64.0 ms                                                                     | 63.6 ms: 1.01x faster                                                            |
| regex_compile            | 134 ms                                                                      | 133 ms: 1.01x faster                                                             |
| xml_etree_parse          | 135 ms                                                                      | 134 ms: 1.01x faster                                                             |
| logging_simple           | 6.18 us                                                                     | 6.15 us: 1.01x faster                                                            |
| sympy_expand             | 500 ms                                                                      | 497 ms: 1.01x faster                                                             |
| sqlglot_v2_transpile     | 1.72 ms                                                                     | 1.71 ms: 1.01x faster                                                            |
| sympy_sum                | 152 ms                                                                      | 151 ms: 1.01x faster                                                             |
| crypto_pyaes             | 77.9 ms                                                                     | 77.6 ms: 1.00x faster                                                            |
| bpe_tokeniser            | 4.59 sec                                                                    | 4.57 sec: 1.00x faster                                                           |
| hexiom                   | 6.16 ms                                                                     | 6.13 ms: 1.00x faster                                                            |
| many_optionals           | 1.05 ms                                                                     | 1.04 ms: 1.00x faster                                                            |
| sympy_str                | 291 ms                                                                      | 290 ms: 1.00x faster                                                             |
| subparsers               | 25.2 ms                                                                     | 25.1 ms: 1.00x faster                                                            |
| sqlglot_v2_optimize      | 58.4 ms                                                                     | 58.2 ms: 1.00x faster                                                            |
| deltablue                | 2.89 ms                                                                     | 2.89 ms: 1.00x faster                                                            |
| pidigits                 | 255 ms                                                                      | 255 ms: 1.00x slower                                                             |
| python_startup           | 15.3 ms                                                                     | 15.4 ms: 1.00x slower                                                            |
| pathlib                  | 16.9 ms                                                                     | 17.0 ms: 1.00x slower                                                            |
| python_startup_no_site   | 8.82 ms                                                                     | 8.86 ms: 1.00x slower                                                            |
| raytrace                 | 293 ms                                                                      | 294 ms: 1.00x slower                                                             |
| async_generators         | 442 ms                                                                      | 444 ms: 1.00x slower                                                             |
| gc_traversal             | 6.45 ms                                                                     | 6.48 ms: 1.00x slower                                                            |
| fannkuch                 | 381 ms                                                                      | 383 ms: 1.01x slower                                                             |
| typing_runtime_protocols | 173 us                                                                      | 174 us: 1.01x slower                                                             |
| telco                    | 159 ms                                                                      | 160 ms: 1.01x slower                                                             |
| xml_etree_iterparse      | 96.1 ms                                                                     | 96.9 ms: 1.01x slower                                                            |
| json_loads               | 25.0 us                                                                     | 25.2 us: 1.01x slower                                                            |
| scimark_sor              | 104 ms                                                                      | 105 ms: 1.01x slower                                                             |
| deepcopy                 | 279 us                                                                      | 281 us: 1.01x slower                                                             |
| connected_components     | 404 ms                                                                      | 408 ms: 1.01x slower                                                             |
| mako                     | 9.95 ms                                                                     | 10.1 ms: 1.01x slower                                                            |
| sqlite_synth             | 2.89 us                                                                     | 2.93 us: 1.01x slower                                                            |
| genshi_text              | 22.9 ms                                                                     | 23.2 ms: 1.01x slower                                                            |
| regex_dna                | 222 ms                                                                      | 225 ms: 1.01x slower                                                             |
| shortest_path            | 436 ms                                                                      | 443 ms: 1.02x slower                                                             |
| regex_v8                 | 23.2 ms                                                                     | 23.6 ms: 1.02x slower                                                            |
| scimark_lu               | 95.6 ms                                                                     | 101 ms: 1.05x slower                                                             |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                     |

Benchmark hidden because not significant (29): pickle_pure_python, richards, pprint_safe_repr, async_tree_none_tg, async_tree_io, unpickle_pure_python, pylint, tomli_loads, async_tree_memoization, async_tree_cpu_io_mixed, k_core, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, nqueens, sqlglot_v2_parse, asyncio_websockets, async_tree_io_tg, docutils, sqlglot_v2_normalize, sympy_integrate, html5lib, djangocms, 2to3, logging_format, dulwich_log, async_tree_none, json, sphinx, deepcopy_reduce
Ignored benchmarks (1) of results/bm-20250707-3.15.0a0-cb99d99-JIT/bm-20250707-pythonperf2-x86_64-python-cb99d992774b67761441-3.15.0a0-cb99d99.json: pycparser

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x