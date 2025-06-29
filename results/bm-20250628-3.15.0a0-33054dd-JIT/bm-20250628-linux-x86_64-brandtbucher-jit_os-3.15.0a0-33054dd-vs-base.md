# Results vs. base

- fork: brandtbucher
- ref: jit_os
- machine: linux-x86_64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.004x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.63 sec                                                              | 2.62 sec: 1.00x faster                                        |
| html5lib       | 62.5 ms                                                               | 62.0 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 499 ms                                                                | 486 ms: 1.03x faster                                          |
| async_tree_cpu_io_mixed    | 503 ms                                                                | 492 ms: 1.02x faster                                          |
| async_generators           | 426 ms                                                                | 431 ms: 1.01x slower                                          |
| coroutines                 | 25.1 ms                                                               | 25.5 ms: 1.02x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 193 ms                                                                | 188 ms: 1.02x faster                                          |
| nbody          | 94.7 ms                                                               | 97.9 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 22.5 ms                                                               | 22.4 ms: 1.00x faster                                         |
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x faster                                          |
| regex_effbot   | 3.14 ms                                                               | 3.25 ms: 1.04x slower                                         |
| regex_dna      | 198 ms                                                                | 207 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_process  | 56.1 ms                                                               | 55.3 ms: 1.01x faster                                         |
| tomli_loads        | 1.85 sec                                                              | 1.83 sec: 1.01x faster                                        |
| xml_etree_generate | 80.8 ms                                                               | 79.9 ms: 1.01x faster                                         |
| xml_etree_parse    | 141 ms                                                                | 140 ms: 1.01x faster                                          |
| pickle_pure_python | 321 us                                                                | 319 us: 1.01x faster                                          |
| Geometric mean     | (ref)                                                                 | 1.01x faster                                                  |

Benchmark hidden because not significant (4): json_dumps, xml_etree_iterparse, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                         |
| python_startup_no_site | 6.93 ms                                                               | 6.96 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 50.7 ms                                                               | 49.7 ms: 1.02x faster                                         |
| mako            | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                         |
| django_template | 32.6 ms                                                               | 32.4 ms: 1.01x faster                                         |
| genshi_text     | 21.6 ms                                                               | 21.8 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pprint_pformat             | 1.50 sec                                                              | 1.41 sec: 1.06x faster                                        |
| pycparser                  | 1.16 sec                                                              | 1.11 sec: 1.04x faster                                        |
| pprint_safe_repr           | 723 ms                                                                | 702 ms: 1.03x faster                                          |
| deepcopy_reduce            | 2.76 us                                                               | 2.68 us: 1.03x faster                                         |
| thrift                     | 790 us                                                                | 769 us: 1.03x faster                                          |
| async_tree_cpu_io_mixed_tg | 499 ms                                                                | 486 ms: 1.03x faster                                          |
| async_tree_cpu_io_mixed    | 503 ms                                                                | 492 ms: 1.02x faster                                          |
| fannkuch                   | 402 ms                                                                | 393 ms: 1.02x faster                                          |
| pidigits                   | 193 ms                                                                | 188 ms: 1.02x faster                                          |
| genshi_xml                 | 50.7 ms                                                               | 49.7 ms: 1.02x faster                                         |
| pathlib                    | 17.3 ms                                                               | 17.0 ms: 1.02x faster                                         |
| gc_traversal               | 5.16 ms                                                               | 5.09 ms: 1.01x faster                                         |
| xml_etree_process          | 56.1 ms                                                               | 55.3 ms: 1.01x faster                                         |
| logging_simple             | 5.72 us                                                               | 5.64 us: 1.01x faster                                         |
| subparsers                 | 23.7 ms                                                               | 23.4 ms: 1.01x faster                                         |
| deepcopy_memo              | 29.9 us                                                               | 29.5 us: 1.01x faster                                         |
| scimark_lu                 | 120 ms                                                                | 119 ms: 1.01x faster                                          |
| scimark_monte_carlo        | 66.3 ms                                                               | 65.5 ms: 1.01x faster                                         |
| tomli_loads                | 1.85 sec                                                              | 1.83 sec: 1.01x faster                                        |
| dulwich_log                | 59.8 ms                                                               | 59.1 ms: 1.01x faster                                         |
| logging_format             | 6.36 us                                                               | 6.29 us: 1.01x faster                                         |
| sympy_sum                  | 150 ms                                                                | 148 ms: 1.01x faster                                          |
| xml_etree_generate         | 80.8 ms                                                               | 79.9 ms: 1.01x faster                                         |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.6 ms: 1.01x faster                                         |
| telco                      | 7.69 ms                                                               | 7.61 ms: 1.01x faster                                         |
| sqlglot_v2_transpile       | 1.57 ms                                                               | 1.55 ms: 1.01x faster                                         |
| sqlglot_v2_parse           | 1.25 ms                                                               | 1.24 ms: 1.01x faster                                         |
| deltablue                  | 3.06 ms                                                               | 3.03 ms: 1.01x faster                                         |
| html5lib                   | 62.5 ms                                                               | 62.0 ms: 1.01x faster                                         |
| sqlglot_v2_normalize       | 108 ms                                                                | 107 ms: 1.01x faster                                          |
| xml_etree_parse            | 141 ms                                                                | 140 ms: 1.01x faster                                          |
| typing_runtime_protocols   | 167 us                                                                | 166 us: 1.01x faster                                          |
| mako                       | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                         |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                        |
| meteor_contest             | 105 ms                                                                | 105 ms: 1.01x faster                                          |
| sympy_str                  | 272 ms                                                                | 270 ms: 1.01x faster                                          |
| sqlite_synth               | 2.82 us                                                               | 2.80 us: 1.01x faster                                         |
| connected_components       | 451 ms                                                                | 448 ms: 1.01x faster                                          |
| bpe_tokeniser              | 4.34 sec                                                              | 4.31 sec: 1.01x faster                                        |
| pickle_pure_python         | 321 us                                                                | 319 us: 1.01x faster                                          |
| django_template            | 32.6 ms                                                               | 32.4 ms: 1.01x faster                                         |
| sympy_expand               | 467 ms                                                                | 465 ms: 1.00x faster                                          |
| sympy_integrate            | 19.4 ms                                                               | 19.3 ms: 1.00x faster                                         |
| regex_v8                   | 22.5 ms                                                               | 22.4 ms: 1.00x faster                                         |
| go                         | 116 ms                                                                | 115 ms: 1.00x faster                                          |
| regex_compile              | 127 ms                                                                | 127 ms: 1.00x faster                                          |
| scimark_sor                | 119 ms                                                                | 118 ms: 1.00x faster                                          |
| docutils                   | 2.63 sec                                                              | 2.62 sec: 1.00x faster                                        |
| raytrace                   | 275 ms                                                                | 274 ms: 1.00x faster                                          |
| shortest_path              | 488 ms                                                                | 489 ms: 1.00x slower                                          |
| create_gc_cycles           | 2.59 ms                                                               | 2.59 ms: 1.00x slower                                         |
| deepcopy                   | 256 us                                                                | 257 us: 1.00x slower                                          |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                         |
| hexiom                     | 6.21 ms                                                               | 6.23 ms: 1.00x slower                                         |
| scimark_fft                | 311 ms                                                                | 312 ms: 1.00x slower                                          |
| python_startup_no_site     | 6.93 ms                                                               | 6.96 ms: 1.00x slower                                         |
| genshi_text                | 21.6 ms                                                               | 21.8 ms: 1.01x slower                                         |
| pyflate                    | 408 ms                                                                | 411 ms: 1.01x slower                                          |
| nqueens                    | 81.7 ms                                                               | 82.6 ms: 1.01x slower                                         |
| async_generators           | 426 ms                                                                | 431 ms: 1.01x slower                                          |
| coroutines                 | 25.1 ms                                                               | 25.5 ms: 1.02x slower                                         |
| spectral_norm              | 90.2 ms                                                               | 91.8 ms: 1.02x slower                                         |
| nbody                      | 94.7 ms                                                               | 97.9 ms: 1.03x slower                                         |
| regex_effbot               | 3.14 ms                                                               | 3.25 ms: 1.04x slower                                         |
| scimark_sparse_mat_mult    | 4.88 ms                                                               | 5.07 ms: 1.04x slower                                         |
| regex_dna                  | 198 ms                                                                | 207 ms: 1.04x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (27): richards_super, async_tree_io_tg, richards, djangocms, crypto_pyaes, async_tree_none_tg, async_tree_memoization, chaos, async_tree_memoization_tg, async_tree_io, many_optionals, pylint, coverage, asyncio_websockets, float, comprehensions, sphinx, 2to3, json_dumps, xml_etree_iterparse, unpickle_pure_python, json, json_loads, generators, async_tree_none, logging_silent, k_core

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x