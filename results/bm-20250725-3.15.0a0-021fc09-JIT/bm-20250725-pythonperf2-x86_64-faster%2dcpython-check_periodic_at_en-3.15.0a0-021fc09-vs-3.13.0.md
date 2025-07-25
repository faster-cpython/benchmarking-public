# Results vs. 3.13.0

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: linux-x86_64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                                  |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                                |
| html5lib       | 73.5 ms                                                      | 67.0 ms: 1.10x faster                                                                 |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                                |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                                  |
| async_tree_memoization     | 453 ms                                                       | 326 ms: 1.39x faster                                                                  |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                                  |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                                  |
| async_tree_io_tg           | 831 ms                                                       | 630 ms: 1.32x faster                                                                  |
| async_tree_none_tg         | 346 ms                                                       | 269 ms: 1.29x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                                  |
| async_generators           | 457 ms                                                       | 417 ms: 1.10x faster                                                                  |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                                 |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                                  |
| nbody          | 89.3 ms                                                      | 97.5 ms: 1.09x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                                 |
| regex_dna      | 247 ms                                                       | 227 ms: 1.09x faster                                                                  |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                                  |
| regex_effbot   | 3.67 ms                                                      | 3.73 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.89 sec: 1.30x faster                                                                |
| unpickle_pure_python | 217 us                                                       | 195 us: 1.11x faster                                                                  |
| xml_etree_process    | 61.2 ms                                                      | 55.3 ms: 1.11x faster                                                                 |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                                  |
| xml_etree_generate   | 86.5 ms                                                      | 80.7 ms: 1.07x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 96.8 ms: 1.06x faster                                                                 |
| json_dumps           | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                                                 |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                                  |
| json_loads           | 24.7 us                                                      | 26.8 us: 1.08x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                                 |
| python_startup_no_site | 8.96 ms                                                      | 8.82 ms: 1.02x faster                                                                 |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                                 |
| django_template | 36.4 ms                                                      | 34.7 ms: 1.05x faster                                                                 |
| genshi_xml      | 57.1 ms                                                      | 54.7 ms: 1.04x faster                                                                 |
| mako            | 10.4 ms                                                      | 9.95 ms: 1.04x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 1.99x faster                                                                |
| richards                   | 52.9 ms                                                      | 34.3 ms: 1.54x faster                                                                 |
| richards_super             | 59.6 ms                                                      | 39.9 ms: 1.49x faster                                                                 |
| deepcopy                   | 392 us                                                       | 277 us: 1.42x faster                                                                  |
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                                  |
| async_tree_memoization     | 453 ms                                                       | 326 ms: 1.39x faster                                                                  |
| deepcopy_memo              | 38.6 us                                                      | 28.0 us: 1.38x faster                                                                 |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                                  |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                                  |
| async_tree_io_tg           | 831 ms                                                       | 630 ms: 1.32x faster                                                                  |
| tomli_loads                | 2.46 sec                                                     | 1.89 sec: 1.30x faster                                                                |
| go                         | 162 ms                                                       | 125 ms: 1.29x faster                                                                  |
| async_tree_none_tg         | 346 ms                                                       | 269 ms: 1.29x faster                                                                  |
| float                      | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                                 |
| pyflate                    | 503 ms                                                       | 401 ms: 1.26x faster                                                                  |
| spectral_norm              | 97.0 ms                                                      | 77.6 ms: 1.25x faster                                                                 |
| scimark_sor                | 123 ms                                                       | 101 ms: 1.22x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                                  |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                                 |
| deltablue                  | 3.42 ms                                                      | 2.87 ms: 1.19x faster                                                                 |
| generators                 | 33.6 ms                                                      | 28.4 ms: 1.18x faster                                                                 |
| dulwich_log                | 68.2 ms                                                      | 59.1 ms: 1.15x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                                  |
| pprint_pformat             | 1.72 sec                                                     | 1.51 sec: 1.14x faster                                                                |
| pprint_safe_repr           | 843 ms                                                       | 745 ms: 1.13x faster                                                                  |
| genshi_text                | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                                 |
| unpickle_pure_python       | 217 us                                                       | 195 us: 1.11x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.57 sec: 1.11x faster                                                                |
| regex_v8                   | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                                 |
| xml_etree_process          | 61.2 ms                                                      | 55.3 ms: 1.11x faster                                                                 |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                                  |
| scimark_fft                | 328 ms                                                       | 298 ms: 1.10x faster                                                                  |
| html5lib                   | 73.5 ms                                                      | 67.0 ms: 1.10x faster                                                                 |
| async_generators           | 457 ms                                                       | 417 ms: 1.10x faster                                                                  |
| regex_dna                  | 247 ms                                                       | 227 ms: 1.09x faster                                                                  |
| thrift                     | 901 us                                                       | 832 us: 1.08x faster                                                                  |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                                |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 80.7 ms: 1.07x faster                                                                 |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                                  |
| connected_components       | 432 ms                                                       | 404 ms: 1.07x faster                                                                  |
| logging_simple             | 6.39 us                                                      | 6.01 us: 1.06x faster                                                                 |
| hexiom                     | 6.55 ms                                                      | 6.17 ms: 1.06x faster                                                                 |
| logging_silent             | 97.9 ns                                                      | 92.1 ns: 1.06x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 96.8 ms: 1.06x faster                                                                 |
| meteor_contest             | 130 ms                                                       | 122 ms: 1.06x faster                                                                  |
| sympy_integrate            | 23.6 ms                                                      | 22.3 ms: 1.06x faster                                                                 |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.7 ms: 1.05x faster                                                                 |
| logging_format             | 6.94 us                                                      | 6.60 us: 1.05x faster                                                                 |
| django_template            | 36.4 ms                                                      | 34.7 ms: 1.05x faster                                                                 |
| shortest_path              | 460 ms                                                       | 440 ms: 1.05x faster                                                                  |
| genshi_xml                 | 57.1 ms                                                      | 54.7 ms: 1.04x faster                                                                 |
| mako                       | 10.4 ms                                                      | 9.95 ms: 1.04x faster                                                                 |
| scimark_lu                 | 98.7 ms                                                      | 94.7 ms: 1.04x faster                                                                 |
| pathlib                    | 17.5 ms                                                      | 16.8 ms: 1.04x faster                                                                 |
| json                       | 5.69 ms                                                      | 5.48 ms: 1.04x faster                                                                 |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                                 |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                                 |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                                |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                                  |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                                  |
| chaos                      | 60.2 ms                                                      | 58.9 ms: 1.02x faster                                                                 |
| sympy_expand               | 509 ms                                                       | 499 ms: 1.02x faster                                                                  |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 8.82 ms: 1.02x faster                                                                 |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                                  |
| fannkuch                   | 363 ms                                                       | 359 ms: 1.01x faster                                                                  |
| comprehensions             | 17.0 us                                                      | 17.2 us: 1.01x slower                                                                 |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                                  |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                                |
| regex_effbot               | 3.67 ms                                                      | 3.73 ms: 1.02x slower                                                                 |
| json_dumps                 | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                                                 |
| nqueens                    | 90.7 ms                                                      | 93.1 ms: 1.03x slower                                                                 |
| coverage                   | 80.0 ms                                                      | 82.3 ms: 1.03x slower                                                                 |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                                |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                                  |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                                 |
| raytrace                   | 273 ms                                                       | 283 ms: 1.04x slower                                                                  |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.96 ms: 1.04x slower                                                                 |
| crypto_pyaes               | 73.3 ms                                                      | 77.5 ms: 1.06x slower                                                                 |
| json_loads                 | 24.7 us                                                      | 26.8 us: 1.08x slower                                                                 |
| create_gc_cycles           | 2.68 ms                                                      | 2.93 ms: 1.09x slower                                                                 |
| nbody                      | 89.3 ms                                                      | 97.5 ms: 1.09x slower                                                                 |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.33x slower                                                                 |
| gc_traversal               | 4.74 ms                                                      | 6.74 ms: 1.42x slower                                                                 |
| subparsers                 | 17.5 ms                                                      | 43.0 ms: 2.46x slower                                                                 |
| telco                      | 8.79 ms                                                      | 162 ms: 18.38x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                          |

Benchmark hidden because not significant (2): djangocms, typing_runtime_protocols
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250725-3.15.0a0-021fc09-JIT/bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x