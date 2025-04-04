# Results vs. base

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 1ae9389
- commit date: 2025-04-03
- overall geometric mean: 1.001x faster
- HPT reliability: 72.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 256 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 23.4 ms                                                                | 23.0 ms: 1.02x faster                                               |
| async_tree_memoization     | 312 ms                                                                 | 310 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 481 ms: 1.02x slower                                                |
| async_generators           | 389 ms                                                                 | 395 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed    | 483 ms                                                                 | 493 ms: 1.02x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none_tg, async_tree_none, asyncio_websockets, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                |
| float          | 69.3 ms                                                                | 69.9 ms: 1.01x slower                                               |
| nbody          | 96.4 ms                                                                | 97.4 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 215 ms                                                                 | 213 ms: 1.01x faster                                                |
| regex_compile  | 127 ms                                                                 | 126 ms: 1.00x faster                                                |
| regex_effbot   | 3.80 ms                                                                | 3.86 ms: 1.02x slower                                               |
| regex_v8       | 22.9 ms                                                                | 23.9 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 99.1 ms                                                                | 97.9 ms: 1.01x faster                                               |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                |
| xml_etree_generate   | 85.0 ms                                                                | 84.2 ms: 1.01x faster                                               |
| json_loads           | 29.9 us                                                                | 29.7 us: 1.01x faster                                               |
| pickle_pure_python   | 321 us                                                                 | 319 us: 1.01x faster                                                |
| xml_etree_process    | 58.9 ms                                                                | 58.6 ms: 1.00x faster                                               |
| xml_etree_parse      | 141 ms                                                                 | 140 ms: 1.00x faster                                                |
| json_dumps           | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.16 ms                                                                | 8.17 ms: 1.00x slower                                               |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.3 ms: 1.02x faster                                               |
| genshi_xml      | 49.6 ms                                                                | 49.2 ms: 1.01x faster                                               |
| genshi_text     | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                               |
| mako            | 11.4 ms                                                                | 11.6 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal               | 5.02 ms                                                                | 4.65 ms: 1.08x faster                                               |
| richards                   | 44.9 ms                                                                | 43.3 ms: 1.04x faster                                               |
| pycparser                  | 1.17 sec                                                               | 1.13 sec: 1.03x faster                                              |
| richards_super             | 50.6 ms                                                                | 49.6 ms: 1.02x faster                                               |
| logging_silent             | 98.9 ns                                                                | 97.0 ns: 1.02x faster                                               |
| django_template            | 31.9 ms                                                                | 31.3 ms: 1.02x faster                                               |
| coroutines                 | 23.4 ms                                                                | 23.0 ms: 1.02x faster                                               |
| logging_simple             | 5.66 us                                                                | 5.58 us: 1.01x faster                                               |
| subparsers                 | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                               |
| create_gc_cycles           | 2.50 ms                                                                | 2.47 ms: 1.01x faster                                               |
| scimark_sor                | 119 ms                                                                 | 117 ms: 1.01x faster                                                |
| deepcopy_reduce            | 2.70 us                                                                | 2.67 us: 1.01x faster                                               |
| xml_etree_iterparse        | 99.1 ms                                                                | 97.9 ms: 1.01x faster                                               |
| raytrace                   | 266 ms                                                                 | 262 ms: 1.01x faster                                                |
| regex_dna                  | 215 ms                                                                 | 213 ms: 1.01x faster                                                |
| go                         | 115 ms                                                                 | 113 ms: 1.01x faster                                                |
| json                       | 5.35 ms                                                                | 5.30 ms: 1.01x faster                                               |
| sympy_expand               | 461 ms                                                                 | 457 ms: 1.01x faster                                                |
| deepcopy_memo              | 30.0 us                                                                | 29.8 us: 1.01x faster                                               |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                |
| genshi_xml                 | 49.6 ms                                                                | 49.2 ms: 1.01x faster                                               |
| xml_etree_generate         | 85.0 ms                                                                | 84.2 ms: 1.01x faster                                               |
| sqlite_synth               | 2.81 us                                                                | 2.78 us: 1.01x faster                                               |
| deltablue                  | 3.15 ms                                                                | 3.12 ms: 1.01x faster                                               |
| hexiom                     | 6.25 ms                                                                | 6.20 ms: 1.01x faster                                               |
| coverage                   | 84.3 ms                                                                | 83.6 ms: 1.01x faster                                               |
| logging_format             | 6.21 us                                                                | 6.17 us: 1.01x faster                                               |
| scimark_monte_carlo        | 67.9 ms                                                                | 67.4 ms: 1.01x faster                                               |
| genshi_text                | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                               |
| sympy_str                  | 268 ms                                                                 | 267 ms: 1.01x faster                                                |
| async_tree_memoization     | 312 ms                                                                 | 310 ms: 1.01x faster                                                |
| many_optionals             | 947 us                                                                 | 941 us: 1.01x faster                                                |
| sqlglot_v2_normalize       | 107 ms                                                                 | 106 ms: 1.01x faster                                                |
| json_loads                 | 29.9 us                                                                | 29.7 us: 1.01x faster                                               |
| pickle_pure_python         | 321 us                                                                 | 319 us: 1.01x faster                                                |
| bpe_tokeniser              | 4.58 sec                                                               | 4.56 sec: 1.01x faster                                              |
| xml_etree_process          | 58.9 ms                                                                | 58.6 ms: 1.00x faster                                               |
| xml_etree_parse            | 141 ms                                                                 | 140 ms: 1.00x faster                                                |
| deepcopy                   | 258 us                                                                 | 257 us: 1.00x faster                                                |
| regex_compile              | 127 ms                                                                 | 126 ms: 1.00x faster                                                |
| dulwich_log                | 58.4 ms                                                                | 58.3 ms: 1.00x faster                                               |
| sqlglot_v2_optimize        | 53.1 ms                                                                | 53.0 ms: 1.00x faster                                               |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x slower                                                |
| python_startup_no_site     | 8.16 ms                                                                | 8.17 ms: 1.00x slower                                               |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| fannkuch                   | 426 ms                                                                 | 427 ms: 1.00x slower                                                |
| sympy_sum                  | 148 ms                                                                 | 149 ms: 1.00x slower                                                |
| typing_runtime_protocols   | 161 us                                                                 | 162 us: 1.01x slower                                                |
| shortest_path              | 493 ms                                                                 | 496 ms: 1.01x slower                                                |
| 2to3                       | 254 ms                                                                 | 256 ms: 1.01x slower                                                |
| generators                 | 28.6 ms                                                                | 28.8 ms: 1.01x slower                                               |
| sqlglot_v2_transpile       | 1.56 ms                                                                | 1.58 ms: 1.01x slower                                               |
| json_dumps                 | 11.5 ms                                                                | 11.6 ms: 1.01x slower                                               |
| float                      | 69.3 ms                                                                | 69.9 ms: 1.01x slower                                               |
| nbody                      | 96.4 ms                                                                | 97.4 ms: 1.01x slower                                               |
| pprint_pformat             | 1.48 sec                                                               | 1.50 sec: 1.01x slower                                              |
| pprint_safe_repr           | 726 ms                                                                 | 736 ms: 1.01x slower                                                |
| pathlib                    | 16.3 ms                                                                | 16.5 ms: 1.01x slower                                               |
| regex_effbot               | 3.80 ms                                                                | 3.86 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 481 ms: 1.02x slower                                                |
| async_generators           | 389 ms                                                                 | 395 ms: 1.02x slower                                                |
| meteor_contest             | 105 ms                                                                 | 107 ms: 1.02x slower                                                |
| connected_components       | 447 ms                                                                 | 455 ms: 1.02x slower                                                |
| sqlglot_v2_parse           | 1.25 ms                                                                | 1.27 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed    | 483 ms                                                                 | 493 ms: 1.02x slower                                                |
| mako                       | 11.4 ms                                                                | 11.6 ms: 1.02x slower                                               |
| scimark_fft                | 355 ms                                                                 | 364 ms: 1.03x slower                                                |
| scimark_sparse_mat_mult    | 4.86 ms                                                                | 5.04 ms: 1.04x slower                                               |
| regex_v8                   | 22.9 ms                                                                | 23.9 ms: 1.04x slower                                               |
| spectral_norm              | 96.3 ms                                                                | 101 ms: 1.05x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (25): async_tree_memoization_tg, html5lib, async_tree_none_tg, async_tree_none, nqueens, telco, comprehensions, sphinx, pyflate, crypto_pyaes, bench_thread_pool, chaos, mdp, scimark_lu, sqlalchemy_imperative, sympy_integrate, asyncio_websockets, sqlalchemy_declarative, bench_mp_pool, async_tree_io_tg, docutils, pylint, async_tree_io, tomli_loads, k_core

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 72.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x