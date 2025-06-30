# Results vs. base

- fork: brandtbucher
- ref: jit_up_12_9
- machine: linux-x86_64
- commit hash: ad5f858
- commit date: 2025-06-29
- overall geometric mean: 1.002x faster
- HPT reliability: 84.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 260 ms: 1.00x slower                                               |
| docutils       | 2.64 sec                                                              | 2.65 sec: 1.00x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                 | 25.3 ms                                                               | 25.0 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 494 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 487 ms: 1.01x faster                                               |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_none, async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, async_generators, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 65.6 ms                                                               | 66.3 ms: 1.01x slower                                              |
| nbody          | 94.8 ms                                                               | 96.3 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                               | 23.9 ms: 1.02x faster                                              |
| regex_dna      | 220 ms                                                                | 216 ms: 1.02x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.42 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.1 us: 1.02x faster                                              |
| unpickle_pure_python | 194 us                                                                | 190 us: 1.02x faster                                               |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.8 ms: 1.00x faster                                              |
| json_dumps           | 11.0 ms                                                               | 11.0 ms: 1.01x slower                                              |
| tomli_loads          | 1.83 sec                                                              | 1.85 sec: 1.01x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.90 ms: 1.01x faster                                              |
| python_startup         | 12.3 ms                                                               | 12.1 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 22.4 ms                                                               | 21.9 ms: 1.02x faster                                              |
| mako           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                               | 4.88 ms: 1.06x faster                                              |
| richards_super             | 38.1 ms                                                               | 36.3 ms: 1.05x faster                                              |
| pprint_pformat             | 1.48 sec                                                              | 1.44 sec: 1.03x faster                                             |
| json_loads                 | 28.7 us                                                               | 28.1 us: 1.02x faster                                              |
| genshi_text                | 22.4 ms                                                               | 21.9 ms: 1.02x faster                                              |
| regex_v8                   | 24.4 ms                                                               | 23.9 ms: 1.02x faster                                              |
| go                         | 117 ms                                                                | 114 ms: 1.02x faster                                               |
| regex_dna                  | 220 ms                                                                | 216 ms: 1.02x faster                                               |
| pprint_safe_repr           | 721 ms                                                                | 708 ms: 1.02x faster                                               |
| logging_simple             | 5.73 us                                                               | 5.64 us: 1.02x faster                                              |
| nqueens                    | 84.3 ms                                                               | 82.9 ms: 1.02x faster                                              |
| unpickle_pure_python       | 194 us                                                                | 190 us: 1.02x faster                                               |
| coroutines                 | 25.3 ms                                                               | 25.0 ms: 1.01x faster                                              |
| logging_format             | 6.44 us                                                               | 6.35 us: 1.01x faster                                              |
| typing_runtime_protocols   | 171 us                                                                | 168 us: 1.01x faster                                               |
| json                       | 5.30 ms                                                               | 5.24 ms: 1.01x faster                                              |
| python_startup_no_site     | 6.99 ms                                                               | 6.90 ms: 1.01x faster                                              |
| python_startup             | 12.3 ms                                                               | 12.1 ms: 1.01x faster                                              |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.99 ms: 1.01x faster                                              |
| mako                       | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                              |
| create_gc_cycles           | 2.60 ms                                                               | 2.58 ms: 1.01x faster                                              |
| sympy_sum                  | 150 ms                                                                | 149 ms: 1.01x faster                                               |
| hexiom                     | 6.27 ms                                                               | 6.21 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 494 ms: 1.01x faster                                               |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.24 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 487 ms: 1.01x faster                                               |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                             |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.8 ms: 1.01x faster                                              |
| raytrace                   | 273 ms                                                                | 272 ms: 1.01x faster                                               |
| sqlglot_v2_normalize       | 107 ms                                                                | 107 ms: 1.01x faster                                               |
| regex_effbot               | 3.43 ms                                                               | 3.42 ms: 1.00x faster                                              |
| shortest_path              | 492 ms                                                                | 491 ms: 1.00x faster                                               |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.8 ms: 1.00x faster                                              |
| docutils                   | 2.64 sec                                                              | 2.65 sec: 1.00x slower                                             |
| sympy_expand               | 467 ms                                                                | 469 ms: 1.00x slower                                               |
| 2to3                       | 259 ms                                                                | 260 ms: 1.00x slower                                               |
| comprehensions             | 16.4 us                                                               | 16.5 us: 1.00x slower                                              |
| deltablue                  | 3.02 ms                                                               | 3.03 ms: 1.00x slower                                              |
| json_dumps                 | 11.0 ms                                                               | 11.0 ms: 1.01x slower                                              |
| scimark_sor                | 117 ms                                                                | 117 ms: 1.01x slower                                               |
| dulwich_log                | 59.0 ms                                                               | 59.4 ms: 1.01x slower                                              |
| deepcopy                   | 257 us                                                                | 259 us: 1.01x slower                                               |
| connected_components       | 455 ms                                                                | 459 ms: 1.01x slower                                               |
| chaos                      | 61.4 ms                                                               | 61.9 ms: 1.01x slower                                              |
| bpe_tokeniser              | 4.34 sec                                                              | 4.38 sec: 1.01x slower                                             |
| deepcopy_reduce            | 2.67 us                                                               | 2.70 us: 1.01x slower                                              |
| tomli_loads                | 1.83 sec                                                              | 1.85 sec: 1.01x slower                                             |
| float                      | 65.6 ms                                                               | 66.3 ms: 1.01x slower                                              |
| scimark_fft                | 315 ms                                                                | 319 ms: 1.01x slower                                               |
| meteor_contest             | 105 ms                                                                | 106 ms: 1.01x slower                                               |
| nbody                      | 94.8 ms                                                               | 96.3 ms: 1.02x slower                                              |
| scimark_lu                 | 117 ms                                                                | 119 ms: 1.02x slower                                               |
| logging_silent             | 103 ns                                                                | 105 ns: 1.02x slower                                               |
| pyflate                    | 410 ms                                                                | 421 ms: 1.03x slower                                               |
| pycparser                  | 1.11 sec                                                              | 1.15 sec: 1.03x slower                                             |
| spectral_norm              | 89.8 ms                                                               | 93.1 ms: 1.04x slower                                              |
| generators                 | 30.0 ms                                                               | 31.7 ms: 1.06x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (36): async_tree_io_tg, djangocms, k_core, async_tree_io, pylint, genshi_xml, sqlite_synth, async_tree_none, async_tree_none_tg, sphinx, xml_etree_process, asyncio_websockets, richards, coverage, regex_compile, xml_etree_parse, sqlglot_v2_transpile, pickle_pure_python, async_tree_memoization_tg, xml_etree_generate, sympy_integrate, pathlib, async_generators, pidigits, django_template, fannkuch, sympy_str, many_optionals, thrift, subparsers, scimark_monte_carlo, telco, deepcopy_memo, html5lib, crypto_pyaes, async_tree_memoization

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 84.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x