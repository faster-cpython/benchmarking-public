# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.030x faster
- HPT reliability: 99.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.98 sec: 1.06x slower                                                       |
| html5lib       | 73.5 ms                                                      | 70.4 ms: 1.04x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.16 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 329 ms: 1.42x faster                                                         |
| async_tree_io              | 843 ms                                                       | 648 ms: 1.30x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 640 ms: 1.30x faster                                                         |
| async_tree_none            | 376 ms                                                       | 293 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 519 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 500 ms: 1.16x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| async_generators           | 457 ms                                                       | 465 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 72.9 ms: 1.12x faster                                                        |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| nbody          | 89.3 ms                                                      | 92.2 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.31 ms: 1.11x faster                                                        |
| regex_dna      | 247 ms                                                       | 235 ms: 1.05x faster                                                         |
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 94.0 ms: 1.09x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 200 us: 1.08x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 56.5 ms: 1.08x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 80.2 ms: 1.08x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 338 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.38 ms: 1.11x faster                                                        |
| genshi_text     | 26.2 ms                                                      | 28.0 ms: 1.07x slower                                                        |
| genshi_xml      | 57.1 ms                                                      | 62.0 ms: 1.09x slower                                                        |
| django_template | 36.4 ms                                                      | 40.2 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 329 ms: 1.42x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 28.5 us: 1.36x faster                                                        |
| deepcopy                   | 392 us                                                       | 295 us: 1.33x faster                                                         |
| async_tree_io              | 843 ms                                                       | 648 ms: 1.30x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 640 ms: 1.30x faster                                                         |
| async_tree_none            | 376 ms                                                       | 293 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                       |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.21x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 3.00 us: 1.18x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.53 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 519 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 500 ms: 1.16x faster                                                         |
| pyflate                    | 503 ms                                                       | 438 ms: 1.15x faster                                                         |
| float                      | 81.3 ms                                                      | 72.9 ms: 1.12x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.31 ms: 1.11x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.38 ms: 1.11x faster                                                        |
| go                         | 162 ms                                                       | 147 ms: 1.10x faster                                                         |
| json                       | 5.69 ms                                                      | 5.16 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.65 sec: 1.10x faster                                                       |
| richards                   | 52.9 ms                                                      | 48.4 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 94.0 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 200 us: 1.08x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 56.5 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 80.2 ms: 1.08x faster                                                        |
| scimark_fft                | 328 ms                                                       | 304 ms: 1.08x faster                                                         |
| richards_super             | 59.6 ms                                                      | 55.8 ms: 1.07x faster                                                        |
| connected_components       | 432 ms                                                       | 406 ms: 1.06x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.05 sec: 1.06x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 91.9 ms: 1.06x faster                                                        |
| regex_dna                  | 247 ms                                                       | 235 ms: 1.05x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.1 ms: 1.05x faster                                                        |
| shortest_path              | 460 ms                                                       | 439 ms: 1.05x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.8 ms: 1.05x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 70.4 ms: 1.04x faster                                                        |
| coverage                   | 80.0 ms                                                      | 76.8 ms: 1.04x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 811 ms: 1.04x faster                                                         |
| pylint                     | 347 ms                                                       | 334 ms: 1.04x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.30 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.68 sec: 1.02x faster                                                       |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                        |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                         |
| 2to3                       | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| thrift                     | 901 us                                                       | 889 us: 1.01x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 98.2 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 157 ms: 1.02x slower                                                         |
| async_generators           | 457 ms                                                       | 465 ms: 1.02x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.59 sec: 1.02x slower                                                       |
| sympy_expand               | 509 ms                                                       | 519 ms: 1.02x slower                                                         |
| logging_simple             | 6.39 us                                                      | 6.53 us: 1.02x slower                                                        |
| sympy_str                  | 298 ms                                                       | 305 ms: 1.02x slower                                                         |
| logging_silent             | 97.9 ns                                                      | 100 ns: 1.02x slower                                                         |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 24.1 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.83 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.43 ms: 1.02x slower                                                        |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.03x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 75.4 ms: 1.03x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.15 us: 1.03x slower                                                        |
| fannkuch                   | 363 ms                                                       | 374 ms: 1.03x slower                                                         |
| sphinx                     | 1.12 sec                                                     | 1.16 sec: 1.03x slower                                                       |
| nbody                      | 89.3 ms                                                      | 92.2 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 124 ms: 1.04x slower                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 61.9 ms: 1.05x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 338 us: 1.05x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.98 sec: 1.06x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 28.0 ms: 1.07x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.13 ms: 1.07x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.02 ms: 1.08x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 62.0 ms: 1.09x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 184 us: 1.09x slower                                                         |
| hexiom                     | 6.55 ms                                                      | 7.13 ms: 1.09x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 99.4 ms: 1.10x slower                                                        |
| django_template            | 36.4 ms                                                      | 40.2 ms: 1.11x slower                                                        |
| comprehensions             | 17.0 us                                                      | 18.9 us: 1.11x slower                                                        |
| chaos                      | 60.2 ms                                                      | 66.8 ms: 1.11x slower                                                        |
| many_optionals             | 930 us                                                       | 1.07 ms: 1.15x slower                                                        |
| generators                 | 33.6 ms                                                      | 39.3 ms: 1.17x slower                                                        |
| raytrace                   | 273 ms                                                       | 330 ms: 1.21x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 23.4 ms: 1.34x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.53 ms: 1.38x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.01 sec: 196.49x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (7): regex_v8, pycparser, dulwich_log, djangocms, asyncio_websockets, json_dumps, create_gc_cycles
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 99.09% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x