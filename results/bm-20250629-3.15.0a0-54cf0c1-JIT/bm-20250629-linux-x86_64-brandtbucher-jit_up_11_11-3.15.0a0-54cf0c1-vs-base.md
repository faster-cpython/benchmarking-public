# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_11
- machine: linux-x86_64
- commit hash: 54cf0c1
- commit date: 2025-06-29
- overall geometric mean: 1.001x slower
- HPT reliability: 56.60%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 258 ms: 1.00x faster                                                |
| html5lib       | 61.7 ms                                                               | 62.2 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|---------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg | 315 ms                                                                | 310 ms: 1.02x faster                                                |
| async_tree_none_tg        | 252 ms                                                                | 248 ms: 1.01x faster                                                |
| async_generators          | 426 ms                                                                | 433 ms: 1.02x slower                                                |
| coroutines                | 25.3 ms                                                               | 25.8 ms: 1.02x slower                                               |
| async_tree_io_tg          | 622 ms                                                                | 637 ms: 1.02x slower                                                |
| Geometric mean            | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 189 ms: 1.00x faster                                                |
| float          | 65.6 ms                                                               | 65.9 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                | 207 ms: 1.06x faster                                                |
| regex_v8       | 24.4 ms                                                               | 23.0 ms: 1.06x faster                                               |
| regex_compile  | 127 ms                                                                | 126 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.0 us: 1.03x faster                                               |
| unpickle_pure_python | 194 us                                                                | 192 us: 1.01x faster                                                |
| json_dumps           | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                               |
| xml_etree_generate   | 80.0 ms                                                               | 81.1 ms: 1.01x slower                                               |
| xml_etree_process    | 55.5 ms                                                               | 56.4 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_iterparse, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                               |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.9 ms: 1.02x faster                                               |
| genshi_xml      | 50.5 ms                                                               | 50.2 ms: 1.01x faster                                               |
| django_template | 32.5 ms                                                               | 32.7 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|---------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| crypto_pyaes              | 74.9 ms                                                               | 70.7 ms: 1.06x faster                                               |
| regex_dna                 | 220 ms                                                                | 207 ms: 1.06x faster                                                |
| regex_v8                  | 24.4 ms                                                               | 23.0 ms: 1.06x faster                                               |
| gc_traversal              | 5.17 ms                                                               | 4.91 ms: 1.05x faster                                               |
| scimark_sparse_mat_mult   | 5.05 ms                                                               | 4.80 ms: 1.05x faster                                               |
| logging_silent            | 103 ns                                                                | 99.2 ns: 1.04x faster                                               |
| hexiom                    | 6.27 ms                                                               | 6.11 ms: 1.03x faster                                               |
| json_loads                | 28.7 us                                                               | 28.0 us: 1.03x faster                                               |
| logging_format            | 6.44 us                                                               | 6.30 us: 1.02x faster                                               |
| genshi_text               | 22.4 ms                                                               | 21.9 ms: 1.02x faster                                               |
| go                        | 117 ms                                                                | 114 ms: 1.02x faster                                                |
| nqueens                   | 84.3 ms                                                               | 82.5 ms: 1.02x faster                                               |
| typing_runtime_protocols  | 171 us                                                                | 167 us: 1.02x faster                                                |
| scimark_fft               | 315 ms                                                                | 309 ms: 1.02x faster                                                |
| pprint_pformat            | 1.48 sec                                                              | 1.46 sec: 1.02x faster                                              |
| pprint_safe_repr          | 721 ms                                                                | 709 ms: 1.02x faster                                                |
| async_tree_memoization_tg | 315 ms                                                                | 310 ms: 1.02x faster                                                |
| json                      | 5.30 ms                                                               | 5.22 ms: 1.02x faster                                               |
| logging_simple            | 5.73 us                                                               | 5.65 us: 1.02x faster                                               |
| async_tree_none_tg        | 252 ms                                                                | 248 ms: 1.01x faster                                                |
| raytrace                  | 273 ms                                                                | 270 ms: 1.01x faster                                                |
| sqlglot_v2_normalize      | 107 ms                                                                | 106 ms: 1.01x faster                                                |
| mdp                       | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                              |
| comprehensions            | 16.4 us                                                               | 16.3 us: 1.01x faster                                               |
| scimark_monte_carlo       | 65.4 ms                                                               | 64.8 ms: 1.01x faster                                               |
| unpickle_pure_python      | 194 us                                                                | 192 us: 1.01x faster                                                |
| python_startup_no_site    | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                               |
| genshi_xml                | 50.5 ms                                                               | 50.2 ms: 1.01x faster                                               |
| python_startup            | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                               |
| chaos                     | 61.4 ms                                                               | 61.1 ms: 1.01x faster                                               |
| regex_compile             | 127 ms                                                                | 126 ms: 1.00x faster                                                |
| 2to3                      | 259 ms                                                                | 258 ms: 1.00x faster                                                |
| create_gc_cycles          | 2.60 ms                                                               | 2.60 ms: 1.00x faster                                               |
| pidigits                  | 189 ms                                                                | 189 ms: 1.00x faster                                                |
| sympy_integrate           | 19.4 ms                                                               | 19.4 ms: 1.00x slower                                               |
| sympy_str                 | 272 ms                                                                | 273 ms: 1.00x slower                                                |
| sqlglot_v2_transpile      | 1.56 ms                                                               | 1.57 ms: 1.00x slower                                               |
| float                     | 65.6 ms                                                               | 65.9 ms: 1.01x slower                                               |
| sqlglot_v2_parse          | 1.24 ms                                                               | 1.25 ms: 1.01x slower                                               |
| django_template           | 32.5 ms                                                               | 32.7 ms: 1.01x slower                                               |
| html5lib                  | 61.7 ms                                                               | 62.2 ms: 1.01x slower                                               |
| connected_components      | 455 ms                                                                | 459 ms: 1.01x slower                                                |
| generators                | 30.0 ms                                                               | 30.3 ms: 1.01x slower                                               |
| deltablue                 | 3.02 ms                                                               | 3.05 ms: 1.01x slower                                               |
| many_optionals            | 975 us                                                                | 986 us: 1.01x slower                                                |
| shortest_path             | 492 ms                                                                | 498 ms: 1.01x slower                                                |
| deepcopy                  | 257 us                                                                | 260 us: 1.01x slower                                                |
| json_dumps                | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                               |
| subparsers                | 23.5 ms                                                               | 23.8 ms: 1.01x slower                                               |
| xml_etree_generate        | 80.0 ms                                                               | 81.1 ms: 1.01x slower                                               |
| dulwich_log               | 59.0 ms                                                               | 59.9 ms: 1.01x slower                                               |
| scimark_lu                | 117 ms                                                                | 118 ms: 1.01x slower                                                |
| pyflate                   | 410 ms                                                                | 416 ms: 1.02x slower                                                |
| spectral_norm             | 89.8 ms                                                               | 91.2 ms: 1.02x slower                                               |
| xml_etree_process         | 55.5 ms                                                               | 56.4 ms: 1.02x slower                                               |
| telco                     | 7.74 ms                                                               | 7.87 ms: 1.02x slower                                               |
| async_generators          | 426 ms                                                                | 433 ms: 1.02x slower                                                |
| coroutines                | 25.3 ms                                                               | 25.8 ms: 1.02x slower                                               |
| async_tree_io_tg          | 622 ms                                                                | 637 ms: 1.02x slower                                                |
| meteor_contest            | 105 ms                                                                | 108 ms: 1.03x slower                                                |
| deepcopy_reduce           | 2.67 us                                                               | 2.78 us: 1.04x slower                                               |
| richards_super            | 38.1 ms                                                               | 45.1 ms: 1.18x slower                                               |
| richards                  | 32.0 ms                                                               | 39.2 ms: 1.22x slower                                               |
| Geometric mean            | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (30): djangocms, k_core, sqlglot_v2_optimize, asyncio_websockets, deepcopy_memo, coverage, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, pathlib, async_tree_memoization, pickle_pure_python, pycparser, xml_etree_iterparse, sphinx, sqlite_synth, pylint, fannkuch, bpe_tokeniser, tomli_loads, sympy_expand, docutils, regex_effbot, xml_etree_parse, sympy_sum, scimark_sor, thrift, nbody, mako

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 56.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x