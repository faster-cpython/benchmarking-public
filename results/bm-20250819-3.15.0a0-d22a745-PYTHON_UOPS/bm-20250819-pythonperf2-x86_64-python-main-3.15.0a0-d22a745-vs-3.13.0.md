# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d22a745
- commit date: 2025-08-19
- overall geometric mean: 1.093x slower
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 320 ms: 1.09x slower                                        |
| docutils       | 2.83 sec                                                     | 3.11 sec: 1.10x slower                                      |
| html5lib       | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                       |
| sphinx         | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                      |
| Geometric mean | (ref)                                                        | 1.04x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 350 ms: 1.33x faster                                        |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                        |
| async_tree_memoization     | 453 ms                                                       | 352 ms: 1.29x faster                                        |
| async_tree_io              | 843 ms                                                       | 656 ms: 1.29x faster                                        |
| async_tree_io_tg           | 831 ms                                                       | 653 ms: 1.27x faster                                        |
| async_tree_none_tg         | 346 ms                                                       | 287 ms: 1.21x faster                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 521 ms: 1.16x faster                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 526 ms: 1.10x faster                                        |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                        |
| async_generators           | 457 ms                                                       | 453 ms: 1.01x faster                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                       |
| Geometric mean             | (ref)                                                        | 1.17x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 257 ms: 1.02x slower                                        |
| float          | 81.3 ms                                                      | 94.0 ms: 1.16x slower                                       |
| nbody          | 89.3 ms                                                      | 159 ms: 1.78x slower                                        |
| Geometric mean | (ref)                                                        | 1.28x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 222 ms: 1.11x faster                                        |
| regex_v8       | 26.1 ms                                                      | 24.1 ms: 1.09x faster                                       |
| regex_effbot   | 3.67 ms                                                      | 3.66 ms: 1.00x faster                                       |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                       |
| xml_etree_parse      | 150 ms                                                       | 148 ms: 1.02x faster                                        |
| json_loads           | 24.7 us                                                      | 25.8 us: 1.04x slower                                       |
| xml_etree_iterparse  | 103 ms                                                       | 108 ms: 1.05x slower                                        |
| tomli_loads          | 2.46 sec                                                     | 2.81 sec: 1.14x slower                                      |
| xml_etree_process    | 61.2 ms                                                      | 71.1 ms: 1.16x slower                                       |
| xml_etree_generate   | 86.5 ms                                                      | 102 ms: 1.18x slower                                        |
| pickle_pure_python   | 323 us                                                       | 400 us: 1.24x slower                                        |
| unpickle_pure_python | 217 us                                                       | 338 us: 1.56x slower                                        |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.84 ms: 1.01x faster                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                       |
| django_template | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                       |
| genshi_xml      | 57.1 ms                                                      | 58.0 ms: 1.02x slower                                       |
| mako            | 10.4 ms                                                      | 15.3 ms: 1.47x slower                                       |
| Geometric mean  | (ref)                                                        | 1.08x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.42 sec: 1.79x faster                                      |
| deepcopy_memo              | 38.6 us                                                      | 28.0 us: 1.38x faster                                       |
| deepcopy                   | 392 us                                                       | 286 us: 1.37x faster                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 350 ms: 1.33x faster                                        |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                        |
| async_tree_memoization     | 453 ms                                                       | 352 ms: 1.29x faster                                        |
| async_tree_io              | 843 ms                                                       | 656 ms: 1.29x faster                                        |
| async_tree_io_tg           | 831 ms                                                       | 653 ms: 1.27x faster                                        |
| async_tree_none_tg         | 346 ms                                                       | 287 ms: 1.21x faster                                        |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.18x faster                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 521 ms: 1.16x faster                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.07 us: 1.15x faster                                       |
| generators                 | 33.6 ms                                                      | 29.2 ms: 1.15x faster                                       |
| regex_dna                  | 247 ms                                                       | 222 ms: 1.11x faster                                        |
| dulwich_log                | 68.2 ms                                                      | 61.5 ms: 1.11x faster                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 526 ms: 1.10x faster                                        |
| json_dumps                 | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                       |
| thrift                     | 901 us                                                       | 828 us: 1.09x faster                                        |
| regex_v8                   | 26.1 ms                                                      | 24.1 ms: 1.09x faster                                       |
| logging_simple             | 6.39 us                                                      | 5.91 us: 1.08x faster                                       |
| logging_silent             | 97.9 ns                                                      | 92.0 ns: 1.06x faster                                       |
| genshi_text                | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                       |
| pathlib                    | 17.5 ms                                                      | 16.6 ms: 1.06x faster                                       |
| logging_format             | 6.94 us                                                      | 6.58 us: 1.06x faster                                       |
| html5lib                   | 73.5 ms                                                      | 70.2 ms: 1.05x faster                                       |
| json                       | 5.69 ms                                                      | 5.46 ms: 1.04x faster                                       |
| django_template            | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                       |
| scimark_lu                 | 98.7 ms                                                      | 95.1 ms: 1.04x faster                                       |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                       |
| xml_etree_parse            | 150 ms                                                       | 148 ms: 1.02x faster                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.84 ms: 1.01x faster                                       |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                        |
| async_generators           | 457 ms                                                       | 453 ms: 1.01x faster                                        |
| regex_effbot               | 3.67 ms                                                      | 3.66 ms: 1.00x faster                                       |
| sympy_integrate            | 23.6 ms                                                      | 23.6 ms: 1.00x slower                                       |
| richards_super             | 59.6 ms                                                      | 60.1 ms: 1.01x slower                                       |
| richards                   | 52.9 ms                                                      | 53.5 ms: 1.01x slower                                       |
| sphinx                     | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                      |
| sqlite_synth               | 2.91 us                                                      | 2.95 us: 1.01x slower                                       |
| genshi_xml                 | 57.1 ms                                                      | 58.0 ms: 1.02x slower                                       |
| pidigits                   | 252 ms                                                       | 257 ms: 1.02x slower                                        |
| coverage                   | 80.0 ms                                                      | 81.9 ms: 1.02x slower                                       |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                       |
| chaos                      | 60.2 ms                                                      | 62.0 ms: 1.03x slower                                       |
| sympy_sum                  | 155 ms                                                       | 161 ms: 1.04x slower                                        |
| k_core                     | 2.17 sec                                                     | 2.26 sec: 1.04x slower                                      |
| json_loads                 | 24.7 us                                                      | 25.8 us: 1.04x slower                                       |
| xml_etree_iterparse        | 103 ms                                                       | 108 ms: 1.05x slower                                        |
| sympy_str                  | 298 ms                                                       | 315 ms: 1.05x slower                                        |
| shortest_path              | 460 ms                                                       | 487 ms: 1.06x slower                                        |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.89 ms: 1.08x slower                                       |
| sympy_expand               | 509 ms                                                       | 553 ms: 1.09x slower                                        |
| 2to3                       | 293 ms                                                       | 320 ms: 1.09x slower                                        |
| connected_components       | 432 ms                                                       | 475 ms: 1.10x slower                                        |
| nqueens                    | 90.7 ms                                                      | 99.6 ms: 1.10x slower                                       |
| docutils                   | 2.83 sec                                                     | 3.11 sec: 1.10x slower                                      |
| pyflate                    | 503 ms                                                       | 560 ms: 1.11x slower                                        |
| tomli_loads                | 2.46 sec                                                     | 2.81 sec: 1.14x slower                                      |
| typing_runtime_protocols   | 169 us                                                       | 193 us: 1.14x slower                                        |
| meteor_contest             | 130 ms                                                       | 149 ms: 1.15x slower                                        |
| float                      | 81.3 ms                                                      | 94.0 ms: 1.16x slower                                       |
| xml_etree_process          | 61.2 ms                                                      | 71.1 ms: 1.16x slower                                       |
| xml_etree_generate         | 86.5 ms                                                      | 102 ms: 1.18x slower                                        |
| pycparser                  | 1.24 sec                                                     | 1.47 sec: 1.18x slower                                      |
| raytrace                   | 273 ms                                                       | 323 ms: 1.18x slower                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.03 sec: 1.19x slower                                      |
| pprint_pformat             | 1.72 sec                                                     | 2.08 sec: 1.21x slower                                      |
| pprint_safe_repr           | 843 ms                                                       | 1.03 sec: 1.22x slower                                      |
| pickle_pure_python         | 323 us                                                       | 400 us: 1.24x slower                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 82.3 ms: 1.24x slower                                       |
| go                         | 162 ms                                                       | 202 ms: 1.24x slower                                        |
| scimark_fft                | 328 ms                                                       | 425 ms: 1.30x slower                                        |
| crypto_pyaes               | 73.3 ms                                                      | 98.4 ms: 1.34x slower                                       |
| many_optionals             | 930 us                                                       | 1.28 ms: 1.38x slower                                       |
| gc_traversal               | 4.74 ms                                                      | 6.73 ms: 1.42x slower                                       |
| mako                       | 10.4 ms                                                      | 15.3 ms: 1.47x slower                                       |
| hexiom                     | 6.55 ms                                                      | 9.70 ms: 1.48x slower                                       |
| spectral_norm              | 97.0 ms                                                      | 147 ms: 1.52x slower                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 7.36 ms: 1.54x slower                                       |
| fannkuch                   | 363 ms                                                       | 562 ms: 1.55x slower                                        |
| deltablue                  | 3.42 ms                                                      | 5.30 ms: 1.55x slower                                       |
| unpickle_pure_python       | 217 us                                                       | 338 us: 1.56x slower                                        |
| comprehensions             | 17.0 us                                                      | 27.4 us: 1.61x slower                                       |
| nbody                      | 89.3 ms                                                      | 159 ms: 1.78x slower                                        |
| subparsers                 | 17.5 ms                                                      | 43.5 ms: 2.49x slower                                       |
| telco                      | 8.79 ms                                                      | 161 ms: 18.29x slower                                       |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                |

Benchmark hidden because not significant (2): pylint, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250819-3.15.0a0-d22a745-PYTHON_UOPS/bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.093x slower

# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x