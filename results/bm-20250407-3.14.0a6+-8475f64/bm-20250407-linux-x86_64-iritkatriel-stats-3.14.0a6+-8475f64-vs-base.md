# Results vs. base

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: 8475f64
- commit date: 2025-04-07
- overall geometric mean: 1.001x slower
- HPT reliability: 97.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 250 ms: 1.00x slower                                         |
| docutils       | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                       |
| html5lib       | 61.1 ms                                                                | 60.4 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines       | 23.7 ms                                                                | 22.9 ms: 1.04x faster                                        |
| async_generators | 393 ms                                                                 | 390 ms: 1.01x faster                                         |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 67.0 ms                                                                | 66.3 ms: 1.01x faster                                        |
| nbody          | 87.2 ms                                                                | 86.4 ms: 1.01x faster                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                                | 22.5 ms: 1.06x faster                                        |
| regex_compile  | 123 ms                                                                 | 124 ms: 1.01x slower                                         |
| regex_dna      | 210 ms                                                                 | 217 ms: 1.03x slower                                         |
| regex_effbot   | 3.12 ms                                                                | 3.45 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads           | 29.8 us                                                                | 29.9 us: 1.00x slower                                        |
| xml_etree_iterparse  | 98.0 ms                                                                | 98.6 ms: 1.01x slower                                        |
| xml_etree_process    | 58.1 ms                                                                | 58.6 ms: 1.01x slower                                        |
| xml_etree_generate   | 83.0 ms                                                                | 83.8 ms: 1.01x slower                                        |
| unpickle_pure_python | 214 us                                                                 | 217 us: 1.01x slower                                         |
| json_dumps           | 11.6 ms                                                                | 11.8 ms: 1.02x slower                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                        |
| python_startup_no_site | 8.17 ms                                                                | 8.21 ms: 1.01x slower                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 31.5 ms                                                                | 31.3 ms: 1.01x faster                                        |
| genshi_xml      | 48.8 ms                                                                | 48.6 ms: 1.01x faster                                        |
| mako            | 11.0 ms                                                                | 11.0 ms: 1.00x slower                                        |
| genshi_text     | 20.6 ms                                                                | 20.7 ms: 1.00x slower                                        |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| gc_traversal             | 5.01 ms                                                                | 4.60 ms: 1.09x faster                                        |
| regex_v8                 | 23.8 ms                                                                | 22.5 ms: 1.06x faster                                        |
| coroutines               | 23.7 ms                                                                | 22.9 ms: 1.04x faster                                        |
| spectral_norm            | 100 ms                                                                 | 97.0 ms: 1.03x faster                                        |
| deepcopy                 | 251 us                                                                 | 245 us: 1.02x faster                                         |
| deepcopy_reduce          | 2.62 us                                                                | 2.57 us: 1.02x faster                                        |
| richards_super           | 49.2 ms                                                                | 48.5 ms: 1.01x faster                                        |
| pprint_safe_repr         | 722 ms                                                                 | 712 ms: 1.01x faster                                         |
| html5lib                 | 61.1 ms                                                                | 60.4 ms: 1.01x faster                                        |
| mdp                      | 1.23 sec                                                               | 1.22 sec: 1.01x faster                                       |
| float                    | 67.0 ms                                                                | 66.3 ms: 1.01x faster                                        |
| pprint_pformat           | 1.47 sec                                                               | 1.46 sec: 1.01x faster                                       |
| nbody                    | 87.2 ms                                                                | 86.4 ms: 1.01x faster                                        |
| sqlalchemy_imperative    | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                        |
| subparsers               | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                        |
| async_generators         | 393 ms                                                                 | 390 ms: 1.01x faster                                         |
| django_template          | 31.5 ms                                                                | 31.3 ms: 1.01x faster                                        |
| richards                 | 43.2 ms                                                                | 42.9 ms: 1.01x faster                                        |
| pathlib                  | 16.5 ms                                                                | 16.3 ms: 1.01x faster                                        |
| genshi_xml               | 48.8 ms                                                                | 48.6 ms: 1.01x faster                                        |
| crypto_pyaes             | 72.4 ms                                                                | 72.0 ms: 1.00x faster                                        |
| dulwich_log              | 59.2 ms                                                                | 59.0 ms: 1.00x faster                                        |
| docutils                 | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                       |
| bench_thread_pool        | 878 us                                                                 | 875 us: 1.00x faster                                         |
| sympy_integrate          | 19.0 ms                                                                | 19.0 ms: 1.00x slower                                        |
| create_gc_cycles         | 2.46 ms                                                                | 2.47 ms: 1.00x slower                                        |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| mako                     | 11.0 ms                                                                | 11.0 ms: 1.00x slower                                        |
| sqlalchemy_declarative   | 130 ms                                                                 | 131 ms: 1.00x slower                                         |
| generators               | 29.6 ms                                                                | 29.8 ms: 1.00x slower                                        |
| 2to3                     | 249 ms                                                                 | 250 ms: 1.00x slower                                         |
| json_loads               | 29.8 us                                                                | 29.9 us: 1.00x slower                                        |
| deltablue                | 3.30 ms                                                                | 3.32 ms: 1.00x slower                                        |
| genshi_text              | 20.6 ms                                                                | 20.7 ms: 1.00x slower                                        |
| python_startup           | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                        |
| sqlglot_v2_optimize      | 51.5 ms                                                                | 51.8 ms: 1.01x slower                                        |
| logging_silent           | 96.6 ns                                                                | 97.2 ns: 1.01x slower                                        |
| python_startup_no_site   | 8.17 ms                                                                | 8.21 ms: 1.01x slower                                        |
| chaos                    | 55.3 ms                                                                | 55.6 ms: 1.01x slower                                        |
| sympy_sum                | 147 ms                                                                 | 148 ms: 1.01x slower                                         |
| bench_mp_pool            | 81.8 ms                                                                | 82.3 ms: 1.01x slower                                        |
| xml_etree_iterparse      | 98.0 ms                                                                | 98.6 ms: 1.01x slower                                        |
| hexiom                   | 6.16 ms                                                                | 6.21 ms: 1.01x slower                                        |
| typing_runtime_protocols | 163 us                                                                 | 165 us: 1.01x slower                                         |
| xml_etree_process        | 58.1 ms                                                                | 58.6 ms: 1.01x slower                                        |
| sympy_str                | 265 ms                                                                 | 267 ms: 1.01x slower                                         |
| xml_etree_generate       | 83.0 ms                                                                | 83.8 ms: 1.01x slower                                        |
| telco                    | 7.72 ms                                                                | 7.79 ms: 1.01x slower                                        |
| coverage                 | 84.6 ms                                                                | 85.4 ms: 1.01x slower                                        |
| go                       | 109 ms                                                                 | 110 ms: 1.01x slower                                         |
| regex_compile            | 123 ms                                                                 | 124 ms: 1.01x slower                                         |
| comprehensions           | 16.5 us                                                                | 16.7 us: 1.01x slower                                        |
| sympy_expand             | 451 ms                                                                 | 455 ms: 1.01x slower                                         |
| scimark_lu               | 115 ms                                                                 | 116 ms: 1.01x slower                                         |
| unpickle_pure_python     | 214 us                                                                 | 217 us: 1.01x slower                                         |
| json_dumps               | 11.6 ms                                                                | 11.8 ms: 1.02x slower                                        |
| fannkuch                 | 401 ms                                                                 | 409 ms: 1.02x slower                                         |
| scimark_sparse_mat_mult  | 4.62 ms                                                                | 4.73 ms: 1.02x slower                                        |
| scimark_sor              | 114 ms                                                                 | 117 ms: 1.03x slower                                         |
| regex_dna                | 210 ms                                                                 | 217 ms: 1.03x slower                                         |
| pycparser                | 1.11 sec                                                               | 1.15 sec: 1.03x slower                                       |
| pyflate                  | 419 ms                                                                 | 446 ms: 1.06x slower                                         |
| regex_effbot             | 3.12 ms                                                                | 3.45 ms: 1.10x slower                                        |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (32): k_core, async_tree_io_tg, tomli_loads, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, connected_components, asyncio_websockets, scimark_fft, logging_simple, json, scimark_monte_carlo, deepcopy_memo, sqlglot_v2_normalize, many_optionals, meteor_contest, sqlite_synth, raytrace, nqueens, async_tree_cpu_io_mixed_tg, async_tree_memoization, sqlglot_v2_parse, sqlglot_v2_transpile, xml_etree_parse, pylint, bpe_tokeniser, sphinx, pickle_pure_python, logging_format, async_tree_io, shortest_path, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 97.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x