# Results vs. base

- fork: brandtbucher
- ref: jit_o2
- machine: windows-amd64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.004x faster
- HPT reliability: 99.41%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                 | 14.8 ms                                                                    | 14.1 ms: 1.05x faster                                              |
| async_generators           | 252 ms                                                                     | 245 ms: 1.03x faster                                               |
| async_tree_io_tg           | 395 ms                                                                     | 388 ms: 1.02x faster                                               |
| async_tree_memoization     | 211 ms                                                                     | 208 ms: 1.01x faster                                               |
| async_tree_none            | 171 ms                                                                     | 170 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 346 ms                                                                     | 344 ms: 1.01x faster                                               |
| async_tree_none_tg         | 169 ms                                                                     | 168 ms: 1.01x faster                                               |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                       |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 55.9 ms                                                                    | 55.1 ms: 1.01x faster                                              |
| float          | 44.6 ms                                                                    | 45.0 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 79.4 ms                                                                    | 78.5 ms: 1.01x faster                                              |
| regex_dna      | 119 ms                                                                     | 121 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                       |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 14.6 us                                                                    | 14.3 us: 1.02x faster                                              |
| unpickle_pure_python | 109 us                                                                     | 108 us: 1.01x faster                                               |
| xml_etree_process    | 35.9 ms                                                                    | 36.1 ms: 1.01x slower                                              |
| pickle_pure_python   | 203 us                                                                     | 205 us: 1.01x slower                                               |
| tomli_loads          | 1.15 sec                                                                   | 1.16 sec: 1.01x slower                                             |
| xml_etree_iterparse  | 62.9 ms                                                                    | 64.6 ms: 1.03x slower                                              |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (3): json_dumps, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 23.7 ms                                                                    | 24.2 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (3): genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| fannkuch                   | 241 ms                                                                     | 214 ms: 1.13x faster                                               |
| coroutines                 | 14.8 ms                                                                    | 14.1 ms: 1.05x faster                                              |
| pprint_safe_repr           | 468 ms                                                                     | 447 ms: 1.05x faster                                               |
| spectral_norm              | 66.7 ms                                                                    | 64.1 ms: 1.04x faster                                              |
| crypto_pyaes               | 46.9 ms                                                                    | 45.5 ms: 1.03x faster                                              |
| async_generators           | 252 ms                                                                     | 245 ms: 1.03x faster                                               |
| logging_simple             | 6.26 us                                                                    | 6.11 us: 1.03x faster                                              |
| scimark_sparse_mat_mult    | 2.31 ms                                                                    | 2.26 ms: 1.02x faster                                              |
| logging_format             | 6.71 us                                                                    | 6.57 us: 1.02x faster                                              |
| sympy_expand               | 298 ms                                                                     | 292 ms: 1.02x faster                                               |
| thrift                     | 508 us                                                                     | 499 us: 1.02x faster                                               |
| async_tree_io_tg           | 395 ms                                                                     | 388 ms: 1.02x faster                                               |
| pycparser                  | 705 ms                                                                     | 694 ms: 1.02x faster                                               |
| scimark_sor                | 81.1 ms                                                                    | 79.9 ms: 1.02x faster                                              |
| scimark_monte_carlo        | 41.8 ms                                                                    | 41.2 ms: 1.02x faster                                              |
| json_loads                 | 14.6 us                                                                    | 14.3 us: 1.02x faster                                              |
| scimark_fft                | 153 ms                                                                     | 151 ms: 1.02x faster                                               |
| pprint_pformat             | 939 ms                                                                     | 925 ms: 1.01x faster                                               |
| sympy_str                  | 172 ms                                                                     | 170 ms: 1.01x faster                                               |
| nbody                      | 55.9 ms                                                                    | 55.1 ms: 1.01x faster                                              |
| sqlglot_v2_parse           | 792 us                                                                     | 781 us: 1.01x faster                                               |
| sympy_integrate            | 12.8 ms                                                                    | 12.7 ms: 1.01x faster                                              |
| async_tree_memoization     | 211 ms                                                                     | 208 ms: 1.01x faster                                               |
| go                         | 78.6 ms                                                                    | 77.7 ms: 1.01x faster                                              |
| regex_compile              | 79.4 ms                                                                    | 78.5 ms: 1.01x faster                                              |
| chaos                      | 41.4 ms                                                                    | 41.0 ms: 1.01x faster                                              |
| deltablue                  | 2.22 ms                                                                    | 2.19 ms: 1.01x faster                                              |
| logging_silent             | 54.6 ns                                                                    | 54.1 ns: 1.01x faster                                              |
| sqlglot_v2_transpile       | 993 us                                                                     | 983 us: 1.01x faster                                               |
| mdp                        | 810 ms                                                                     | 802 ms: 1.01x faster                                               |
| unpickle_pure_python       | 109 us                                                                     | 108 us: 1.01x faster                                               |
| async_tree_none            | 171 ms                                                                     | 170 ms: 1.01x faster                                               |
| sqlglot_v2_normalize       | 71.0 ms                                                                    | 70.4 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed_tg | 346 ms                                                                     | 344 ms: 1.01x faster                                               |
| async_tree_none_tg         | 169 ms                                                                     | 168 ms: 1.01x faster                                               |
| sqlglot_v2_optimize        | 34.3 ms                                                                    | 34.5 ms: 1.01x slower                                              |
| comprehensions             | 10.6 us                                                                    | 10.7 us: 1.01x slower                                              |
| nqueens                    | 59.1 ms                                                                    | 59.5 ms: 1.01x slower                                              |
| dulwich_log                | 41.2 ms                                                                    | 41.5 ms: 1.01x slower                                              |
| xml_etree_process          | 35.9 ms                                                                    | 36.1 ms: 1.01x slower                                              |
| pathlib                    | 31.9 ms                                                                    | 32.1 ms: 1.01x slower                                              |
| connected_components       | 327 ms                                                                     | 330 ms: 1.01x slower                                               |
| generators                 | 19.4 ms                                                                    | 19.6 ms: 1.01x slower                                              |
| float                      | 44.6 ms                                                                    | 45.0 ms: 1.01x slower                                              |
| shortest_path              | 358 ms                                                                     | 361 ms: 1.01x slower                                               |
| richards_super             | 31.3 ms                                                                    | 31.7 ms: 1.01x slower                                              |
| pickle_pure_python         | 203 us                                                                     | 205 us: 1.01x slower                                               |
| raytrace                   | 179 ms                                                                     | 181 ms: 1.01x slower                                               |
| tomli_loads                | 1.15 sec                                                                   | 1.16 sec: 1.01x slower                                             |
| deepcopy_memo              | 17.9 us                                                                    | 18.1 us: 1.02x slower                                              |
| coverage                   | 49.3 ms                                                                    | 50.1 ms: 1.02x slower                                              |
| deepcopy                   | 168 us                                                                     | 172 us: 1.02x slower                                               |
| regex_dna                  | 119 ms                                                                     | 121 ms: 1.02x slower                                               |
| django_template            | 23.7 ms                                                                    | 24.2 ms: 1.02x slower                                              |
| deepcopy_reduce            | 1.82 us                                                                    | 1.86 us: 1.03x slower                                              |
| xml_etree_iterparse        | 62.9 ms                                                                    | 64.6 ms: 1.03x slower                                              |
| json                       | 2.97 ms                                                                    | 3.25 ms: 1.09x slower                                              |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                       |

Benchmark hidden because not significant (35): asyncio_websockets, async_tree_io, regex_v8, json_dumps, async_tree_memoization_tg, pylint, sqlite_synth, html5lib, subparsers, xml_etree_generate, create_gc_cycles, xml_etree_parse, telco, genshi_xml, typing_runtime_protocols, docutils, many_optionals, regex_effbot, pidigits, bpe_tokeniser, mako, meteor_contest, pyflate, sympy_sum, python_startup, richards, genshi_text, python_startup_no_site, scimark_lu, 2to3, gc_traversal, sphinx, hexiom, k_core, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown