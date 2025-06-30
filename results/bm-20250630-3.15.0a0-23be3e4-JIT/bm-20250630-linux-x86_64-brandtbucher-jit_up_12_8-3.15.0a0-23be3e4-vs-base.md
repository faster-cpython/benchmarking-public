# Results vs. base

- fork: brandtbucher
- ref: jit_up_12_8
- machine: linux-x86_64
- commit hash: 23be3e4
- commit date: 2025-06-30
- overall geometric mean: 1.001x faster
- HPT reliability: 91.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 261 ms: 1.01x slower                                               |
| docutils       | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                             |
| html5lib       | 61.7 ms                                                               | 62.3 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                 | 25.3 ms                                                               | 24.9 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 501 ms: 1.00x slower                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 495 ms: 1.01x slower                                               |
| async_generators           | 426 ms                                                                | 437 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 65.6 ms                                                               | 66.2 ms: 1.01x slower                                              |
| nbody          | 94.8 ms                                                               | 101 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                               | 23.0 ms: 1.06x faster                                              |
| regex_dna      | 220 ms                                                                | 208 ms: 1.06x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.45 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                                | 190 us: 1.02x faster                                               |
| xml_etree_parse      | 141 ms                                                                | 140 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.4 ms: 1.01x faster                                              |
| pickle_pure_python   | 320 us                                                                | 322 us: 1.00x slower                                               |
| json_dumps           | 11.0 ms                                                               | 11.2 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (4): json_loads, xml_etree_generate, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.96 ms: 1.00x faster                                              |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako           | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                              |
| genshi_text    | 22.4 ms                                                               | 22.0 ms: 1.02x faster                                              |
| genshi_xml     | 50.5 ms                                                               | 50.8 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8                   | 24.4 ms                                                               | 23.0 ms: 1.06x faster                                              |
| regex_dna                  | 220 ms                                                                | 208 ms: 1.06x faster                                               |
| gc_traversal               | 5.17 ms                                                               | 4.95 ms: 1.04x faster                                              |
| pprint_safe_repr           | 721 ms                                                                | 697 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.90 ms: 1.03x faster                                              |
| pprint_pformat             | 1.48 sec                                                              | 1.45 sec: 1.02x faster                                             |
| mako                       | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                              |
| logging_format             | 6.44 us                                                               | 6.32 us: 1.02x faster                                              |
| unpickle_pure_python       | 194 us                                                                | 190 us: 1.02x faster                                               |
| coroutines                 | 25.3 ms                                                               | 24.9 ms: 1.02x faster                                              |
| genshi_text                | 22.4 ms                                                               | 22.0 ms: 1.02x faster                                              |
| go                         | 117 ms                                                                | 115 ms: 1.02x faster                                               |
| raytrace                   | 273 ms                                                                | 269 ms: 1.02x faster                                               |
| nqueens                    | 84.3 ms                                                               | 83.0 ms: 1.02x faster                                              |
| typing_runtime_protocols   | 171 us                                                                | 168 us: 1.01x faster                                               |
| scimark_fft                | 315 ms                                                                | 311 ms: 1.01x faster                                               |
| pathlib                    | 17.1 ms                                                               | 16.9 ms: 1.01x faster                                              |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.01x faster                                               |
| telco                      | 7.74 ms                                                               | 7.68 ms: 1.01x faster                                              |
| xml_etree_parse            | 141 ms                                                                | 140 ms: 1.01x faster                                               |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.7 ms: 1.01x faster                                              |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                             |
| comprehensions             | 16.4 us                                                               | 16.3 us: 1.01x faster                                              |
| hexiom                     | 6.27 ms                                                               | 6.24 ms: 1.01x faster                                              |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.4 ms: 1.01x faster                                              |
| deepcopy_memo              | 29.8 us                                                               | 29.7 us: 1.00x faster                                              |
| python_startup_no_site     | 6.99 ms                                                               | 6.96 ms: 1.00x faster                                              |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| create_gc_cycles           | 2.60 ms                                                               | 2.60 ms: 1.00x faster                                              |
| shortest_path              | 492 ms                                                                | 491 ms: 1.00x faster                                               |
| deltablue                  | 3.02 ms                                                               | 3.03 ms: 1.00x slower                                              |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.25 ms: 1.00x slower                                              |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 501 ms: 1.00x slower                                               |
| pickle_pure_python         | 320 us                                                                | 322 us: 1.00x slower                                               |
| regex_effbot               | 3.43 ms                                                               | 3.45 ms: 1.00x slower                                              |
| docutils                   | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                             |
| genshi_xml                 | 50.5 ms                                                               | 50.8 ms: 1.01x slower                                              |
| 2to3                       | 259 ms                                                                | 261 ms: 1.01x slower                                               |
| sympy_str                  | 272 ms                                                                | 273 ms: 1.01x slower                                               |
| many_optionals             | 975 us                                                                | 981 us: 1.01x slower                                               |
| pyflate                    | 410 ms                                                                | 413 ms: 1.01x slower                                               |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.57 ms: 1.01x slower                                              |
| sympy_integrate            | 19.4 ms                                                               | 19.5 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 495 ms: 1.01x slower                                               |
| float                      | 65.6 ms                                                               | 66.2 ms: 1.01x slower                                              |
| html5lib                   | 61.7 ms                                                               | 62.3 ms: 1.01x slower                                              |
| bpe_tokeniser              | 4.34 sec                                                              | 4.38 sec: 1.01x slower                                             |
| deepcopy_reduce            | 2.67 us                                                               | 2.70 us: 1.01x slower                                              |
| scimark_sor                | 117 ms                                                                | 118 ms: 1.01x slower                                               |
| dulwich_log                | 59.0 ms                                                               | 59.7 ms: 1.01x slower                                              |
| spectral_norm              | 89.8 ms                                                               | 91.0 ms: 1.01x slower                                              |
| deepcopy                   | 257 us                                                                | 261 us: 1.01x slower                                               |
| meteor_contest             | 105 ms                                                                | 106 ms: 1.01x slower                                               |
| subparsers                 | 23.5 ms                                                               | 23.8 ms: 1.02x slower                                              |
| json_dumps                 | 11.0 ms                                                               | 11.2 ms: 1.02x slower                                              |
| logging_silent             | 103 ns                                                                | 105 ns: 1.02x slower                                               |
| async_generators           | 426 ms                                                                | 437 ms: 1.03x slower                                               |
| scimark_lu                 | 117 ms                                                                | 121 ms: 1.04x slower                                               |
| generators                 | 30.0 ms                                                               | 31.4 ms: 1.05x slower                                              |
| richards                   | 32.0 ms                                                               | 33.7 ms: 1.05x slower                                              |
| nbody                      | 94.8 ms                                                               | 101 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (32): k_core, logging_simple, scimark_monte_carlo, sqlite_synth, coverage, richards_super, chaos, djangocms, connected_components, pycparser, pidigits, json_loads, xml_etree_generate, asyncio_websockets, json, regex_compile, async_tree_none_tg, tomli_loads, sympy_expand, async_tree_memoization, django_template, async_tree_none, sympy_sum, sphinx, fannkuch, pylint, xml_etree_process, thrift, async_tree_io, crypto_pyaes, async_tree_memoization_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 91.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x