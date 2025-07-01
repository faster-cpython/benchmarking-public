# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_8
- machine: linux-x86_64
- commit hash: 10bb0c5
- commit date: 2025-06-30
- overall geometric mean: 1.002x faster
- HPT reliability: 70.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 261 ms: 1.01x slower                                               |
| html5lib       | 61.7 ms                                                               | 62.4 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 315 ms                                                                | 311 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 485 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 493 ms: 1.01x faster                                               |
| async_tree_none_tg         | 252 ms                                                                | 249 ms: 1.01x faster                                               |
| asyncio_websockets         | 555 ms                                                                | 551 ms: 1.01x faster                                               |
| async_tree_memoization     | 314 ms                                                                | 312 ms: 1.01x faster                                               |
| async_generators           | 426 ms                                                                | 428 ms: 1.00x slower                                               |
| async_tree_io_tg           | 622 ms                                                                | 639 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (3): async_tree_io, async_tree_none, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 94.8 ms                                                               | 93.1 ms: 1.02x faster                                              |
| pidigits       | 189 ms                                                                | 188 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                               | 22.8 ms: 1.07x faster                                              |
| regex_dna      | 220 ms                                                                | 208 ms: 1.06x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.42 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.83 sec                                                              | 1.80 sec: 1.02x faster                                             |
| unpickle_pure_python | 194 us                                                                | 192 us: 1.01x faster                                               |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.2 ms: 1.01x faster                                              |
| json_dumps           | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                              |
| xml_etree_generate   | 80.0 ms                                                               | 80.9 ms: 1.01x slower                                              |
| pickle_pure_python   | 320 us                                                                | 324 us: 1.01x slower                                               |
| xml_etree_process    | 55.5 ms                                                               | 56.3 ms: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                              |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.2 ms: 1.05x faster                                              |
| genshi_xml      | 50.5 ms                                                               | 49.7 ms: 1.02x faster                                              |
| mako            | 10.6 ms                                                               | 10.5 ms: 1.02x faster                                              |
| django_template | 32.5 ms                                                               | 33.1 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8                   | 24.4 ms                                                               | 22.8 ms: 1.07x faster                                              |
| regex_dna                  | 220 ms                                                                | 208 ms: 1.06x faster                                               |
| crypto_pyaes               | 74.9 ms                                                               | 70.8 ms: 1.06x faster                                              |
| genshi_text                | 22.4 ms                                                               | 21.2 ms: 1.05x faster                                              |
| nqueens                    | 84.3 ms                                                               | 80.7 ms: 1.04x faster                                              |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.84 ms: 1.04x faster                                              |
| gc_traversal               | 5.17 ms                                                               | 4.98 ms: 1.04x faster                                              |
| logging_format             | 6.44 us                                                               | 6.22 us: 1.04x faster                                              |
| scimark_fft                | 315 ms                                                                | 307 ms: 1.02x faster                                               |
| typing_runtime_protocols   | 171 us                                                                | 167 us: 1.02x faster                                               |
| thrift                     | 780 us                                                                | 766 us: 1.02x faster                                               |
| nbody                      | 94.8 ms                                                               | 93.1 ms: 1.02x faster                                              |
| hexiom                     | 6.27 ms                                                               | 6.16 ms: 1.02x faster                                              |
| logging_simple             | 5.73 us                                                               | 5.64 us: 1.02x faster                                              |
| genshi_xml                 | 50.5 ms                                                               | 49.7 ms: 1.02x faster                                              |
| tomli_loads                | 1.83 sec                                                              | 1.80 sec: 1.02x faster                                             |
| mako                       | 10.6 ms                                                               | 10.5 ms: 1.02x faster                                              |
| async_tree_memoization_tg  | 315 ms                                                                | 311 ms: 1.01x faster                                               |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.4 ms: 1.01x faster                                              |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 485 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 493 ms: 1.01x faster                                               |
| async_tree_none_tg         | 252 ms                                                                | 249 ms: 1.01x faster                                               |
| raytrace                   | 273 ms                                                                | 271 ms: 1.01x faster                                               |
| unpickle_pure_python       | 194 us                                                                | 192 us: 1.01x faster                                               |
| sqlite_synth               | 2.79 us                                                               | 2.77 us: 1.01x faster                                              |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.2 ms: 1.01x faster                                              |
| asyncio_websockets         | 555 ms                                                                | 551 ms: 1.01x faster                                               |
| comprehensions             | 16.4 us                                                               | 16.3 us: 1.01x faster                                              |
| python_startup_no_site     | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                              |
| async_tree_memoization     | 314 ms                                                                | 312 ms: 1.01x faster                                               |
| deepcopy_memo              | 29.8 us                                                               | 29.6 us: 1.01x faster                                              |
| create_gc_cycles           | 2.60 ms                                                               | 2.59 ms: 1.00x faster                                              |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| pidigits                   | 189 ms                                                                | 188 ms: 1.00x faster                                               |
| regex_effbot               | 3.43 ms                                                               | 3.42 ms: 1.00x faster                                              |
| shortest_path              | 492 ms                                                                | 493 ms: 1.00x slower                                               |
| chaos                      | 61.4 ms                                                               | 61.6 ms: 1.00x slower                                              |
| dulwich_log                | 59.0 ms                                                               | 59.3 ms: 1.00x slower                                              |
| async_generators           | 426 ms                                                                | 428 ms: 1.00x slower                                               |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.25 ms: 1.01x slower                                              |
| sympy_integrate            | 19.4 ms                                                               | 19.5 ms: 1.01x slower                                              |
| 2to3                       | 259 ms                                                                | 261 ms: 1.01x slower                                               |
| json_dumps                 | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                              |
| deepcopy                   | 257 us                                                                | 260 us: 1.01x slower                                               |
| sympy_sum                  | 150 ms                                                                | 152 ms: 1.01x slower                                               |
| subparsers                 | 23.5 ms                                                               | 23.7 ms: 1.01x slower                                              |
| bpe_tokeniser              | 4.34 sec                                                              | 4.38 sec: 1.01x slower                                             |
| meteor_contest             | 105 ms                                                                | 106 ms: 1.01x slower                                               |
| xml_etree_generate         | 80.0 ms                                                               | 80.9 ms: 1.01x slower                                              |
| json                       | 5.30 ms                                                               | 5.36 ms: 1.01x slower                                              |
| html5lib                   | 61.7 ms                                                               | 62.4 ms: 1.01x slower                                              |
| pickle_pure_python         | 320 us                                                                | 324 us: 1.01x slower                                               |
| connected_components       | 455 ms                                                                | 461 ms: 1.01x slower                                               |
| deltablue                  | 3.02 ms                                                               | 3.06 ms: 1.01x slower                                              |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.58 ms: 1.01x slower                                              |
| many_optionals             | 975 us                                                                | 988 us: 1.01x slower                                               |
| xml_etree_process          | 55.5 ms                                                               | 56.3 ms: 1.01x slower                                              |
| django_template            | 32.5 ms                                                               | 33.1 ms: 1.02x slower                                              |
| scimark_sor                | 117 ms                                                                | 119 ms: 1.02x slower                                               |
| logging_silent             | 103 ns                                                                | 105 ns: 1.02x slower                                               |
| async_tree_io_tg           | 622 ms                                                                | 639 ms: 1.03x slower                                               |
| pycparser                  | 1.11 sec                                                              | 1.16 sec: 1.04x slower                                             |
| generators                 | 30.0 ms                                                               | 31.6 ms: 1.06x slower                                              |
| richards_super             | 38.1 ms                                                               | 40.7 ms: 1.07x slower                                              |
| richards                   | 32.0 ms                                                               | 36.2 ms: 1.13x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (27): djangocms, scimark_monte_carlo, telco, pathlib, async_tree_io, float, json_loads, k_core, mdp, coverage, regex_compile, sympy_expand, xml_etree_parse, sphinx, docutils, async_tree_none, pylint, fannkuch, coroutines, pyflate, sympy_str, spectral_norm, deepcopy_reduce, go, scimark_lu, pprint_pformat, pprint_safe_repr

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 70.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x