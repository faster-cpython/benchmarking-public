# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 406dc71
- commit date: 2025-08-03
- overall geometric mean: 1.119x slower
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 325 ms: 1.11x slower                                        |
| docutils       | 2.83 sec                                                     | 3.14 sec: 1.11x slower                                      |
| html5lib       | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 354 ms: 1.32x faster                                        |
| async_tree_io              | 843 ms                                                       | 667 ms: 1.26x faster                                        |
| async_tree_memoization     | 453 ms                                                       | 362 ms: 1.25x faster                                        |
| async_tree_io_tg           | 831 ms                                                       | 671 ms: 1.24x faster                                        |
| async_tree_none            | 376 ms                                                       | 306 ms: 1.23x faster                                        |
| async_tree_none_tg         | 346 ms                                                       | 290 ms: 1.19x faster                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 531 ms: 1.14x faster                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 527 ms: 1.10x faster                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.03x slower                                       |
| Geometric mean             | (ref)                                                        | 1.15x faster                                                |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 257 ms: 1.02x slower                                        |
| float          | 81.3 ms                                                      | 107 ms: 1.31x slower                                        |
| nbody          | 89.3 ms                                                      | 184 ms: 2.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.40x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 223 ms: 1.11x faster                                        |
| regex_v8       | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                       |
| regex_effbot   | 3.67 ms                                                      | 3.64 ms: 1.01x faster                                       |
| regex_compile  | 143 ms                                                       | 159 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 142 ms: 1.06x faster                                        |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                       |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                        |
| xml_etree_process    | 61.2 ms                                                      | 76.1 ms: 1.24x slower                                       |
| tomli_loads          | 2.46 sec                                                     | 3.08 sec: 1.25x slower                                      |
| xml_etree_generate   | 86.5 ms                                                      | 109 ms: 1.26x slower                                        |
| pickle_pure_python   | 323 us                                                       | 410 us: 1.27x slower                                        |
| unpickle_pure_python | 217 us                                                       | 388 us: 1.78x slower                                        |
| Geometric mean       | (ref)                                                        | 1.19x slower                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.7 ms: 1.11x faster                                       |
| django_template | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                       |
| genshi_xml      | 57.1 ms                                                      | 57.7 ms: 1.01x slower                                       |
| mako            | 10.4 ms                                                      | 16.9 ms: 1.63x slower                                       |
| Geometric mean  | (ref)                                                        | 1.10x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.46 sec: 1.74x faster                                      |
| deepcopy                   | 392 us                                                       | 279 us: 1.40x faster                                        |
| deepcopy_memo              | 38.6 us                                                      | 27.6 us: 1.40x faster                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 354 ms: 1.32x faster                                        |
| async_tree_io              | 843 ms                                                       | 667 ms: 1.26x faster                                        |
| async_tree_memoization     | 453 ms                                                       | 362 ms: 1.25x faster                                        |
| async_tree_io_tg           | 831 ms                                                       | 671 ms: 1.24x faster                                        |
| async_tree_none            | 376 ms                                                       | 306 ms: 1.23x faster                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                       |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.20x faster                                        |
| async_tree_none_tg         | 346 ms                                                       | 290 ms: 1.19x faster                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 531 ms: 1.14x faster                                        |
| generators                 | 33.6 ms                                                      | 29.9 ms: 1.12x faster                                       |
| dulwich_log                | 68.2 ms                                                      | 60.9 ms: 1.12x faster                                       |
| genshi_text                | 26.2 ms                                                      | 23.7 ms: 1.11x faster                                       |
| regex_dna                  | 247 ms                                                       | 223 ms: 1.11x faster                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 527 ms: 1.10x faster                                        |
| regex_v8                   | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                       |
| logging_silent             | 97.9 ns                                                      | 91.7 ns: 1.07x faster                                       |
| json                       | 5.69 ms                                                      | 5.33 ms: 1.07x faster                                       |
| scimark_lu                 | 98.7 ms                                                      | 92.5 ms: 1.07x faster                                       |
| xml_etree_parse            | 150 ms                                                       | 142 ms: 1.06x faster                                        |
| thrift                     | 901 us                                                       | 857 us: 1.05x faster                                        |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                       |
| logging_simple             | 6.39 us                                                      | 6.10 us: 1.05x faster                                       |
| html5lib                   | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                       |
| pylint                     | 347 ms                                                       | 334 ms: 1.04x faster                                        |
| logging_format             | 6.94 us                                                      | 6.69 us: 1.04x faster                                       |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                       |
| django_template            | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                       |
| coverage                   | 80.0 ms                                                      | 77.8 ms: 1.03x faster                                       |
| python_startup_no_site     | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                       |
| regex_effbot               | 3.67 ms                                                      | 3.64 ms: 1.01x faster                                       |
| sympy_integrate            | 23.6 ms                                                      | 23.7 ms: 1.01x slower                                       |
| genshi_xml                 | 57.1 ms                                                      | 57.7 ms: 1.01x slower                                       |
| pidigits                   | 252 ms                                                       | 257 ms: 1.02x slower                                        |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                       |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.03x slower                                       |
| sqlite_synth               | 2.91 us                                                      | 3.01 us: 1.04x slower                                       |
| sympy_sum                  | 155 ms                                                       | 161 ms: 1.04x slower                                        |
| chaos                      | 60.2 ms                                                      | 63.4 ms: 1.05x slower                                       |
| sympy_str                  | 298 ms                                                       | 315 ms: 1.06x slower                                        |
| k_core                     | 2.17 sec                                                     | 2.29 sec: 1.06x slower                                      |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                        |
| sympy_expand               | 509 ms                                                       | 552 ms: 1.08x slower                                        |
| shortest_path              | 460 ms                                                       | 501 ms: 1.09x slower                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.94 ms: 1.10x slower                                       |
| 2to3                       | 293 ms                                                       | 325 ms: 1.11x slower                                        |
| docutils                   | 2.83 sec                                                     | 3.14 sec: 1.11x slower                                      |
| regex_compile              | 143 ms                                                       | 159 ms: 1.11x slower                                        |
| connected_components       | 432 ms                                                       | 487 ms: 1.13x slower                                        |
| nqueens                    | 90.7 ms                                                      | 103 ms: 1.14x slower                                        |
| typing_runtime_protocols   | 169 us                                                       | 201 us: 1.19x slower                                        |
| pycparser                  | 1.24 sec                                                     | 1.52 sec: 1.22x slower                                      |
| meteor_contest             | 130 ms                                                       | 160 ms: 1.23x slower                                        |
| xml_etree_process          | 61.2 ms                                                      | 76.1 ms: 1.24x slower                                       |
| tomli_loads                | 2.46 sec                                                     | 3.08 sec: 1.25x slower                                      |
| raytrace                   | 273 ms                                                       | 341 ms: 1.25x slower                                        |
| pyflate                    | 503 ms                                                       | 632 ms: 1.26x slower                                        |
| xml_etree_generate         | 86.5 ms                                                      | 109 ms: 1.26x slower                                        |
| pickle_pure_python         | 323 us                                                       | 410 us: 1.27x slower                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.48 sec: 1.27x slower                                      |
| float                      | 81.3 ms                                                      | 107 ms: 1.31x slower                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.26 sec: 1.31x slower                                      |
| pprint_safe_repr           | 843 ms                                                       | 1.11 sec: 1.32x slower                                      |
| scimark_monte_carlo        | 66.1 ms                                                      | 88.9 ms: 1.35x slower                                       |
| many_optionals             | 930 us                                                       | 1.28 ms: 1.37x slower                                       |
| go                         | 162 ms                                                       | 224 ms: 1.38x slower                                        |
| scimark_fft                | 328 ms                                                       | 462 ms: 1.41x slower                                        |
| gc_traversal               | 4.74 ms                                                      | 6.77 ms: 1.43x slower                                       |
| crypto_pyaes               | 73.3 ms                                                      | 105 ms: 1.43x slower                                        |
| hexiom                     | 6.55 ms                                                      | 10.6 ms: 1.62x slower                                       |
| mako                       | 10.4 ms                                                      | 16.9 ms: 1.63x slower                                       |
| fannkuch                   | 363 ms                                                       | 607 ms: 1.67x slower                                        |
| spectral_norm              | 97.0 ms                                                      | 168 ms: 1.73x slower                                        |
| deltablue                  | 3.42 ms                                                      | 5.97 ms: 1.75x slower                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 8.35 ms: 1.75x slower                                       |
| unpickle_pure_python       | 217 us                                                       | 388 us: 1.78x slower                                        |
| comprehensions             | 17.0 us                                                      | 30.6 us: 1.80x slower                                       |
| nbody                      | 89.3 ms                                                      | 184 ms: 2.06x slower                                        |
| subparsers                 | 17.5 ms                                                      | 43.2 ms: 2.47x slower                                       |
| telco                      | 8.79 ms                                                      | 159 ms: 18.13x slower                                       |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                |

Benchmark hidden because not significant (7): asyncio_websockets, djangocms, async_generators, richards_super, json_dumps, richards, sphinx
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250803-3.15.0a0-406dc71-PYTHON_UOPS/bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-406dc71.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.119x slower

# HPT report

- Reliability score: 99.63% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x