# Results vs. base

- fork: brandtbucher
- ref: jit_up_12_11
- machine: linux-x86_64
- commit hash: af1f59b
- commit date: 2025-06-29
- overall geometric mean: 1.006x faster
- HPT reliability: 96.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.64 sec: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 25.3 ms                                                               | 24.7 ms: 1.02x faster                                               |
| async_tree_none_tg         | 252 ms                                                                | 248 ms: 1.02x faster                                                |
| async_tree_memoization     | 314 ms                                                                | 311 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 502 ms: 1.01x slower                                                |
| async_generators           | 426 ms                                                                | 430 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 496 ms: 1.01x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_none, async_tree_io, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 193 ms: 1.02x slower                                                |
| nbody          | 94.8 ms                                                               | 100 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                | 215 ms: 1.02x faster                                                |
| regex_v8       | 24.4 ms                                                               | 24.0 ms: 1.02x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.41 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                                | 189 us: 1.03x faster                                                |
| json_loads           | 28.7 us                                                               | 28.1 us: 1.02x faster                                               |
| tomli_loads          | 1.83 sec                                                              | 1.81 sec: 1.01x faster                                              |
| xml_etree_generate   | 80.0 ms                                                               | 79.7 ms: 1.00x faster                                               |
| json_dumps           | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.95 ms: 1.01x faster                                               |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.5 ms: 1.04x faster                                               |
| genshi_xml      | 50.5 ms                                                               | 49.7 ms: 1.02x faster                                               |
| mako            | 10.6 ms                                                               | 10.6 ms: 1.01x faster                                               |
| django_template | 32.5 ms                                                               | 32.9 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_11-3.15.0a0-af1f59b |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                               | 4.76 ms: 1.09x faster                                               |
| richards_super             | 38.1 ms                                                               | 35.7 ms: 1.07x faster                                               |
| richards                   | 32.0 ms                                                               | 30.3 ms: 1.06x faster                                               |
| genshi_text                | 22.4 ms                                                               | 21.5 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.87 ms: 1.04x faster                                               |
| logging_simple             | 5.73 us                                                               | 5.57 us: 1.03x faster                                               |
| nqueens                    | 84.3 ms                                                               | 82.1 ms: 1.03x faster                                               |
| logging_format             | 6.44 us                                                               | 6.27 us: 1.03x faster                                               |
| unpickle_pure_python       | 194 us                                                                | 189 us: 1.03x faster                                                |
| coroutines                 | 25.3 ms                                                               | 24.7 ms: 1.02x faster                                               |
| json_loads                 | 28.7 us                                                               | 28.1 us: 1.02x faster                                               |
| regex_dna                  | 220 ms                                                                | 215 ms: 1.02x faster                                                |
| typing_runtime_protocols   | 171 us                                                                | 167 us: 1.02x faster                                                |
| pprint_pformat             | 1.48 sec                                                              | 1.46 sec: 1.02x faster                                              |
| json                       | 5.30 ms                                                               | 5.21 ms: 1.02x faster                                               |
| hexiom                     | 6.27 ms                                                               | 6.17 ms: 1.02x faster                                               |
| pyflate                    | 410 ms                                                                | 403 ms: 1.02x faster                                                |
| async_tree_none_tg         | 252 ms                                                                | 248 ms: 1.02x faster                                                |
| genshi_xml                 | 50.5 ms                                                               | 49.7 ms: 1.02x faster                                               |
| thrift                     | 780 us                                                                | 768 us: 1.02x faster                                                |
| regex_v8                   | 24.4 ms                                                               | 24.0 ms: 1.02x faster                                               |
| comprehensions             | 16.4 us                                                               | 16.2 us: 1.01x faster                                               |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.01x faster                                                |
| tomli_loads                | 1.83 sec                                                              | 1.81 sec: 1.01x faster                                              |
| spectral_norm              | 89.8 ms                                                               | 88.7 ms: 1.01x faster                                               |
| create_gc_cycles           | 2.60 ms                                                               | 2.57 ms: 1.01x faster                                               |
| sympy_sum                  | 150 ms                                                                | 148 ms: 1.01x faster                                                |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.6 ms: 1.01x faster                                               |
| scimark_fft                | 315 ms                                                                | 311 ms: 1.01x faster                                                |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                              |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.23 ms: 1.01x faster                                               |
| go                         | 117 ms                                                                | 115 ms: 1.01x faster                                                |
| async_tree_memoization     | 314 ms                                                                | 311 ms: 1.01x faster                                                |
| deepcopy_memo              | 29.8 us                                                               | 29.5 us: 1.01x faster                                               |
| regex_effbot               | 3.43 ms                                                               | 3.41 ms: 1.01x faster                                               |
| mako                       | 10.6 ms                                                               | 10.6 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.99 ms                                                               | 6.95 ms: 1.01x faster                                               |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.55 ms: 1.00x faster                                               |
| xml_etree_generate         | 80.0 ms                                                               | 79.7 ms: 1.00x faster                                               |
| sympy_expand               | 467 ms                                                                | 465 ms: 1.00x faster                                                |
| python_startup             | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                               |
| docutils                   | 2.64 sec                                                              | 2.64 sec: 1.00x faster                                              |
| meteor_contest             | 105 ms                                                                | 105 ms: 1.00x slower                                                |
| deepcopy                   | 257 us                                                                | 258 us: 1.01x slower                                                |
| dulwich_log                | 59.0 ms                                                               | 59.3 ms: 1.01x slower                                               |
| connected_components       | 455 ms                                                                | 458 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed    | 498 ms                                                                | 502 ms: 1.01x slower                                                |
| json_dumps                 | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                               |
| async_generators           | 426 ms                                                                | 430 ms: 1.01x slower                                                |
| scimark_monte_carlo        | 65.4 ms                                                               | 66.0 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 496 ms: 1.01x slower                                                |
| django_template            | 32.5 ms                                                               | 32.9 ms: 1.01x slower                                               |
| subparsers                 | 23.5 ms                                                               | 23.8 ms: 1.01x slower                                               |
| scimark_lu                 | 117 ms                                                                | 119 ms: 1.02x slower                                                |
| generators                 | 30.0 ms                                                               | 30.6 ms: 1.02x slower                                               |
| scimark_sor                | 117 ms                                                                | 119 ms: 1.02x slower                                                |
| pidigits                   | 189 ms                                                                | 193 ms: 1.02x slower                                                |
| deepcopy_reduce            | 2.67 us                                                               | 2.74 us: 1.02x slower                                               |
| pathlib                    | 17.1 ms                                                               | 17.5 ms: 1.03x slower                                               |
| pycparser                  | 1.11 sec                                                              | 1.15 sec: 1.03x slower                                              |
| nbody                      | 94.8 ms                                                               | 100 ms: 1.06x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (32): async_tree_memoization_tg, k_core, async_tree_none, djangocms, async_tree_io, html5lib, pprint_safe_repr, raytrace, asyncio_websockets, sympy_integrate, xml_etree_process, xml_etree_parse, pickle_pure_python, async_tree_io_tg, shortest_path, regex_compile, telco, bpe_tokeniser, xml_etree_iterparse, coverage, sympy_str, pylint, 2to3, float, sphinx, many_optionals, sqlite_synth, deltablue, chaos, fannkuch, logging_silent, crypto_pyaes

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 96.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x