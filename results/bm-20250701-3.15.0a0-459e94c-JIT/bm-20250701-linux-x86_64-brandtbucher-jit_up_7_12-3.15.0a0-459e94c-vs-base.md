# Results vs. base

- fork: brandtbucher
- ref: jit_up_7_12
- machine: linux-x86_64
- commit hash: 459e94c
- commit date: 2025-07-01
- overall geometric mean: 1.003x faster
- HPT reliability: 94.42%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 262 ms: 1.01x slower                                               |
| docutils       | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization     | 314 ms                                                                | 316 ms: 1.01x slower                                               |
| coroutines                 | 25.3 ms                                                               | 25.6 ms: 1.01x slower                                              |
| async_generators           | 426 ms                                                                | 431 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 507 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 500 ms: 1.02x slower                                               |
| async_tree_none            | 262 ms                                                                | 268 ms: 1.03x slower                                               |
| async_tree_io_tg           | 622 ms                                                                | 639 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 94.8 ms                                                               | 92.3 ms: 1.03x faster                                              |
| float          | 65.6 ms                                                               | 66.0 ms: 1.01x slower                                              |
| pidigits       | 189 ms                                                                | 193 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                | 216 ms: 1.02x faster                                               |
| regex_v8       | 24.4 ms                                                               | 24.0 ms: 1.02x faster                                              |
| regex_effbot   | 3.43 ms                                                               | 3.41 ms: 1.01x faster                                              |
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads          | 28.7 us                                                               | 28.2 us: 1.02x faster                                              |
| xml_etree_parse     | 141 ms                                                                | 140 ms: 1.01x faster                                               |
| xml_etree_iterparse | 99.0 ms                                                               | 98.3 ms: 1.01x faster                                              |
| xml_etree_generate  | 80.0 ms                                                               | 79.6 ms: 1.01x faster                                              |
| json_dumps          | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                              |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (4): unpickle_pure_python, tomli_loads, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.96 ms: 1.00x faster                                              |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.6 ms: 1.04x faster                                              |
| mako            | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                              |
| django_template | 32.5 ms                                                               | 33.2 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| richards_super             | 38.1 ms                                                               | 35.9 ms: 1.06x faster                                              |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.80 ms: 1.05x faster                                              |
| gc_traversal               | 5.17 ms                                                               | 4.92 ms: 1.05x faster                                              |
| logging_format             | 6.44 us                                                               | 6.17 us: 1.04x faster                                              |
| genshi_text                | 22.4 ms                                                               | 21.6 ms: 1.04x faster                                              |
| richards                   | 32.0 ms                                                               | 31.0 ms: 1.03x faster                                              |
| nbody                      | 94.8 ms                                                               | 92.3 ms: 1.03x faster                                              |
| hexiom                     | 6.27 ms                                                               | 6.13 ms: 1.02x faster                                              |
| logging_simple             | 5.73 us                                                               | 5.60 us: 1.02x faster                                              |
| pprint_pformat             | 1.48 sec                                                              | 1.45 sec: 1.02x faster                                             |
| nqueens                    | 84.3 ms                                                               | 82.5 ms: 1.02x faster                                              |
| regex_dna                  | 220 ms                                                                | 216 ms: 1.02x faster                                               |
| json_loads                 | 28.7 us                                                               | 28.2 us: 1.02x faster                                              |
| crypto_pyaes               | 74.9 ms                                                               | 73.7 ms: 1.02x faster                                              |
| regex_v8                   | 24.4 ms                                                               | 24.0 ms: 1.02x faster                                              |
| json                       | 5.30 ms                                                               | 5.22 ms: 1.02x faster                                              |
| pyflate                    | 410 ms                                                                | 404 ms: 1.02x faster                                               |
| mako                       | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                              |
| scimark_fft                | 315 ms                                                                | 311 ms: 1.01x faster                                               |
| typing_runtime_protocols   | 171 us                                                                | 169 us: 1.01x faster                                               |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                             |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.01x faster                                               |
| thrift                     | 780 us                                                                | 773 us: 1.01x faster                                               |
| xml_etree_parse            | 141 ms                                                                | 140 ms: 1.01x faster                                               |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.24 ms: 1.01x faster                                              |
| fannkuch                   | 395 ms                                                                | 392 ms: 1.01x faster                                               |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.3 ms: 1.01x faster                                              |
| xml_etree_generate         | 80.0 ms                                                               | 79.6 ms: 1.01x faster                                              |
| regex_effbot               | 3.43 ms                                                               | 3.41 ms: 1.01x faster                                              |
| sympy_expand               | 467 ms                                                                | 465 ms: 1.00x faster                                               |
| python_startup_no_site     | 6.99 ms                                                               | 6.96 ms: 1.00x faster                                              |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                              |
| regex_compile              | 127 ms                                                                | 127 ms: 1.00x slower                                               |
| deltablue                  | 3.02 ms                                                               | 3.03 ms: 1.00x slower                                              |
| connected_components       | 455 ms                                                                | 458 ms: 1.01x slower                                               |
| float                      | 65.6 ms                                                               | 66.0 ms: 1.01x slower                                              |
| docutils                   | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                             |
| async_tree_memoization     | 314 ms                                                                | 316 ms: 1.01x slower                                               |
| logging_silent             | 103 ns                                                                | 104 ns: 1.01x slower                                               |
| json_dumps                 | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                              |
| dulwich_log                | 59.0 ms                                                               | 59.6 ms: 1.01x slower                                              |
| coroutines                 | 25.3 ms                                                               | 25.6 ms: 1.01x slower                                              |
| async_generators           | 426 ms                                                                | 431 ms: 1.01x slower                                               |
| pathlib                    | 17.1 ms                                                               | 17.3 ms: 1.01x slower                                              |
| scimark_sor                | 117 ms                                                                | 118 ms: 1.01x slower                                               |
| sympy_sum                  | 150 ms                                                                | 152 ms: 1.01x slower                                               |
| subparsers                 | 23.5 ms                                                               | 23.8 ms: 1.01x slower                                              |
| 2to3                       | 259 ms                                                                | 262 ms: 1.01x slower                                               |
| sympy_integrate            | 19.4 ms                                                               | 19.6 ms: 1.01x slower                                              |
| many_optionals             | 975 us                                                                | 988 us: 1.01x slower                                               |
| scimark_lu                 | 117 ms                                                                | 119 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 507 ms: 1.02x slower                                               |
| spectral_norm              | 89.8 ms                                                               | 91.5 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 500 ms: 1.02x slower                                               |
| pidigits                   | 189 ms                                                                | 193 ms: 1.02x slower                                               |
| django_template            | 32.5 ms                                                               | 33.2 ms: 1.02x slower                                              |
| async_tree_none            | 262 ms                                                                | 268 ms: 1.03x slower                                               |
| async_tree_io_tg           | 622 ms                                                                | 639 ms: 1.03x slower                                               |
| pycparser                  | 1.11 sec                                                              | 1.15 sec: 1.03x slower                                             |
| deepcopy_reduce            | 2.67 us                                                               | 2.79 us: 1.04x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (33): k_core, genshi_xml, sqlglot_v2_optimize, unpickle_pure_python, tomli_loads, asyncio_websockets, telco, raytrace, go, sqlglot_v2_transpile, scimark_monte_carlo, meteor_contest, html5lib, coverage, bpe_tokeniser, comprehensions, generators, shortest_path, sqlite_synth, create_gc_cycles, sphinx, deepcopy_memo, sympy_str, chaos, xml_etree_process, async_tree_none_tg, async_tree_memoization_tg, deepcopy, pickle_pure_python, async_tree_io, djangocms, pprint_safe_repr, pylint

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 94.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x