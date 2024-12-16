# Results vs. 3.13.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: linux-x86_64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.027x faster
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.99 sec: 1.06x slower                                                       |
| html5lib       | 73.5 ms                                                      | 71.5 ms: 1.03x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.16 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 637 ms: 1.31x faster                                                         |
| async_tree_io              | 843 ms                                                       | 653 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 293 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 275 ms: 1.26x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 361 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 524 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| async_generators           | 457 ms                                                       | 465 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 72.8 ms: 1.12x faster                                                        |
| pidigits       | 252 ms                                                       | 251 ms: 1.01x faster                                                         |
| nbody          | 89.3 ms                                                      | 90.8 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.24 ms: 1.13x faster                                                        |
| regex_dna      | 247 ms                                                       | 234 ms: 1.06x faster                                                         |
| regex_compile  | 143 ms                                                       | 138 ms: 1.04x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 25.2 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 94.0 ms: 1.09x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 56.9 ms: 1.07x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 202 us: 1.07x faster                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 80.7 ms: 1.07x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 341 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.38 ms: 1.11x faster                                                        |
| django_template | 36.4 ms                                                      | 39.5 ms: 1.09x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 28.7 ms: 1.09x slower                                                        |
| genshi_xml      | 57.1 ms                                                      | 62.8 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 637 ms: 1.31x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.8 us: 1.30x faster                                                        |
| async_tree_io              | 843 ms                                                       | 653 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 293 ms: 1.28x faster                                                         |
| deepcopy                   | 392 us                                                       | 310 us: 1.26x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 275 ms: 1.26x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 361 ms: 1.26x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                        |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 524 ms: 1.15x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.65 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.24 ms: 1.13x faster                                                        |
| go                         | 162 ms                                                       | 145 ms: 1.12x faster                                                         |
| float                      | 81.3 ms                                                      | 72.8 ms: 1.12x faster                                                        |
| pyflate                    | 503 ms                                                       | 451 ms: 1.12x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| mako                       | 10.4 ms                                                      | 9.38 ms: 1.11x faster                                                        |
| richards                   | 52.9 ms                                                      | 48.2 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.65 sec: 1.09x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 94.0 ms: 1.09x faster                                                        |
| richards_super             | 59.6 ms                                                      | 54.8 ms: 1.09x faster                                                        |
| json                       | 5.69 ms                                                      | 5.25 ms: 1.08x faster                                                        |
| scimark_fft                | 328 ms                                                       | 305 ms: 1.08x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 56.9 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 202 us: 1.07x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 80.7 ms: 1.07x faster                                                        |
| connected_components       | 432 ms                                                       | 404 ms: 1.07x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 797 ms: 1.06x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.05 sec: 1.06x faster                                                       |
| regex_dna                  | 247 ms                                                       | 234 ms: 1.06x faster                                                         |
| shortest_path              | 460 ms                                                       | 437 ms: 1.05x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.9 ms: 1.05x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                                        |
| pylint                     | 347 ms                                                       | 331 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.65 sec: 1.04x faster                                                       |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 93.6 ms: 1.04x faster                                                        |
| regex_compile              | 143 ms                                                       | 138 ms: 1.04x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 25.2 ms: 1.03x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.31 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 71.5 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                        |
| thrift                     | 901 us                                                       | 883 us: 1.02x faster                                                         |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                       |
| 2to3                       | 293 ms                                                       | 290 ms: 1.01x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 67.7 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 251 ms: 1.01x faster                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.42 ms: 1.01x slower                                                        |
| nbody                      | 89.3 ms                                                      | 90.8 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.82 ms: 1.02x slower                                                        |
| async_generators           | 457 ms                                                       | 465 ms: 1.02x slower                                                         |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                        |
| coverage                   | 80.0 ms                                                      | 81.5 ms: 1.02x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 24.0 ms: 1.02x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 158 ms: 1.02x slower                                                         |
| sympy_expand               | 509 ms                                                       | 521 ms: 1.02x slower                                                         |
| sympy_str                  | 298 ms                                                       | 305 ms: 1.02x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.60 sec: 1.02x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 75.3 ms: 1.03x slower                                                        |
| sphinx                     | 1.12 sec                                                     | 1.16 sec: 1.03x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 101 ns: 1.03x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 970 us: 1.03x slower                                                         |
| logging_simple             | 6.39 us                                                      | 6.60 us: 1.03x slower                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 61.3 ms: 1.03x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.23 us: 1.04x slower                                                        |
| fannkuch                   | 363 ms                                                       | 379 ms: 1.04x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 125 ms: 1.05x slower                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.02 ms: 1.05x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 341 us: 1.06x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.99 sec: 1.06x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 7.08 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 183 us: 1.08x slower                                                         |
| django_template            | 36.4 ms                                                      | 39.5 ms: 1.09x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 28.7 ms: 1.09x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 62.8 ms: 1.10x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 101 ms: 1.12x slower                                                         |
| comprehensions             | 17.0 us                                                      | 19.0 us: 1.12x slower                                                        |
| chaos                      | 60.2 ms                                                      | 67.6 ms: 1.12x slower                                                        |
| many_optionals             | 930 us                                                       | 1.06 ms: 1.14x slower                                                        |
| generators                 | 33.6 ms                                                      | 39.8 ms: 1.18x slower                                                        |
| raytrace                   | 273 ms                                                       | 338 ms: 1.24x slower                                                         |
| gc_traversal               | 4.74 ms                                                      | 6.31 ms: 1.33x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 23.9 ms: 1.37x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.10 sec: 215.24x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (6): djangocms, asyncio_websockets, meteor_contest, scimark_lu, json_dumps, create_gc_cycles
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: mypy2

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 99.11% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x