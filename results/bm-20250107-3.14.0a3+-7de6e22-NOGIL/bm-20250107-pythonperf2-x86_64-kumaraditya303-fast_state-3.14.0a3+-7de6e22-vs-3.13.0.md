# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.167x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 383 ms: 1.31x slower                                                       |
| docutils       | 2.83 sec                                                     | 3.15 sec: 1.11x slower                                                     |
| html5lib       | 73.5 ms                                                      | 93.8 ms: 1.28x slower                                                      |
| sphinx         | 1.12 sec                                                     | 1.24 sec: 1.11x slower                                                     |
| Geometric mean | (ref)                                                        | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 405 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 831 ms                                                       | 728 ms: 1.14x faster                                                       |
| async_tree_io              | 843 ms                                                       | 765 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 315 ms: 1.10x faster                                                       |
| async_tree_none            | 376 ms                                                       | 357 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 566 ms: 1.03x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 442 ms: 1.03x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 379 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 605 ms: 1.00x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 23.3 ms: 1.08x slower                                                      |
| async_generators           | 457 ms                                                       | 515 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 248 ms: 1.02x faster                                                       |
| float          | 81.3 ms                                                      | 104 ms: 1.28x slower                                                       |
| nbody          | 89.3 ms                                                      | 132 ms: 1.48x slower                                                       |
| Geometric mean | (ref)                                                        | 1.23x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.31 ms: 1.11x faster                                                      |
| regex_dna      | 247 ms                                                       | 251 ms: 1.02x slower                                                       |
| regex_compile  | 143 ms                                                       | 172 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 91.3 ms: 1.13x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                       |
| tomli_loads          | 2.46 sec                                                     | 2.62 sec: 1.07x slower                                                     |
| json_loads           | 24.7 us                                                      | 28.1 us: 1.14x slower                                                      |
| xml_etree_generate   | 86.5 ms                                                      | 100 ms: 1.16x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 75.8 ms: 1.24x slower                                                      |
| json_dumps           | 11.1 ms                                                      | 14.4 ms: 1.30x slower                                                      |
| unpickle_pure_python | 217 us                                                       | 325 us: 1.50x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 514 us: 1.59x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                      |
| python_startup_no_site | 8.96 ms                                                      | 12.0 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 67.8 ms: 1.19x slower                                                      |
| genshi_text     | 26.2 ms                                                      | 33.0 ms: 1.26x slower                                                      |
| django_template | 36.4 ms                                                      | 53.4 ms: 1.47x slower                                                      |
| mako            | 10.4 ms                                                      | 19.4 ms: 1.87x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.42x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 3.81 ms: 1.24x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 405 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 831 ms                                                       | 728 ms: 1.14x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 91.3 ms: 1.13x faster                                                      |
| deepcopy                   | 392 us                                                       | 348 us: 1.12x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.31 ms: 1.11x faster                                                      |
| async_tree_io              | 843 ms                                                       | 765 ms: 1.10x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.64 us: 1.10x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 315 ms: 1.10x faster                                                       |
| async_tree_none            | 376 ms                                                       | 357 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 566 ms: 1.03x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 442 ms: 1.03x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                      |
| asyncio_websockets         | 388 ms                                                       | 379 ms: 1.02x faster                                                       |
| pidigits                   | 252 ms                                                       | 248 ms: 1.02x faster                                                       |
| json                       | 5.69 ms                                                      | 5.59 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 605 ms: 1.00x slower                                                       |
| deepcopy_memo              | 38.6 us                                                      | 39.2 us: 1.02x slower                                                      |
| regex_dna                  | 247 ms                                                       | 251 ms: 1.02x slower                                                       |
| scimark_fft                | 328 ms                                                       | 345 ms: 1.05x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.84 ms: 1.06x slower                                                      |
| tomli_loads                | 2.46 sec                                                     | 2.62 sec: 1.07x slower                                                     |
| deepcopy_reduce            | 3.54 us                                                      | 3.78 us: 1.07x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 23.3 ms: 1.08x slower                                                      |
| telco                      | 8.79 ms                                                      | 9.52 ms: 1.08x slower                                                      |
| spectral_norm              | 97.0 ms                                                      | 105 ms: 1.09x slower                                                       |
| pylint                     | 347 ms                                                       | 380 ms: 1.10x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.24 sec: 1.11x slower                                                     |
| bpe_tokeniser              | 5.09 sec                                                     | 5.63 sec: 1.11x slower                                                     |
| docutils                   | 2.83 sec                                                     | 3.15 sec: 1.11x slower                                                     |
| async_generators           | 457 ms                                                       | 515 ms: 1.13x slower                                                       |
| k_core                     | 2.17 sec                                                     | 2.46 sec: 1.13x slower                                                     |
| mdp                        | 2.54 sec                                                     | 2.88 sec: 1.13x slower                                                     |
| json_loads                 | 24.7 us                                                      | 28.1 us: 1.14x slower                                                      |
| dulwich_log                | 68.2 ms                                                      | 78.3 ms: 1.15x slower                                                      |
| generators                 | 33.6 ms                                                      | 38.7 ms: 1.15x slower                                                      |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.51 ms: 1.15x slower                                                      |
| xml_etree_generate         | 86.5 ms                                                      | 100 ms: 1.16x slower                                                       |
| connected_components       | 432 ms                                                       | 502 ms: 1.16x slower                                                       |
| shortest_path              | 460 ms                                                       | 537 ms: 1.17x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.45 sec: 1.17x slower                                                     |
| sympy_expand               | 509 ms                                                       | 599 ms: 1.18x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 183 ms: 1.18x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 67.8 ms: 1.19x slower                                                      |
| python_startup             | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                      |
| meteor_contest             | 130 ms                                                       | 156 ms: 1.20x slower                                                       |
| sympy_str                  | 298 ms                                                       | 359 ms: 1.20x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 28.5 ms: 1.21x slower                                                      |
| regex_compile              | 143 ms                                                       | 172 ms: 1.21x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 145 ms: 1.22x slower                                                       |
| sqlglot_optimize           | 59.3 ms                                                      | 72.6 ms: 1.22x slower                                                      |
| thrift                     | 901 us                                                       | 1.11 ms: 1.23x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 1.04 sec: 1.23x slower                                                     |
| xml_etree_process          | 61.2 ms                                                      | 75.8 ms: 1.24x slower                                                      |
| sqlalchemy_imperative      | 18.3 ms                                                      | 22.7 ms: 1.24x slower                                                      |
| nqueens                    | 90.7 ms                                                      | 113 ms: 1.24x slower                                                       |
| many_optionals             | 930 us                                                       | 1.16 ms: 1.25x slower                                                      |
| genshi_text                | 26.2 ms                                                      | 33.0 ms: 1.26x slower                                                      |
| pprint_pformat             | 1.72 sec                                                     | 2.17 sec: 1.26x slower                                                     |
| html5lib                   | 73.5 ms                                                      | 93.8 ms: 1.28x slower                                                      |
| float                      | 81.3 ms                                                      | 104 ms: 1.28x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 14.4 ms: 1.30x slower                                                      |
| pyflate                    | 503 ms                                                       | 654 ms: 1.30x slower                                                       |
| richards_super             | 59.6 ms                                                      | 77.9 ms: 1.31x slower                                                      |
| 2to3                       | 293 ms                                                       | 383 ms: 1.31x slower                                                       |
| coverage                   | 80.0 ms                                                      | 106 ms: 1.32x slower                                                       |
| richards                   | 52.9 ms                                                      | 70.0 ms: 1.32x slower                                                      |
| python_startup_no_site     | 8.96 ms                                                      | 12.0 ms: 1.34x slower                                                      |
| scimark_lu                 | 98.7 ms                                                      | 133 ms: 1.35x slower                                                       |
| sqlalchemy_declarative     | 148 ms                                                       | 201 ms: 1.35x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 99.2 ms: 1.35x slower                                                      |
| logging_simple             | 6.39 us                                                      | 8.72 us: 1.36x slower                                                      |
| typing_runtime_protocols   | 169 us                                                       | 231 us: 1.37x slower                                                       |
| logging_format             | 6.94 us                                                      | 9.59 us: 1.38x slower                                                      |
| fannkuch                   | 363 ms                                                       | 516 ms: 1.42x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 9.32 ms: 1.42x slower                                                      |
| django_template            | 36.4 ms                                                      | 53.4 ms: 1.47x slower                                                      |
| nbody                      | 89.3 ms                                                      | 132 ms: 1.48x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 325 us: 1.50x slower                                                       |
| go                         | 162 ms                                                       | 245 ms: 1.51x slower                                                       |
| scimark_sor                | 123 ms                                                       | 194 ms: 1.58x slower                                                       |
| sqlglot_transpile          | 1.79 ms                                                      | 2.82 ms: 1.58x slower                                                      |
| pickle_pure_python         | 323 us                                                       | 514 us: 1.59x slower                                                       |
| comprehensions             | 17.0 us                                                      | 27.2 us: 1.60x slower                                                      |
| chaos                      | 60.2 ms                                                      | 96.4 ms: 1.60x slower                                                      |
| subparsers                 | 17.5 ms                                                      | 28.3 ms: 1.62x slower                                                      |
| bench_thread_pool          | 942 us                                                       | 1.55 ms: 1.64x slower                                                      |
| scimark_monte_carlo        | 66.1 ms                                                      | 109 ms: 1.65x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 164 ns: 1.68x slower                                                       |
| sqlglot_parse              | 1.40 ms                                                      | 2.35 ms: 1.68x slower                                                      |
| raytrace                   | 273 ms                                                       | 471 ms: 1.73x slower                                                       |
| mako                       | 10.4 ms                                                      | 19.4 ms: 1.87x slower                                                      |
| deltablue                  | 3.42 ms                                                      | 7.14 ms: 2.09x slower                                                      |
| bench_mp_pool              | 5.12 ms                                                      | 52.5 ms: 10.24x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.23x slower                                                               |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: mypy2

- Geometric mean (including insignificant results): 1.167x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.22x