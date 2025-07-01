# Results vs. base

- fork: brandtbucher
- ref: jit_up_10_9
- machine: linux-x86_64
- commit hash: 2f53411
- commit date: 2025-06-30
- overall geometric mean: 1.001x slower
- HPT reliability: 89.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 261 ms: 1.01x slower                                               |
| html5lib       | 61.7 ms                                                               | 62.3 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                 | 25.3 ms                                                               | 24.9 ms: 1.02x faster                                              |
| asyncio_websockets         | 555 ms                                                                | 552 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 504 ms: 1.01x slower                                               |
| async_generators           | 426 ms                                                                | 432 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 499 ms: 1.02x slower                                               |
| async_tree_io_tg           | 622 ms                                                                | 640 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 65.6 ms                                                               | 66.3 ms: 1.01x slower                                              |
| pidigits       | 189 ms                                                                | 193 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                               | 22.0 ms: 1.11x faster                                              |
| regex_dna      | 220 ms                                                                | 203 ms: 1.08x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.27 ms: 1.05x faster                                              |
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                                | 190 us: 1.02x faster                                               |
| xml_etree_process    | 55.5 ms                                                               | 55.2 ms: 1.01x faster                                              |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.7 ms: 1.00x faster                                              |
| json_dumps           | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (5): tomli_loads, xml_etree_parse, json_loads, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.93 ms: 1.01x faster                                              |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.6 ms: 1.04x faster                                              |
| mako            | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                              |
| genshi_xml      | 50.5 ms                                                               | 50.8 ms: 1.01x slower                                              |
| django_template | 32.5 ms                                                               | 32.8 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_10_9-3.15.0a0-2f53411 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8                   | 24.4 ms                                                               | 22.0 ms: 1.11x faster                                              |
| gc_traversal               | 5.17 ms                                                               | 4.76 ms: 1.09x faster                                              |
| regex_dna                  | 220 ms                                                                | 203 ms: 1.08x faster                                               |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.74 ms: 1.06x faster                                              |
| regex_effbot               | 3.43 ms                                                               | 3.27 ms: 1.05x faster                                              |
| crypto_pyaes               | 74.9 ms                                                               | 71.6 ms: 1.05x faster                                              |
| genshi_text                | 22.4 ms                                                               | 21.6 ms: 1.04x faster                                              |
| logging_simple             | 5.73 us                                                               | 5.58 us: 1.03x faster                                              |
| pprint_pformat             | 1.48 sec                                                              | 1.45 sec: 1.03x faster                                             |
| logging_silent             | 103 ns                                                                | 101 ns: 1.03x faster                                               |
| mako                       | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                              |
| logging_format             | 6.44 us                                                               | 6.32 us: 1.02x faster                                              |
| unpickle_pure_python       | 194 us                                                                | 190 us: 1.02x faster                                               |
| coroutines                 | 25.3 ms                                                               | 24.9 ms: 1.02x faster                                              |
| pprint_safe_repr           | 721 ms                                                                | 710 ms: 1.02x faster                                               |
| pathlib                    | 17.1 ms                                                               | 16.8 ms: 1.02x faster                                              |
| create_gc_cycles           | 2.60 ms                                                               | 2.57 ms: 1.01x faster                                              |
| typing_runtime_protocols   | 171 us                                                                | 168 us: 1.01x faster                                               |
| go                         | 117 ms                                                                | 115 ms: 1.01x faster                                               |
| scimark_fft                | 315 ms                                                                | 312 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.99 ms                                                               | 6.93 ms: 1.01x faster                                              |
| hexiom                     | 6.27 ms                                                               | 6.23 ms: 1.01x faster                                              |
| asyncio_websockets         | 555 ms                                                                | 552 ms: 1.01x faster                                               |
| xml_etree_process          | 55.5 ms                                                               | 55.2 ms: 1.01x faster                                              |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.00x faster                                             |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.7 ms: 1.00x faster                                              |
| coverage                   | 88.0 ms                                                               | 88.3 ms: 1.00x slower                                              |
| regex_compile              | 127 ms                                                                | 127 ms: 1.00x slower                                               |
| bpe_tokeniser              | 4.34 sec                                                              | 4.36 sec: 1.00x slower                                             |
| sympy_str                  | 272 ms                                                                | 273 ms: 1.01x slower                                               |
| 2to3                       | 259 ms                                                                | 261 ms: 1.01x slower                                               |
| genshi_xml                 | 50.5 ms                                                               | 50.8 ms: 1.01x slower                                              |
| django_template            | 32.5 ms                                                               | 32.8 ms: 1.01x slower                                              |
| html5lib                   | 61.7 ms                                                               | 62.3 ms: 1.01x slower                                              |
| json_dumps                 | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                              |
| sqlite_synth               | 2.79 us                                                               | 2.82 us: 1.01x slower                                              |
| meteor_contest             | 105 ms                                                                | 106 ms: 1.01x slower                                               |
| float                      | 65.6 ms                                                               | 66.3 ms: 1.01x slower                                              |
| pyflate                    | 410 ms                                                                | 415 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 504 ms: 1.01x slower                                               |
| dulwich_log                | 59.0 ms                                                               | 59.8 ms: 1.01x slower                                              |
| sympy_integrate            | 19.4 ms                                                               | 19.6 ms: 1.01x slower                                              |
| deepcopy                   | 257 us                                                                | 260 us: 1.01x slower                                               |
| sympy_sum                  | 150 ms                                                                | 152 ms: 1.01x slower                                               |
| scimark_sor                | 117 ms                                                                | 119 ms: 1.01x slower                                               |
| async_generators           | 426 ms                                                                | 432 ms: 1.01x slower                                               |
| deltablue                  | 3.02 ms                                                               | 3.07 ms: 1.02x slower                                              |
| subparsers                 | 23.5 ms                                                               | 23.8 ms: 1.02x slower                                              |
| scimark_lu                 | 117 ms                                                                | 119 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 499 ms: 1.02x slower                                               |
| comprehensions             | 16.4 us                                                               | 16.7 us: 1.02x slower                                              |
| fannkuch                   | 395 ms                                                                | 402 ms: 1.02x slower                                               |
| scimark_monte_carlo        | 65.4 ms                                                               | 66.7 ms: 1.02x slower                                              |
| pidigits                   | 189 ms                                                                | 193 ms: 1.02x slower                                               |
| many_optionals             | 975 us                                                                | 997 us: 1.02x slower                                               |
| deepcopy_reduce            | 2.67 us                                                               | 2.74 us: 1.02x slower                                              |
| generators                 | 30.0 ms                                                               | 30.8 ms: 1.03x slower                                              |
| async_tree_io_tg           | 622 ms                                                                | 640 ms: 1.03x slower                                               |
| connected_components       | 455 ms                                                                | 485 ms: 1.07x slower                                               |
| richards_super             | 38.1 ms                                                               | 43.5 ms: 1.14x slower                                              |
| richards                   | 32.0 ms                                                               | 38.7 ms: 1.21x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (31): nbody, k_core, async_tree_memoization_tg, sqlglot_v2_optimize, tomli_loads, nqueens, chaos, sqlglot_v2_parse, shortest_path, async_tree_none, deepcopy_memo, async_tree_none_tg, raytrace, xml_etree_parse, sqlglot_v2_transpile, async_tree_io, json_loads, pycparser, sympy_expand, spectral_norm, json, docutils, sphinx, xml_etree_generate, sqlglot_v2_normalize, async_tree_memoization, pickle_pure_python, thrift, telco, pylint, djangocms

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 89.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x