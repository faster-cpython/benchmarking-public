# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.286x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 427 ms: 1.46x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.42 sec: 1.22x slower                                                       |
| html5lib       | 72.9 ms                                                      | 104 ms: 1.43x slower                                                         |
| sphinx         | 1.11 sec                                                     | 1.36 sec: 1.22x slower                                                       |
| Geometric mean | (ref)                                                        | 1.33x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 478 ms: 1.04x slower                                                         |
| async_tree_none_tg         | 342 ms                                                       | 371 ms: 1.08x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 897 ms: 1.09x slower                                                         |
| async_tree_none            | 370 ms                                                       | 414 ms: 1.12x slower                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 644 ms: 1.12x slower                                                         |
| async_tree_io              | 832 ms                                                       | 944 ms: 1.14x slower                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 680 ms: 1.14x slower                                                         |
| async_tree_memoization     | 447 ms                                                       | 514 ms: 1.15x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 26.7 ms: 1.24x slower                                                        |
| async_generators           | 364 ms                                                       | 479 ms: 1.32x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.12x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| float          | 81.6 ms                                                      | 140 ms: 1.72x slower                                                         |
| nbody          | 92.1 ms                                                      | 179 ms: 1.95x slower                                                         |
| Geometric mean | (ref)                                                        | 1.49x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                        |
| regex_dna      | 238 ms                                                       | 250 ms: 1.05x slower                                                         |
| regex_v8       | 24.9 ms                                                      | 27.2 ms: 1.09x slower                                                        |
| regex_compile  | 143 ms                                                       | 224 ms: 1.57x slower                                                         |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 99.8 ms                                                      | 110 ms: 1.11x slower                                                         |
| json_loads           | 24.7 us                                                      | 28.6 us: 1.16x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 3.27 sec: 1.34x slower                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 115 ms: 1.35x slower                                                         |
| json_dumps           | 10.8 ms                                                      | 15.1 ms: 1.39x slower                                                        |
| xml_etree_process    | 60.7 ms                                                      | 93.9 ms: 1.55x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 399 us: 1.85x slower                                                         |
| pickle_pure_python   | 322 us                                                       | 602 us: 1.87x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.37x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 19.8 ms: 1.27x slower                                                        |
| python_startup_no_site | 8.93 ms                                                      | 12.1 ms: 1.35x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 80.8 ms: 1.39x slower                                                        |
| genshi_text     | 27.2 ms                                                      | 41.8 ms: 1.54x slower                                                        |
| django_template | 38.9 ms                                                      | 68.2 ms: 1.75x slower                                                        |
| mako            | 10.3 ms                                                      | 22.1 ms: 2.14x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.68x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.48 ms                                                      | 3.85 ms: 1.16x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| create_gc_cycles           | 2.65 ms                                                      | 2.58 ms: 1.03x faster                                                        |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| regex_effbot               | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 478 ms: 1.04x slower                                                         |
| regex_dna                  | 238 ms                                                       | 250 ms: 1.05x slower                                                         |
| json                       | 5.62 ms                                                      | 5.90 ms: 1.05x slower                                                        |
| async_tree_none_tg         | 342 ms                                                       | 371 ms: 1.08x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 897 ms: 1.09x slower                                                         |
| regex_v8                   | 24.9 ms                                                      | 27.2 ms: 1.09x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 110 ms: 1.11x slower                                                         |
| deepcopy                   | 388 us                                                       | 431 us: 1.11x slower                                                         |
| async_tree_none            | 370 ms                                                       | 414 ms: 1.12x slower                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 644 ms: 1.12x slower                                                         |
| pathlib                    | 17.4 ms                                                      | 19.6 ms: 1.12x slower                                                        |
| async_tree_io              | 832 ms                                                       | 944 ms: 1.14x slower                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 680 ms: 1.14x slower                                                         |
| async_tree_memoization     | 447 ms                                                       | 514 ms: 1.15x slower                                                         |
| telco                      | 8.77 ms                                                      | 10.1 ms: 1.16x slower                                                        |
| json_loads                 | 24.7 us                                                      | 28.6 us: 1.16x slower                                                        |
| scimark_fft                | 298 ms                                                       | 353 ms: 1.19x slower                                                         |
| shortest_path              | 477 ms                                                       | 570 ms: 1.19x slower                                                         |
| generators                 | 33.9 ms                                                      | 40.8 ms: 1.20x slower                                                        |
| connected_components       | 443 ms                                                       | 536 ms: 1.21x slower                                                         |
| docutils                   | 2.81 sec                                                     | 3.42 sec: 1.22x slower                                                       |
| sphinx                     | 1.11 sec                                                     | 1.36 sec: 1.22x slower                                                       |
| k_core                     | 2.18 sec                                                     | 2.69 sec: 1.23x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 26.7 ms: 1.24x slower                                                        |
| coverage                   | 84.5 ms                                                      | 106 ms: 1.25x slower                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 6.39 sec: 1.26x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.29 ms: 1.26x slower                                                        |
| pylint                     | 345 ms                                                       | 434 ms: 1.26x slower                                                         |
| python_startup             | 15.6 ms                                                      | 19.8 ms: 1.27x slower                                                        |
| mdp                        | 2.53 sec                                                     | 3.23 sec: 1.28x slower                                                       |
| deepcopy_memo              | 38.9 us                                                      | 50.5 us: 1.30x slower                                                        |
| meteor_contest             | 130 ms                                                       | 170 ms: 1.31x slower                                                         |
| async_generators           | 364 ms                                                       | 479 ms: 1.32x slower                                                         |
| sqlalchemy_imperative      | 18.1 ms                                                      | 24.2 ms: 1.33x slower                                                        |
| tomli_loads                | 2.43 sec                                                     | 3.27 sec: 1.34x slower                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 115 ms: 1.35x slower                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 4.72 us: 1.35x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 12.1 ms: 1.35x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 89.8 ms: 1.37x slower                                                        |
| pycparser                  | 1.28 sec                                                     | 1.76 sec: 1.37x slower                                                       |
| nqueens                    | 92.3 ms                                                      | 128 ms: 1.38x slower                                                         |
| genshi_xml                 | 58.0 ms                                                      | 80.8 ms: 1.39x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 15.1 ms: 1.39x slower                                                        |
| sympy_integrate            | 23.4 ms                                                      | 32.8 ms: 1.40x slower                                                        |
| html5lib                   | 72.9 ms                                                      | 104 ms: 1.43x slower                                                         |
| spectral_norm              | 97.4 ms                                                      | 140 ms: 1.44x slower                                                         |
| fannkuch                   | 384 ms                                                       | 560 ms: 1.46x slower                                                         |
| 2to3                       | 293 ms                                                       | 427 ms: 1.46x slower                                                         |
| thrift                     | 918 us                                                       | 1.39 ms: 1.52x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 266 us: 1.52x slower                                                         |
| sympy_str                  | 297 ms                                                       | 452 ms: 1.53x slower                                                         |
| pyflate                    | 493 ms                                                       | 752 ms: 1.53x slower                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 227 ms: 1.53x slower                                                         |
| genshi_text                | 27.2 ms                                                      | 41.8 ms: 1.54x slower                                                        |
| xml_etree_process          | 60.7 ms                                                      | 93.9 ms: 1.55x slower                                                        |
| richards                   | 52.5 ms                                                      | 81.2 ms: 1.55x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 185 ms: 1.55x slower                                                         |
| regex_compile              | 143 ms                                                       | 224 ms: 1.57x slower                                                         |
| sqlglot_optimize           | 58.7 ms                                                      | 92.4 ms: 1.57x slower                                                        |
| sympy_expand               | 506 ms                                                       | 814 ms: 1.61x slower                                                         |
| pprint_safe_repr           | 835 ms                                                       | 1.36 sec: 1.63x slower                                                       |
| richards_super             | 60.2 ms                                                      | 98.0 ms: 1.63x slower                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 121 ms: 1.64x slower                                                         |
| pprint_pformat             | 1.70 sec                                                     | 2.82 sec: 1.66x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 263 ms: 1.71x slower                                                         |
| go                         | 167 ms                                                       | 286 ms: 1.71x slower                                                         |
| float                      | 81.6 ms                                                      | 140 ms: 1.72x slower                                                         |
| bench_thread_pool          | 929 us                                                       | 1.60 ms: 1.72x slower                                                        |
| django_template            | 38.9 ms                                                      | 68.2 ms: 1.75x slower                                                        |
| comprehensions             | 17.3 us                                                      | 30.4 us: 1.76x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 11.5 ms: 1.78x slower                                                        |
| logging_format             | 6.95 us                                                      | 12.5 us: 1.80x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 399 us: 1.85x slower                                                         |
| logging_simple             | 6.28 us                                                      | 11.6 us: 1.85x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 602 us: 1.87x slower                                                         |
| scimark_sor                | 125 ms                                                       | 238 ms: 1.90x slower                                                         |
| logging_silent             | 97.5 ns                                                      | 186 ns: 1.91x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 3.38 ms: 1.92x slower                                                        |
| nbody                      | 92.1 ms                                                      | 179 ms: 1.95x slower                                                         |
| chaos                      | 60.6 ms                                                      | 119 ms: 1.96x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 130 ms: 1.99x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 2.79 ms: 2.04x slower                                                        |
| mako                       | 10.3 ms                                                      | 22.1 ms: 2.14x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 215 ms: 2.20x slower                                                         |
| raytrace                   | 267 ms                                                       | 595 ms: 2.22x slower                                                         |
| deltablue                  | 3.38 ms                                                      | 8.35 ms: 2.47x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 53.6 ms: 11.12x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.44x slower                                                                 |
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.286x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: 1.21x