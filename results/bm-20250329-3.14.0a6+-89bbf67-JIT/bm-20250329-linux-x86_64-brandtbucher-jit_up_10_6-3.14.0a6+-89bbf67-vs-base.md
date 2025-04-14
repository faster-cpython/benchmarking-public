# Results vs. base

- fork: brandtbucher
- ref: jit_up_10_6
- machine: linux-x86_64
- commit hash: 89bbf67
- commit date: 2025-03-29
- overall geometric mean: 1.002x slower
- HPT reliability: 89.07%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 267 ms: 1.02x slower                                                |
| docutils       | 2.69 sec                                                               | 2.70 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines             | 24.1 ms                                                                | 23.4 ms: 1.03x faster                                               |
| async_tree_none        | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| async_tree_none_tg     | 255 ms                                                                 | 252 ms: 1.01x faster                                                |
| async_tree_memoization | 319 ms                                                                 | 315 ms: 1.01x faster                                                |
| async_generators       | 418 ms                                                                 | 415 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 86.6 ms: 1.03x faster                                               |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 22.7 ms: 1.03x faster                                               |
| regex_dna      | 217 ms                                                                 | 211 ms: 1.03x faster                                                |
| regex_effbot   | 3.16 ms                                                                | 3.08 ms: 1.02x faster                                               |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 214 us                                                                 | 211 us: 1.01x faster                                                |
| xml_etree_process    | 57.1 ms                                                                | 56.7 ms: 1.01x faster                                               |
| xml_etree_generate   | 80.8 ms                                                                | 80.2 ms: 1.01x faster                                               |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                |
| pickle_pure_python   | 325 us                                                                 | 328 us: 1.01x slower                                                |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.7 ms: 1.01x slower                                               |
| tomli_loads          | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                               |
| python_startup_no_site | 8.19 ms                                                                | 8.23 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                               |
| django_template | 32.0 ms                                                                | 31.8 ms: 1.01x faster                                               |
| mako            | 11.0 ms                                                                | 11.1 ms: 1.00x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal            | 5.05 ms                                                                | 4.82 ms: 1.05x faster                                               |
| comprehensions          | 19.0 us                                                                | 18.4 us: 1.04x faster                                               |
| regex_v8                | 23.5 ms                                                                | 22.7 ms: 1.03x faster                                               |
| nbody                   | 89.4 ms                                                                | 86.6 ms: 1.03x faster                                               |
| coroutines              | 24.1 ms                                                                | 23.4 ms: 1.03x faster                                               |
| crypto_pyaes            | 78.3 ms                                                                | 76.0 ms: 1.03x faster                                               |
| regex_dna               | 217 ms                                                                 | 211 ms: 1.03x faster                                                |
| regex_effbot            | 3.16 ms                                                                | 3.08 ms: 1.02x faster                                               |
| async_tree_none         | 266 ms                                                                 | 260 ms: 1.02x faster                                                |
| unpickle_pure_python    | 214 us                                                                 | 211 us: 1.01x faster                                                |
| async_tree_none_tg      | 255 ms                                                                 | 252 ms: 1.01x faster                                                |
| shortest_path           | 494 ms                                                                 | 488 ms: 1.01x faster                                                |
| async_tree_memoization  | 319 ms                                                                 | 315 ms: 1.01x faster                                                |
| genshi_text             | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                               |
| thrift                  | 783 us                                                                 | 776 us: 1.01x faster                                                |
| django_template         | 32.0 ms                                                                | 31.8 ms: 1.01x faster                                               |
| logging_format          | 6.16 us                                                                | 6.11 us: 1.01x faster                                               |
| chaos                   | 60.3 ms                                                                | 59.8 ms: 1.01x faster                                               |
| xml_etree_process       | 57.1 ms                                                                | 56.7 ms: 1.01x faster                                               |
| xml_etree_generate      | 80.8 ms                                                                | 80.2 ms: 1.01x faster                                               |
| deltablue               | 3.06 ms                                                                | 3.03 ms: 1.01x faster                                               |
| raytrace                | 269 ms                                                                 | 267 ms: 1.01x faster                                                |
| logging_simple          | 5.59 us                                                                | 5.55 us: 1.01x faster                                               |
| generators              | 29.2 ms                                                                | 29.0 ms: 1.01x faster                                               |
| xml_etree_parse         | 140 ms                                                                 | 139 ms: 1.01x faster                                                |
| subparsers              | 21.0 ms                                                                | 20.9 ms: 1.01x faster                                               |
| async_generators        | 418 ms                                                                 | 415 ms: 1.00x faster                                                |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x faster                                                |
| scimark_fft             | 312 ms                                                                 | 313 ms: 1.00x slower                                                |
| mako                    | 11.0 ms                                                                | 11.1 ms: 1.00x slower                                               |
| python_startup          | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                               |
| python_startup_no_site  | 8.19 ms                                                                | 8.23 ms: 1.00x slower                                               |
| create_gc_cycles        | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                               |
| deepcopy_memo           | 29.0 us                                                                | 29.1 us: 1.01x slower                                               |
| docutils                | 2.69 sec                                                               | 2.70 sec: 1.01x slower                                              |
| dulwich_log             | 60.6 ms                                                                | 61.0 ms: 1.01x slower                                               |
| sympy_expand            | 475 ms                                                                 | 478 ms: 1.01x slower                                                |
| pickle_pure_python      | 325 us                                                                 | 328 us: 1.01x slower                                                |
| regex_compile           | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| bench_thread_pool       | 882 us                                                                 | 889 us: 1.01x slower                                                |
| go                      | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult | 4.61 ms                                                                | 4.65 ms: 1.01x slower                                               |
| xml_etree_iterparse     | 97.6 ms                                                                | 98.7 ms: 1.01x slower                                               |
| mdp                     | 2.48 sec                                                               | 2.51 sec: 1.01x slower                                              |
| scimark_lu              | 118 ms                                                                 | 119 ms: 1.01x slower                                                |
| tomli_loads             | 1.87 sec                                                               | 1.89 sec: 1.01x slower                                              |
| 2to3                    | 263 ms                                                                 | 267 ms: 1.02x slower                                                |
| sqlglot_v2_parse        | 1.29 ms                                                                | 1.31 ms: 1.02x slower                                               |
| pprint_pformat          | 1.55 sec                                                               | 1.58 sec: 1.02x slower                                              |
| bpe_tokeniser           | 4.57 sec                                                               | 4.65 sec: 1.02x slower                                              |
| sqlglot_v2_optimize     | 54.1 ms                                                                | 55.0 ms: 1.02x slower                                               |
| sqlite_synth            | 2.72 us                                                                | 2.76 us: 1.02x slower                                               |
| sympy_str               | 274 ms                                                                 | 279 ms: 1.02x slower                                                |
| nqueens                 | 84.9 ms                                                                | 86.3 ms: 1.02x slower                                               |
| sympy_integrate         | 20.0 ms                                                                | 20.4 ms: 1.02x slower                                               |
| deepcopy                | 260 us                                                                 | 265 us: 1.02x slower                                                |
| sqlglot_v2_normalize    | 107 ms                                                                 | 110 ms: 1.02x slower                                                |
| sympy_sum               | 152 ms                                                                 | 155 ms: 1.02x slower                                                |
| many_optionals          | 970 us                                                                 | 994 us: 1.02x slower                                                |
| hexiom                  | 6.86 ms                                                                | 7.04 ms: 1.03x slower                                               |
| sqlglot_v2_transpile    | 1.61 ms                                                                | 1.65 ms: 1.03x slower                                               |
| pyflate                 | 432 ms                                                                 | 443 ms: 1.03x slower                                                |
| deepcopy_reduce         | 2.66 us                                                                | 2.74 us: 1.03x slower                                               |
| telco                   | 7.93 ms                                                                | 8.16 ms: 1.03x slower                                               |
| sqlalchemy_imperative   | 17.1 ms                                                                | 17.6 ms: 1.03x slower                                               |
| sqlalchemy_declarative  | 133 ms                                                                 | 138 ms: 1.04x slower                                                |
| richards                | 35.8 ms                                                                | 37.2 ms: 1.04x slower                                               |
| richards_super          | 41.1 ms                                                                | 42.8 ms: 1.04x slower                                               |
| logging_silent          | 95.7 ns                                                                | 100 ns: 1.05x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (27): async_tree_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, pathlib, json_dumps, scimark_monte_carlo, float, fannkuch, json_loads, connected_components, asyncio_websockets, k_core, html5lib, genshi_xml, bench_mp_pool, scimark_sor, async_tree_cpu_io_mixed, meteor_contest, spectral_norm, json, pprint_safe_repr, pycparser, sphinx, typing_runtime_protocols, coverage, pylint

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 89.07% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x