# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 273 ms: 1.07x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.79 sec: 1.01x faster                                                       |
| html5lib       | 73.5 ms                                                      | 64.7 ms: 1.14x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.06 sec: 1.06x faster                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 316 ms: 1.47x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 323 ms: 1.40x faster                                                         |
| async_tree_none            | 376 ms                                                       | 270 ms: 1.39x faster                                                         |
| async_tree_io              | 843 ms                                                       | 613 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 608 ms: 1.37x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 262 ms: 1.32x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 532 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 517 ms: 1.12x faster                                                         |
| async_generators           | 457 ms                                                       | 411 ms: 1.11x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.4 ms: 1.06x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 391 ms: 1.01x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 65.3 ms: 1.25x faster                                                        |
| nbody          | 89.3 ms                                                      | 82.2 ms: 1.09x faster                                                        |
| pidigits       | 252 ms                                                       | 291 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.02 ms: 1.21x faster                                                        |
| regex_compile  | 143 ms                                                       | 130 ms: 1.10x faster                                                         |
| regex_dna      | 247 ms                                                       | 226 ms: 1.09x faster                                                         |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.00 sec: 1.23x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 53.8 ms: 1.14x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 76.9 ms: 1.12x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 198 us: 1.10x faster                                                         |
| pickle_pure_python   | 323 us                                                       | 304 us: 1.06x faster                                                         |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.1 us: 1.06x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 163 ms: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 9.09 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 21.0 ms: 1.25x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 49.2 ms: 1.16x faster                                                        |
| django_template | 36.4 ms                                                      | 33.2 ms: 1.09x faster                                                        |
| mako            | 10.4 ms                                                      | 10.5 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.12x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 258 us: 1.52x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 26.1 us: 1.48x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 316 ms: 1.47x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 323 ms: 1.40x faster                                                         |
| async_tree_none            | 376 ms                                                       | 270 ms: 1.39x faster                                                         |
| async_tree_io              | 843 ms                                                       | 613 ms: 1.37x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 70.9 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 608 ms: 1.37x faster                                                         |
| go                         | 162 ms                                                       | 120 ms: 1.36x faster                                                         |
| scimark_sor                | 123 ms                                                       | 90.9 ms: 1.35x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.62 us: 1.35x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 262 ms: 1.32x faster                                                         |
| richards                   | 52.9 ms                                                      | 40.8 ms: 1.30x faster                                                        |
| pyflate                    | 503 ms                                                       | 395 ms: 1.28x faster                                                         |
| richards_super             | 59.6 ms                                                      | 46.7 ms: 1.27x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 21.0 ms: 1.25x faster                                                        |
| float                      | 81.3 ms                                                      | 65.3 ms: 1.25x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.00 sec: 1.23x faster                                                       |
| scimark_fft                | 328 ms                                                       | 267 ms: 1.23x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 54.4 ms: 1.22x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.02 ms: 1.21x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.35 ms: 1.20x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.8 ms: 1.17x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 84.3 ns: 1.16x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 49.2 ms: 1.16x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 5.72 ms: 1.15x faster                                                        |
| comprehensions             | 17.0 us                                                      | 14.9 us: 1.15x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.17 ms: 1.14x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 53.8 ms: 1.14x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 64.7 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 532 ms: 1.14x faster                                                         |
| pylint                     | 347 ms                                                       | 306 ms: 1.13x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 87.2 ms: 1.13x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.50 sec: 1.13x faster                                                       |
| thrift                     | 901 us                                                       | 800 us: 1.13x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 76.9 ms: 1.12x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.24 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 517 ms: 1.12x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.04 ms: 1.12x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 754 ms: 1.12x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 15.7 ms: 1.12x faster                                                        |
| async_generators           | 457 ms                                                       | 411 ms: 1.11x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.55 sec: 1.11x faster                                                       |
| sqlglot_transpile          | 1.79 ms                                                      | 1.62 ms: 1.11x faster                                                        |
| chaos                      | 60.2 ms                                                      | 54.8 ms: 1.10x faster                                                        |
| regex_compile              | 143 ms                                                       | 130 ms: 1.10x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 198 us: 1.10x faster                                                         |
| django_template            | 36.4 ms                                                      | 33.2 ms: 1.09x faster                                                        |
| regex_dna                  | 247 ms                                                       | 226 ms: 1.09x faster                                                         |
| nbody                      | 89.3 ms                                                      | 82.2 ms: 1.09x faster                                                        |
| sympy_expand               | 509 ms                                                       | 471 ms: 1.08x faster                                                         |
| raytrace                   | 273 ms                                                       | 252 ms: 1.08x faster                                                         |
| coverage                   | 80.0 ms                                                      | 74.2 ms: 1.08x faster                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 55.0 ms: 1.08x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 138 ms: 1.08x faster                                                         |
| sqlglot_normalize          | 119 ms                                                       | 111 ms: 1.08x faster                                                         |
| logging_simple             | 6.39 us                                                      | 5.95 us: 1.07x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 84.5 ms: 1.07x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.0 ms: 1.07x faster                                                        |
| 2to3                       | 293 ms                                                       | 273 ms: 1.07x faster                                                         |
| sympy_str                  | 298 ms                                                       | 278 ms: 1.07x faster                                                         |
| json                       | 5.69 ms                                                      | 5.31 ms: 1.07x faster                                                        |
| bench_thread_pool          | 942 us                                                       | 883 us: 1.07x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 22.1 ms: 1.06x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.06 sec: 1.06x faster                                                       |
| typing_runtime_protocols   | 169 us                                                       | 159 us: 1.06x faster                                                         |
| sympy_sum                  | 155 ms                                                       | 146 ms: 1.06x faster                                                         |
| pickle_pure_python         | 323 us                                                       | 304 us: 1.06x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 64.3 ms: 1.06x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.05 sec: 1.06x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.56 us: 1.06x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.4 ms: 1.06x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.76 us: 1.05x faster                                                        |
| shortest_path              | 460 ms                                                       | 446 ms: 1.03x faster                                                         |
| connected_components       | 432 ms                                                       | 422 ms: 1.02x faster                                                         |
| fannkuch                   | 363 ms                                                       | 356 ms: 1.02x faster                                                         |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                         |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                       |
| docutils                   | 2.83 sec                                                     | 2.79 sec: 1.01x faster                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 72.5 ms: 1.01x faster                                                        |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 391 ms: 1.01x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.09 ms: 1.01x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.5 ms: 1.01x slower                                                        |
| mdp                        | 2.54 sec                                                     | 2.59 sec: 1.02x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.81 ms: 1.05x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                        |
| many_optionals             | 930 us                                                       | 982 us: 1.06x slower                                                         |
| json_loads                 | 24.7 us                                                      | 26.1 us: 1.06x slower                                                        |
| xml_etree_parse            | 150 ms                                                       | 163 ms: 1.08x slower                                                         |
| pidigits                   | 252 ms                                                       | 291 ms: 1.15x slower                                                         |
| gc_traversal               | 4.74 ms                                                      | 5.66 ms: 1.19x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.2 ms: 1.27x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.22 sec: 238.95x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): regex_v8, xml_etree_iterparse
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.06x