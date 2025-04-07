# Results vs. base

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: 4300c89
- commit date: 2025-04-06
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 251 ms: 1.01x slower                                         |
| html5lib       | 61.1 ms                                                                | 60.5 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                 | 23.7 ms                                                                | 23.3 ms: 1.02x faster                                        |
| async_tree_cpu_io_mixed    | 478 ms                                                                 | 483 ms: 1.01x slower                                         |
| async_generators           | 393 ms                                                                 | 397 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 479 ms: 1.01x slower                                         |
| async_tree_none            | 255 ms                                                                 | 259 ms: 1.01x slower                                         |
| async_tree_none_tg         | 245 ms                                                                 | 249 ms: 1.02x slower                                         |
| async_tree_memoization     | 307 ms                                                                 | 312 ms: 1.02x slower                                         |
| async_tree_io              | 606 ms                                                                 | 615 ms: 1.02x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (3): async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| float          | 67.0 ms                                                                | 68.2 ms: 1.02x slower                                        |
| nbody          | 87.2 ms                                                                | 92.2 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                                | 23.0 ms: 1.04x faster                                        |
| regex_compile  | 123 ms                                                                 | 125 ms: 1.02x slower                                         |
| regex_dna      | 210 ms                                                                 | 220 ms: 1.04x slower                                         |
| regex_effbot   | 3.12 ms                                                                | 3.32 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads           | 29.8 us                                                                | 29.7 us: 1.00x faster                                        |
| xml_etree_process    | 58.1 ms                                                                | 58.3 ms: 1.00x slower                                        |
| unpickle_pure_python | 214 us                                                                 | 215 us: 1.00x slower                                         |
| json_dumps           | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                        |
| xml_etree_generate   | 83.0 ms                                                                | 83.5 ms: 1.01x slower                                        |
| pickle_pure_python   | 312 us                                                                 | 315 us: 1.01x slower                                         |
| tomli_loads          | 1.93 sec                                                               | 1.96 sec: 1.01x slower                                       |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                        |
| python_startup_no_site | 8.17 ms                                                                | 8.18 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 48.8 ms                                                                | 49.3 ms: 1.01x slower                                        |
| genshi_text    | 20.6 ms                                                                | 20.9 ms: 1.02x slower                                        |
| mako           | 11.0 ms                                                                | 11.3 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250406-linux-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| gc_traversal               | 5.01 ms                                                                | 4.77 ms: 1.05x faster                                        |
| regex_v8                   | 23.8 ms                                                                | 23.0 ms: 1.04x faster                                        |
| pprint_safe_repr           | 722 ms                                                                 | 701 ms: 1.03x faster                                         |
| richards                   | 43.2 ms                                                                | 42.2 ms: 1.02x faster                                        |
| pprint_pformat             | 1.47 sec                                                               | 1.44 sec: 1.02x faster                                       |
| deepcopy_reduce            | 2.62 us                                                                | 2.57 us: 1.02x faster                                        |
| coroutines                 | 23.7 ms                                                                | 23.3 ms: 1.02x faster                                        |
| richards_super             | 49.2 ms                                                                | 48.4 ms: 1.02x faster                                        |
| connected_components       | 452 ms                                                                 | 447 ms: 1.01x faster                                         |
| html5lib                   | 61.1 ms                                                                | 60.5 ms: 1.01x faster                                        |
| deepcopy                   | 251 us                                                                 | 249 us: 1.01x faster                                         |
| logging_silent             | 96.6 ns                                                                | 96.1 ns: 1.01x faster                                        |
| json_loads                 | 29.8 us                                                                | 29.7 us: 1.00x faster                                        |
| mdp                        | 1.23 sec                                                               | 1.23 sec: 1.00x faster                                       |
| hexiom                     | 6.16 ms                                                                | 6.14 ms: 1.00x faster                                        |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| python_startup             | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                        |
| python_startup_no_site     | 8.17 ms                                                                | 8.18 ms: 1.00x slower                                        |
| sympy_integrate            | 19.0 ms                                                                | 19.0 ms: 1.00x slower                                        |
| xml_etree_process          | 58.1 ms                                                                | 58.3 ms: 1.00x slower                                        |
| unpickle_pure_python       | 214 us                                                                 | 215 us: 1.00x slower                                         |
| deepcopy_memo              | 28.6 us                                                                | 28.8 us: 1.00x slower                                        |
| nqueens                    | 80.3 ms                                                                | 80.6 ms: 1.00x slower                                        |
| sqlglot_v2_transpile       | 1.52 ms                                                                | 1.53 ms: 1.00x slower                                        |
| sqlglot_v2_parse           | 1.22 ms                                                                | 1.22 ms: 1.01x slower                                        |
| bench_thread_pool          | 878 us                                                                 | 883 us: 1.01x slower                                         |
| json_dumps                 | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                        |
| create_gc_cycles           | 2.46 ms                                                                | 2.47 ms: 1.01x slower                                        |
| xml_etree_generate         | 83.0 ms                                                                | 83.5 ms: 1.01x slower                                        |
| bpe_tokeniser              | 4.52 sec                                                               | 4.55 sec: 1.01x slower                                       |
| sqlite_synth               | 2.76 us                                                                | 2.78 us: 1.01x slower                                        |
| sqlglot_v2_normalize       | 105 ms                                                                 | 105 ms: 1.01x slower                                         |
| pickle_pure_python         | 312 us                                                                 | 315 us: 1.01x slower                                         |
| sympy_sum                  | 147 ms                                                                 | 149 ms: 1.01x slower                                         |
| genshi_xml                 | 48.8 ms                                                                | 49.3 ms: 1.01x slower                                        |
| 2to3                       | 249 ms                                                                 | 251 ms: 1.01x slower                                         |
| sqlalchemy_declarative     | 130 ms                                                                 | 131 ms: 1.01x slower                                         |
| logging_format             | 6.05 us                                                                | 6.11 us: 1.01x slower                                        |
| async_tree_cpu_io_mixed    | 478 ms                                                                 | 483 ms: 1.01x slower                                         |
| sqlglot_v2_optimize        | 51.5 ms                                                                | 52.1 ms: 1.01x slower                                        |
| async_generators           | 393 ms                                                                 | 397 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 479 ms: 1.01x slower                                         |
| sympy_expand               | 451 ms                                                                 | 456 ms: 1.01x slower                                         |
| tomli_loads                | 1.93 sec                                                               | 1.96 sec: 1.01x slower                                       |
| crypto_pyaes               | 72.4 ms                                                                | 73.3 ms: 1.01x slower                                        |
| async_tree_none            | 255 ms                                                                 | 259 ms: 1.01x slower                                         |
| regex_compile              | 123 ms                                                                 | 125 ms: 1.02x slower                                         |
| async_tree_none_tg         | 245 ms                                                                 | 249 ms: 1.02x slower                                         |
| sympy_str                  | 265 ms                                                                 | 269 ms: 1.02x slower                                         |
| async_tree_memoization     | 307 ms                                                                 | 312 ms: 1.02x slower                                         |
| async_tree_io              | 606 ms                                                                 | 615 ms: 1.02x slower                                         |
| genshi_text                | 20.6 ms                                                                | 20.9 ms: 1.02x slower                                        |
| float                      | 67.0 ms                                                                | 68.2 ms: 1.02x slower                                        |
| deltablue                  | 3.30 ms                                                                | 3.37 ms: 1.02x slower                                        |
| spectral_norm              | 100 ms                                                                 | 102 ms: 1.02x slower                                         |
| chaos                      | 55.3 ms                                                                | 56.4 ms: 1.02x slower                                        |
| scimark_lu                 | 115 ms                                                                 | 117 ms: 1.02x slower                                         |
| scimark_monte_carlo        | 64.1 ms                                                                | 65.5 ms: 1.02x slower                                        |
| go                         | 109 ms                                                                 | 111 ms: 1.02x slower                                         |
| typing_runtime_protocols   | 163 us                                                                 | 167 us: 1.02x slower                                         |
| scimark_fft                | 333 ms                                                                 | 342 ms: 1.03x slower                                         |
| scimark_sparse_mat_mult    | 4.62 ms                                                                | 4.75 ms: 1.03x slower                                        |
| mako                       | 11.0 ms                                                                | 11.3 ms: 1.03x slower                                        |
| raytrace                   | 253 ms                                                                 | 261 ms: 1.03x slower                                         |
| comprehensions             | 16.5 us                                                                | 17.0 us: 1.03x slower                                        |
| fannkuch                   | 401 ms                                                                 | 413 ms: 1.03x slower                                         |
| regex_dna                  | 210 ms                                                                 | 220 ms: 1.04x slower                                         |
| scimark_sor                | 114 ms                                                                 | 119 ms: 1.04x slower                                         |
| pycparser                  | 1.11 sec                                                               | 1.16 sec: 1.05x slower                                       |
| nbody                      | 87.2 ms                                                                | 92.2 ms: 1.06x slower                                        |
| regex_effbot               | 3.12 ms                                                                | 3.32 ms: 1.06x slower                                        |
| pyflate                    | 419 ms                                                                 | 462 ms: 1.10x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (23): json, telco, k_core, sqlalchemy_imperative, generators, django_template, shortest_path, many_optionals, pathlib, subparsers, async_tree_io_tg, asyncio_websockets, bench_mp_pool, meteor_contest, coverage, dulwich_log, pylint, docutils, xml_etree_iterparse, logging_simple, xml_etree_parse, sphinx, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x