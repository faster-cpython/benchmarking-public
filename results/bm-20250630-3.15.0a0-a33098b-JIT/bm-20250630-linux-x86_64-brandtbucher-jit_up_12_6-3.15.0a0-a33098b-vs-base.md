# Results vs. base

- fork: brandtbucher
- ref: jit_up_12_6
- machine: linux-x86_64
- commit hash: a33098b
- commit date: 2025-06-30
- overall geometric mean: 1.007x faster
- HPT reliability: 91.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 258 ms: 1.00x faster                                               |
| html5lib       | 61.7 ms                                                               | 62.7 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 315 ms                                                                | 311 ms: 1.02x faster                                               |
| async_tree_none_tg         | 252 ms                                                                | 248 ms: 1.01x faster                                               |
| coroutines                 | 25.3 ms                                                               | 25.0 ms: 1.01x faster                                              |
| async_generators           | 426 ms                                                                | 428 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 496 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 505 ms: 1.01x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (5): async_tree_none, async_tree_io, async_tree_memoization, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 65.6 ms                                                               | 66.1 ms: 1.01x slower                                              |
| pidigits       | 189 ms                                                                | 193 ms: 1.02x slower                                               |
| nbody          | 94.8 ms                                                               | 98.2 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                               | 22.1 ms: 1.10x faster                                              |
| regex_dna      | 220 ms                                                                | 206 ms: 1.07x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.31 ms: 1.04x faster                                              |
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.0 us: 1.02x faster                                              |
| unpickle_pure_python | 194 us                                                                | 191 us: 1.01x faster                                               |
| tomli_loads          | 1.83 sec                                                              | 1.81 sec: 1.01x faster                                             |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.6 ms: 1.00x faster                                              |
| xml_etree_generate   | 80.0 ms                                                               | 80.5 ms: 1.01x slower                                              |
| pickle_pure_python   | 320 us                                                                | 322 us: 1.01x slower                                               |
| json_dumps           | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                              |
| xml_etree_process    | 55.5 ms                                                               | 56.4 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.93 ms: 1.01x faster                                              |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako           | 10.6 ms                                                               | 10.4 ms: 1.03x faster                                              |
| genshi_text    | 22.4 ms                                                               | 21.8 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| richards_super             | 38.1 ms                                                               | 33.8 ms: 1.13x faster                                              |
| regex_v8                   | 24.4 ms                                                               | 22.1 ms: 1.10x faster                                              |
| gc_traversal               | 5.17 ms                                                               | 4.75 ms: 1.09x faster                                              |
| richards                   | 32.0 ms                                                               | 29.5 ms: 1.08x faster                                              |
| regex_dna                  | 220 ms                                                                | 206 ms: 1.07x faster                                               |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.77 ms: 1.06x faster                                              |
| regex_effbot               | 3.43 ms                                                               | 3.31 ms: 1.04x faster                                              |
| logging_format             | 6.44 us                                                               | 6.25 us: 1.03x faster                                              |
| mako                       | 10.6 ms                                                               | 10.4 ms: 1.03x faster                                              |
| genshi_text                | 22.4 ms                                                               | 21.8 ms: 1.03x faster                                              |
| json_loads                 | 28.7 us                                                               | 28.0 us: 1.02x faster                                              |
| pprint_pformat             | 1.48 sec                                                              | 1.45 sec: 1.02x faster                                             |
| go                         | 117 ms                                                                | 114 ms: 1.02x faster                                               |
| hexiom                     | 6.27 ms                                                               | 6.13 ms: 1.02x faster                                              |
| nqueens                    | 84.3 ms                                                               | 82.4 ms: 1.02x faster                                              |
| logging_simple             | 5.73 us                                                               | 5.62 us: 1.02x faster                                              |
| async_tree_memoization_tg  | 315 ms                                                                | 311 ms: 1.02x faster                                               |
| async_tree_none_tg         | 252 ms                                                                | 248 ms: 1.01x faster                                               |
| json                       | 5.30 ms                                                               | 5.24 ms: 1.01x faster                                              |
| coroutines                 | 25.3 ms                                                               | 25.0 ms: 1.01x faster                                              |
| create_gc_cycles           | 2.60 ms                                                               | 2.57 ms: 1.01x faster                                              |
| unpickle_pure_python       | 194 us                                                                | 191 us: 1.01x faster                                               |
| tomli_loads                | 1.83 sec                                                              | 1.81 sec: 1.01x faster                                             |
| coverage                   | 88.0 ms                                                               | 87.1 ms: 1.01x faster                                              |
| telco                      | 7.74 ms                                                               | 7.67 ms: 1.01x faster                                              |
| raytrace                   | 273 ms                                                                | 271 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.99 ms                                                               | 6.93 ms: 1.01x faster                                              |
| logging_silent             | 103 ns                                                                | 102 ns: 1.01x faster                                               |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                              |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.24 ms: 1.01x faster                                              |
| comprehensions             | 16.4 us                                                               | 16.3 us: 1.01x faster                                              |
| deepcopy_memo              | 29.8 us                                                               | 29.6 us: 1.01x faster                                              |
| scimark_fft                | 315 ms                                                                | 313 ms: 1.01x faster                                               |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.6 ms: 1.00x faster                                              |
| sympy_sum                  | 150 ms                                                                | 150 ms: 1.00x faster                                               |
| regex_compile              | 127 ms                                                                | 127 ms: 1.00x faster                                               |
| 2to3                       | 259 ms                                                                | 258 ms: 1.00x faster                                               |
| sympy_expand               | 467 ms                                                                | 466 ms: 1.00x faster                                               |
| bpe_tokeniser              | 4.34 sec                                                              | 4.36 sec: 1.00x slower                                             |
| async_generators           | 426 ms                                                                | 428 ms: 1.01x slower                                               |
| xml_etree_generate         | 80.0 ms                                                               | 80.5 ms: 1.01x slower                                              |
| pickle_pure_python         | 320 us                                                                | 322 us: 1.01x slower                                               |
| float                      | 65.6 ms                                                               | 66.1 ms: 1.01x slower                                              |
| many_optionals             | 975 us                                                                | 983 us: 1.01x slower                                               |
| dulwich_log                | 59.0 ms                                                               | 59.6 ms: 1.01x slower                                              |
| json_dumps                 | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                              |
| deltablue                  | 3.02 ms                                                               | 3.06 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 496 ms: 1.01x slower                                               |
| subparsers                 | 23.5 ms                                                               | 23.8 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 505 ms: 1.01x slower                                               |
| pyflate                    | 410 ms                                                                | 415 ms: 1.01x slower                                               |
| deepcopy                   | 257 us                                                                | 261 us: 1.01x slower                                               |
| xml_etree_process          | 55.5 ms                                                               | 56.4 ms: 1.02x slower                                              |
| html5lib                   | 61.7 ms                                                               | 62.7 ms: 1.02x slower                                              |
| scimark_lu                 | 117 ms                                                                | 119 ms: 1.02x slower                                               |
| meteor_contest             | 105 ms                                                                | 107 ms: 1.02x slower                                               |
| pidigits                   | 189 ms                                                                | 193 ms: 1.02x slower                                               |
| fannkuch                   | 395 ms                                                                | 403 ms: 1.02x slower                                               |
| spectral_norm              | 89.8 ms                                                               | 91.7 ms: 1.02x slower                                              |
| scimark_sor                | 117 ms                                                                | 119 ms: 1.02x slower                                               |
| nbody                      | 94.8 ms                                                               | 98.2 ms: 1.04x slower                                              |
| deepcopy_reduce            | 2.67 us                                                               | 2.81 us: 1.05x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (31): pprint_safe_repr, k_core, djangocms, typing_runtime_protocols, pathlib, sqlglot_v2_normalize, genshi_xml, sqlglot_v2_optimize, connected_components, async_tree_none, thrift, async_tree_io, django_template, mdp, docutils, sphinx, async_tree_memoization, generators, xml_etree_parse, sqlite_synth, asyncio_websockets, pylint, sympy_str, pycparser, chaos, sympy_integrate, shortest_path, sqlglot_v2_transpile, crypto_pyaes, scimark_monte_carlo, async_tree_io_tg

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 91.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x