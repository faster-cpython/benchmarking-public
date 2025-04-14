# Results vs. 3.13.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.062x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 336 ms: 1.15x slower                                                                   |
| docutils       | 2.83 sec                                                     | 2.99 sec: 1.06x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 74.2 ms: 1.01x slower                                                                  |
| sphinx         | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 577 ms: 1.44x faster                                                                   |
| async_tree_memoization_tg  | 466 ms                                                       | 329 ms: 1.42x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 256 ms: 1.35x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.28x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 364 ms: 1.25x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 495 ms: 1.18x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 532 ms: 1.13x faster                                                                   |
| asyncio_websockets         | 388 ms                                                       | 380 ms: 1.02x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                                  |
| async_generators           | 457 ms                                                       | 469 ms: 1.03x slower                                                                   |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 75.0 ms: 1.09x faster                                                                  |
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                                   |
| nbody          | 89.3 ms                                                      | 138 ms: 1.55x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.16 ms: 1.16x faster                                                                  |
| regex_v8       | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                                  |
| regex_dna      | 247 ms                                                       | 241 ms: 1.02x faster                                                                   |
| regex_compile  | 143 ms                                                       | 156 ms: 1.09x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 89.3 ms: 1.15x faster                                                                  |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                                   |
| tomli_loads          | 2.46 sec                                                     | 2.41 sec: 1.02x faster                                                                 |
| unpickle_pure_python | 217 us                                                       | 242 us: 1.12x slower                                                                   |
| json_loads           | 24.7 us                                                      | 27.7 us: 1.12x slower                                                                  |
| xml_etree_generate   | 86.5 ms                                                      | 100 ms: 1.16x slower                                                                   |
| pickle_pure_python   | 323 us                                                       | 380 us: 1.18x slower                                                                   |
| xml_etree_process    | 61.2 ms                                                      | 72.4 ms: 1.18x slower                                                                  |
| json_dumps           | 11.1 ms                                                      | 13.5 ms: 1.21x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 18.6 ms: 1.17x slower                                                                  |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 62.4 ms: 1.09x slower                                                                  |
| genshi_text     | 26.2 ms                                                      | 29.0 ms: 1.11x slower                                                                  |
| django_template | 36.4 ms                                                      | 47.2 ms: 1.30x slower                                                                  |
| mako            | 10.4 ms                                                      | 18.0 ms: 1.73x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.28x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 577 ms: 1.44x faster                                                                   |
| async_tree_memoization_tg  | 466 ms                                                       | 329 ms: 1.42x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 256 ms: 1.35x faster                                                                   |
| create_gc_cycles           | 2.68 ms                                                      | 2.02 ms: 1.33x faster                                                                  |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.28x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 364 ms: 1.25x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 495 ms: 1.18x faster                                                                   |
| gc_traversal               | 4.74 ms                                                      | 4.05 ms: 1.17x faster                                                                  |
| regex_effbot               | 3.67 ms                                                      | 3.16 ms: 1.16x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 89.3 ms: 1.15x faster                                                                  |
| deepcopy                   | 392 us                                                       | 341 us: 1.15x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 532 ms: 1.13x faster                                                                   |
| sqlite_synth               | 2.91 us                                                      | 2.59 us: 1.12x faster                                                                  |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                                   |
| float                      | 81.3 ms                                                      | 75.0 ms: 1.09x faster                                                                  |
| generators                 | 33.6 ms                                                      | 31.1 ms: 1.08x faster                                                                  |
| pathlib                    | 17.5 ms                                                      | 16.3 ms: 1.08x faster                                                                  |
| go                         | 162 ms                                                       | 151 ms: 1.07x faster                                                                   |
| regex_v8                   | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                                  |
| deepcopy_memo              | 38.6 us                                                      | 37.4 us: 1.03x faster                                                                  |
| json                       | 5.69 ms                                                      | 5.54 ms: 1.03x faster                                                                  |
| regex_dna                  | 247 ms                                                       | 241 ms: 1.02x faster                                                                   |
| tomli_loads                | 2.46 sec                                                     | 2.41 sec: 1.02x faster                                                                 |
| scimark_sor                | 123 ms                                                       | 121 ms: 1.02x faster                                                                   |
| asyncio_websockets         | 388 ms                                                       | 380 ms: 1.02x faster                                                                   |
| pyflate                    | 503 ms                                                       | 496 ms: 1.02x faster                                                                   |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                                   |
| html5lib                   | 73.5 ms                                                      | 74.2 ms: 1.01x slower                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 5.17 sec: 1.02x slower                                                                 |
| dulwich_log                | 68.2 ms                                                      | 70.0 ms: 1.03x slower                                                                  |
| async_generators           | 457 ms                                                       | 469 ms: 1.03x slower                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 3.65 us: 1.03x slower                                                                  |
| pycparser                  | 1.24 sec                                                     | 1.29 sec: 1.04x slower                                                                 |
| telco                      | 8.79 ms                                                      | 9.13 ms: 1.04x slower                                                                  |
| spectral_norm              | 97.0 ms                                                      | 102 ms: 1.05x slower                                                                   |
| logging_silent             | 97.9 ns                                                      | 103 ns: 1.05x slower                                                                   |
| docutils                   | 2.83 sec                                                     | 2.99 sec: 1.06x slower                                                                 |
| scimark_fft                | 328 ms                                                       | 347 ms: 1.06x slower                                                                   |
| pprint_safe_repr           | 843 ms                                                       | 900 ms: 1.07x slower                                                                   |
| sphinx                     | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                                                 |
| pprint_pformat             | 1.72 sec                                                     | 1.86 sec: 1.08x slower                                                                 |
| regex_compile              | 143 ms                                                       | 156 ms: 1.09x slower                                                                   |
| mdp                        | 2.54 sec                                                     | 2.77 sec: 1.09x slower                                                                 |
| genshi_xml                 | 57.1 ms                                                      | 62.4 ms: 1.09x slower                                                                  |
| sqlglot_normalize          | 119 ms                                                       | 131 ms: 1.10x slower                                                                   |
| hexiom                     | 6.55 ms                                                      | 7.21 ms: 1.10x slower                                                                  |
| genshi_text                | 26.2 ms                                                      | 29.0 ms: 1.11x slower                                                                  |
| richards                   | 52.9 ms                                                      | 58.5 ms: 1.11x slower                                                                  |
| k_core                     | 2.17 sec                                                     | 2.41 sec: 1.11x slower                                                                 |
| sqlglot_optimize           | 59.3 ms                                                      | 65.9 ms: 1.11x slower                                                                  |
| unpickle_pure_python       | 217 us                                                       | 242 us: 1.12x slower                                                                   |
| logging_simple             | 6.39 us                                                      | 7.16 us: 1.12x slower                                                                  |
| json_loads                 | 24.7 us                                                      | 27.7 us: 1.12x slower                                                                  |
| sympy_expand               | 509 ms                                                       | 575 ms: 1.13x slower                                                                   |
| richards_super             | 59.6 ms                                                      | 67.3 ms: 1.13x slower                                                                  |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.7 ms: 1.14x slower                                                                  |
| connected_components       | 432 ms                                                       | 494 ms: 1.14x slower                                                                   |
| sympy_sum                  | 155 ms                                                       | 177 ms: 1.14x slower                                                                   |
| sympy_str                  | 298 ms                                                       | 341 ms: 1.14x slower                                                                   |
| logging_format             | 6.94 us                                                      | 7.95 us: 1.15x slower                                                                  |
| 2to3                       | 293 ms                                                       | 336 ms: 1.15x slower                                                                   |
| shortest_path              | 460 ms                                                       | 530 ms: 1.15x slower                                                                   |
| thrift                     | 901 us                                                       | 1.04 ms: 1.15x slower                                                                  |
| sqlglot_parse              | 1.40 ms                                                      | 1.62 ms: 1.16x slower                                                                  |
| sympy_integrate            | 23.6 ms                                                      | 27.2 ms: 1.16x slower                                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 100 ms: 1.16x slower                                                                   |
| python_startup             | 15.9 ms                                                      | 18.6 ms: 1.17x slower                                                                  |
| sqlglot_transpile          | 1.79 ms                                                      | 2.09 ms: 1.17x slower                                                                  |
| pickle_pure_python         | 323 us                                                       | 380 us: 1.18x slower                                                                   |
| xml_etree_process          | 61.2 ms                                                      | 72.4 ms: 1.18x slower                                                                  |
| chaos                      | 60.2 ms                                                      | 71.3 ms: 1.18x slower                                                                  |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.66 ms: 1.19x slower                                                                  |
| sqlalchemy_declarative     | 148 ms                                                       | 177 ms: 1.19x slower                                                                   |
| meteor_contest             | 130 ms                                                       | 155 ms: 1.20x slower                                                                   |
| many_optionals             | 930 us                                                       | 1.13 ms: 1.21x slower                                                                  |
| json_dumps                 | 11.1 ms                                                      | 13.5 ms: 1.21x slower                                                                  |
| scimark_lu                 | 98.7 ms                                                      | 120 ms: 1.22x slower                                                                   |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.23x slower                                                                   |
| comprehensions             | 17.0 us                                                      | 21.2 us: 1.25x slower                                                                  |
| coverage                   | 80.0 ms                                                      | 100 ms: 1.25x slower                                                                   |
| raytrace                   | 273 ms                                                       | 342 ms: 1.26x slower                                                                   |
| crypto_pyaes               | 73.3 ms                                                      | 92.9 ms: 1.27x slower                                                                  |
| django_template            | 36.4 ms                                                      | 47.2 ms: 1.30x slower                                                                  |
| fannkuch                   | 363 ms                                                       | 475 ms: 1.31x slower                                                                   |
| typing_runtime_protocols   | 169 us                                                       | 221 us: 1.31x slower                                                                   |
| python_startup_no_site     | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                                  |
| deltablue                  | 3.42 ms                                                      | 4.51 ms: 1.32x slower                                                                  |
| scimark_monte_carlo        | 66.1 ms                                                      | 87.9 ms: 1.33x slower                                                                  |
| subparsers                 | 17.5 ms                                                      | 25.7 ms: 1.47x slower                                                                  |
| nbody                      | 89.3 ms                                                      | 138 ms: 1.55x slower                                                                   |
| bench_thread_pool          | 942 us                                                       | 1.47 ms: 1.56x slower                                                                  |
| mako                       | 10.4 ms                                                      | 18.0 ms: 1.73x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 48.8 ms: 9.53x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                           |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.062x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.23x