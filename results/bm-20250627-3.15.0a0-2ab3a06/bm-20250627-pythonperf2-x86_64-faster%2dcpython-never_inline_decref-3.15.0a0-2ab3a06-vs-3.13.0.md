# Results vs. 3.13.0

- fork: faster-cpython
- ref: never_inline_decref
- machine: linux-x86_64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                                 |
| docutils       | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                               |
| html5lib       | 73.5 ms                                                      | 66.6 ms: 1.10x faster                                                                |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                               |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                                 |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                                 |
| async_tree_io              | 843 ms                                                       | 636 ms: 1.33x faster                                                                 |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.32x faster                                                                 |
| async_tree_io_tg           | 831 ms                                                       | 641 ms: 1.30x faster                                                                 |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.26x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 508 ms: 1.19x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 514 ms: 1.13x faster                                                                 |
| async_generators           | 457 ms                                                       | 427 ms: 1.07x faster                                                                 |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 22.8 ms: 1.06x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.4 ms: 1.15x faster                                                                |
| pidigits       | 252 ms                                                       | 258 ms: 1.02x slower                                                                 |
| nbody          | 89.3 ms                                                      | 94.5 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 225 ms: 1.10x faster                                                                 |
| regex_v8       | 26.1 ms                                                      | 24.2 ms: 1.08x faster                                                                |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                                 |
| regex_effbot   | 3.67 ms                                                      | 3.75 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads         | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                               |
| xml_etree_process   | 61.2 ms                                                      | 59.2 ms: 1.03x faster                                                                |
| xml_etree_parse     | 150 ms                                                       | 146 ms: 1.03x faster                                                                 |
| xml_etree_generate  | 86.5 ms                                                      | 84.9 ms: 1.02x faster                                                                |
| xml_etree_iterparse | 103 ms                                                       | 102 ms: 1.01x faster                                                                 |
| json_loads          | 24.7 us                                                      | 25.4 us: 1.03x slower                                                                |
| json_dumps          | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                                |
| pickle_pure_python  | 323 us                                                       | 340 us: 1.05x slower                                                                 |
| Geometric mean      | (ref)                                                        | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                                |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                                |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                                |
| genshi_xml      | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                                |
| django_template | 36.4 ms                                                      | 35.9 ms: 1.01x faster                                                                |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.04x slower                                                                |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                               |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                                 |
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                                 |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                                 |
| go                         | 162 ms                                                       | 119 ms: 1.36x faster                                                                 |
| deepcopy_memo              | 38.6 us                                                      | 28.5 us: 1.36x faster                                                                |
| async_tree_io              | 843 ms                                                       | 636 ms: 1.33x faster                                                                 |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.32x faster                                                                 |
| async_tree_io_tg           | 831 ms                                                       | 641 ms: 1.30x faster                                                                 |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.26x faster                                                                 |
| pyflate                    | 503 ms                                                       | 415 ms: 1.21x faster                                                                 |
| tomli_loads                | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 508 ms: 1.19x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 3.00 us: 1.18x faster                                                                |
| richards                   | 52.9 ms                                                      | 45.4 ms: 1.17x faster                                                                |
| richards_super             | 59.6 ms                                                      | 51.4 ms: 1.16x faster                                                                |
| scimark_sor                | 123 ms                                                       | 107 ms: 1.16x faster                                                                 |
| float                      | 81.3 ms                                                      | 70.4 ms: 1.15x faster                                                                |
| genshi_text                | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                                |
| spectral_norm              | 97.0 ms                                                      | 85.7 ms: 1.13x faster                                                                |
| generators                 | 33.6 ms                                                      | 29.7 ms: 1.13x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 514 ms: 1.13x faster                                                                 |
| dulwich_log                | 68.2 ms                                                      | 60.5 ms: 1.13x faster                                                                |
| hexiom                     | 6.55 ms                                                      | 5.93 ms: 1.10x faster                                                                |
| html5lib                   | 73.5 ms                                                      | 66.6 ms: 1.10x faster                                                                |
| regex_dna                  | 247 ms                                                       | 225 ms: 1.10x faster                                                                 |
| regex_v8                   | 26.1 ms                                                      | 24.2 ms: 1.08x faster                                                                |
| thrift                     | 901 us                                                       | 835 us: 1.08x faster                                                                 |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                                 |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                                 |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                                 |
| async_generators           | 457 ms                                                       | 427 ms: 1.07x faster                                                                 |
| logging_simple             | 6.39 us                                                      | 5.98 us: 1.07x faster                                                                |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.07x faster                                                               |
| deltablue                  | 3.42 ms                                                      | 3.20 ms: 1.07x faster                                                                |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                               |
| pprint_safe_repr           | 843 ms                                                       | 793 ms: 1.06x faster                                                                 |
| telco                      | 8.79 ms                                                      | 8.28 ms: 1.06x faster                                                                |
| sympy_integrate            | 23.6 ms                                                      | 22.2 ms: 1.06x faster                                                                |
| genshi_xml                 | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                                |
| logging_format             | 6.94 us                                                      | 6.58 us: 1.05x faster                                                                |
| json                       | 5.69 ms                                                      | 5.40 ms: 1.05x faster                                                                |
| logging_silent             | 97.9 ns                                                      | 93.3 ns: 1.05x faster                                                                |
| scimark_fft                | 328 ms                                                       | 314 ms: 1.05x faster                                                                 |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.4 ms: 1.04x faster                                                                |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                                 |
| comprehensions             | 17.0 us                                                      | 16.4 us: 1.04x faster                                                                |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                                |
| xml_etree_process          | 61.2 ms                                                      | 59.2 ms: 1.03x faster                                                                |
| connected_components       | 432 ms                                                       | 420 ms: 1.03x faster                                                                 |
| xml_etree_parse            | 150 ms                                                       | 146 ms: 1.03x faster                                                                 |
| typing_runtime_protocols   | 169 us                                                       | 164 us: 1.03x faster                                                                 |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                               |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                                |
| sympy_expand               | 509 ms                                                       | 496 ms: 1.03x faster                                                                 |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.03x faster                                                                 |
| k_core                     | 2.17 sec                                                     | 2.12 sec: 1.02x faster                                                               |
| shortest_path              | 460 ms                                                       | 450 ms: 1.02x faster                                                                 |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                               |
| xml_etree_generate         | 86.5 ms                                                      | 84.9 ms: 1.02x faster                                                                |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                                |
| sympy_sum                  | 155 ms                                                       | 153 ms: 1.01x faster                                                                 |
| django_template            | 36.4 ms                                                      | 35.9 ms: 1.01x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                                 |
| chaos                      | 60.2 ms                                                      | 59.7 ms: 1.01x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                                 |
| docutils                   | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                               |
| fannkuch                   | 363 ms                                                       | 370 ms: 1.02x slower                                                                 |
| regex_effbot               | 3.67 ms                                                      | 3.75 ms: 1.02x slower                                                                |
| pidigits                   | 252 ms                                                       | 258 ms: 1.02x slower                                                                 |
| raytrace                   | 273 ms                                                       | 280 ms: 1.03x slower                                                                 |
| json_loads                 | 24.7 us                                                      | 25.4 us: 1.03x slower                                                                |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.93 ms: 1.03x slower                                                                |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.04x slower                                                                |
| crypto_pyaes               | 73.3 ms                                                      | 76.0 ms: 1.04x slower                                                                |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                                |
| pickle_pure_python         | 323 us                                                       | 340 us: 1.05x slower                                                                 |
| coroutines                 | 21.6 ms                                                      | 22.8 ms: 1.06x slower                                                                |
| nbody                      | 89.3 ms                                                      | 94.5 ms: 1.06x slower                                                                |
| create_gc_cycles           | 2.68 ms                                                      | 2.88 ms: 1.07x slower                                                                |
| coverage                   | 80.0 ms                                                      | 87.9 ms: 1.10x slower                                                                |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.12x slower                                                                |
| gc_traversal               | 4.74 ms                                                      | 6.73 ms: 1.42x slower                                                                |
| subparsers                 | 17.5 ms                                                      | 25.0 ms: 1.43x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                         |

Benchmark hidden because not significant (5): djangocms, unpickle_pure_python, scimark_lu, sqlite_synth, nqueens
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-pythonperf2-x86_64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x