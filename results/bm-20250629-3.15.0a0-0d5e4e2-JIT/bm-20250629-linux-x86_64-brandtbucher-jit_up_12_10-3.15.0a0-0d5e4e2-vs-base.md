# Results vs. base

- fork: brandtbucher
- ref: jit_up_12_10
- machine: linux-x86_64
- commit hash: 0d5e4e2
- commit date: 2025-06-29
- overall geometric mean: 1.000x faster
- HPT reliability: 78.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.66 sec: 1.00x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines              | 25.3 ms                                                               | 24.5 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed | 498 ms                                                                | 496 ms: 1.01x faster                                                |
| async_tree_none_tg      | 252 ms                                                                | 255 ms: 1.01x slower                                                |
| async_generators        | 426 ms                                                                | 438 ms: 1.03x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_io, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 189 ms: 1.00x slower                                                |
| nbody          | 94.8 ms                                                               | 97.1 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                | 212 ms: 1.04x faster                                                |
| regex_v8       | 24.4 ms                                                               | 23.9 ms: 1.02x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.37 ms: 1.02x faster                                               |
| regex_compile  | 127 ms                                                                | 128 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.5 us: 1.01x faster                                               |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.5 ms: 1.01x faster                                               |
| unpickle_pure_python | 194 us                                                                | 193 us: 1.00x faster                                                |
| pickle_pure_python   | 320 us                                                                | 322 us: 1.01x slower                                                |
| xml_etree_generate   | 80.0 ms                                                               | 80.6 ms: 1.01x slower                                               |
| json_dumps           | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                               |
| python_startup_no_site | 6.99 ms                                                               | 6.96 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 50.5 ms                                                               | 51.4 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (3): django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna                | 220 ms                                                                | 212 ms: 1.04x faster                                                |
| pprint_pformat           | 1.48 sec                                                              | 1.43 sec: 1.04x faster                                              |
| coroutines               | 25.3 ms                                                               | 24.5 ms: 1.03x faster                                               |
| logging_format           | 6.44 us                                                               | 6.26 us: 1.03x faster                                               |
| pprint_safe_repr         | 721 ms                                                                | 704 ms: 1.03x faster                                                |
| logging_simple           | 5.73 us                                                               | 5.60 us: 1.02x faster                                               |
| regex_v8                 | 24.4 ms                                                               | 23.9 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult  | 5.05 ms                                                               | 4.94 ms: 1.02x faster                                               |
| nqueens                  | 84.3 ms                                                               | 82.7 ms: 1.02x faster                                               |
| regex_effbot             | 3.43 ms                                                               | 3.37 ms: 1.02x faster                                               |
| typing_runtime_protocols | 171 us                                                                | 168 us: 1.02x faster                                                |
| sqlglot_v2_normalize     | 107 ms                                                                | 106 ms: 1.01x faster                                                |
| pyflate                  | 410 ms                                                                | 406 ms: 1.01x faster                                                |
| pathlib                  | 17.1 ms                                                               | 17.0 ms: 1.01x faster                                               |
| json_loads               | 28.7 us                                                               | 28.5 us: 1.01x faster                                               |
| sqlglot_v2_optimize      | 53.1 ms                                                               | 52.7 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed  | 498 ms                                                                | 496 ms: 1.01x faster                                                |
| thrift                   | 780 us                                                                | 776 us: 1.01x faster                                                |
| xml_etree_iterparse      | 99.0 ms                                                               | 98.5 ms: 1.01x faster                                               |
| unpickle_pure_python     | 194 us                                                                | 193 us: 1.00x faster                                                |
| scimark_fft              | 315 ms                                                                | 313 ms: 1.00x faster                                                |
| python_startup           | 12.3 ms                                                               | 12.2 ms: 1.00x faster                                               |
| python_startup_no_site   | 6.99 ms                                                               | 6.96 ms: 1.00x faster                                               |
| gc_traversal             | 5.17 ms                                                               | 5.17 ms: 1.00x slower                                               |
| pidigits                 | 189 ms                                                                | 189 ms: 1.00x slower                                                |
| sympy_str                | 272 ms                                                                | 272 ms: 1.00x slower                                                |
| deepcopy                 | 257 us                                                                | 258 us: 1.00x slower                                                |
| create_gc_cycles         | 2.60 ms                                                               | 2.61 ms: 1.00x slower                                               |
| spectral_norm            | 89.8 ms                                                               | 90.2 ms: 1.00x slower                                               |
| sympy_integrate          | 19.4 ms                                                               | 19.4 ms: 1.00x slower                                               |
| sympy_expand             | 467 ms                                                                | 469 ms: 1.00x slower                                                |
| docutils                 | 2.64 sec                                                              | 2.66 sec: 1.00x slower                                              |
| regex_compile            | 127 ms                                                                | 128 ms: 1.01x slower                                                |
| connected_components     | 455 ms                                                                | 457 ms: 1.01x slower                                                |
| chaos                    | 61.4 ms                                                               | 61.7 ms: 1.01x slower                                               |
| deepcopy_memo            | 29.8 us                                                               | 29.9 us: 1.01x slower                                               |
| pickle_pure_python       | 320 us                                                                | 322 us: 1.01x slower                                                |
| xml_etree_generate       | 80.0 ms                                                               | 80.6 ms: 1.01x slower                                               |
| json_dumps               | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                               |
| subparsers               | 23.5 ms                                                               | 23.6 ms: 1.01x slower                                               |
| many_optionals           | 975 us                                                                | 984 us: 1.01x slower                                                |
| deltablue                | 3.02 ms                                                               | 3.05 ms: 1.01x slower                                               |
| async_tree_none_tg       | 252 ms                                                                | 255 ms: 1.01x slower                                                |
| bpe_tokeniser            | 4.34 sec                                                              | 4.39 sec: 1.01x slower                                              |
| dulwich_log              | 59.0 ms                                                               | 59.7 ms: 1.01x slower                                               |
| deepcopy_reduce          | 2.67 us                                                               | 2.71 us: 1.01x slower                                               |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                |
| shortest_path            | 492 ms                                                                | 498 ms: 1.01x slower                                                |
| generators               | 30.0 ms                                                               | 30.4 ms: 1.01x slower                                               |
| scimark_monte_carlo      | 65.4 ms                                                               | 66.6 ms: 1.02x slower                                               |
| genshi_xml               | 50.5 ms                                                               | 51.4 ms: 1.02x slower                                               |
| nbody                    | 94.8 ms                                                               | 97.1 ms: 1.02x slower                                               |
| scimark_sor              | 117 ms                                                                | 120 ms: 1.03x slower                                                |
| async_generators         | 426 ms                                                                | 438 ms: 1.03x slower                                                |
| logging_silent           | 103 ns                                                                | 106 ns: 1.03x slower                                                |
| pycparser                | 1.11 sec                                                              | 1.16 sec: 1.04x slower                                              |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (37): async_tree_io_tg, richards_super, k_core, html5lib, xml_etree_parse, json, async_tree_io, telco, sqlite_synth, mdp, sympy_sum, async_tree_memoization, hexiom, django_template, coverage, sqlglot_v2_parse, asyncio_websockets, pylint, 2to3, genshi_text, sqlglot_v2_transpile, raytrace, float, go, fannkuch, comprehensions, tomli_loads, async_tree_cpu_io_mixed_tg, scimark_lu, crypto_pyaes, sphinx, xml_etree_process, async_tree_none, djangocms, mako, richards, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 78.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x