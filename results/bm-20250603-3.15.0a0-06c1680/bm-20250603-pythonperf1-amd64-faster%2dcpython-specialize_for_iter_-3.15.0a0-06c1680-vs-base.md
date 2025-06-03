# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.010x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 222 ms                                                                     | 219 ms: 1.01x faster                                                                 |
| html5lib       | 38.9 ms                                                                    | 38.1 ms: 1.02x faster                                                                |
| sphinx         | 645 ms                                                                     | 632 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coroutines                | 14.6 ms                                                                    | 13.8 ms: 1.06x faster                                                                |
| async_tree_io_tg          | 399 ms                                                                     | 391 ms: 1.02x faster                                                                 |
| async_tree_memoization_tg | 211 ms                                                                     | 207 ms: 1.02x faster                                                                 |
| Geometric mean            | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (8): async_generators, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 62.6 ms                                                                    | 60.9 ms: 1.03x faster                                                                |
| float          | 44.7 ms                                                                    | 43.9 ms: 1.02x faster                                                                |
| pidigits       | 149 ms                                                                     | 148 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 14.3 ms                                                                    | 14.0 ms: 1.02x faster                                                                |
| regex_effbot   | 1.58 ms                                                                    | 1.55 ms: 1.02x faster                                                                |
| regex_dna      | 121 ms                                                                     | 120 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                                   | 1.34 sec: 1.02x faster                                                               |
| pickle_pure_python   | 211 us                                                                     | 208 us: 1.01x faster                                                                 |
| json_loads           | 14.4 us                                                                    | 14.2 us: 1.01x faster                                                                |
| unpickle_pure_python | 133 us                                                                     | 132 us: 1.01x faster                                                                 |
| xml_etree_generate   | 55.8 ms                                                                    | 55.5 ms: 1.01x faster                                                                |
| xml_etree_process    | 39.1 ms                                                                    | 39.4 ms: 1.01x slower                                                                |
| xml_etree_parse      | 88.3 ms                                                                    | 89.5 ms: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.7 ms                                                                    | 15.1 ms: 1.03x faster                                                                |
| django_template | 25.1 ms                                                                    | 24.3 ms: 1.03x faster                                                                |
| genshi_xml      | 35.2 ms                                                                    | 34.3 ms: 1.03x faster                                                                |
| mako            | 6.45 ms                                                                    | 6.54 ms: 1.02x slower                                                                |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coroutines                | 14.6 ms                                                                    | 13.8 ms: 1.06x faster                                                                |
| chaos                     | 39.8 ms                                                                    | 37.8 ms: 1.05x faster                                                                |
| scimark_sor               | 77.0 ms                                                                    | 73.2 ms: 1.05x faster                                                                |
| sqlglot_v2_normalize      | 72.6 ms                                                                    | 69.5 ms: 1.04x faster                                                                |
| spectral_norm             | 58.5 ms                                                                    | 56.6 ms: 1.04x faster                                                                |
| genshi_text               | 15.7 ms                                                                    | 15.1 ms: 1.03x faster                                                                |
| django_template           | 25.1 ms                                                                    | 24.3 ms: 1.03x faster                                                                |
| deepcopy_reduce           | 1.86 us                                                                    | 1.81 us: 1.03x faster                                                                |
| deltablue                 | 2.20 ms                                                                    | 2.14 ms: 1.03x faster                                                                |
| genshi_xml                | 35.2 ms                                                                    | 34.3 ms: 1.03x faster                                                                |
| nbody                     | 62.6 ms                                                                    | 60.9 ms: 1.03x faster                                                                |
| sqlglot_v2_optimize       | 34.4 ms                                                                    | 33.5 ms: 1.03x faster                                                                |
| subparsers                | 17.2 ms                                                                    | 16.8 ms: 1.03x faster                                                                |
| tomli_loads               | 1.37 sec                                                                   | 1.34 sec: 1.02x faster                                                               |
| pycparser                 | 719 ms                                                                     | 702 ms: 1.02x faster                                                                 |
| deepcopy_memo             | 18.2 us                                                                    | 17.7 us: 1.02x faster                                                                |
| sqlglot_v2_transpile      | 1.03 ms                                                                    | 1.01 ms: 1.02x faster                                                                |
| regex_v8                  | 14.3 ms                                                                    | 14.0 ms: 1.02x faster                                                                |
| bpe_tokeniser             | 2.91 sec                                                                   | 2.85 sec: 1.02x faster                                                               |
| nqueens                   | 60.8 ms                                                                    | 59.5 ms: 1.02x faster                                                                |
| generators                | 19.7 ms                                                                    | 19.3 ms: 1.02x faster                                                                |
| sphinx                    | 645 ms                                                                     | 632 ms: 1.02x faster                                                                 |
| scimark_fft               | 178 ms                                                                     | 175 ms: 1.02x faster                                                                 |
| regex_effbot              | 1.58 ms                                                                    | 1.55 ms: 1.02x faster                                                                |
| html5lib                  | 38.9 ms                                                                    | 38.1 ms: 1.02x faster                                                                |
| pyflate                   | 282 ms                                                                     | 277 ms: 1.02x faster                                                                 |
| sqlglot_v2_parse          | 828 us                                                                     | 811 us: 1.02x faster                                                                 |
| deepcopy                  | 173 us                                                                     | 169 us: 1.02x faster                                                                 |
| many_optionals            | 441 us                                                                     | 433 us: 1.02x faster                                                                 |
| async_tree_io_tg          | 399 ms                                                                     | 391 ms: 1.02x faster                                                                 |
| go                        | 75.3 ms                                                                    | 73.9 ms: 1.02x faster                                                                |
| float                     | 44.7 ms                                                                    | 43.9 ms: 1.02x faster                                                                |
| hexiom                    | 4.06 ms                                                                    | 3.99 ms: 1.02x faster                                                                |
| raytrace                  | 182 ms                                                                     | 179 ms: 1.02x faster                                                                 |
| typing_runtime_protocols  | 105 us                                                                     | 103 us: 1.02x faster                                                                 |
| logging_silent            | 315 ns                                                                     | 310 ns: 1.02x faster                                                                 |
| async_tree_memoization_tg | 211 ms                                                                     | 207 ms: 1.02x faster                                                                 |
| coverage                  | 294 ms                                                                     | 289 ms: 1.01x faster                                                                 |
| pathlib                   | 31.8 ms                                                                    | 31.4 ms: 1.01x faster                                                                |
| pickle_pure_python        | 211 us                                                                     | 208 us: 1.01x faster                                                                 |
| logging_simple            | 6.29 us                                                                    | 6.22 us: 1.01x faster                                                                |
| 2to3                      | 222 ms                                                                     | 219 ms: 1.01x faster                                                                 |
| sympy_expand              | 288 ms                                                                     | 285 ms: 1.01x faster                                                                 |
| pprint_pformat            | 1.11 sec                                                                   | 1.10 sec: 1.01x faster                                                               |
| pprint_safe_repr          | 546 ms                                                                     | 540 ms: 1.01x faster                                                                 |
| json_loads                | 14.4 us                                                                    | 14.2 us: 1.01x faster                                                                |
| shortest_path             | 364 ms                                                                     | 361 ms: 1.01x faster                                                                 |
| logging_format            | 6.76 us                                                                    | 6.70 us: 1.01x faster                                                                |
| regex_dna                 | 121 ms                                                                     | 120 ms: 1.01x faster                                                                 |
| unpickle_pure_python      | 133 us                                                                     | 132 us: 1.01x faster                                                                 |
| xml_etree_generate        | 55.8 ms                                                                    | 55.5 ms: 1.01x faster                                                                |
| fannkuch                  | 251 ms                                                                     | 250 ms: 1.01x faster                                                                 |
| mdp                       | 810 ms                                                                     | 806 ms: 1.01x faster                                                                 |
| sympy_str                 | 168 ms                                                                     | 167 ms: 1.01x faster                                                                 |
| pidigits                  | 149 ms                                                                     | 148 ms: 1.00x faster                                                                 |
| crypto_pyaes              | 46.7 ms                                                                    | 46.5 ms: 1.00x faster                                                                |
| scimark_lu                | 58.6 ms                                                                    | 59.1 ms: 1.01x slower                                                                |
| xml_etree_process         | 39.1 ms                                                                    | 39.4 ms: 1.01x slower                                                                |
| scimark_monte_carlo       | 40.2 ms                                                                    | 40.6 ms: 1.01x slower                                                                |
| scimark_sparse_mat_mult   | 2.49 ms                                                                    | 2.51 ms: 1.01x slower                                                                |
| xml_etree_parse           | 88.3 ms                                                                    | 89.5 ms: 1.01x slower                                                                |
| mako                      | 6.45 ms                                                                    | 6.54 ms: 1.02x slower                                                                |
| telco                     | 4.59 ms                                                                    | 4.66 ms: 1.02x slower                                                                |
| meteor_contest            | 71.4 ms                                                                    | 72.7 ms: 1.02x slower                                                                |
| richards                  | 27.2 ms                                                                    | 27.8 ms: 1.02x slower                                                                |
| comprehensions            | 10.5 us                                                                    | 11.0 us: 1.05x slower                                                                |
| Geometric mean            | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (26): pylint, async_generators, connected_components, async_tree_memoization, sympy_sum, xml_etree_iterparse, async_tree_cpu_io_mixed, python_startup_no_site, async_tree_none_tg, thrift, async_tree_io, async_tree_none, sympy_integrate, python_startup, dulwich_log, gc_traversal, async_tree_cpu_io_mixed_tg, json_dumps, sqlite_synth, regex_compile, create_gc_cycles, k_core, docutils, richards_super, asyncio_websockets, json

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown