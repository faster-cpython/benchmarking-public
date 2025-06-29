# Results vs. base

- fork: brandtbucher
- ref: jit_os
- machine: windows-amd64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.006x slower
- HPT reliability: 97.60%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.67 sec                                                                   | 1.65 sec: 1.01x faster                                             |
| html5lib       | 38.1 ms                                                                    | 38.5 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                       |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization     | 216 ms                                                                     | 210 ms: 1.03x faster                                               |
| coroutines                 | 14.4 ms                                                                    | 14.2 ms: 1.01x faster                                              |
| async_tree_none            | 169 ms                                                                     | 171 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 330 ms                                                                     | 334 ms: 1.01x slower                                               |
| async_tree_io_tg           | 389 ms                                                                     | 394 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                     | 346 ms: 1.01x slower                                               |
| async_tree_io              | 393 ms                                                                     | 399 ms: 1.01x slower                                               |
| async_tree_none_tg         | 166 ms                                                                     | 170 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 44.3 ms                                                                    | 45.0 ms: 1.02x slower                                              |
| nbody          | 52.7 ms                                                                    | 59.7 ms: 1.13x slower                                              |
| Geometric mean | (ref)                                                                      | 1.05x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 1.63 ms                                                                    | 1.56 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                       |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|--------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads        | 1.14 sec                                                                   | 1.14 sec: 1.00x slower                                             |
| xml_etree_parse    | 87.9 ms                                                                    | 89.0 ms: 1.01x slower                                              |
| pickle_pure_python | 200 us                                                                     | 205 us: 1.03x slower                                               |
| json_dumps         | 6.12 ms                                                                    | 6.29 ms: 1.03x slower                                              |
| xml_etree_generate | 50.8 ms                                                                    | 54.1 ms: 1.06x slower                                              |
| Geometric mean     | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (4): json_loads, unpickle_pure_python, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako           | 5.45 ms                                                                    | 5.31 ms: 1.03x faster                                              |
| genshi_text    | 15.4 ms                                                                    | 15.5 ms: 1.01x slower                                              |
| genshi_xml     | 34.0 ms                                                                    | 34.5 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| fannkuch                   | 227 ms                                                                     | 216 ms: 1.05x faster                                               |
| regex_effbot               | 1.63 ms                                                                    | 1.56 ms: 1.04x faster                                              |
| async_tree_memoization     | 216 ms                                                                     | 210 ms: 1.03x faster                                               |
| mako                       | 5.45 ms                                                                    | 5.31 ms: 1.03x faster                                              |
| gc_traversal               | 2.18 ms                                                                    | 2.14 ms: 1.02x faster                                              |
| meteor_contest             | 71.6 ms                                                                    | 70.4 ms: 1.02x faster                                              |
| shortest_path              | 362 ms                                                                     | 357 ms: 1.01x faster                                               |
| docutils                   | 1.67 sec                                                                   | 1.65 sec: 1.01x faster                                             |
| scimark_sparse_mat_mult    | 2.31 ms                                                                    | 2.29 ms: 1.01x faster                                              |
| dulwich_log                | 41.3 ms                                                                    | 40.9 ms: 1.01x faster                                              |
| scimark_lu                 | 60.8 ms                                                                    | 60.2 ms: 1.01x faster                                              |
| sqlglot_v2_parse           | 789 us                                                                     | 782 us: 1.01x faster                                               |
| coroutines                 | 14.4 ms                                                                    | 14.2 ms: 1.01x faster                                              |
| sqlglot_v2_normalize       | 71.6 ms                                                                    | 71.1 ms: 1.01x faster                                              |
| crypto_pyaes               | 46.3 ms                                                                    | 46.0 ms: 1.01x faster                                              |
| connected_components       | 330 ms                                                                     | 328 ms: 1.01x faster                                               |
| generators                 | 19.9 ms                                                                    | 19.7 ms: 1.01x faster                                              |
| mdp                        | 807 ms                                                                     | 803 ms: 1.00x faster                                               |
| tomli_loads                | 1.14 sec                                                                   | 1.14 sec: 1.00x slower                                             |
| nqueens                    | 60.4 ms                                                                    | 60.8 ms: 1.01x slower                                              |
| richards                   | 27.0 ms                                                                    | 27.2 ms: 1.01x slower                                              |
| sympy_expand               | 294 ms                                                                     | 296 ms: 1.01x slower                                               |
| raytrace                   | 177 ms                                                                     | 179 ms: 1.01x slower                                               |
| telco                      | 4.26 ms                                                                    | 4.29 ms: 1.01x slower                                              |
| many_optionals             | 446 us                                                                     | 450 us: 1.01x slower                                               |
| sympy_sum                  | 87.7 ms                                                                    | 88.3 ms: 1.01x slower                                              |
| genshi_text                | 15.4 ms                                                                    | 15.5 ms: 1.01x slower                                              |
| deepcopy                   | 169 us                                                                     | 171 us: 1.01x slower                                               |
| html5lib                   | 38.1 ms                                                                    | 38.5 ms: 1.01x slower                                              |
| typing_runtime_protocols   | 104 us                                                                     | 105 us: 1.01x slower                                               |
| richards_super             | 30.5 ms                                                                    | 30.9 ms: 1.01x slower                                              |
| async_tree_none            | 169 ms                                                                     | 171 ms: 1.01x slower                                               |
| xml_etree_parse            | 87.9 ms                                                                    | 89.0 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed    | 330 ms                                                                     | 334 ms: 1.01x slower                                               |
| async_tree_io_tg           | 389 ms                                                                     | 394 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                     | 346 ms: 1.01x slower                                               |
| scimark_fft                | 149 ms                                                                     | 151 ms: 1.01x slower                                               |
| deepcopy_reduce            | 1.82 us                                                                    | 1.85 us: 1.01x slower                                              |
| async_tree_io              | 393 ms                                                                     | 399 ms: 1.01x slower                                               |
| logging_silent             | 54.5 ns                                                                    | 55.3 ns: 1.01x slower                                              |
| genshi_xml                 | 34.0 ms                                                                    | 34.5 ms: 1.01x slower                                              |
| float                      | 44.3 ms                                                                    | 45.0 ms: 1.02x slower                                              |
| logging_simple             | 6.09 us                                                                    | 6.19 us: 1.02x slower                                              |
| deltablue                  | 2.17 ms                                                                    | 2.22 ms: 1.02x slower                                              |
| scimark_sor                | 77.2 ms                                                                    | 78.9 ms: 1.02x slower                                              |
| coverage                   | 49.1 ms                                                                    | 50.3 ms: 1.02x slower                                              |
| pickle_pure_python         | 200 us                                                                     | 205 us: 1.03x slower                                               |
| logging_format             | 6.46 us                                                                    | 6.63 us: 1.03x slower                                              |
| async_tree_none_tg         | 166 ms                                                                     | 170 ms: 1.03x slower                                               |
| spectral_norm              | 62.6 ms                                                                    | 64.3 ms: 1.03x slower                                              |
| thrift                     | 494 us                                                                     | 507 us: 1.03x slower                                               |
| go                         | 75.8 ms                                                                    | 77.9 ms: 1.03x slower                                              |
| json_dumps                 | 6.12 ms                                                                    | 6.29 ms: 1.03x slower                                              |
| chaos                      | 40.0 ms                                                                    | 41.2 ms: 1.03x slower                                              |
| json                       | 3.00 ms                                                                    | 3.17 ms: 1.05x slower                                              |
| deepcopy_memo              | 17.5 us                                                                    | 18.5 us: 1.06x slower                                              |
| scimark_monte_carlo        | 40.2 ms                                                                    | 42.6 ms: 1.06x slower                                              |
| xml_etree_generate         | 50.8 ms                                                                    | 54.1 ms: 1.06x slower                                              |
| nbody                      | 52.7 ms                                                                    | 59.7 ms: 1.13x slower                                              |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                       |

Benchmark hidden because not significant (33): python_startup, asyncio_websockets, 2to3, pprint_pformat, pathlib, regex_dna, create_gc_cycles, hexiom, async_generators, django_template, json_loads, sphinx, pyflate, k_core, pprint_safe_repr, pycparser, sqlglot_v2_transpile, comprehensions, regex_v8, bpe_tokeniser, python_startup_no_site, pylint, unpickle_pure_python, sqlite_synth, subparsers, sympy_str, pidigits, xml_etree_process, sqlglot_v2_optimize, async_tree_memoization_tg, xml_etree_iterparse, sympy_integrate, regex_compile

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 97.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown