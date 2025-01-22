# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.061x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 336 ms: 1.15x slower                                                 |
| docutils       | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                               |
| html5lib       | 73.5 ms                                                      | 73.9 ms: 1.01x slower                                                |
| sphinx         | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                               |
| Geometric mean | (ref)                                                        | 1.07x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 320 ms: 1.46x faster                                                 |
| async_tree_io_tg           | 831 ms                                                       | 573 ms: 1.45x faster                                                 |
| async_tree_none_tg         | 346 ms                                                       | 248 ms: 1.39x faster                                                 |
| async_tree_io              | 843 ms                                                       | 609 ms: 1.38x faster                                                 |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                 |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 487 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 527 ms: 1.14x faster                                                 |
| asyncio_websockets         | 388 ms                                                       | 380 ms: 1.02x faster                                                 |
| async_generators           | 457 ms                                                       | 470 ms: 1.03x slower                                                 |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.04x slower                                                |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 74.6 ms: 1.09x faster                                                |
| pidigits       | 252 ms                                                       | 249 ms: 1.02x faster                                                 |
| nbody          | 89.3 ms                                                      | 134 ms: 1.50x slower                                                 |
| Geometric mean | (ref)                                                        | 1.11x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                |
| regex_dna      | 247 ms                                                       | 246 ms: 1.00x faster                                                 |
| regex_compile  | 143 ms                                                       | 156 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 87.8 ms: 1.17x faster                                                |
| xml_etree_parse      | 150 ms                                                       | 132 ms: 1.14x faster                                                 |
| tomli_loads          | 2.46 sec                                                     | 2.42 sec: 1.02x faster                                               |
| json_loads           | 24.7 us                                                      | 27.7 us: 1.12x slower                                                |
| xml_etree_generate   | 86.5 ms                                                      | 97.4 ms: 1.13x slower                                                |
| unpickle_pure_python | 217 us                                                       | 250 us: 1.15x slower                                                 |
| json_dumps           | 11.1 ms                                                      | 13.4 ms: 1.20x slower                                                |
| xml_etree_process    | 61.2 ms                                                      | 74.2 ms: 1.21x slower                                                |
| pickle_pure_python   | 323 us                                                       | 392 us: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 18.7 ms: 1.18x slower                                                |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 63.9 ms: 1.12x slower                                                |
| genshi_text     | 26.2 ms                                                      | 30.2 ms: 1.15x slower                                                |
| django_template | 36.4 ms                                                      | 46.2 ms: 1.27x slower                                                |
| mako            | 10.4 ms                                                      | 18.0 ms: 1.73x slower                                                |
| Geometric mean  | (ref)                                                        | 1.30x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 320 ms: 1.46x faster                                                 |
| async_tree_io_tg           | 831 ms                                                       | 573 ms: 1.45x faster                                                 |
| async_tree_none_tg         | 346 ms                                                       | 248 ms: 1.39x faster                                                 |
| async_tree_io              | 843 ms                                                       | 609 ms: 1.38x faster                                                 |
| create_gc_cycles           | 2.68 ms                                                      | 2.05 ms: 1.31x faster                                                |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                 |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 487 ms: 1.20x faster                                                 |
| deepcopy                   | 392 us                                                       | 332 us: 1.18x faster                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 87.8 ms: 1.17x faster                                                |
| gc_traversal               | 4.74 ms                                                      | 4.09 ms: 1.16x faster                                                |
| regex_effbot               | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 527 ms: 1.14x faster                                                 |
| xml_etree_parse            | 150 ms                                                       | 132 ms: 1.14x faster                                                 |
| sqlite_synth               | 2.91 us                                                      | 2.60 us: 1.12x faster                                                |
| go                         | 162 ms                                                       | 147 ms: 1.11x faster                                                 |
| float                      | 81.3 ms                                                      | 74.6 ms: 1.09x faster                                                |
| pathlib                    | 17.5 ms                                                      | 16.2 ms: 1.08x faster                                                |
| generators                 | 33.6 ms                                                      | 31.7 ms: 1.06x faster                                                |
| deepcopy_memo              | 38.6 us                                                      | 37.4 us: 1.03x faster                                                |
| scimark_sor                | 123 ms                                                       | 119 ms: 1.03x faster                                                 |
| json                       | 5.69 ms                                                      | 5.54 ms: 1.03x faster                                                |
| pyflate                    | 503 ms                                                       | 491 ms: 1.02x faster                                                 |
| asyncio_websockets         | 388 ms                                                       | 380 ms: 1.02x faster                                                 |
| tomli_loads                | 2.46 sec                                                     | 2.42 sec: 1.02x faster                                               |
| pidigits                   | 252 ms                                                       | 249 ms: 1.02x faster                                                 |
| regex_dna                  | 247 ms                                                       | 246 ms: 1.00x faster                                                 |
| html5lib                   | 73.5 ms                                                      | 73.9 ms: 1.01x slower                                                |
| deepcopy_reduce            | 3.54 us                                                      | 3.61 us: 1.02x slower                                                |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                               |
| dulwich_log                | 68.2 ms                                                      | 69.7 ms: 1.02x slower                                                |
| spectral_norm              | 97.0 ms                                                      | 99.4 ms: 1.03x slower                                                |
| telco                      | 8.79 ms                                                      | 9.03 ms: 1.03x slower                                                |
| async_generators           | 457 ms                                                       | 470 ms: 1.03x slower                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 5.25 sec: 1.03x slower                                               |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.04x slower                                                |
| logging_silent             | 97.9 ns                                                      | 102 ns: 1.04x slower                                                 |
| scimark_fft                | 328 ms                                                       | 343 ms: 1.05x slower                                                 |
| docutils                   | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                               |
| sphinx                     | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                               |
| richards                   | 52.9 ms                                                      | 57.1 ms: 1.08x slower                                                |
| sqlglot_normalize          | 119 ms                                                       | 130 ms: 1.09x slower                                                 |
| regex_compile              | 143 ms                                                       | 156 ms: 1.09x slower                                                 |
| mdp                        | 2.54 sec                                                     | 2.77 sec: 1.09x slower                                               |
| pprint_safe_repr           | 843 ms                                                       | 920 ms: 1.09x slower                                                 |
| hexiom                     | 6.55 ms                                                      | 7.24 ms: 1.11x slower                                                |
| sqlglot_optimize           | 59.3 ms                                                      | 65.5 ms: 1.11x slower                                                |
| pprint_pformat             | 1.72 sec                                                     | 1.90 sec: 1.11x slower                                               |
| k_core                     | 2.17 sec                                                     | 2.40 sec: 1.11x slower                                               |
| richards_super             | 59.6 ms                                                      | 66.1 ms: 1.11x slower                                                |
| sympy_expand               | 509 ms                                                       | 570 ms: 1.12x slower                                                 |
| genshi_xml                 | 57.1 ms                                                      | 63.9 ms: 1.12x slower                                                |
| json_loads                 | 24.7 us                                                      | 27.7 us: 1.12x slower                                                |
| xml_etree_generate         | 86.5 ms                                                      | 97.4 ms: 1.13x slower                                                |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.9 ms: 1.14x slower                                                |
| connected_components       | 432 ms                                                       | 494 ms: 1.14x slower                                                 |
| sympy_str                  | 298 ms                                                       | 341 ms: 1.14x slower                                                 |
| sympy_sum                  | 155 ms                                                       | 177 ms: 1.15x slower                                                 |
| 2to3                       | 293 ms                                                       | 336 ms: 1.15x slower                                                 |
| shortest_path              | 460 ms                                                       | 528 ms: 1.15x slower                                                 |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.49 ms: 1.15x slower                                                |
| genshi_text                | 26.2 ms                                                      | 30.2 ms: 1.15x slower                                                |
| thrift                     | 901 us                                                       | 1.04 ms: 1.15x slower                                                |
| unpickle_pure_python       | 217 us                                                       | 250 us: 1.15x slower                                                 |
| sqlglot_parse              | 1.40 ms                                                      | 1.61 ms: 1.15x slower                                                |
| sympy_integrate            | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                                |
| logging_simple             | 6.39 us                                                      | 7.39 us: 1.16x slower                                                |
| sqlglot_transpile          | 1.79 ms                                                      | 2.08 ms: 1.16x slower                                                |
| python_startup             | 15.9 ms                                                      | 18.7 ms: 1.18x slower                                                |
| logging_format             | 6.94 us                                                      | 8.18 us: 1.18x slower                                                |
| chaos                      | 60.2 ms                                                      | 71.1 ms: 1.18x slower                                                |
| sqlalchemy_declarative     | 148 ms                                                       | 177 ms: 1.19x slower                                                 |
| meteor_contest             | 130 ms                                                       | 155 ms: 1.20x slower                                                 |
| json_dumps                 | 11.1 ms                                                      | 13.4 ms: 1.20x slower                                                |
| scimark_lu                 | 98.7 ms                                                      | 119 ms: 1.21x slower                                                 |
| many_optionals             | 930 us                                                       | 1.13 ms: 1.21x slower                                                |
| xml_etree_process          | 61.2 ms                                                      | 74.2 ms: 1.21x slower                                                |
| pickle_pure_python         | 323 us                                                       | 392 us: 1.21x slower                                                 |
| raytrace                   | 273 ms                                                       | 338 ms: 1.24x slower                                                 |
| comprehensions             | 17.0 us                                                      | 21.3 us: 1.25x slower                                                |
| nqueens                    | 90.7 ms                                                      | 114 ms: 1.25x slower                                                 |
| scimark_monte_carlo        | 66.1 ms                                                      | 83.3 ms: 1.26x slower                                                |
| crypto_pyaes               | 73.3 ms                                                      | 93.0 ms: 1.27x slower                                                |
| django_template            | 36.4 ms                                                      | 46.2 ms: 1.27x slower                                                |
| coverage                   | 80.0 ms                                                      | 102 ms: 1.27x slower                                                 |
| fannkuch                   | 363 ms                                                       | 473 ms: 1.30x slower                                                 |
| deltablue                  | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                |
| python_startup_no_site     | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                |
| typing_runtime_protocols   | 169 us                                                       | 225 us: 1.33x slower                                                 |
| subparsers                 | 17.5 ms                                                      | 25.7 ms: 1.47x slower                                                |
| nbody                      | 89.3 ms                                                      | 134 ms: 1.50x slower                                                 |
| bench_thread_pool          | 942 us                                                       | 1.44 ms: 1.53x slower                                                |
| mako                       | 10.4 ms                                                      | 18.0 ms: 1.73x slower                                                |
| bench_mp_pool              | 5.12 ms                                                      | 49.0 ms: 9.58x slower                                                |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                         |

Benchmark hidden because not significant (2): regex_v8, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.061x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.23x