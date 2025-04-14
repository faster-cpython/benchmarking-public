# Results vs. 3.13.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-x86_64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 69.3 ms: 1.06x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 312 ms: 1.50x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 321 ms: 1.41x faster                                                         |
| async_tree_none            | 376 ms                                                       | 266 ms: 1.41x faster                                                         |
| async_tree_io              | 843 ms                                                       | 609 ms: 1.38x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 611 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 259 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 494 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 482 ms: 1.21x faster                                                         |
| async_generators           | 457 ms                                                       | 402 ms: 1.14x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.0 ms: 1.08x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.1 ms: 1.16x faster                                                        |
| nbody          | 89.3 ms                                                      | 91.2 ms: 1.02x slower                                                        |
| pidigits       | 252 ms                                                       | 261 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 2.52 ms: 1.46x faster                                                        |
| regex_dna      | 247 ms                                                       | 192 ms: 1.28x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 24.3 ms: 1.07x faster                                                        |
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 124 ms: 1.21x faster                                                         |
| tomli_loads          | 2.46 sec                                                     | 2.18 sec: 1.13x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 91.8 ms: 1.12x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 80.6 ms: 1.07x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 57.1 ms: 1.07x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 216 us: 1.00x faster                                                         |
| pickle_pure_python   | 323 us                                                       | 325 us: 1.00x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.16 ms: 1.02x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.2 ms: 1.08x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 55.6 ms: 1.03x faster                                                        |
| django_template | 36.4 ms                                                      | 37.2 ms: 1.02x slower                                                        |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 312 ms: 1.50x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 2.52 ms: 1.46x faster                                                        |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 321 ms: 1.41x faster                                                         |
| async_tree_none            | 376 ms                                                       | 266 ms: 1.41x faster                                                         |
| async_tree_io              | 843 ms                                                       | 609 ms: 1.38x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 611 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 259 ms: 1.34x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 28.9 us: 1.34x faster                                                        |
| regex_dna                  | 247 ms                                                       | 192 ms: 1.28x faster                                                         |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.86 us: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 494 ms: 1.22x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 124 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 482 ms: 1.21x faster                                                         |
| generators                 | 33.6 ms                                                      | 28.1 ms: 1.20x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 56.5 ms: 1.17x faster                                                        |
| pyflate                    | 503 ms                                                       | 431 ms: 1.17x faster                                                         |
| float                      | 81.3 ms                                                      | 70.1 ms: 1.16x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.59 ms: 1.16x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 83.8 ms: 1.16x faster                                                        |
| scimark_fft                | 328 ms                                                       | 284 ms: 1.16x faster                                                         |
| richards                   | 52.9 ms                                                      | 46.3 ms: 1.14x faster                                                        |
| meteor_contest             | 130 ms                                                       | 114 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 402 ms: 1.14x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.18 sec: 1.13x faster                                                       |
| scimark_sor                | 123 ms                                                       | 109 ms: 1.13x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 91.8 ms: 1.12x faster                                                        |
| richards_super             | 59.6 ms                                                      | 53.2 ms: 1.12x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.55 sec: 1.12x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.54 sec: 1.12x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 757 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.38 ms: 1.09x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.03 ms: 1.09x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.2 ms: 1.08x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.0 ms: 1.08x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.3 ms: 1.07x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 80.6 ms: 1.07x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 57.1 ms: 1.07x faster                                                        |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 69.3 ms: 1.06x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.6 ms: 1.06x faster                                                        |
| fannkuch                   | 363 ms                                                       | 346 ms: 1.05x faster                                                         |
| mdp                        | 2.54 sec                                                     | 2.43 sec: 1.04x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                         |
| thrift                     | 901 us                                                       | 865 us: 1.04x faster                                                         |
| connected_components       | 432 ms                                                       | 418 ms: 1.03x faster                                                         |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 88.2 ms: 1.03x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                       |
| deltablue                  | 3.42 ms                                                      | 3.33 ms: 1.03x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 55.6 ms: 1.03x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.01x faster                                                         |
| 2to3                       | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| comprehensions             | 17.0 us                                                      | 16.8 us: 1.01x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 58.9 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 216 us: 1.00x faster                                                         |
| sympy_expand               | 509 ms                                                       | 507 ms: 1.00x faster                                                         |
| chaos                      | 60.2 ms                                                      | 60.5 ms: 1.00x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 325 us: 1.00x slower                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.7 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.80 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 121 ms: 1.01x slower                                                         |
| dulwich_log                | 68.2 ms                                                      | 69.2 ms: 1.02x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 157 ms: 1.02x slower                                                         |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                                       |
| nbody                      | 89.3 ms                                                      | 91.2 ms: 1.02x slower                                                        |
| django_template            | 36.4 ms                                                      | 37.2 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 9.16 ms: 1.02x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                        |
| pidigits                   | 252 ms                                                       | 261 ms: 1.03x slower                                                         |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.66 us: 1.04x slower                                                        |
| coverage                   | 80.0 ms                                                      | 83.3 ms: 1.04x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.80 ms: 1.04x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 77.6 ms: 1.06x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.00 ms: 1.06x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.40 us: 1.07x slower                                                        |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.09x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 5.46 ms: 1.15x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 23.1 ms: 1.32x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 853 ms: 166.58x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (8): json, logging_silent, json_dumps, sqlalchemy_imperative, sqlglot_parse, raytrace, sympy_str, json_loads
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x