# Results vs. base

- fork: brandtbucher
- ref: jit_up_10_12
- machine: linux-x86_64
- commit hash: 0f33ad5
- commit date: 2025-06-29
- overall geometric mean: 1.000x slower
- HPT reliability: 92.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 261 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 25.3 ms                                                               | 24.6 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 486 ms: 1.01x faster                                                |
| asyncio_websockets         | 555 ms                                                                | 552 ms: 1.00x faster                                                |
| async_tree_memoization     | 314 ms                                                                | 317 ms: 1.01x slower                                                |
| async_generators           | 426 ms                                                                | 433 ms: 1.02x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 188 ms: 1.00x faster                                                |
| float          | 65.6 ms                                                               | 65.8 ms: 1.00x slower                                               |
| nbody          | 94.8 ms                                                               | 97.0 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                               | 23.0 ms: 1.06x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.32 ms: 1.03x faster                                               |
| regex_dna      | 220 ms                                                                | 215 ms: 1.02x faster                                                |
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.0 us: 1.03x faster                                               |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.1 ms: 1.01x faster                                               |
| unpickle_pure_python | 194 us                                                                | 192 us: 1.01x faster                                                |
| xml_etree_generate   | 80.0 ms                                                               | 79.5 ms: 1.01x faster                                               |
| pickle_pure_python   | 320 us                                                                | 322 us: 1.01x slower                                                |
| json_dumps           | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.93 ms: 1.01x faster                                               |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.7 ms: 1.03x faster                                               |
| mako            | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                               |
| django_template | 32.5 ms                                                               | 33.0 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8                   | 24.4 ms                                                               | 23.0 ms: 1.06x faster                                               |
| gc_traversal               | 5.17 ms                                                               | 4.93 ms: 1.05x faster                                               |
| crypto_pyaes               | 74.9 ms                                                               | 71.6 ms: 1.05x faster                                               |
| regex_effbot               | 3.43 ms                                                               | 3.32 ms: 1.03x faster                                               |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.89 ms: 1.03x faster                                               |
| genshi_text                | 22.4 ms                                                               | 21.7 ms: 1.03x faster                                               |
| coroutines                 | 25.3 ms                                                               | 24.6 ms: 1.03x faster                                               |
| json_loads                 | 28.7 us                                                               | 28.0 us: 1.03x faster                                               |
| regex_dna                  | 220 ms                                                                | 215 ms: 1.02x faster                                                |
| json                       | 5.30 ms                                                               | 5.19 ms: 1.02x faster                                               |
| telco                      | 7.74 ms                                                               | 7.58 ms: 1.02x faster                                               |
| thrift                     | 780 us                                                                | 766 us: 1.02x faster                                                |
| nqueens                    | 84.3 ms                                                               | 82.9 ms: 1.02x faster                                               |
| typing_runtime_protocols   | 171 us                                                                | 168 us: 1.01x faster                                                |
| logging_silent             | 103 ns                                                                | 102 ns: 1.01x faster                                                |
| logging_format             | 6.44 us                                                               | 6.36 us: 1.01x faster                                               |
| mako                       | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                               |
| logging_simple             | 5.73 us                                                               | 5.67 us: 1.01x faster                                               |
| pathlib                    | 17.1 ms                                                               | 16.9 ms: 1.01x faster                                               |
| create_gc_cycles           | 2.60 ms                                                               | 2.58 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 486 ms: 1.01x faster                                                |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.1 ms: 1.01x faster                                               |
| unpickle_pure_python       | 194 us                                                                | 192 us: 1.01x faster                                                |
| python_startup_no_site     | 6.99 ms                                                               | 6.93 ms: 1.01x faster                                               |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                               |
| xml_etree_generate         | 80.0 ms                                                               | 79.5 ms: 1.01x faster                                               |
| coverage                   | 88.0 ms                                                               | 87.6 ms: 1.00x faster                                               |
| asyncio_websockets         | 555 ms                                                                | 552 ms: 1.00x faster                                                |
| pidigits                   | 189 ms                                                                | 188 ms: 1.00x faster                                                |
| regex_compile              | 127 ms                                                                | 127 ms: 1.00x slower                                                |
| float                      | 65.6 ms                                                               | 65.8 ms: 1.00x slower                                               |
| sympy_str                  | 272 ms                                                                | 273 ms: 1.00x slower                                                |
| subparsers                 | 23.5 ms                                                               | 23.6 ms: 1.01x slower                                               |
| meteor_contest             | 105 ms                                                                | 105 ms: 1.01x slower                                                |
| sympy_expand               | 467 ms                                                                | 470 ms: 1.01x slower                                                |
| pickle_pure_python         | 320 us                                                                | 322 us: 1.01x slower                                                |
| many_optionals             | 975 us                                                                | 982 us: 1.01x slower                                                |
| sympy_sum                  | 150 ms                                                                | 151 ms: 1.01x slower                                                |
| 2to3                       | 259 ms                                                                | 261 ms: 1.01x slower                                                |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.58 ms: 1.01x slower                                               |
| raytrace                   | 273 ms                                                                | 276 ms: 1.01x slower                                                |
| async_tree_memoization     | 314 ms                                                                | 317 ms: 1.01x slower                                                |
| sympy_integrate            | 19.4 ms                                                               | 19.6 ms: 1.01x slower                                               |
| dulwich_log                | 59.0 ms                                                               | 59.6 ms: 1.01x slower                                               |
| pyflate                    | 410 ms                                                                | 414 ms: 1.01x slower                                                |
| json_dumps                 | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                               |
| django_template            | 32.5 ms                                                               | 33.0 ms: 1.01x slower                                               |
| deltablue                  | 3.02 ms                                                               | 3.06 ms: 1.01x slower                                               |
| comprehensions             | 16.4 us                                                               | 16.7 us: 1.02x slower                                               |
| async_generators           | 426 ms                                                                | 433 ms: 1.02x slower                                                |
| scimark_lu                 | 117 ms                                                                | 119 ms: 1.02x slower                                                |
| deepcopy                   | 257 us                                                                | 262 us: 1.02x slower                                                |
| scimark_sor                | 117 ms                                                                | 119 ms: 1.02x slower                                                |
| nbody                      | 94.8 ms                                                               | 97.0 ms: 1.02x slower                                               |
| spectral_norm              | 89.8 ms                                                               | 92.0 ms: 1.02x slower                                               |
| deepcopy_reduce            | 2.67 us                                                               | 2.74 us: 1.03x slower                                               |
| pycparser                  | 1.11 sec                                                              | 1.15 sec: 1.03x slower                                              |
| richards_super             | 38.1 ms                                                               | 39.4 ms: 1.03x slower                                               |
| pprint_safe_repr           | 721 ms                                                                | 754 ms: 1.05x slower                                                |
| richards                   | 32.0 ms                                                               | 34.3 ms: 1.07x slower                                               |
| connected_components       | 455 ms                                                                | 493 ms: 1.08x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (32): k_core, async_tree_memoization_tg, genshi_xml, djangocms, xml_etree_parse, sphinx, shortest_path, mdp, xml_etree_process, sqlite_synth, async_tree_cpu_io_mixed, generators, async_tree_none_tg, docutils, fannkuch, hexiom, deepcopy_memo, bpe_tokeniser, scimark_fft, go, async_tree_io, html5lib, sqlglot_v2_parse, tomli_loads, sqlglot_v2_normalize, sqlglot_v2_optimize, chaos, pylint, scimark_monte_carlo, async_tree_none, async_tree_io_tg, pprint_pformat

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 92.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x