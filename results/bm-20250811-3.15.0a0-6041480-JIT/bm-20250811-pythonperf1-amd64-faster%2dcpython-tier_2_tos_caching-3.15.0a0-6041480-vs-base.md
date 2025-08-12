# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 6041480
- commit date: 2025-08-11
- overall geometric mean: 1.006x faster
- HPT reliability: 94.95%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 1.67 sec                                                                   | 1.65 sec: 1.01x faster                                                             |
| html5lib       | 40.1 ms                                                                    | 39.1 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 389 ms                                                                     | 383 ms: 1.02x faster                                                               |
| async_generators        | 250 ms                                                                     | 246 ms: 1.01x faster                                                               |
| async_tree_cpu_io_mixed | 332 ms                                                                     | 335 ms: 1.01x slower                                                               |
| Geometric mean          | (ref)                                                                      | 1.00x faster                                                                       |

Benchmark hidden because not significant (8): async_tree_none, async_tree_memoization, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 52.8 ms                                                                    | 45.2 ms: 1.17x faster                                                              |
| float          | 44.9 ms                                                                    | 43.7 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.06x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                     | 115 ms: 1.04x faster                                                               |
| regex_v8       | 13.7 ms                                                                    | 13.3 ms: 1.03x faster                                                              |
| regex_effbot   | 1.59 ms                                                                    | 1.54 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_process    | 35.7 ms                                                                    | 35.0 ms: 1.02x faster                                                              |
| xml_etree_generate   | 51.1 ms                                                                    | 50.2 ms: 1.02x faster                                                              |
| xml_etree_parse      | 87.9 ms                                                                    | 87.1 ms: 1.01x faster                                                              |
| json_loads           | 14.1 us                                                                    | 14.3 us: 1.01x slower                                                              |
| tomli_loads          | 1.09 sec                                                                   | 1.11 sec: 1.02x slower                                                             |
| unpickle_pure_python | 105 us                                                                     | 108 us: 1.03x slower                                                               |
| json_dumps           | 5.39 ms                                                                    | 5.60 ms: 1.04x slower                                                              |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 26.8 ms                                                                    | 26.5 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_xml     | 35.0 ms                                                                    | 34.2 ms: 1.02x faster                                                              |
| genshi_text    | 15.6 ms                                                                    | 15.7 ms: 1.01x slower                                                              |
| mako           | 5.38 ms                                                                    | 5.47 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                   | 52.8 ms                                                                    | 45.2 ms: 1.17x faster                                                              |
| telco                   | 4.75 ms                                                                    | 4.25 ms: 1.12x faster                                                              |
| deepcopy_memo           | 18.1 us                                                                    | 17.2 us: 1.05x faster                                                              |
| sqlite_synth            | 1.61 us                                                                    | 1.54 us: 1.05x faster                                                              |
| scimark_monte_carlo     | 41.6 ms                                                                    | 39.8 ms: 1.04x faster                                                              |
| regex_dna               | 120 ms                                                                     | 115 ms: 1.04x faster                                                               |
| regex_v8                | 13.7 ms                                                                    | 13.3 ms: 1.03x faster                                                              |
| float                   | 44.9 ms                                                                    | 43.7 ms: 1.03x faster                                                              |
| regex_effbot            | 1.59 ms                                                                    | 1.54 ms: 1.03x faster                                                              |
| richards                | 27.3 ms                                                                    | 26.6 ms: 1.03x faster                                                              |
| scimark_fft             | 151 ms                                                                     | 147 ms: 1.03x faster                                                               |
| html5lib                | 40.1 ms                                                                    | 39.1 ms: 1.02x faster                                                              |
| genshi_xml              | 35.0 ms                                                                    | 34.2 ms: 1.02x faster                                                              |
| richards_super          | 30.8 ms                                                                    | 30.1 ms: 1.02x faster                                                              |
| meteor_contest          | 71.6 ms                                                                    | 70.2 ms: 1.02x faster                                                              |
| xml_etree_process       | 35.7 ms                                                                    | 35.0 ms: 1.02x faster                                                              |
| deepcopy                | 169 us                                                                     | 166 us: 1.02x faster                                                               |
| create_gc_cycles        | 1.33 ms                                                                    | 1.31 ms: 1.02x faster                                                              |
| xml_etree_generate      | 51.1 ms                                                                    | 50.2 ms: 1.02x faster                                                              |
| generators              | 19.7 ms                                                                    | 19.4 ms: 1.02x faster                                                              |
| json                    | 3.10 ms                                                                    | 3.05 ms: 1.02x faster                                                              |
| async_tree_io           | 389 ms                                                                     | 383 ms: 1.02x faster                                                               |
| crypto_pyaes            | 46.3 ms                                                                    | 45.6 ms: 1.02x faster                                                              |
| nqueens                 | 59.9 ms                                                                    | 59.1 ms: 1.01x faster                                                              |
| sympy_str               | 173 ms                                                                     | 171 ms: 1.01x faster                                                               |
| async_generators        | 250 ms                                                                     | 246 ms: 1.01x faster                                                               |
| comprehensions          | 10.6 us                                                                    | 10.5 us: 1.01x faster                                                              |
| python_startup          | 26.8 ms                                                                    | 26.5 ms: 1.01x faster                                                              |
| sqlglot_v2_transpile    | 985 us                                                                     | 976 us: 1.01x faster                                                               |
| xml_etree_parse         | 87.9 ms                                                                    | 87.1 ms: 1.01x faster                                                              |
| scimark_sparse_mat_mult | 2.33 ms                                                                    | 2.32 ms: 1.01x faster                                                              |
| docutils                | 1.67 sec                                                                   | 1.65 sec: 1.01x faster                                                             |
| scimark_lu              | 57.2 ms                                                                    | 56.9 ms: 1.01x faster                                                              |
| mdp                     | 800 ms                                                                     | 796 ms: 1.00x faster                                                               |
| genshi_text             | 15.6 ms                                                                    | 15.7 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed | 332 ms                                                                     | 335 ms: 1.01x slower                                                               |
| scimark_sor             | 74.5 ms                                                                    | 75.4 ms: 1.01x slower                                                              |
| json_loads              | 14.1 us                                                                    | 14.3 us: 1.01x slower                                                              |
| fannkuch                | 209 ms                                                                     | 212 ms: 1.01x slower                                                               |
| deltablue               | 2.26 ms                                                                    | 2.29 ms: 1.01x slower                                                              |
| raytrace                | 174 ms                                                                     | 177 ms: 1.02x slower                                                               |
| sympy_expand            | 292 ms                                                                     | 297 ms: 1.02x slower                                                               |
| hexiom                  | 4.06 ms                                                                    | 4.13 ms: 1.02x slower                                                              |
| mako                    | 5.38 ms                                                                    | 5.47 ms: 1.02x slower                                                              |
| coverage                | 48.5 ms                                                                    | 49.5 ms: 1.02x slower                                                              |
| tomli_loads             | 1.09 sec                                                                   | 1.11 sec: 1.02x slower                                                             |
| sqlglot_v2_optimize     | 34.4 ms                                                                    | 35.2 ms: 1.02x slower                                                              |
| logging_format          | 6.43 us                                                                    | 6.60 us: 1.03x slower                                                              |
| sqlglot_v2_normalize    | 70.6 ms                                                                    | 72.5 ms: 1.03x slower                                                              |
| bpe_tokeniser           | 2.49 sec                                                                   | 2.56 sec: 1.03x slower                                                             |
| unpickle_pure_python    | 105 us                                                                     | 108 us: 1.03x slower                                                               |
| json_dumps              | 5.39 ms                                                                    | 5.60 ms: 1.04x slower                                                              |
| Geometric mean          | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (40): python_startup_no_site, pathlib, sphinx, async_tree_none, pycparser, deepcopy_reduce, 2to3, async_tree_memoization, gc_traversal, pprint_safe_repr, asyncio_websockets, pyflate, sqlglot_v2_parse, many_optionals, async_tree_memoization_tg, async_tree_none_tg, shortest_path, async_tree_io_tg, xml_etree_iterparse, pickle_pure_python, logging_silent, go, typing_runtime_protocols, pidigits, connected_components, sympy_integrate, django_template, subparsers, regex_compile, sympy_sum, pylint, spectral_norm, chaos, k_core, async_tree_cpu_io_mixed_tg, pprint_pformat, thrift, logging_simple, coroutines, dulwich_log

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 94.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown