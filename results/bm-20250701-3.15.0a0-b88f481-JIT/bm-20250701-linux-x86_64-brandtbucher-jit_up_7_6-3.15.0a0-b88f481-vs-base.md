# Results vs. base

- fork: brandtbucher
- ref: jit_up_7_6
- machine: linux-x86_64
- commit hash: b88f481
- commit date: 2025-07-01
- overall geometric mean: 1.004x faster
- HPT reliability: 57.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 265 ms: 1.02x slower                                              |
| docutils       | 2.64 sec                                                              | 2.67 sec: 1.01x slower                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none_tg         | 252 ms                                                                | 248 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 483 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 492 ms: 1.01x faster                                              |
| async_tree_memoization_tg  | 315 ms                                                                | 311 ms: 1.01x faster                                              |
| coroutines                 | 25.3 ms                                                               | 25.0 ms: 1.01x faster                                             |
| async_generators           | 426 ms                                                                | 434 ms: 1.02x slower                                              |
| async_tree_io_tg           | 622 ms                                                                | 637 ms: 1.03x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (4): async_tree_none, asyncio_websockets, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 94.8 ms                                                               | 93.0 ms: 1.02x faster                                             |
| pidigits       | 189 ms                                                                | 196 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                | 202 ms: 1.09x faster                                              |
| regex_v8       | 24.4 ms                                                               | 22.5 ms: 1.08x faster                                             |
| regex_effbot   | 3.43 ms                                                               | 3.32 ms: 1.03x faster                                             |
| regex_compile  | 127 ms                                                                | 129 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.3 us: 1.02x faster                                             |
| xml_etree_parse      | 141 ms                                                                | 139 ms: 1.01x faster                                              |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.2 ms: 1.01x faster                                             |
| xml_etree_generate   | 80.0 ms                                                               | 80.4 ms: 1.00x slower                                             |
| xml_etree_process    | 55.5 ms                                                               | 55.8 ms: 1.01x slower                                             |
| tomli_loads          | 1.83 sec                                                              | 1.84 sec: 1.01x slower                                            |
| unpickle_pure_python | 194 us                                                                | 196 us: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (2): pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                             |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.5 ms: 1.04x faster                                             |
| mako            | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                             |
| django_template | 32.5 ms                                                               | 32.7 ms: 1.00x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna                  | 220 ms                                                                | 202 ms: 1.09x faster                                              |
| regex_v8                   | 24.4 ms                                                               | 22.5 ms: 1.08x faster                                             |
| gc_traversal               | 5.17 ms                                                               | 4.91 ms: 1.05x faster                                             |
| richards_super             | 38.1 ms                                                               | 36.2 ms: 1.05x faster                                             |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.82 ms: 1.05x faster                                             |
| genshi_text                | 22.4 ms                                                               | 21.5 ms: 1.04x faster                                             |
| regex_effbot               | 3.43 ms                                                               | 3.32 ms: 1.03x faster                                             |
| nqueens                    | 84.3 ms                                                               | 81.5 ms: 1.03x faster                                             |
| logging_format             | 6.44 us                                                               | 6.26 us: 1.03x faster                                             |
| go                         | 117 ms                                                                | 114 ms: 1.03x faster                                              |
| pprint_pformat             | 1.48 sec                                                              | 1.45 sec: 1.02x faster                                            |
| richards                   | 32.0 ms                                                               | 31.3 ms: 1.02x faster                                             |
| logging_simple             | 5.73 us                                                               | 5.61 us: 1.02x faster                                             |
| nbody                      | 94.8 ms                                                               | 93.0 ms: 1.02x faster                                             |
| typing_runtime_protocols   | 171 us                                                                | 167 us: 1.02x faster                                              |
| json_loads                 | 28.7 us                                                               | 28.3 us: 1.02x faster                                             |
| chaos                      | 61.4 ms                                                               | 60.4 ms: 1.02x faster                                             |
| async_tree_none_tg         | 252 ms                                                                | 248 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 483 ms: 1.01x faster                                              |
| telco                      | 7.74 ms                                                               | 7.63 ms: 1.01x faster                                             |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 492 ms: 1.01x faster                                              |
| async_tree_memoization_tg  | 315 ms                                                                | 311 ms: 1.01x faster                                              |
| json                       | 5.30 ms                                                               | 5.24 ms: 1.01x faster                                             |
| xml_etree_parse            | 141 ms                                                                | 139 ms: 1.01x faster                                              |
| coroutines                 | 25.3 ms                                                               | 25.0 ms: 1.01x faster                                             |
| mako                       | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                             |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.01x faster                                              |
| fannkuch                   | 395 ms                                                                | 391 ms: 1.01x faster                                              |
| raytrace                   | 273 ms                                                                | 271 ms: 1.01x faster                                              |
| pyflate                    | 410 ms                                                                | 406 ms: 1.01x faster                                              |
| hexiom                     | 6.27 ms                                                               | 6.22 ms: 1.01x faster                                             |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.2 ms: 1.01x faster                                             |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                            |
| python_startup_no_site     | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                             |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                             |
| connected_components       | 455 ms                                                                | 453 ms: 1.01x faster                                              |
| shortest_path              | 492 ms                                                                | 490 ms: 1.00x faster                                              |
| coverage                   | 88.0 ms                                                               | 88.5 ms: 1.00x slower                                             |
| django_template            | 32.5 ms                                                               | 32.7 ms: 1.00x slower                                             |
| xml_etree_generate         | 80.0 ms                                                               | 80.4 ms: 1.00x slower                                             |
| xml_etree_process          | 55.5 ms                                                               | 55.8 ms: 1.01x slower                                             |
| deepcopy                   | 257 us                                                                | 259 us: 1.01x slower                                              |
| pathlib                    | 17.1 ms                                                               | 17.2 ms: 1.01x slower                                             |
| scimark_sor                | 117 ms                                                                | 118 ms: 1.01x slower                                              |
| tomli_loads                | 1.83 sec                                                              | 1.84 sec: 1.01x slower                                            |
| deltablue                  | 3.02 ms                                                               | 3.05 ms: 1.01x slower                                             |
| scimark_lu                 | 117 ms                                                                | 118 ms: 1.01x slower                                              |
| unpickle_pure_python       | 194 us                                                                | 196 us: 1.01x slower                                              |
| dulwich_log                | 59.0 ms                                                               | 59.7 ms: 1.01x slower                                             |
| sympy_str                  | 272 ms                                                                | 274 ms: 1.01x slower                                              |
| sqlite_synth               | 2.79 us                                                               | 2.82 us: 1.01x slower                                             |
| docutils                   | 2.64 sec                                                              | 2.67 sec: 1.01x slower                                            |
| scimark_monte_carlo        | 65.4 ms                                                               | 66.2 ms: 1.01x slower                                             |
| bpe_tokeniser              | 4.34 sec                                                              | 4.40 sec: 1.01x slower                                            |
| generators                 | 30.0 ms                                                               | 30.4 ms: 1.01x slower                                             |
| regex_compile              | 127 ms                                                                | 129 ms: 1.02x slower                                              |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.59 ms: 1.02x slower                                             |
| async_generators           | 426 ms                                                                | 434 ms: 1.02x slower                                              |
| sympy_integrate            | 19.4 ms                                                               | 19.8 ms: 1.02x slower                                             |
| meteor_contest             | 105 ms                                                                | 107 ms: 1.02x slower                                              |
| 2to3                       | 259 ms                                                                | 265 ms: 1.02x slower                                              |
| sympy_sum                  | 150 ms                                                                | 154 ms: 1.02x slower                                              |
| many_optionals             | 975 us                                                                | 999 us: 1.02x slower                                              |
| async_tree_io_tg           | 622 ms                                                                | 637 ms: 1.03x slower                                              |
| spectral_norm              | 89.8 ms                                                               | 92.2 ms: 1.03x slower                                             |
| deepcopy_reduce            | 2.67 us                                                               | 2.75 us: 1.03x slower                                             |
| pidigits                   | 189 ms                                                                | 196 ms: 1.04x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (26): crypto_pyaes, k_core, thrift, async_tree_none, comprehensions, pprint_safe_repr, asyncio_websockets, async_tree_memoization, deepcopy_memo, genshi_xml, create_gc_cycles, sympy_expand, scimark_fft, async_tree_io, float, pickle_pure_python, subparsers, sqlglot_v2_parse, logging_silent, sqlglot_v2_optimize, sphinx, json_dumps, html5lib, pycparser, djangocms, pylint

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 57.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x