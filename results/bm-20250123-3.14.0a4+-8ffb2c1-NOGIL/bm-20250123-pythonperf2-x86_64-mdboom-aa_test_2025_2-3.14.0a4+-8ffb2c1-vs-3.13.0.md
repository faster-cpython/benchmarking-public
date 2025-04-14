# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.064x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 337 ms: 1.15x slower                                                   |
| docutils       | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                                 |
| sphinx         | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                                 |
| Geometric mean | (ref)                                                        | 1.07x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 568 ms: 1.46x faster                                                   |
| async_tree_memoization_tg  | 466 ms                                                       | 319 ms: 1.46x faster                                                   |
| async_tree_none_tg         | 346 ms                                                       | 247 ms: 1.40x faster                                                   |
| async_tree_io              | 843 ms                                                       | 608 ms: 1.39x faster                                                   |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                   |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 485 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 525 ms: 1.15x faster                                                   |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                   |
| async_generators           | 457 ms                                                       | 466 ms: 1.02x slower                                                   |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 76.0 ms: 1.07x faster                                                  |
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                   |
| nbody          | 89.3 ms                                                      | 134 ms: 1.50x slower                                                   |
| Geometric mean | (ref)                                                        | 1.11x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.27 ms: 1.12x faster                                                  |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                   |
| regex_compile  | 143 ms                                                       | 155 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 91.2 ms: 1.13x faster                                                  |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                   |
| tomli_loads          | 2.46 sec                                                     | 2.40 sec: 1.03x faster                                                 |
| xml_etree_generate   | 86.5 ms                                                      | 98.4 ms: 1.14x slower                                                  |
| json_loads           | 24.7 us                                                      | 28.4 us: 1.15x slower                                                  |
| unpickle_pure_python | 217 us                                                       | 254 us: 1.17x slower                                                   |
| json_dumps           | 11.1 ms                                                      | 13.4 ms: 1.20x slower                                                  |
| pickle_pure_python   | 323 us                                                       | 392 us: 1.21x slower                                                   |
| xml_etree_process    | 61.2 ms                                                      | 74.4 ms: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 18.7 ms: 1.17x slower                                                  |
| python_startup_no_site | 8.96 ms                                                      | 11.7 ms: 1.31x slower                                                  |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 65.2 ms: 1.14x slower                                                  |
| genshi_text     | 26.2 ms                                                      | 30.6 ms: 1.17x slower                                                  |
| django_template | 36.4 ms                                                      | 46.3 ms: 1.27x slower                                                  |
| mako            | 10.4 ms                                                      | 17.7 ms: 1.71x slower                                                  |
| Geometric mean  | (ref)                                                        | 1.31x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 568 ms: 1.46x faster                                                   |
| async_tree_memoization_tg  | 466 ms                                                       | 319 ms: 1.46x faster                                                   |
| async_tree_none_tg         | 346 ms                                                       | 247 ms: 1.40x faster                                                   |
| async_tree_io              | 843 ms                                                       | 608 ms: 1.39x faster                                                   |
| create_gc_cycles           | 2.68 ms                                                      | 1.99 ms: 1.34x faster                                                  |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                   |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 485 ms: 1.20x faster                                                   |
| deepcopy                   | 392 us                                                       | 335 us: 1.17x faster                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 525 ms: 1.15x faster                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 91.2 ms: 1.13x faster                                                  |
| sqlite_synth               | 2.91 us                                                      | 2.58 us: 1.12x faster                                                  |
| regex_effbot               | 3.67 ms                                                      | 3.27 ms: 1.12x faster                                                  |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                   |
| go                         | 162 ms                                                       | 149 ms: 1.09x faster                                                   |
| pathlib                    | 17.5 ms                                                      | 16.2 ms: 1.08x faster                                                  |
| float                      | 81.3 ms                                                      | 76.0 ms: 1.07x faster                                                  |
| generators                 | 33.6 ms                                                      | 31.4 ms: 1.07x faster                                                  |
| scimark_sor                | 123 ms                                                       | 119 ms: 1.04x faster                                                   |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                   |
| tomli_loads                | 2.46 sec                                                     | 2.40 sec: 1.03x faster                                                 |
| deepcopy_memo              | 38.6 us                                                      | 37.9 us: 1.02x faster                                                  |
| json                       | 5.69 ms                                                      | 5.58 ms: 1.02x faster                                                  |
| pyflate                    | 503 ms                                                       | 494 ms: 1.02x faster                                                   |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                   |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                   |
| async_generators           | 457 ms                                                       | 466 ms: 1.02x slower                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 3.62 us: 1.02x slower                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 5.21 sec: 1.03x slower                                                 |
| scimark_fft                | 328 ms                                                       | 336 ms: 1.03x slower                                                   |
| dulwich_log                | 68.2 ms                                                      | 70.0 ms: 1.03x slower                                                  |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                  |
| telco                      | 8.79 ms                                                      | 9.13 ms: 1.04x slower                                                  |
| pycparser                  | 1.24 sec                                                     | 1.29 sec: 1.04x slower                                                 |
| spectral_norm              | 97.0 ms                                                      | 101 ms: 1.04x slower                                                   |
| gc_traversal               | 4.74 ms                                                      | 4.95 ms: 1.04x slower                                                  |
| docutils                   | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                                 |
| sphinx                     | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                                 |
| sqlglot_normalize          | 119 ms                                                       | 129 ms: 1.08x slower                                                   |
| pprint_safe_repr           | 843 ms                                                       | 915 ms: 1.09x slower                                                   |
| mdp                        | 2.54 sec                                                     | 2.76 sec: 1.09x slower                                                 |
| richards                   | 52.9 ms                                                      | 57.5 ms: 1.09x slower                                                  |
| regex_compile              | 143 ms                                                       | 155 ms: 1.09x slower                                                   |
| pprint_pformat             | 1.72 sec                                                     | 1.89 sec: 1.10x slower                                                 |
| sqlglot_optimize           | 59.3 ms                                                      | 65.3 ms: 1.10x slower                                                  |
| hexiom                     | 6.55 ms                                                      | 7.25 ms: 1.11x slower                                                  |
| k_core                     | 2.17 sec                                                     | 2.40 sec: 1.11x slower                                                 |
| sympy_expand               | 509 ms                                                       | 565 ms: 1.11x slower                                                   |
| richards_super             | 59.6 ms                                                      | 67.0 ms: 1.13x slower                                                  |
| logging_silent             | 97.9 ns                                                      | 110 ns: 1.13x slower                                                   |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.43 ms: 1.14x slower                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 98.4 ms: 1.14x slower                                                  |
| sympy_str                  | 298 ms                                                       | 339 ms: 1.14x slower                                                   |
| sympy_sum                  | 155 ms                                                       | 177 ms: 1.14x slower                                                   |
| connected_components       | 432 ms                                                       | 494 ms: 1.14x slower                                                   |
| genshi_xml                 | 57.1 ms                                                      | 65.2 ms: 1.14x slower                                                  |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.9 ms: 1.14x slower                                                  |
| sqlglot_parse              | 1.40 ms                                                      | 1.60 ms: 1.15x slower                                                  |
| shortest_path              | 460 ms                                                       | 528 ms: 1.15x slower                                                   |
| sympy_integrate            | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                  |
| 2to3                       | 293 ms                                                       | 337 ms: 1.15x slower                                                   |
| json_loads                 | 24.7 us                                                      | 28.4 us: 1.15x slower                                                  |
| chaos                      | 60.2 ms                                                      | 69.8 ms: 1.16x slower                                                  |
| sqlglot_transpile          | 1.79 ms                                                      | 2.08 ms: 1.16x slower                                                  |
| thrift                     | 901 us                                                       | 1.05 ms: 1.16x slower                                                  |
| logging_simple             | 6.39 us                                                      | 7.43 us: 1.16x slower                                                  |
| genshi_text                | 26.2 ms                                                      | 30.6 ms: 1.17x slower                                                  |
| unpickle_pure_python       | 217 us                                                       | 254 us: 1.17x slower                                                   |
| python_startup             | 15.9 ms                                                      | 18.7 ms: 1.17x slower                                                  |
| logging_format             | 6.94 us                                                      | 8.15 us: 1.17x slower                                                  |
| meteor_contest             | 130 ms                                                       | 153 ms: 1.18x slower                                                   |
| sqlalchemy_declarative     | 148 ms                                                       | 177 ms: 1.19x slower                                                   |
| json_dumps                 | 11.1 ms                                                      | 13.4 ms: 1.20x slower                                                  |
| many_optionals             | 930 us                                                       | 1.12 ms: 1.20x slower                                                  |
| pickle_pure_python         | 323 us                                                       | 392 us: 1.21x slower                                                   |
| scimark_lu                 | 98.7 ms                                                      | 120 ms: 1.22x slower                                                   |
| xml_etree_process          | 61.2 ms                                                      | 74.4 ms: 1.22x slower                                                  |
| nqueens                    | 90.7 ms                                                      | 112 ms: 1.24x slower                                                   |
| raytrace                   | 273 ms                                                       | 341 ms: 1.25x slower                                                   |
| crypto_pyaes               | 73.3 ms                                                      | 92.6 ms: 1.26x slower                                                  |
| comprehensions             | 17.0 us                                                      | 21.5 us: 1.26x slower                                                  |
| django_template            | 36.4 ms                                                      | 46.3 ms: 1.27x slower                                                  |
| coverage                   | 80.0 ms                                                      | 103 ms: 1.29x slower                                                   |
| scimark_monte_carlo        | 66.1 ms                                                      | 85.8 ms: 1.30x slower                                                  |
| deltablue                  | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 11.7 ms: 1.31x slower                                                  |
| typing_runtime_protocols   | 169 us                                                       | 226 us: 1.34x slower                                                   |
| fannkuch                   | 363 ms                                                       | 489 ms: 1.35x slower                                                   |
| subparsers                 | 17.5 ms                                                      | 25.6 ms: 1.46x slower                                                  |
| nbody                      | 89.3 ms                                                      | 134 ms: 1.50x slower                                                   |
| bench_thread_pool          | 942 us                                                       | 1.46 ms: 1.55x slower                                                  |
| mako                       | 10.4 ms                                                      | 17.7 ms: 1.71x slower                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 48.9 ms: 9.55x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                           |

Benchmark hidden because not significant (3): regex_v8, html5lib, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.064x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.23x