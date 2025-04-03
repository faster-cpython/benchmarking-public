# Results vs. base

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 9e0e134
- commit date: 2025-04-03
- overall geometric mean: 1.005x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_generators        | 389 ms                                                                 | 392 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed | 483 ms                                                                 | 488 ms: 1.01x slower                                                |
| coroutines              | 23.4 ms                                                                | 23.8 ms: 1.02x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| nbody          | 96.4 ms                                                                | 97.7 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                 | 126 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 29.9 us                                                                | 29.5 us: 1.01x faster                                               |
| pickle_pure_python   | 321 us                                                                 | 317 us: 1.01x faster                                                |
| xml_etree_generate   | 85.0 ms                                                                | 84.2 ms: 1.01x faster                                               |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                |
| xml_etree_iterparse  | 99.1 ms                                                                | 98.4 ms: 1.01x faster                                               |
| xml_etree_process    | 58.9 ms                                                                | 58.5 ms: 1.01x faster                                               |
| json_dumps           | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                               |
| xml_etree_parse      | 141 ms                                                                 | 142 ms: 1.01x slower                                                |
| tomli_loads          | 1.95 sec                                                               | 2.00 sec: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.16 ms                                                                | 8.19 ms: 1.00x slower                                               |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.4 ms: 1.02x faster                                               |
| genshi_xml      | 49.6 ms                                                                | 48.8 ms: 1.02x faster                                               |
| mako            | 11.4 ms                                                                | 11.3 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 4.86 ms                                                                | 4.63 ms: 1.05x faster                                               |
| pyflate                 | 449 ms                                                                 | 432 ms: 1.04x faster                                                |
| gc_traversal            | 5.02 ms                                                                | 4.85 ms: 1.03x faster                                               |
| logging_simple          | 5.66 us                                                                | 5.48 us: 1.03x faster                                               |
| logging_silent          | 98.9 ns                                                                | 96.1 ns: 1.03x faster                                               |
| hexiom                  | 6.25 ms                                                                | 6.08 ms: 1.03x faster                                               |
| go                      | 115 ms                                                                 | 112 ms: 1.02x faster                                                |
| logging_format          | 6.21 us                                                                | 6.07 us: 1.02x faster                                               |
| richards                | 44.9 ms                                                                | 44.1 ms: 1.02x faster                                               |
| coverage                | 84.3 ms                                                                | 82.8 ms: 1.02x faster                                               |
| django_template         | 31.9 ms                                                                | 31.4 ms: 1.02x faster                                               |
| sqlite_synth            | 2.81 us                                                                | 2.76 us: 1.02x faster                                               |
| genshi_xml              | 49.6 ms                                                                | 48.8 ms: 1.02x faster                                               |
| deepcopy                | 258 us                                                                 | 254 us: 1.02x faster                                                |
| fannkuch                | 426 ms                                                                 | 419 ms: 1.01x faster                                                |
| deepcopy_memo           | 30.0 us                                                                | 29.6 us: 1.01x faster                                               |
| json_loads              | 29.9 us                                                                | 29.5 us: 1.01x faster                                               |
| json                    | 5.35 ms                                                                | 5.28 ms: 1.01x faster                                               |
| richards_super          | 50.6 ms                                                                | 50.0 ms: 1.01x faster                                               |
| deltablue               | 3.15 ms                                                                | 3.11 ms: 1.01x faster                                               |
| pickle_pure_python      | 321 us                                                                 | 317 us: 1.01x faster                                                |
| subparsers              | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                               |
| crypto_pyaes            | 73.8 ms                                                                | 73.0 ms: 1.01x faster                                               |
| sympy_expand            | 461 ms                                                                 | 457 ms: 1.01x faster                                                |
| comprehensions          | 16.7 us                                                                | 16.5 us: 1.01x faster                                               |
| xml_etree_generate      | 85.0 ms                                                                | 84.2 ms: 1.01x faster                                               |
| sqlglot_v2_normalize    | 107 ms                                                                 | 106 ms: 1.01x faster                                                |
| nqueens                 | 82.6 ms                                                                | 81.8 ms: 1.01x faster                                               |
| unpickle_pure_python    | 219 us                                                                 | 217 us: 1.01x faster                                                |
| sympy_str               | 268 ms                                                                 | 266 ms: 1.01x faster                                                |
| mako                    | 11.4 ms                                                                | 11.3 ms: 1.01x faster                                               |
| sympy_integrate         | 19.2 ms                                                                | 19.0 ms: 1.01x faster                                               |
| regex_compile           | 127 ms                                                                 | 126 ms: 1.01x faster                                                |
| sqlglot_v2_optimize     | 53.1 ms                                                                | 52.7 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 99.1 ms                                                                | 98.4 ms: 1.01x faster                                               |
| sympy_sum               | 148 ms                                                                 | 147 ms: 1.01x faster                                                |
| mdp                     | 1.24 sec                                                               | 1.23 sec: 1.01x faster                                              |
| create_gc_cycles        | 2.50 ms                                                                | 2.48 ms: 1.01x faster                                               |
| xml_etree_process       | 58.9 ms                                                                | 58.5 ms: 1.01x faster                                               |
| scimark_sor             | 119 ms                                                                 | 118 ms: 1.01x faster                                                |
| pprint_safe_repr        | 726 ms                                                                 | 722 ms: 1.01x faster                                                |
| scimark_fft             | 355 ms                                                                 | 354 ms: 1.01x faster                                                |
| pprint_pformat          | 1.48 sec                                                               | 1.47 sec: 1.01x faster                                              |
| pidigits                | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| sqlalchemy_declarative  | 130 ms                                                                 | 130 ms: 1.00x faster                                                |
| sqlglot_v2_transpile    | 1.56 ms                                                                | 1.56 ms: 1.00x faster                                               |
| bench_thread_pool       | 872 us                                                                 | 869 us: 1.00x faster                                                |
| many_optionals          | 947 us                                                                 | 944 us: 1.00x faster                                                |
| sqlalchemy_imperative   | 16.6 ms                                                                | 16.6 ms: 1.00x faster                                               |
| python_startup_no_site  | 8.16 ms                                                                | 8.19 ms: 1.00x slower                                               |
| python_startup          | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| chaos                   | 58.1 ms                                                                | 58.3 ms: 1.00x slower                                               |
| bench_mp_pool           | 82.5 ms                                                                | 82.9 ms: 1.01x slower                                               |
| pathlib                 | 16.3 ms                                                                | 16.4 ms: 1.01x slower                                               |
| json_dumps              | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                               |
| async_generators        | 389 ms                                                                 | 392 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed | 483 ms                                                                 | 488 ms: 1.01x slower                                                |
| xml_etree_parse         | 141 ms                                                                 | 142 ms: 1.01x slower                                                |
| nbody                   | 96.4 ms                                                                | 97.7 ms: 1.01x slower                                               |
| connected_components    | 447 ms                                                                 | 455 ms: 1.02x slower                                                |
| meteor_contest          | 105 ms                                                                 | 107 ms: 1.02x slower                                                |
| coroutines              | 23.4 ms                                                                | 23.8 ms: 1.02x slower                                               |
| tomli_loads             | 1.95 sec                                                               | 2.00 sec: 1.02x slower                                              |
| spectral_norm           | 96.3 ms                                                                | 100.0 ms: 1.04x slower                                              |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (31): html5lib, async_tree_memoization_tg, float, pycparser, typing_runtime_protocols, scimark_monte_carlo, async_tree_io, docutils, async_tree_io_tg, async_tree_none_tg, bpe_tokeniser, async_tree_memoization, regex_v8, 2to3, deepcopy_reduce, dulwich_log, regex_dna, pylint, raytrace, regex_effbot, sqlglot_v2_parse, asyncio_websockets, generators, genshi_text, scimark_lu, k_core, telco, sphinx, async_tree_cpu_io_mixed_tg, async_tree_none, shortest_path

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x