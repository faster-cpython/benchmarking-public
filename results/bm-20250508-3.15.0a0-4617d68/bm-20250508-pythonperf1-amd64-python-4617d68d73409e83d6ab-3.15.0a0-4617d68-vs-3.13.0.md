# Results vs. 3.13.0

- fork: python
- ref: 4617d68d73409e83d6ab
- machine: windows-amd64
- commit hash: 4617d68
- commit date: 2025-05-08
- overall geometric mean: 1.031x slower
- HPT reliability: 98.44%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 228 ms: 1.06x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                     |
| sphinx         | 617 ms                                                      | 652 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 405 ms: 1.23x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 223 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.70x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 81.4 ms: 1.01x slower                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.6 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.78 ms: 1.09x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| mako            | 6.56 ms                                                     | 6.77 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| mdp                        | 1.43 sec                                                    | 795 ms: 1.80x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.70x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                       |
| deepcopy                   | 223 us                                                      | 171 us: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                                      |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 405 ms: 1.23x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 223 ms: 1.19x faster                                                       |
| float                      | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                       |
| json                       | 3.30 ms                                                     | 2.99 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 78.3 ms: 1.08x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 58.8 ms: 1.08x faster                                                      |
| nbody                      | 66.3 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.48 ms: 1.05x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.67 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.7 ms: 1.03x faster                                                      |
| scimark_fft                | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 75.5 ms: 1.01x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 57.1 ms: 1.01x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 81.4 ms: 1.01x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.91 sec: 1.01x slower                                                     |
| chaos                      | 37.9 ms                                                     | 38.4 ms: 1.01x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| pidigits                   | 146 ms                                                      | 149 ms: 1.01x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.4 ns: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 363 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 495 ms: 1.02x slower                                                       |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                       |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| crypto_pyaes               | 45.6 ms                                                     | 47.0 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                       |
| pycparser                  | 695 ms                                                      | 717 ms: 1.03x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.77 ms: 1.03x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 74.7 ms: 1.04x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.02 sec: 1.04x slower                                                     |
| sympy_sum                  | 85.2 ms                                                     | 88.8 ms: 1.04x slower                                                      |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                       |
| connected_components       | 320 ms                                                      | 336 ms: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.2 ms: 1.05x slower                                                      |
| sphinx                     | 617 ms                                                      | 652 ms: 1.06x slower                                                       |
| 2to3                       | 215 ms                                                      | 228 ms: 1.06x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.07 ms: 1.06x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.9 ms: 1.06x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.7 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 110 us: 1.07x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.7 ms: 1.08x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.25 us: 1.08x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                     |
| logging_format             | 6.18 us                                                     | 6.69 us: 1.08x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.6 ms: 1.08x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 883 us: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.78 ms: 1.09x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.14 ms: 1.13x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.23 ms: 1.13x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.15x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 97.6 ms: 1.16x slower                                                      |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 444 us: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.55x slower                                                      |
| coverage                   | 45.3 ms                                                     | 294 ms: 6.48x slower                                                       |
| thrift                     | 8.47 ms                                                     | 103 ms: 12.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (8): pylint, json_loads, fannkuch, xml_etree_parse, pyflate, genshi_xml, html5lib, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250508-3.15.0a0-4617d68/bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.031x slower

# HPT report

- Reliability score: 98.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown