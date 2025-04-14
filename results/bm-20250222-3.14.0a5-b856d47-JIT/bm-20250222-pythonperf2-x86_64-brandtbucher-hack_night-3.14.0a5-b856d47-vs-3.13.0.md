# Results vs. 3.13.0

- fork: brandtbucher
- ref: hack_night
- machine: linux-x86_64
- commit hash: b856d47
- commit date: 2025-02-22
- overall geometric mean: 1.046x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 291 ms: 1.00x faster                                                    |
| docutils       | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                                  |
| html5lib       | 73.5 ms                                                      | 68.5 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                    |
| async_tree_io              | 843 ms                                                       | 640 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 831 ms                                                       | 643 ms: 1.29x faster                                                    |
| async_tree_none            | 376 ms                                                       | 291 ms: 1.29x faster                                                    |
| async_tree_memoization     | 453 ms                                                       | 353 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 346 ms                                                       | 280 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 524 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                    |
| async_generators           | 457 ms                                                       | 434 ms: 1.05x faster                                                    |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                   |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                   |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                    |
| nbody          | 89.3 ms                                                      | 100.0 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                   |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                    |
| regex_dna      | 247 ms                                                       | 238 ms: 1.04x faster                                                    |
| regex_v8       | 26.1 ms                                                      | 25.5 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                  |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                    |
| xml_etree_process    | 61.2 ms                                                      | 55.9 ms: 1.09x faster                                                   |
| xml_etree_generate   | 86.5 ms                                                      | 79.8 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 103 ms                                                       | 96.6 ms: 1.06x faster                                                   |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.05x faster                                                    |
| pickle_pure_python   | 323 us                                                       | 337 us: 1.04x slower                                                    |
| json_dumps           | 11.1 ms                                                      | 11.8 ms: 1.06x slower                                                   |
| json_loads           | 24.7 us                                                      | 26.6 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 10.4 ms                                                      | 9.61 ms: 1.08x faster                                                   |
| genshi_text    | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                   |
| genshi_xml     | 57.1 ms                                                      | 58.3 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                    |
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                    |
| deepcopy_memo              | 38.6 us                                                      | 28.9 us: 1.34x faster                                                   |
| async_tree_io              | 843 ms                                                       | 640 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 831 ms                                                       | 643 ms: 1.29x faster                                                    |
| async_tree_none            | 376 ms                                                       | 291 ms: 1.29x faster                                                    |
| async_tree_memoization     | 453 ms                                                       | 353 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 346 ms                                                       | 280 ms: 1.24x faster                                                    |
| tomli_loads                | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                  |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                   |
| pyflate                    | 503 ms                                                       | 425 ms: 1.19x faster                                                    |
| spectral_norm              | 97.0 ms                                                      | 82.4 ms: 1.18x faster                                                   |
| richards                   | 52.9 ms                                                      | 45.1 ms: 1.17x faster                                                   |
| regex_effbot               | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                   |
| float                      | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                   |
| richards_super             | 59.6 ms                                                      | 51.0 ms: 1.17x faster                                                   |
| generators                 | 33.6 ms                                                      | 28.9 ms: 1.16x faster                                                   |
| telco                      | 8.79 ms                                                      | 7.58 ms: 1.16x faster                                                   |
| scimark_sor                | 123 ms                                                       | 107 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 524 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                    |
| bpe_tokeniser              | 5.09 sec                                                     | 4.58 sec: 1.11x faster                                                  |
| scimark_fft                | 328 ms                                                       | 295 ms: 1.11x faster                                                    |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                    |
| xml_etree_process          | 61.2 ms                                                      | 55.9 ms: 1.09x faster                                                   |
| go                         | 162 ms                                                       | 149 ms: 1.09x faster                                                    |
| xml_etree_generate         | 86.5 ms                                                      | 79.8 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.1 ms: 1.08x faster                                                   |
| mako                       | 10.4 ms                                                      | 9.61 ms: 1.08x faster                                                   |
| pylint                     | 347 ms                                                       | 321 ms: 1.08x faster                                                    |
| html5lib                   | 73.5 ms                                                      | 68.5 ms: 1.07x faster                                                   |
| connected_components       | 432 ms                                                       | 403 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 103 ms                                                       | 96.6 ms: 1.06x faster                                                   |
| shortest_path              | 460 ms                                                       | 435 ms: 1.06x faster                                                    |
| pathlib                    | 17.5 ms                                                      | 16.6 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.05x faster                                                    |
| async_generators           | 457 ms                                                       | 434 ms: 1.05x faster                                                    |
| json                       | 5.69 ms                                                      | 5.41 ms: 1.05x faster                                                   |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                    |
| genshi_text                | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                   |
| k_core                     | 2.17 sec                                                     | 2.07 sec: 1.05x faster                                                  |
| sqlite_synth               | 2.91 us                                                      | 2.78 us: 1.05x faster                                                   |
| regex_dna                  | 247 ms                                                       | 238 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.72 sec                                                     | 1.66 sec: 1.04x faster                                                  |
| pprint_safe_repr           | 843 ms                                                       | 813 ms: 1.04x faster                                                    |
| thrift                     | 901 us                                                       | 873 us: 1.03x faster                                                    |
| coverage                   | 80.0 ms                                                      | 77.8 ms: 1.03x faster                                                   |
| regex_v8                   | 26.1 ms                                                      | 25.5 ms: 1.03x faster                                                   |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                   |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                    |
| sqlglot_parse              | 1.40 ms                                                      | 1.38 ms: 1.01x faster                                                   |
| dulwich_log                | 68.2 ms                                                      | 67.4 ms: 1.01x faster                                                   |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.1 ms: 1.01x faster                                                   |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.73 ms: 1.01x faster                                                   |
| scimark_lu                 | 98.7 ms                                                      | 97.7 ms: 1.01x faster                                                   |
| logging_silent             | 97.9 ns                                                      | 97.3 ns: 1.01x faster                                                   |
| 2to3                       | 293 ms                                                       | 291 ms: 1.00x faster                                                    |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                    |
| sympy_integrate            | 23.6 ms                                                      | 23.7 ms: 1.01x slower                                                   |
| deltablue                  | 3.42 ms                                                      | 3.44 ms: 1.01x slower                                                   |
| sympy_str                  | 298 ms                                                       | 300 ms: 1.01x slower                                                    |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                   |
| python_startup_no_site     | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                   |
| mdp                        | 2.54 sec                                                     | 2.57 sec: 1.01x slower                                                  |
| sympy_expand               | 509 ms                                                       | 515 ms: 1.01x slower                                                    |
| sympy_sum                  | 155 ms                                                       | 157 ms: 1.01x slower                                                    |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.02x slower                                                  |
| sqlglot_optimize           | 59.3 ms                                                      | 60.3 ms: 1.02x slower                                                   |
| genshi_xml                 | 57.1 ms                                                      | 58.3 ms: 1.02x slower                                                   |
| bench_thread_pool          | 942 us                                                       | 965 us: 1.02x slower                                                    |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.03x slower                                                    |
| chaos                      | 60.2 ms                                                      | 62.1 ms: 1.03x slower                                                   |
| pickle_pure_python         | 323 us                                                       | 337 us: 1.04x slower                                                    |
| crypto_pyaes               | 73.3 ms                                                      | 76.7 ms: 1.05x slower                                                   |
| docutils                   | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                                  |
| typing_runtime_protocols   | 169 us                                                       | 177 us: 1.05x slower                                                    |
| fannkuch                   | 363 ms                                                       | 382 ms: 1.05x slower                                                    |
| json_dumps                 | 11.1 ms                                                      | 11.8 ms: 1.06x slower                                                   |
| hexiom                     | 6.55 ms                                                      | 7.04 ms: 1.07x slower                                                   |
| json_loads                 | 24.7 us                                                      | 26.6 us: 1.08x slower                                                   |
| raytrace                   | 273 ms                                                       | 295 ms: 1.08x slower                                                    |
| nqueens                    | 90.7 ms                                                      | 99.3 ms: 1.09x slower                                                   |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.10x slower                                                   |
| comprehensions             | 17.0 us                                                      | 19.0 us: 1.12x slower                                                   |
| nbody                      | 89.3 ms                                                      | 100.0 ms: 1.12x slower                                                  |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.32x slower                                                   |
| gc_traversal               | 4.74 ms                                                      | 6.33 ms: 1.33x slower                                                   |
| bench_mp_pool              | 5.12 ms                                                      | 1.64 sec: 319.76x slower                                                |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (8): sphinx, logging_simple, logging_format, sqlglot_transpile, django_template, create_gc_cycles, sqlglot_normalize, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x