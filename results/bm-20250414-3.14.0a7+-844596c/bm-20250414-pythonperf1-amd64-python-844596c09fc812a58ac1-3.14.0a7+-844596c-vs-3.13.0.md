# Results vs. 3.13.0

- fork: python
- ref: 844596c09fc812a58ac1
- machine: windows-amd64
- commit hash: 844596c
- commit date: 2025-04-14
- overall geometric mean: 1.030x faster
- HPT reliability: 80.42%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| sphinx         | 617 ms                                                      | 651 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                        |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.26x faster                                                        |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.9 ms: 1.18x faster                                                       |
| nbody          | 66.3 ms                                                     | 61.3 ms: 1.08x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.7 ms: 1.62x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.49 ms: 1.13x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 79.5 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.8 ms: 1.03x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.5 us: 1.03x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 133 us: 1.03x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 55.7 ms: 1.04x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.0 ms: 1.06x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.79 ms: 1.10x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.9 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.62 ms: 1.01x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                       |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.3 ms: 2.33x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                        |
| mdp                        | 1.43 sec                                                    | 813 ms: 1.76x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.7 ms: 1.62x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                        |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 17.7 us: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                        |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.26x faster                                                        |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                        |
| float                      | 50.8 ms                                                     | 42.9 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.49 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.13x faster                                                       |
| go                         | 84.7 ms                                                     | 76.4 ms: 1.11x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 57.5 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.04 ms: 1.08x faster                                                       |
| nbody                      | 66.3 ms                                                     | 61.3 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.3 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.45 ms: 1.06x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.64 ms: 1.05x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.8 ms: 1.03x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 74.5 ms: 1.02x faster                                                       |
| fannkuch                   | 252 ms                                                      | 246 ms: 1.02x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 79.5 ms: 1.02x faster                                                       |
| pyflate                    | 283 ms                                                      | 279 ms: 1.01x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 54.2 ns: 1.01x faster                                                       |
| mako                       | 6.56 ms                                                     | 6.62 ms: 1.01x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.90 sec: 1.01x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 73.1 ms: 1.02x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.4 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 494 ms: 1.02x slower                                                        |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 3.94 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.03x slower                                                        |
| shortest_path              | 355 ms                                                      | 364 ms: 1.03x slower                                                        |
| json_loads                 | 15.1 us                                                     | 15.5 us: 1.03x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 133 us: 1.03x slower                                                        |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.26 ms: 1.03x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.00 sec: 1.03x slower                                                      |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                        |
| pycparser                  | 695 ms                                                      | 717 ms: 1.03x slower                                                        |
| sympy_expand               | 286 ms                                                      | 295 ms: 1.03x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                       |
| connected_components       | 320 ms                                                      | 331 ms: 1.04x slower                                                        |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.7 ms: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.7 ms: 1.04x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.0 ms: 1.04x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 55.7 ms: 1.04x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.5 ms: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 651 ms: 1.05x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.07 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.0 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.0 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.6 ms: 1.08x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 882 us: 1.09x slower                                                        |
| xml_etree_process          | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.31 us: 1.09x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.79 ms: 1.10x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 61.9 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.84 us: 1.11x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.10 ms: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 50.4 ms: 1.11x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                        |
| raytrace                   | 153 ms                                                      | 174 ms: 1.14x slower                                                        |
| many_optionals             | 361 us                                                      | 425 us: 1.18x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.9 ms: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.8 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (7): pylint, html5lib, scimark_fft, scimark_lu, chaos, genshi_xml, k_core
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250414-3.14.0a7+-844596c/bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 80.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown