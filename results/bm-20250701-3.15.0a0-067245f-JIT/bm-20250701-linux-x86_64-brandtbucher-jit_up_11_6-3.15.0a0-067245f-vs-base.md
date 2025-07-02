# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_6
- machine: linux-x86_64
- commit hash: 067245f
- commit date: 2025-07-01
- overall geometric mean: 1.004x faster
- HPT reliability: 60.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 261 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 498 ms                                                                | 494 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 487 ms: 1.01x faster                                               |
| asyncio_websockets         | 555 ms                                                                | 553 ms: 1.00x faster                                               |
| async_generators           | 426 ms                                                                | 424 ms: 1.00x faster                                               |
| async_tree_io_tg           | 622 ms                                                                | 639 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (6): async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, coroutines, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 94.8 ms                                                               | 93.6 ms: 1.01x faster                                              |
| pidigits       | 189 ms                                                                | 189 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                               | 23.8 ms: 1.02x faster                                              |
| regex_dna      | 220 ms                                                                | 216 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.0 us: 1.03x faster                                              |
| unpickle_pure_python | 194 us                                                                | 190 us: 1.02x faster                                               |
| tomli_loads          | 1.83 sec                                                              | 1.82 sec: 1.01x faster                                             |
| xml_etree_iterparse  | 99.0 ms                                                               | 99.3 ms: 1.00x slower                                              |
| pickle_pure_python   | 320 us                                                                | 322 us: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (4): json_dumps, xml_etree_generate, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.95 ms: 1.01x faster                                              |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.5 ms: 1.04x faster                                              |
| mako            | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                              |
| genshi_xml      | 50.5 ms                                                               | 50.1 ms: 1.01x faster                                              |
| django_template | 32.5 ms                                                               | 32.4 ms: 1.00x faster                                              |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                               | 4.87 ms: 1.06x faster                                              |
| pprint_safe_repr           | 721 ms                                                                | 691 ms: 1.04x faster                                               |
| pprint_pformat             | 1.48 sec                                                              | 1.43 sec: 1.04x faster                                             |
| genshi_text                | 22.4 ms                                                               | 21.5 ms: 1.04x faster                                              |
| logging_format             | 6.44 us                                                               | 6.21 us: 1.04x faster                                              |
| logging_simple             | 5.73 us                                                               | 5.53 us: 1.04x faster                                              |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.87 ms: 1.04x faster                                              |
| crypto_pyaes               | 74.9 ms                                                               | 72.8 ms: 1.03x faster                                              |
| json_loads                 | 28.7 us                                                               | 28.0 us: 1.03x faster                                              |
| go                         | 117 ms                                                                | 114 ms: 1.03x faster                                               |
| json                       | 5.30 ms                                                               | 5.17 ms: 1.03x faster                                              |
| regex_v8                   | 24.4 ms                                                               | 23.8 ms: 1.02x faster                                              |
| typing_runtime_protocols   | 171 us                                                                | 167 us: 1.02x faster                                               |
| nqueens                    | 84.3 ms                                                               | 82.4 ms: 1.02x faster                                              |
| unpickle_pure_python       | 194 us                                                                | 190 us: 1.02x faster                                               |
| mako                       | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                              |
| k_core                     | 2.30 sec                                                              | 2.25 sec: 1.02x faster                                             |
| regex_dna                  | 220 ms                                                                | 216 ms: 1.02x faster                                               |
| deepcopy_memo              | 29.8 us                                                               | 29.4 us: 1.01x faster                                              |
| raytrace                   | 273 ms                                                                | 270 ms: 1.01x faster                                               |
| nbody                      | 94.8 ms                                                               | 93.6 ms: 1.01x faster                                              |
| create_gc_cycles           | 2.60 ms                                                               | 2.57 ms: 1.01x faster                                              |
| comprehensions             | 16.4 us                                                               | 16.3 us: 1.01x faster                                              |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.6 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 494 ms: 1.01x faster                                               |
| genshi_xml                 | 50.5 ms                                                               | 50.1 ms: 1.01x faster                                              |
| coverage                   | 88.0 ms                                                               | 87.4 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 487 ms: 1.01x faster                                               |
| tomli_loads                | 1.83 sec                                                              | 1.82 sec: 1.01x faster                                             |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                             |
| scimark_fft                | 315 ms                                                                | 313 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.99 ms                                                               | 6.95 ms: 1.01x faster                                              |
| hexiom                     | 6.27 ms                                                               | 6.25 ms: 1.00x faster                                              |
| asyncio_websockets         | 555 ms                                                                | 553 ms: 1.00x faster                                               |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| django_template            | 32.5 ms                                                               | 32.4 ms: 1.00x faster                                              |
| async_generators           | 426 ms                                                                | 424 ms: 1.00x faster                                               |
| pidigits                   | 189 ms                                                                | 189 ms: 1.00x faster                                               |
| spectral_norm              | 89.8 ms                                                               | 90.0 ms: 1.00x slower                                              |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.57 ms: 1.00x slower                                              |
| sympy_str                  | 272 ms                                                                | 272 ms: 1.00x slower                                               |
| xml_etree_iterparse        | 99.0 ms                                                               | 99.3 ms: 1.00x slower                                              |
| sympy_sum                  | 150 ms                                                                | 151 ms: 1.00x slower                                               |
| shortest_path              | 492 ms                                                                | 494 ms: 1.01x slower                                               |
| sympy_integrate            | 19.4 ms                                                               | 19.5 ms: 1.01x slower                                              |
| scimark_sor                | 117 ms                                                                | 118 ms: 1.01x slower                                               |
| deltablue                  | 3.02 ms                                                               | 3.04 ms: 1.01x slower                                              |
| pickle_pure_python         | 320 us                                                                | 322 us: 1.01x slower                                               |
| 2to3                       | 259 ms                                                                | 261 ms: 1.01x slower                                               |
| generators                 | 30.0 ms                                                               | 30.2 ms: 1.01x slower                                              |
| bpe_tokeniser              | 4.34 sec                                                              | 4.37 sec: 1.01x slower                                             |
| pathlib                    | 17.1 ms                                                               | 17.2 ms: 1.01x slower                                              |
| sqlite_synth               | 2.79 us                                                               | 2.82 us: 1.01x slower                                              |
| pyflate                    | 410 ms                                                                | 415 ms: 1.01x slower                                               |
| fannkuch                   | 395 ms                                                                | 401 ms: 1.01x slower                                               |
| connected_components       | 455 ms                                                                | 462 ms: 1.02x slower                                               |
| many_optionals             | 975 us                                                                | 991 us: 1.02x slower                                               |
| dulwich_log                | 59.0 ms                                                               | 60.0 ms: 1.02x slower                                              |
| logging_silent             | 103 ns                                                                | 105 ns: 1.02x slower                                               |
| meteor_contest             | 105 ms                                                                | 107 ms: 1.02x slower                                               |
| richards_super             | 38.1 ms                                                               | 38.9 ms: 1.02x slower                                              |
| subparsers                 | 23.5 ms                                                               | 24.0 ms: 1.02x slower                                              |
| pycparser                  | 1.11 sec                                                              | 1.14 sec: 1.03x slower                                             |
| async_tree_io_tg           | 622 ms                                                                | 639 ms: 1.03x slower                                               |
| scimark_lu                 | 117 ms                                                                | 120 ms: 1.03x slower                                               |
| richards                   | 32.0 ms                                                               | 33.7 ms: 1.05x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (27): scimark_monte_carlo, sqlglot_v2_normalize, djangocms, async_tree_io, regex_compile, regex_effbot, thrift, async_tree_none_tg, async_tree_memoization_tg, sympy_expand, deepcopy_reduce, float, json_dumps, sqlglot_v2_parse, deepcopy, telco, async_tree_memoization, xml_etree_generate, docutils, chaos, pylint, coroutines, async_tree_none, xml_etree_parse, html5lib, sphinx, xml_etree_process

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 60.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x