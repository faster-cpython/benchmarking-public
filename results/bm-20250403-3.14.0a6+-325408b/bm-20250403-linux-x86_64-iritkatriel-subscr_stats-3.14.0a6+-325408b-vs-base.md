# Results vs. base

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 325408b
- commit date: 2025-04-03
- overall geometric mean: 1.001x faster
- HPT reliability: 75.45%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization  | 312 ms                                                                 | 314 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed | 483 ms                                                                 | 487 ms: 1.01x slower                                                |
| async_generators        | 389 ms                                                                 | 394 ms: 1.01x slower                                                |
| async_tree_io           | 610 ms                                                                 | 619 ms: 1.01x slower                                                |
| async_tree_none         | 259 ms                                                                 | 262 ms: 1.01x slower                                                |
| async_tree_none_tg      | 249 ms                                                                 | 254 ms: 1.02x slower                                                |
| coroutines              | 23.4 ms                                                                | 23.8 ms: 1.02x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 96.4 ms                                                                | 97.0 ms: 1.01x slower                                               |
| float          | 69.3 ms                                                                | 71.4 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 215 ms                                                                 | 203 ms: 1.06x faster                                                |
| regex_effbot   | 3.80 ms                                                                | 3.74 ms: 1.01x faster                                               |
| regex_compile  | 127 ms                                                                 | 126 ms: 1.01x faster                                                |
| regex_v8       | 22.9 ms                                                                | 22.8 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 29.9 us                                                                | 29.5 us: 1.01x faster                                               |
| json_dumps           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                               |
| pickle_pure_python   | 321 us                                                                 | 320 us: 1.00x faster                                                |
| unpickle_pure_python | 219 us                                                                 | 219 us: 1.00x slower                                                |
| tomli_loads          | 1.95 sec                                                               | 1.96 sec: 1.00x slower                                              |
| xml_etree_parse      | 141 ms                                                                 | 141 ms: 1.01x slower                                                |
| xml_etree_process    | 58.9 ms                                                                | 59.5 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.16 ms                                                                | 8.16 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                                | 21.0 ms: 1.02x faster                                               |
| mako            | 11.4 ms                                                                | 11.2 ms: 1.02x faster                                               |
| django_template | 31.9 ms                                                                | 32.3 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna                | 215 ms                                                                 | 203 ms: 1.06x faster                                                |
| pycparser                | 1.17 sec                                                               | 1.13 sec: 1.04x faster                                              |
| logging_simple           | 5.66 us                                                                | 5.49 us: 1.03x faster                                               |
| scimark_sparse_mat_mult  | 4.86 ms                                                                | 4.75 ms: 1.02x faster                                               |
| logging_format           | 6.21 us                                                                | 6.07 us: 1.02x faster                                               |
| genshi_text              | 21.5 ms                                                                | 21.0 ms: 1.02x faster                                               |
| deepcopy_memo            | 30.0 us                                                                | 29.4 us: 1.02x faster                                               |
| mako                     | 11.4 ms                                                                | 11.2 ms: 1.02x faster                                               |
| scimark_fft              | 355 ms                                                                 | 350 ms: 1.02x faster                                                |
| regex_effbot             | 3.80 ms                                                                | 3.74 ms: 1.01x faster                                               |
| json_loads               | 29.9 us                                                                | 29.5 us: 1.01x faster                                               |
| json                     | 5.35 ms                                                                | 5.28 ms: 1.01x faster                                               |
| sympy_expand             | 461 ms                                                                 | 455 ms: 1.01x faster                                                |
| coverage                 | 84.3 ms                                                                | 83.2 ms: 1.01x faster                                               |
| nqueens                  | 82.6 ms                                                                | 81.7 ms: 1.01x faster                                               |
| crypto_pyaes             | 73.8 ms                                                                | 73.0 ms: 1.01x faster                                               |
| regex_compile            | 127 ms                                                                 | 126 ms: 1.01x faster                                                |
| json_dumps               | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                               |
| scimark_lu               | 115 ms                                                                 | 114 ms: 1.01x faster                                                |
| create_gc_cycles         | 2.50 ms                                                                | 2.48 ms: 1.01x faster                                               |
| richards_super           | 50.6 ms                                                                | 50.3 ms: 1.01x faster                                               |
| sqlite_synth             | 2.81 us                                                                | 2.79 us: 1.01x faster                                               |
| mdp                      | 1.24 sec                                                               | 1.23 sec: 1.01x faster                                              |
| sympy_str                | 268 ms                                                                 | 267 ms: 1.01x faster                                                |
| sqlalchemy_imperative    | 16.6 ms                                                                | 16.6 ms: 1.00x faster                                               |
| sqlglot_v2_normalize     | 107 ms                                                                 | 106 ms: 1.00x faster                                                |
| gc_traversal             | 5.02 ms                                                                | 4.99 ms: 1.00x faster                                               |
| sympy_integrate          | 19.2 ms                                                                | 19.1 ms: 1.00x faster                                               |
| regex_v8                 | 22.9 ms                                                                | 22.8 ms: 1.00x faster                                               |
| hexiom                   | 6.25 ms                                                                | 6.23 ms: 1.00x faster                                               |
| pickle_pure_python       | 321 us                                                                 | 320 us: 1.00x faster                                                |
| dulwich_log              | 58.4 ms                                                                | 58.3 ms: 1.00x faster                                               |
| sqlalchemy_declarative   | 130 ms                                                                 | 130 ms: 1.00x faster                                                |
| sqlglot_v2_optimize      | 53.1 ms                                                                | 52.9 ms: 1.00x faster                                               |
| python_startup_no_site   | 8.16 ms                                                                | 8.16 ms: 1.00x faster                                               |
| unpickle_pure_python     | 219 us                                                                 | 219 us: 1.00x slower                                                |
| pprint_pformat           | 1.48 sec                                                               | 1.48 sec: 1.00x slower                                              |
| tomli_loads              | 1.95 sec                                                               | 1.96 sec: 1.00x slower                                              |
| pprint_safe_repr         | 726 ms                                                                 | 730 ms: 1.00x slower                                                |
| 2to3                     | 254 ms                                                                 | 255 ms: 1.01x slower                                                |
| nbody                    | 96.4 ms                                                                | 97.0 ms: 1.01x slower                                               |
| xml_etree_parse          | 141 ms                                                                 | 141 ms: 1.01x slower                                                |
| async_tree_memoization   | 312 ms                                                                 | 314 ms: 1.01x slower                                                |
| fannkuch                 | 426 ms                                                                 | 429 ms: 1.01x slower                                                |
| bench_mp_pool            | 82.5 ms                                                                | 83.1 ms: 1.01x slower                                               |
| go                       | 115 ms                                                                 | 115 ms: 1.01x slower                                                |
| chaos                    | 58.1 ms                                                                | 58.5 ms: 1.01x slower                                               |
| deepcopy_reduce          | 2.70 us                                                                | 2.72 us: 1.01x slower                                               |
| async_tree_cpu_io_mixed  | 483 ms                                                                 | 487 ms: 1.01x slower                                                |
| xml_etree_process        | 58.9 ms                                                                | 59.5 ms: 1.01x slower                                               |
| django_template          | 31.9 ms                                                                | 32.3 ms: 1.01x slower                                               |
| deltablue                | 3.15 ms                                                                | 3.19 ms: 1.01x slower                                               |
| meteor_contest           | 105 ms                                                                 | 107 ms: 1.01x slower                                                |
| async_generators         | 389 ms                                                                 | 394 ms: 1.01x slower                                                |
| async_tree_io            | 610 ms                                                                 | 619 ms: 1.01x slower                                                |
| async_tree_none          | 259 ms                                                                 | 262 ms: 1.01x slower                                                |
| sqlglot_v2_transpile     | 1.56 ms                                                                | 1.58 ms: 1.01x slower                                               |
| scimark_sor              | 119 ms                                                                 | 120 ms: 1.01x slower                                                |
| async_tree_none_tg       | 249 ms                                                                 | 254 ms: 1.02x slower                                                |
| pathlib                  | 16.3 ms                                                                | 16.6 ms: 1.02x slower                                               |
| comprehensions           | 16.7 us                                                                | 17.0 us: 1.02x slower                                               |
| coroutines               | 23.4 ms                                                                | 23.8 ms: 1.02x slower                                               |
| sqlglot_v2_parse         | 1.25 ms                                                                | 1.28 ms: 1.03x slower                                               |
| typing_runtime_protocols | 161 us                                                                 | 166 us: 1.03x slower                                                |
| float                    | 69.3 ms                                                                | 71.4 ms: 1.03x slower                                               |
| pyflate                  | 449 ms                                                                 | 473 ms: 1.05x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (29): richards, sphinx, shortest_path, xml_etree_iterparse, html5lib, deepcopy, xml_etree_generate, genshi_xml, docutils, telco, raytrace, bench_thread_pool, logging_silent, pidigits, python_startup, generators, asyncio_websockets, many_optionals, scimark_monte_carlo, spectral_norm, sympy_sum, pylint, k_core, bpe_tokeniser, async_tree_memoization_tg, connected_components, subparsers, async_tree_cpu_io_mixed_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 75.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x