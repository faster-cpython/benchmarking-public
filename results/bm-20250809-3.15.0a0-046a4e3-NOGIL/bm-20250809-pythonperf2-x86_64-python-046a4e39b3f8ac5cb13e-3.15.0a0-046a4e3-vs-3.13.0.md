# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.055x slower
- HPT reliability: 98.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 316 ms: 1.08x slower                                                        |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                      |
| html5lib       | 73.5 ms                                                      | 70.7 ms: 1.04x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 295 ms: 1.58x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 531 ms: 1.57x faster                                                        |
| async_tree_io              | 843 ms                                                       | 561 ms: 1.50x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 232 ms: 1.49x faster                                                        |
| async_tree_none            | 376 ms                                                       | 263 ms: 1.43x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 468 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 496 ms: 1.22x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 391 ms: 1.01x slower                                                        |
| async_generators           | 457 ms                                                       | 468 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.7 ms: 1.13x faster                                                       |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                        |
| nbody          | 89.3 ms                                                      | 125 ms: 1.40x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 22.8 ms: 1.14x faster                                                       |
| regex_dna      | 247 ms                                                       | 222 ms: 1.11x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.53 ms: 1.04x faster                                                       |
| regex_compile  | 143 ms                                                       | 153 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 86.1 ms: 1.19x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 132 ms: 1.14x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.33 sec: 1.06x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 241 us: 1.11x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 97.5 ms: 1.13x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 364 us: 1.13x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 69.7 ms: 1.14x slower                                                       |
| json_loads           | 24.7 us                                                      | 29.0 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.2 ms: 1.21x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 65.2 ms: 1.14x slower                                                       |
| genshi_text     | 26.2 ms                                                      | 30.6 ms: 1.17x slower                                                       |
| django_template | 36.4 ms                                                      | 42.9 ms: 1.18x slower                                                       |
| mako            | 10.4 ms                                                      | 17.6 ms: 1.70x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.28x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.24 ms: 2.12x faster                                                       |
| mdp                        | 2.54 sec                                                     | 1.45 sec: 1.75x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 295 ms: 1.58x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 531 ms: 1.57x faster                                                        |
| async_tree_io              | 843 ms                                                       | 561 ms: 1.50x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 232 ms: 1.49x faster                                                        |
| async_tree_none            | 376 ms                                                       | 263 ms: 1.43x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 320 ms: 1.41x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.02 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 468 ms: 1.24x faster                                                        |
| deepcopy                   | 392 us                                                       | 319 us: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 496 ms: 1.22x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 86.1 ms: 1.19x faster                                                       |
| go                         | 162 ms                                                       | 137 ms: 1.19x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.3 ms: 1.15x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 22.8 ms: 1.14x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 132 ms: 1.14x faster                                                        |
| float                      | 81.3 ms                                                      | 71.7 ms: 1.13x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.61 us: 1.11x faster                                                       |
| regex_dna                  | 247 ms                                                       | 222 ms: 1.11x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 34.8 us: 1.11x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 61.8 ms: 1.10x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.33 sec: 1.06x faster                                                      |
| pyflate                    | 503 ms                                                       | 477 ms: 1.05x faster                                                        |
| scimark_sor                | 123 ms                                                       | 117 ms: 1.05x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.53 ms: 1.04x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 70.7 ms: 1.04x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                       |
| json                       | 5.69 ms                                                      | 5.48 ms: 1.04x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 96.6 ns: 1.01x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.50 us: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 252 ms: 1.00x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.10 sec: 1.00x slower                                                      |
| hexiom                     | 6.55 ms                                                      | 6.57 ms: 1.00x slower                                                       |
| asyncio_websockets         | 388 ms                                                       | 391 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                      |
| sphinx                     | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                      |
| async_generators           | 457 ms                                                       | 468 ms: 1.02x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.28 sec: 1.03x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| richards                   | 52.9 ms                                                      | 55.4 ms: 1.05x slower                                                       |
| comprehensions             | 17.0 us                                                      | 18.0 us: 1.06x slower                                                       |
| scimark_fft                | 328 ms                                                       | 348 ms: 1.06x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 25.1 ms: 1.06x slower                                                       |
| logging_simple             | 6.39 us                                                      | 6.82 us: 1.07x slower                                                       |
| richards_super             | 59.6 ms                                                      | 63.6 ms: 1.07x slower                                                       |
| regex_compile              | 143 ms                                                       | 153 ms: 1.07x slower                                                        |
| k_core                     | 2.17 sec                                                     | 2.33 sec: 1.07x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 906 ms: 1.07x slower                                                        |
| 2to3                       | 293 ms                                                       | 316 ms: 1.08x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 3.70 ms: 1.08x slower                                                       |
| sympy_expand               | 509 ms                                                       | 554 ms: 1.09x slower                                                        |
| thrift                     | 901 us                                                       | 979 us: 1.09x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.88 sec: 1.09x slower                                                      |
| logging_format             | 6.94 us                                                      | 7.60 us: 1.10x slower                                                       |
| sympy_str                  | 298 ms                                                       | 327 ms: 1.10x slower                                                        |
| chaos                      | 60.2 ms                                                      | 66.5 ms: 1.10x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 171 ms: 1.11x slower                                                        |
| connected_components       | 432 ms                                                       | 478 ms: 1.11x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 241 us: 1.11x slower                                                        |
| shortest_path              | 460 ms                                                       | 510 ms: 1.11x slower                                                        |
| meteor_contest             | 130 ms                                                       | 145 ms: 1.12x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 97.5 ms: 1.13x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 364 us: 1.13x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 69.7 ms: 1.14x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 65.2 ms: 1.14x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 30.6 ms: 1.17x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 106 ms: 1.17x slower                                                        |
| spectral_norm              | 97.0 ms                                                      | 114 ms: 1.17x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 116 ms: 1.17x slower                                                        |
| json_loads                 | 24.7 us                                                      | 29.0 us: 1.18x slower                                                       |
| django_template            | 36.4 ms                                                      | 42.9 ms: 1.18x slower                                                       |
| python_startup             | 15.9 ms                                                      | 19.2 ms: 1.21x slower                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 80.2 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 206 us: 1.22x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.83 ms: 1.22x slower                                                       |
| raytrace                   | 273 ms                                                       | 335 ms: 1.23x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 93.0 ms: 1.27x slower                                                       |
| fannkuch                   | 363 ms                                                       | 475 ms: 1.31x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                       |
| many_optionals             | 930 us                                                       | 1.28 ms: 1.37x slower                                                       |
| nbody                      | 89.3 ms                                                      | 125 ms: 1.40x slower                                                        |
| coverage                   | 80.0 ms                                                      | 119 ms: 1.48x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.41 ms: 1.50x slower                                                       |
| mako                       | 10.4 ms                                                      | 17.6 ms: 1.70x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 48.2 ms: 2.76x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 57.7 ms: 11.26x slower                                                      |
| telco                      | 8.79 ms                                                      | 174 ms: 19.76x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (2): pylint, json_dumps
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.055x slower

# HPT report

- Reliability score: 98.10% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.31x