# Results vs. base

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: ebd800a
- commit date: 2025-04-03
- overall geometric mean: 1.000x slower
- HPT reliability: 83.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.01x slower                                                |
| html5lib       | 63.0 ms                                                                | 61.9 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 483 ms                                                                 | 486 ms: 1.01x slower                                                |
| async_tree_none_tg      | 249 ms                                                                 | 251 ms: 1.01x slower                                                |
| async_generators        | 389 ms                                                                 | 392 ms: 1.01x slower                                                |
| async_tree_memoization  | 312 ms                                                                 | 315 ms: 1.01x slower                                                |
| async_tree_none         | 259 ms                                                                 | 262 ms: 1.01x slower                                                |
| coroutines              | 23.4 ms                                                                | 24.3 ms: 1.04x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (5): async_tree_memoization_tg, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| float          | 69.3 ms                                                                | 70.4 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 215 ms                                                                 | 207 ms: 1.04x faster                                                |
| regex_effbot   | 3.80 ms                                                                | 3.76 ms: 1.01x faster                                               |
| regex_v8       | 22.9 ms                                                                | 22.8 ms: 1.01x faster                                               |
| regex_compile  | 127 ms                                                                 | 126 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python | 321 us                                                                 | 322 us: 1.01x slower                                                |
| tomli_loads        | 1.95 sec                                                               | 1.97 sec: 1.01x slower                                              |
| json_dumps         | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                               |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (6): xml_etree_iterparse, json_loads, xml_etree_generate, unpickle_pure_python, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.16 ms                                                                | 8.17 ms: 1.00x slower                                               |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                               |
| django_template | 31.9 ms                                                                | 32.2 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal             | 5.02 ms                                                                | 4.82 ms: 1.04x faster                                               |
| regex_dna                | 215 ms                                                                 | 207 ms: 1.04x faster                                                |
| pycparser                | 1.17 sec                                                               | 1.13 sec: 1.03x faster                                              |
| scimark_fft              | 355 ms                                                                 | 346 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult  | 4.86 ms                                                                | 4.77 ms: 1.02x faster                                               |
| html5lib                 | 63.0 ms                                                                | 61.9 ms: 1.02x faster                                               |
| richards                 | 44.9 ms                                                                | 44.2 ms: 1.02x faster                                               |
| json                     | 5.35 ms                                                                | 5.27 ms: 1.02x faster                                               |
| sqlite_synth             | 2.81 us                                                                | 2.76 us: 1.02x faster                                               |
| deepcopy_reduce          | 2.70 us                                                                | 2.66 us: 1.01x faster                                               |
| mdp                      | 1.24 sec                                                               | 1.22 sec: 1.01x faster                                              |
| scimark_sor              | 119 ms                                                                 | 117 ms: 1.01x faster                                                |
| deepcopy                 | 258 us                                                                 | 255 us: 1.01x faster                                                |
| regex_effbot             | 3.80 ms                                                                | 3.76 ms: 1.01x faster                                               |
| scimark_monte_carlo      | 67.9 ms                                                                | 67.2 ms: 1.01x faster                                               |
| genshi_text              | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                               |
| go                       | 115 ms                                                                 | 114 ms: 1.01x faster                                                |
| sympy_expand             | 461 ms                                                                 | 458 ms: 1.01x faster                                                |
| logging_simple           | 5.66 us                                                                | 5.62 us: 1.01x faster                                               |
| regex_v8                 | 22.9 ms                                                                | 22.8 ms: 1.01x faster                                               |
| deepcopy_memo            | 30.0 us                                                                | 29.8 us: 1.01x faster                                               |
| sympy_str                | 268 ms                                                                 | 267 ms: 1.01x faster                                                |
| dulwich_log              | 58.4 ms                                                                | 58.1 ms: 1.01x faster                                               |
| create_gc_cycles         | 2.50 ms                                                                | 2.49 ms: 1.01x faster                                               |
| richards_super           | 50.6 ms                                                                | 50.3 ms: 1.01x faster                                               |
| pidigits                 | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| regex_compile            | 127 ms                                                                 | 126 ms: 1.00x faster                                                |
| sympy_integrate          | 19.2 ms                                                                | 19.1 ms: 1.00x faster                                               |
| python_startup_no_site   | 8.16 ms                                                                | 8.17 ms: 1.00x slower                                               |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| sqlalchemy_declarative   | 130 ms                                                                 | 131 ms: 1.00x slower                                                |
| sqlglot_v2_optimize      | 53.1 ms                                                                | 53.2 ms: 1.00x slower                                               |
| deltablue                | 3.15 ms                                                                | 3.16 ms: 1.00x slower                                               |
| bench_mp_pool            | 82.5 ms                                                                | 82.9 ms: 1.00x slower                                               |
| pickle_pure_python       | 321 us                                                                 | 322 us: 1.01x slower                                                |
| 2to3                     | 254 ms                                                                 | 255 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed  | 483 ms                                                                 | 486 ms: 1.01x slower                                                |
| comprehensions           | 16.7 us                                                                | 16.8 us: 1.01x slower                                               |
| django_template          | 31.9 ms                                                                | 32.2 ms: 1.01x slower                                               |
| async_tree_none_tg       | 249 ms                                                                 | 251 ms: 1.01x slower                                                |
| async_generators         | 389 ms                                                                 | 392 ms: 1.01x slower                                                |
| shortest_path            | 493 ms                                                                 | 497 ms: 1.01x slower                                                |
| tomli_loads              | 1.95 sec                                                               | 1.97 sec: 1.01x slower                                              |
| async_tree_memoization   | 312 ms                                                                 | 315 ms: 1.01x slower                                                |
| scimark_lu               | 115 ms                                                                 | 116 ms: 1.01x slower                                                |
| async_tree_none          | 259 ms                                                                 | 262 ms: 1.01x slower                                                |
| pathlib                  | 16.3 ms                                                                | 16.5 ms: 1.01x slower                                               |
| hexiom                   | 6.25 ms                                                                | 6.33 ms: 1.01x slower                                               |
| connected_components     | 447 ms                                                                 | 454 ms: 1.01x slower                                                |
| spectral_norm            | 96.3 ms                                                                | 97.7 ms: 1.01x slower                                               |
| sqlglot_v2_transpile     | 1.56 ms                                                                | 1.59 ms: 1.02x slower                                               |
| logging_silent           | 98.9 ns                                                                | 101 ns: 1.02x slower                                                |
| float                    | 69.3 ms                                                                | 70.4 ms: 1.02x slower                                               |
| meteor_contest           | 105 ms                                                                 | 107 ms: 1.02x slower                                                |
| json_dumps               | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                               |
| typing_runtime_protocols | 161 us                                                                 | 164 us: 1.02x slower                                                |
| pprint_pformat           | 1.48 sec                                                               | 1.51 sec: 1.02x slower                                              |
| sqlglot_v2_parse         | 1.25 ms                                                                | 1.27 ms: 1.02x slower                                               |
| pprint_safe_repr         | 726 ms                                                                 | 742 ms: 1.02x slower                                                |
| coroutines               | 23.4 ms                                                                | 24.3 ms: 1.04x slower                                               |
| pyflate                  | 449 ms                                                                 | 468 ms: 1.04x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (34): xml_etree_iterparse, json_loads, chaos, xml_etree_generate, genshi_xml, docutils, sphinx, mako, raytrace, sympy_sum, bench_thread_pool, async_tree_memoization_tg, generators, unpickle_pure_python, telco, fannkuch, crypto_pyaes, subparsers, xml_etree_parse, xml_etree_process, many_optionals, sqlalchemy_imperative, asyncio_websockets, nbody, coverage, nqueens, async_tree_io_tg, logging_format, bpe_tokeniser, sqlglot_v2_normalize, async_tree_cpu_io_mixed_tg, k_core, pylint, async_tree_io

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 83.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x