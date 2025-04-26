# Results vs. 3.13.0

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: windows-amd64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.035x faster
- HPT reliability: 78.16%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                        |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.3 ms: 1.20x faster                                                       |
| nbody          | 66.3 ms                                                     | 62.2 ms: 1.07x faster                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                                       |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.5 ms: 1.08x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.80 ms: 1.10x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.5 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                       |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.4 ms: 2.32x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                        |
| mdp                        | 1.43 sec                                                    | 785 ms: 1.82x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                        |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                       |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                        |
| float                      | 50.8 ms                                                     | 42.3 ms: 1.20x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.79 us: 1.13x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 56.4 ms: 1.12x faster                                                       |
| go                         | 84.7 ms                                                     | 75.8 ms: 1.12x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.53 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.07x faster                                                       |
| nbody                      | 66.3 ms                                                     | 62.2 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.47 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.77 sec: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.9 ms: 1.02x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 75.0 ms: 1.02x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                       |
| pyflate                    | 283 ms                                                      | 281 ms: 1.01x faster                                                        |
| fannkuch                   | 252 ms                                                      | 250 ms: 1.01x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 54.9 ns: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.7 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 991 ms: 1.02x slower                                                        |
| scimark_fft                | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                        |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 46.7 ms: 1.03x slower                                                       |
| shortest_path              | 355 ms                                                      | 364 ms: 1.03x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 3.94 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.26 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.8 ms: 1.03x slower                                                       |
| sympy_expand               | 286 ms                                                      | 295 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                        |
| k_core                     | 1.70 sec                                                    | 1.76 sec: 1.04x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.9 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.9 ms: 1.05x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.6 ms: 1.05x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 59.0 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.4 ms: 1.06x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.1 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.4 ms: 1.06x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.07x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 871 us: 1.07x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.5 ms: 1.08x slower                                                       |
| coverage                   | 45.3 ms                                                     | 49.8 ms: 1.10x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.80 ms: 1.10x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.35 us: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.80 us: 1.10x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.10 ms: 1.11x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                        |
| raytrace                   | 153 ms                                                      | 174 ms: 1.14x slower                                                        |
| many_optionals             | 361 us                                                      | 421 us: 1.17x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.5 ms: 1.21x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (9): pylint, html5lib, regex_dna, chaos, sqlite_synth, pprint_safe_repr, mako, pycparser, genshi_xml
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 78.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown