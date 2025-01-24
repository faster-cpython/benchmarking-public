# Results vs. base

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.000x faster
- HPT reliability: 52.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                       | 280 ms: 1.00x slower                                                                   |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_generators          | 413 ms                                                                       | 405 ms: 1.02x faster                                                                   |
| coroutines                | 21.0 ms                                                                      | 20.7 ms: 1.01x faster                                                                  |
| async_tree_memoization_tg | 335 ms                                                                       | 331 ms: 1.01x faster                                                                   |
| async_tree_memoization    | 347 ms                                                                       | 350 ms: 1.01x slower                                                                   |
| async_tree_none           | 285 ms                                                                       | 289 ms: 1.01x slower                                                                   |
| async_tree_cpu_io_mixed   | 514 ms                                                                       | 522 ms: 1.01x slower                                                                   |
| Geometric mean            | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 69.6 ms                                                                      | 68.7 ms: 1.01x faster                                                                  |
| nbody          | 86.4 ms                                                                      | 87.8 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 240 ms                                                                       | 236 ms: 1.02x faster                                                                   |
| regex_compile  | 133 ms                                                                       | 135 ms: 1.02x slower                                                                   |
| regex_v8       | 25.6 ms                                                                      | 26.3 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                                       | 205 us: 1.03x faster                                                                   |
| pickle_pure_python   | 328 us                                                                       | 323 us: 1.02x faster                                                                   |
| tomli_loads          | 2.06 sec                                                                     | 2.04 sec: 1.01x faster                                                                 |
| xml_etree_generate   | 84.9 ms                                                                      | 84.1 ms: 1.01x faster                                                                  |
| xml_etree_process    | 59.1 ms                                                                      | 58.7 ms: 1.01x faster                                                                  |
| json_loads           | 25.4 us                                                                      | 25.6 us: 1.01x slower                                                                  |
| xml_etree_parse      | 134 ms                                                                       | 136 ms: 1.01x slower                                                                   |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (2): json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                                      | 16.0 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text    | 23.3 ms                                                                      | 23.5 ms: 1.01x slower                                                                  |
| genshi_xml     | 51.7 ms                                                                      | 52.3 ms: 1.01x slower                                                                  |
| mako           | 10.8 ms                                                                      | 10.9 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|---------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| bench_thread_pool         | 961 us                                                                       | 922 us: 1.04x faster                                                                   |
| generators                | 29.0 ms                                                                      | 28.0 ms: 1.03x faster                                                                  |
| scimark_sor               | 110 ms                                                                       | 107 ms: 1.03x faster                                                                   |
| unpickle_pure_python      | 210 us                                                                       | 205 us: 1.03x faster                                                                   |
| chaos                     | 59.7 ms                                                                      | 58.2 ms: 1.03x faster                                                                  |
| richards_super            | 52.8 ms                                                                      | 51.6 ms: 1.02x faster                                                                  |
| scimark_monte_carlo       | 63.2 ms                                                                      | 62.0 ms: 1.02x faster                                                                  |
| async_generators          | 413 ms                                                                       | 405 ms: 1.02x faster                                                                   |
| richards                  | 46.2 ms                                                                      | 45.4 ms: 1.02x faster                                                                  |
| regex_dna                 | 240 ms                                                                       | 236 ms: 1.02x faster                                                                   |
| logging_simple            | 6.27 us                                                                      | 6.17 us: 1.02x faster                                                                  |
| sqlite_synth              | 2.82 us                                                                      | 2.78 us: 1.02x faster                                                                  |
| scimark_sparse_mat_mult   | 4.58 ms                                                                      | 4.51 ms: 1.02x faster                                                                  |
| pickle_pure_python        | 328 us                                                                       | 323 us: 1.02x faster                                                                   |
| nqueens                   | 90.0 ms                                                                      | 88.7 ms: 1.02x faster                                                                  |
| coroutines                | 21.0 ms                                                                      | 20.7 ms: 1.01x faster                                                                  |
| scimark_fft               | 305 ms                                                                       | 300 ms: 1.01x faster                                                                   |
| float                     | 69.6 ms                                                                      | 68.7 ms: 1.01x faster                                                                  |
| tomli_loads               | 2.06 sec                                                                     | 2.04 sec: 1.01x faster                                                                 |
| async_tree_memoization_tg | 335 ms                                                                       | 331 ms: 1.01x faster                                                                   |
| pycparser                 | 1.22 sec                                                                     | 1.21 sec: 1.01x faster                                                                 |
| xml_etree_generate        | 84.9 ms                                                                      | 84.1 ms: 1.01x faster                                                                  |
| raytrace                  | 265 ms                                                                       | 263 ms: 1.01x faster                                                                   |
| bpe_tokeniser             | 4.66 sec                                                                     | 4.62 sec: 1.01x faster                                                                 |
| xml_etree_process         | 59.1 ms                                                                      | 58.7 ms: 1.01x faster                                                                  |
| sqlglot_normalize         | 114 ms                                                                       | 113 ms: 1.01x faster                                                                   |
| scimark_lu                | 93.5 ms                                                                      | 93.1 ms: 1.00x faster                                                                  |
| sqlglot_transpile         | 1.71 ms                                                                      | 1.70 ms: 1.00x faster                                                                  |
| sympy_sum                 | 151 ms                                                                       | 150 ms: 1.00x faster                                                                   |
| sympy_integrate           | 23.0 ms                                                                      | 22.9 ms: 1.00x faster                                                                  |
| sqlalchemy_declarative    | 144 ms                                                                       | 143 ms: 1.00x faster                                                                   |
| spectral_norm             | 83.5 ms                                                                      | 83.2 ms: 1.00x faster                                                                  |
| go                        | 125 ms                                                                       | 125 ms: 1.00x faster                                                                   |
| python_startup            | 16.0 ms                                                                      | 16.0 ms: 1.00x slower                                                                  |
| 2to3                      | 280 ms                                                                       | 280 ms: 1.00x slower                                                                   |
| mdp                       | 2.44 sec                                                                     | 2.44 sec: 1.00x slower                                                                 |
| sqlglot_optimize          | 56.9 ms                                                                      | 57.1 ms: 1.00x slower                                                                  |
| logging_silent            | 96.9 ns                                                                      | 97.4 ns: 1.01x slower                                                                  |
| many_optionals            | 1.00 ms                                                                      | 1.01 ms: 1.01x slower                                                                  |
| deepcopy_reduce           | 2.89 us                                                                      | 2.91 us: 1.01x slower                                                                  |
| fannkuch                  | 358 ms                                                                       | 361 ms: 1.01x slower                                                                   |
| deepcopy_memo             | 30.0 us                                                                      | 30.2 us: 1.01x slower                                                                  |
| async_tree_memoization    | 347 ms                                                                       | 350 ms: 1.01x slower                                                                   |
| genshi_text               | 23.3 ms                                                                      | 23.5 ms: 1.01x slower                                                                  |
| json_loads                | 25.4 us                                                                      | 25.6 us: 1.01x slower                                                                  |
| connected_components      | 411 ms                                                                       | 414 ms: 1.01x slower                                                                   |
| shortest_path             | 438 ms                                                                       | 442 ms: 1.01x slower                                                                   |
| pathlib                   | 15.8 ms                                                                      | 15.9 ms: 1.01x slower                                                                  |
| sympy_expand              | 488 ms                                                                       | 493 ms: 1.01x slower                                                                   |
| coverage                  | 75.6 ms                                                                      | 76.5 ms: 1.01x slower                                                                  |
| genshi_xml                | 51.7 ms                                                                      | 52.3 ms: 1.01x slower                                                                  |
| meteor_contest            | 126 ms                                                                       | 128 ms: 1.01x slower                                                                   |
| async_tree_none           | 285 ms                                                                       | 289 ms: 1.01x slower                                                                   |
| mako                      | 10.8 ms                                                                      | 10.9 ms: 1.01x slower                                                                  |
| xml_etree_parse           | 134 ms                                                                       | 136 ms: 1.01x slower                                                                   |
| async_tree_cpu_io_mixed   | 514 ms                                                                       | 522 ms: 1.01x slower                                                                   |
| regex_compile             | 133 ms                                                                       | 135 ms: 1.02x slower                                                                   |
| nbody                     | 86.4 ms                                                                      | 87.8 ms: 1.02x slower                                                                  |
| comprehensions            | 17.5 us                                                                      | 17.8 us: 1.02x slower                                                                  |
| crypto_pyaes              | 72.4 ms                                                                      | 73.8 ms: 1.02x slower                                                                  |
| typing_runtime_protocols  | 171 us                                                                       | 174 us: 1.02x slower                                                                   |
| thrift                    | 857 us                                                                       | 874 us: 1.02x slower                                                                   |
| pyflate                   | 443 ms                                                                       | 452 ms: 1.02x slower                                                                   |
| gc_traversal              | 6.17 ms                                                                      | 6.32 ms: 1.03x slower                                                                  |
| regex_v8                  | 25.6 ms                                                                      | 26.3 ms: 1.03x slower                                                                  |
| subparsers                | 22.4 ms                                                                      | 23.0 ms: 1.03x slower                                                                  |
| Geometric mean            | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (30): html5lib, pylint, async_tree_cpu_io_mixed_tg, dulwich_log, django_template, sqlalchemy_imperative, create_gc_cycles, deltablue, regex_effbot, sqlglot_parse, pprint_pformat, async_tree_io_tg, pidigits, logging_format, deepcopy, python_startup_no_site, pprint_safe_repr, hexiom, telco, docutils, sympy_str, sphinx, k_core, json, async_tree_io, asyncio_websockets, async_tree_none_tg, json_dumps, xml_etree_iterparse, bench_mp_pool

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 52.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x