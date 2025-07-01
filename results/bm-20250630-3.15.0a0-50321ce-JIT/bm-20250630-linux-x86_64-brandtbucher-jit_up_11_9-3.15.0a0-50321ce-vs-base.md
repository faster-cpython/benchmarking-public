# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_9
- machine: linux-x86_64
- commit hash: 50321ce
- commit date: 2025-06-30
- overall geometric mean: 1.005x faster
- HPT reliability: 97.02%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 259 ms: 1.00x slower                                               |
| html5lib       | 61.7 ms                                                               | 62.3 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 315 ms                                                                | 310 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 492 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 485 ms: 1.01x faster                                               |
| coroutines                 | 25.3 ms                                                               | 25.0 ms: 1.01x faster                                              |
| async_tree_none_tg         | 252 ms                                                                | 249 ms: 1.01x faster                                               |
| async_tree_memoization     | 314 ms                                                                | 312 ms: 1.01x faster                                               |
| asyncio_websockets         | 555 ms                                                                | 553 ms: 1.00x faster                                               |
| async_generators           | 426 ms                                                                | 431 ms: 1.01x slower                                               |
| async_tree_io_tg           | 622 ms                                                                | 637 ms: 1.02x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (2): async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 189 ms: 1.00x faster                                               |
| float          | 65.6 ms                                                               | 66.2 ms: 1.01x slower                                              |
| nbody          | 94.8 ms                                                               | 95.8 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                | 198 ms: 1.11x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.14 ms: 1.09x faster                                              |
| regex_v8       | 24.4 ms                                                               | 22.6 ms: 1.08x faster                                              |
| regex_compile  | 127 ms                                                                | 128 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.4 us: 1.01x faster                                              |
| unpickle_pure_python | 194 us                                                                | 192 us: 1.01x faster                                               |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.4 ms: 1.01x faster                                              |
| tomli_loads          | 1.83 sec                                                              | 1.82 sec: 1.00x faster                                             |
| json_dumps           | 11.0 ms                                                               | 11.2 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                              |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.5 ms: 1.04x faster                                              |
| genshi_xml      | 50.5 ms                                                               | 49.7 ms: 1.02x faster                                              |
| mako            | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                              |
| django_template | 32.5 ms                                                               | 32.4 ms: 1.00x faster                                              |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna                  | 220 ms                                                                | 198 ms: 1.11x faster                                               |
| regex_effbot               | 3.43 ms                                                               | 3.14 ms: 1.09x faster                                              |
| regex_v8                   | 24.4 ms                                                               | 22.6 ms: 1.08x faster                                              |
| crypto_pyaes               | 74.9 ms                                                               | 70.8 ms: 1.06x faster                                              |
| pprint_pformat             | 1.48 sec                                                              | 1.43 sec: 1.04x faster                                             |
| gc_traversal               | 5.17 ms                                                               | 4.97 ms: 1.04x faster                                              |
| logging_format             | 6.44 us                                                               | 6.20 us: 1.04x faster                                              |
| genshi_text                | 22.4 ms                                                               | 21.5 ms: 1.04x faster                                              |
| thrift                     | 780 us                                                                | 761 us: 1.03x faster                                               |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.92 ms: 1.03x faster                                              |
| logging_simple             | 5.73 us                                                               | 5.60 us: 1.02x faster                                              |
| scimark_fft                | 315 ms                                                                | 308 ms: 1.02x faster                                               |
| typing_runtime_protocols   | 171 us                                                                | 168 us: 1.02x faster                                               |
| async_tree_memoization_tg  | 315 ms                                                                | 310 ms: 1.02x faster                                               |
| genshi_xml                 | 50.5 ms                                                               | 49.7 ms: 1.02x faster                                              |
| mako                       | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                              |
| nqueens                    | 84.3 ms                                                               | 83.2 ms: 1.01x faster                                              |
| json_loads                 | 28.7 us                                                               | 28.4 us: 1.01x faster                                              |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 492 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 485 ms: 1.01x faster                                               |
| coroutines                 | 25.3 ms                                                               | 25.0 ms: 1.01x faster                                              |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.5 ms: 1.01x faster                                              |
| hexiom                     | 6.27 ms                                                               | 6.21 ms: 1.01x faster                                              |
| async_tree_none_tg         | 252 ms                                                                | 249 ms: 1.01x faster                                               |
| coverage                   | 88.0 ms                                                               | 87.2 ms: 1.01x faster                                              |
| raytrace                   | 273 ms                                                                | 271 ms: 1.01x faster                                               |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.23 ms: 1.01x faster                                              |
| comprehensions             | 16.4 us                                                               | 16.3 us: 1.01x faster                                              |
| json                       | 5.30 ms                                                               | 5.26 ms: 1.01x faster                                              |
| unpickle_pure_python       | 194 us                                                                | 192 us: 1.01x faster                                               |
| create_gc_cycles           | 2.60 ms                                                               | 2.58 ms: 1.01x faster                                              |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                             |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.55 ms: 1.01x faster                                              |
| python_startup_no_site     | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                              |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.4 ms: 1.01x faster                                              |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                              |
| async_tree_memoization     | 314 ms                                                                | 312 ms: 1.01x faster                                               |
| deepcopy_memo              | 29.8 us                                                               | 29.6 us: 1.01x faster                                              |
| asyncio_websockets         | 555 ms                                                                | 553 ms: 1.00x faster                                               |
| django_template            | 32.5 ms                                                               | 32.4 ms: 1.00x faster                                              |
| tomli_loads                | 1.83 sec                                                              | 1.82 sec: 1.00x faster                                             |
| sympy_expand               | 467 ms                                                                | 465 ms: 1.00x faster                                               |
| pidigits                   | 189 ms                                                                | 189 ms: 1.00x faster                                               |
| 2to3                       | 259 ms                                                                | 259 ms: 1.00x slower                                               |
| deltablue                  | 3.02 ms                                                               | 3.03 ms: 1.00x slower                                              |
| connected_components       | 455 ms                                                                | 458 ms: 1.01x slower                                               |
| chaos                      | 61.4 ms                                                               | 61.8 ms: 1.01x slower                                              |
| sympy_integrate            | 19.4 ms                                                               | 19.5 ms: 1.01x slower                                              |
| dulwich_log                | 59.0 ms                                                               | 59.5 ms: 1.01x slower                                              |
| regex_compile              | 127 ms                                                                | 128 ms: 1.01x slower                                               |
| bpe_tokeniser              | 4.34 sec                                                              | 4.37 sec: 1.01x slower                                             |
| deepcopy                   | 257 us                                                                | 260 us: 1.01x slower                                               |
| float                      | 65.6 ms                                                               | 66.2 ms: 1.01x slower                                              |
| html5lib                   | 61.7 ms                                                               | 62.3 ms: 1.01x slower                                              |
| sympy_sum                  | 150 ms                                                                | 152 ms: 1.01x slower                                               |
| nbody                      | 94.8 ms                                                               | 95.8 ms: 1.01x slower                                              |
| many_optionals             | 975 us                                                                | 986 us: 1.01x slower                                               |
| async_generators           | 426 ms                                                                | 431 ms: 1.01x slower                                               |
| meteor_contest             | 105 ms                                                                | 106 ms: 1.01x slower                                               |
| json_dumps                 | 11.0 ms                                                               | 11.2 ms: 1.02x slower                                              |
| pyflate                    | 410 ms                                                                | 417 ms: 1.02x slower                                               |
| deepcopy_reduce            | 2.67 us                                                               | 2.73 us: 1.02x slower                                              |
| async_tree_io_tg           | 622 ms                                                                | 637 ms: 1.02x slower                                               |
| scimark_sor                | 117 ms                                                                | 120 ms: 1.03x slower                                               |
| pycparser                  | 1.11 sec                                                              | 1.15 sec: 1.03x slower                                             |
| spectral_norm              | 89.8 ms                                                               | 92.6 ms: 1.03x slower                                              |
| richards_super             | 38.1 ms                                                               | 39.7 ms: 1.04x slower                                              |
| richards                   | 32.0 ms                                                               | 34.7 ms: 1.08x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (25): k_core, pprint_safe_repr, go, sphinx, sqlglot_v2_normalize, async_tree_io, xml_etree_parse, async_tree_none, djangocms, telco, xml_etree_generate, xml_etree_process, scimark_monte_carlo, shortest_path, docutils, scimark_lu, logging_silent, pylint, generators, sympy_str, pickle_pure_python, sqlite_synth, pathlib, subparsers, fannkuch

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 97.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x