# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.001x faster
- HPT reliability: 69.18%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| sphinx         | 653 ms                                                                     | 637 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 218 ms                                                                     | 209 ms: 1.04x faster                                                                 |
| async_tree_cpu_io_mixed   | 330 ms                                                                     | 328 ms: 1.00x faster                                                                 |
| async_tree_none           | 170 ms                                                                     | 172 ms: 1.01x slower                                                                 |
| async_generators          | 229 ms                                                                     | 233 ms: 1.02x slower                                                                 |
| async_tree_io_tg          | 391 ms                                                                     | 401 ms: 1.03x slower                                                                 |
| Geometric mean            | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_none_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 66.0 ms                                                                    | 64.1 ms: 1.03x faster                                                                |
| float          | 45.2 ms                                                                    | 45.8 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 13.9 ms                                                                    | 14.1 ms: 1.01x slower                                                                |
| regex_compile  | 79.6 ms                                                                    | 81.6 ms: 1.03x slower                                                                |
| regex_effbot   | 1.49 ms                                                                    | 1.58 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads        | 15.5 us                                                                    | 14.9 us: 1.04x faster                                                                |
| xml_etree_parse   | 88.9 ms                                                                    | 87.6 ms: 1.01x faster                                                                |
| xml_etree_process | 39.0 ms                                                                    | 38.7 ms: 1.01x faster                                                                |
| Geometric mean    | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (6): xml_etree_iterparse, json_dumps, xml_etree_generate, pickle_pure_python, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text    | 15.2 ms                                                                    | 15.3 ms: 1.01x slower                                                                |
| mako           | 6.57 ms                                                                    | 6.64 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| sqlglot_v2_normalize      | 75.9 ms                                                                    | 70.0 ms: 1.08x faster                                                                |
| sqlglot_v2_optimize       | 36.2 ms                                                                    | 33.8 ms: 1.07x faster                                                                |
| sqlglot_v2_transpile      | 1.08 ms                                                                    | 1.03 ms: 1.05x faster                                                                |
| sqlite_synth              | 1.67 us                                                                    | 1.59 us: 1.05x faster                                                                |
| sqlglot_v2_parse          | 862 us                                                                     | 826 us: 1.04x faster                                                                 |
| async_tree_memoization_tg | 218 ms                                                                     | 209 ms: 1.04x faster                                                                 |
| chaos                     | 40.1 ms                                                                    | 38.5 ms: 1.04x faster                                                                |
| json_loads                | 15.5 us                                                                    | 14.9 us: 1.04x faster                                                                |
| logging_silent            | 329 ns                                                                     | 318 ns: 1.03x faster                                                                 |
| nbody                     | 66.0 ms                                                                    | 64.1 ms: 1.03x faster                                                                |
| sphinx                    | 653 ms                                                                     | 637 ms: 1.02x faster                                                                 |
| pyflate                   | 285 ms                                                                     | 279 ms: 1.02x faster                                                                 |
| scimark_monte_carlo       | 41.8 ms                                                                    | 40.9 ms: 1.02x faster                                                                |
| scimark_sor               | 78.1 ms                                                                    | 76.8 ms: 1.02x faster                                                                |
| xml_etree_parse           | 88.9 ms                                                                    | 87.6 ms: 1.01x faster                                                                |
| scimark_lu                | 59.5 ms                                                                    | 58.8 ms: 1.01x faster                                                                |
| sympy_expand              | 293 ms                                                                     | 290 ms: 1.01x faster                                                                 |
| sympy_str                 | 171 ms                                                                     | 169 ms: 1.01x faster                                                                 |
| raytrace                  | 183 ms                                                                     | 182 ms: 1.01x faster                                                                 |
| shortest_path             | 361 ms                                                                     | 358 ms: 1.01x faster                                                                 |
| xml_etree_process         | 39.0 ms                                                                    | 38.7 ms: 1.01x faster                                                                |
| sympy_integrate           | 12.6 ms                                                                    | 12.5 ms: 1.01x faster                                                                |
| async_tree_cpu_io_mixed   | 330 ms                                                                     | 328 ms: 1.00x faster                                                                 |
| scimark_fft               | 182 ms                                                                     | 181 ms: 1.00x faster                                                                 |
| crypto_pyaes              | 47.4 ms                                                                    | 47.3 ms: 1.00x faster                                                                |
| bpe_tokeniser             | 2.90 sec                                                                   | 2.90 sec: 1.00x slower                                                               |
| coverage                  | 290 ms                                                                     | 291 ms: 1.00x slower                                                                 |
| genshi_text               | 15.2 ms                                                                    | 15.3 ms: 1.01x slower                                                                |
| pprint_safe_repr          | 554 ms                                                                     | 558 ms: 1.01x slower                                                                 |
| async_tree_none           | 170 ms                                                                     | 172 ms: 1.01x slower                                                                 |
| go                        | 76.6 ms                                                                    | 77.2 ms: 1.01x slower                                                                |
| logging_simple            | 6.28 us                                                                    | 6.33 us: 1.01x slower                                                                |
| subparsers                | 16.8 ms                                                                    | 17.0 ms: 1.01x slower                                                                |
| deepcopy                  | 170 us                                                                     | 172 us: 1.01x slower                                                                 |
| regex_v8                  | 13.9 ms                                                                    | 14.1 ms: 1.01x slower                                                                |
| richards_super            | 31.3 ms                                                                    | 31.6 ms: 1.01x slower                                                                |
| mako                      | 6.57 ms                                                                    | 6.64 ms: 1.01x slower                                                                |
| float                     | 45.2 ms                                                                    | 45.8 ms: 1.01x slower                                                                |
| json                      | 3.11 ms                                                                    | 3.15 ms: 1.01x slower                                                                |
| pycparser                 | 706 ms                                                                     | 716 ms: 1.01x slower                                                                 |
| pprint_pformat            | 1.12 sec                                                                   | 1.14 sec: 1.01x slower                                                               |
| async_generators          | 229 ms                                                                     | 233 ms: 1.02x slower                                                                 |
| generators                | 19.7 ms                                                                    | 20.0 ms: 1.02x slower                                                                |
| meteor_contest            | 71.6 ms                                                                    | 72.9 ms: 1.02x slower                                                                |
| mdp                       | 802 ms                                                                     | 817 ms: 1.02x slower                                                                 |
| dulwich_log               | 40.0 ms                                                                    | 40.9 ms: 1.02x slower                                                                |
| nqueens                   | 61.5 ms                                                                    | 62.9 ms: 1.02x slower                                                                |
| deepcopy_reduce           | 1.84 us                                                                    | 1.88 us: 1.02x slower                                                                |
| fannkuch                  | 250 ms                                                                     | 256 ms: 1.02x slower                                                                 |
| comprehensions            | 10.7 us                                                                    | 11.0 us: 1.03x slower                                                                |
| regex_compile             | 79.6 ms                                                                    | 81.6 ms: 1.03x slower                                                                |
| async_tree_io_tg          | 391 ms                                                                     | 401 ms: 1.03x slower                                                                 |
| hexiom                    | 4.04 ms                                                                    | 4.15 ms: 1.03x slower                                                                |
| deepcopy_memo             | 18.0 us                                                                    | 18.5 us: 1.03x slower                                                                |
| gc_traversal              | 2.13 ms                                                                    | 2.19 ms: 1.03x slower                                                                |
| regex_effbot              | 1.49 ms                                                                    | 1.58 ms: 1.06x slower                                                                |
| Geometric mean            | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (38): pylint, python_startup_no_site, logging_format, sympy_sum, telco, 2to3, typing_runtime_protocols, html5lib, spectral_norm, xml_etree_iterparse, create_gc_cycles, asyncio_websockets, json_dumps, connected_components, pathlib, async_tree_none_tg, xml_etree_generate, pickle_pure_python, coroutines, richards, scimark_sparse_mat_mult, python_startup, django_template, async_tree_cpu_io_mixed_tg, docutils, many_optionals, pidigits, bench_mp_pool, regex_dna, thrift, unpickle_pure_python, deltablue, tomli_loads, genshi_xml, bench_thread_pool, async_tree_memoization, k_core, async_tree_io

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 69.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown