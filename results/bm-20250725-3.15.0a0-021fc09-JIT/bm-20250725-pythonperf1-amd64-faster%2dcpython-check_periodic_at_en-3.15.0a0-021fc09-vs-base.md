# Results vs. base

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: windows-amd64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.002x faster
- HPT reliability: 68.75%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| html5lib       | 39.4 ms                                                                    | 38.8 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coroutines                 | 14.8 ms                                                                    | 14.5 ms: 1.02x faster                                                                |
| async_tree_cpu_io_mixed_tg | 348 ms                                                                     | 342 ms: 1.02x faster                                                                 |
| async_generators           | 249 ms                                                                     | 252 ms: 1.01x slower                                                                 |
| async_tree_memoization     | 211 ms                                                                     | 214 ms: 1.02x slower                                                                 |
| async_tree_none_tg         | 166 ms                                                                     | 173 ms: 1.04x slower                                                                 |
| asyncio_websockets         | 162 ms                                                                     | 177 ms: 1.09x slower                                                                 |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 45.6 ms                                                                    | 44.5 ms: 1.03x faster                                                                |
| pidigits       | 146 ms                                                                     | 150 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 81.4 ms                                                                    | 78.7 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 94.6 ms                                                                    | 91.1 ms: 1.04x faster                                                                |
| xml_etree_generate   | 52.4 ms                                                                    | 51.4 ms: 1.02x faster                                                                |
| tomli_loads          | 1.13 sec                                                                   | 1.11 sec: 1.01x faster                                                               |
| json_dumps           | 6.39 ms                                                                    | 6.30 ms: 1.01x faster                                                                |
| json_loads           | 14.5 us                                                                    | 14.8 us: 1.03x slower                                                                |
| unpickle_pure_python | 106 us                                                                     | 113 us: 1.07x slower                                                                 |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 36.6 ms                                                                    | 35.1 ms: 1.04x faster                                                                |
| genshi_text     | 16.3 ms                                                                    | 15.7 ms: 1.04x faster                                                                |
| django_template | 24.5 ms                                                                    | 24.1 ms: 1.02x faster                                                                |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| subparsers                 | 31.9 ms                                                                    | 29.8 ms: 1.07x faster                                                                |
| deepcopy_memo              | 19.2 us                                                                    | 18.0 us: 1.07x faster                                                                |
| many_optionals             | 598 us                                                                     | 571 us: 1.05x faster                                                                 |
| genshi_xml                 | 36.6 ms                                                                    | 35.1 ms: 1.04x faster                                                                |
| nqueens                    | 62.7 ms                                                                    | 60.4 ms: 1.04x faster                                                                |
| raytrace                   | 184 ms                                                                     | 177 ms: 1.04x faster                                                                 |
| logging_simple             | 6.40 us                                                                    | 6.17 us: 1.04x faster                                                                |
| xml_etree_parse            | 94.6 ms                                                                    | 91.1 ms: 1.04x faster                                                                |
| genshi_text                | 16.3 ms                                                                    | 15.7 ms: 1.04x faster                                                                |
| deepcopy_reduce            | 1.92 us                                                                    | 1.85 us: 1.03x faster                                                                |
| regex_compile              | 81.4 ms                                                                    | 78.7 ms: 1.03x faster                                                                |
| deepcopy                   | 176 us                                                                     | 170 us: 1.03x faster                                                                 |
| logging_silent             | 57.3 ns                                                                    | 55.6 ns: 1.03x faster                                                                |
| hexiom                     | 4.28 ms                                                                    | 4.16 ms: 1.03x faster                                                                |
| float                      | 45.6 ms                                                                    | 44.5 ms: 1.03x faster                                                                |
| coroutines                 | 14.8 ms                                                                    | 14.5 ms: 1.02x faster                                                                |
| django_template            | 24.5 ms                                                                    | 24.1 ms: 1.02x faster                                                                |
| xml_etree_generate         | 52.4 ms                                                                    | 51.4 ms: 1.02x faster                                                                |
| async_tree_cpu_io_mixed_tg | 348 ms                                                                     | 342 ms: 1.02x faster                                                                 |
| create_gc_cycles           | 1.37 ms                                                                    | 1.34 ms: 1.02x faster                                                                |
| json                       | 3.07 ms                                                                    | 3.02 ms: 1.02x faster                                                                |
| html5lib                   | 39.4 ms                                                                    | 38.8 ms: 1.02x faster                                                                |
| tomli_loads                | 1.13 sec                                                                   | 1.11 sec: 1.01x faster                                                               |
| comprehensions             | 10.6 us                                                                    | 10.5 us: 1.01x faster                                                                |
| json_dumps                 | 6.39 ms                                                                    | 6.30 ms: 1.01x faster                                                                |
| sympy_expand               | 298 ms                                                                     | 294 ms: 1.01x faster                                                                 |
| richards_super             | 31.2 ms                                                                    | 30.8 ms: 1.01x faster                                                                |
| bpe_tokeniser              | 2.52 sec                                                                   | 2.53 sec: 1.00x slower                                                               |
| mdp                        | 815 ms                                                                     | 823 ms: 1.01x slower                                                                 |
| async_generators           | 249 ms                                                                     | 252 ms: 1.01x slower                                                                 |
| crypto_pyaes               | 45.9 ms                                                                    | 46.6 ms: 1.01x slower                                                                |
| generators                 | 19.5 ms                                                                    | 19.8 ms: 1.02x slower                                                                |
| fannkuch                   | 213 ms                                                                     | 217 ms: 1.02x slower                                                                 |
| sqlite_synth               | 1.55 us                                                                    | 1.58 us: 1.02x slower                                                                |
| async_tree_memoization     | 211 ms                                                                     | 214 ms: 1.02x slower                                                                 |
| deltablue                  | 2.24 ms                                                                    | 2.28 ms: 1.02x slower                                                                |
| telco                      | 4.22 ms                                                                    | 4.30 ms: 1.02x slower                                                                |
| sqlglot_v2_optimize        | 34.8 ms                                                                    | 35.6 ms: 1.02x slower                                                                |
| sqlglot_v2_parse           | 787 us                                                                     | 807 us: 1.03x slower                                                                 |
| json_loads                 | 14.5 us                                                                    | 14.8 us: 1.03x slower                                                                |
| pidigits                   | 146 ms                                                                     | 150 ms: 1.03x slower                                                                 |
| scimark_monte_carlo        | 40.5 ms                                                                    | 41.8 ms: 1.03x slower                                                                |
| coverage                   | 49.4 ms                                                                    | 50.9 ms: 1.03x slower                                                                |
| meteor_contest             | 71.4 ms                                                                    | 74.0 ms: 1.04x slower                                                                |
| async_tree_none_tg         | 166 ms                                                                     | 173 ms: 1.04x slower                                                                 |
| spectral_norm              | 65.5 ms                                                                    | 68.8 ms: 1.05x slower                                                                |
| scimark_sparse_mat_mult    | 2.28 ms                                                                    | 2.39 ms: 1.05x slower                                                                |
| unpickle_pure_python       | 106 us                                                                     | 113 us: 1.07x slower                                                                 |
| asyncio_websockets         | 162 ms                                                                     | 177 ms: 1.09x slower                                                                 |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (43): richards, k_core, pickle_pure_python, chaos, scimark_sor, sqlglot_v2_normalize, async_tree_memoization_tg, thrift, dulwich_log, async_tree_io_tg, xml_etree_iterparse, async_tree_cpu_io_mixed, xml_etree_process, go, sympy_sum, scimark_lu, docutils, 2to3, python_startup_no_site, pylint, connected_components, python_startup, scimark_fft, pprint_pformat, sqlglot_v2_transpile, logging_format, shortest_path, async_tree_io, nbody, gc_traversal, regex_effbot, sympy_integrate, pycparser, mako, sympy_str, sphinx, pyflate, pathlib, typing_runtime_protocols, regex_dna, async_tree_none, pprint_safe_repr, regex_v8

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 68.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown