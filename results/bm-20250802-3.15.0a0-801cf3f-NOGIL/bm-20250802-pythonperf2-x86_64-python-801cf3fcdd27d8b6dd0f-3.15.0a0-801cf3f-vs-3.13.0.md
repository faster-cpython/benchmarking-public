# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.055x slower
- HPT reliability: 95.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 316 ms: 1.08x slower                                                        |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 294 ms: 1.59x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 528 ms: 1.57x faster                                                        |
| async_tree_io              | 843 ms                                                       | 558 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 232 ms: 1.49x faster                                                        |
| async_tree_none            | 376 ms                                                       | 263 ms: 1.43x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 320 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 467 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 495 ms: 1.22x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 376 ms: 1.03x faster                                                        |
| async_generators           | 457 ms                                                       | 463 ms: 1.01x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.4 ms: 1.14x faster                                                       |
| pidigits       | 252 ms                                                       | 251 ms: 1.01x faster                                                        |
| nbody          | 89.3 ms                                                      | 127 ms: 1.43x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| regex_dna      | 247 ms                                                       | 234 ms: 1.06x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.55 ms: 1.04x faster                                                       |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 87.5 ms: 1.17x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.30 sec: 1.07x faster                                                      |
| json_dumps           | 11.1 ms                                                      | 12.0 ms: 1.07x slower                                                       |
| unpickle_pure_python | 217 us                                                       | 237 us: 1.09x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 362 us: 1.12x slower                                                        |
| json_loads           | 24.7 us                                                      | 27.9 us: 1.13x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 69.9 ms: 1.14x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 99.6 ms: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 11.7 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 65.8 ms: 1.15x slower                                                       |
| genshi_text     | 26.2 ms                                                      | 30.3 ms: 1.15x slower                                                       |
| django_template | 36.4 ms                                                      | 43.0 ms: 1.18x slower                                                       |
| mako            | 10.4 ms                                                      | 17.5 ms: 1.68x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.28x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.22 ms: 2.13x faster                                                       |
| mdp                        | 2.54 sec                                                     | 1.45 sec: 1.75x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 294 ms: 1.59x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 528 ms: 1.57x faster                                                        |
| async_tree_io              | 843 ms                                                       | 558 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 232 ms: 1.49x faster                                                        |
| async_tree_none            | 376 ms                                                       | 263 ms: 1.43x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 320 ms: 1.42x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.03 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 467 ms: 1.25x faster                                                        |
| deepcopy                   | 392 us                                                       | 315 us: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 495 ms: 1.22x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 87.5 ms: 1.17x faster                                                       |
| go                         | 162 ms                                                       | 139 ms: 1.17x faster                                                        |
| float                      | 81.3 ms                                                      | 71.4 ms: 1.14x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 34.2 us: 1.13x faster                                                       |
| generators                 | 33.6 ms                                                      | 29.9 ms: 1.12x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.60 us: 1.12x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 62.1 ms: 1.10x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.30 sec: 1.07x faster                                                      |
| pyflate                    | 503 ms                                                       | 476 ms: 1.06x faster                                                        |
| regex_dna                  | 247 ms                                                       | 234 ms: 1.06x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                       |
| scimark_sor                | 123 ms                                                       | 118 ms: 1.05x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.8 ms: 1.05x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.55 ms: 1.04x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 376 ms: 1.03x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.48 us: 1.02x faster                                                       |
| json                       | 5.69 ms                                                      | 5.62 ms: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 251 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.07 sec: 1.00x faster                                                      |
| async_generators           | 457 ms                                                       | 463 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| pycparser                  | 1.24 sec                                                     | 1.28 sec: 1.03x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 878 ms: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| richards                   | 52.9 ms                                                      | 55.6 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.82 sec: 1.06x slower                                                      |
| logging_simple             | 6.39 us                                                      | 6.79 us: 1.06x slower                                                       |
| scimark_fft                | 328 ms                                                       | 349 ms: 1.06x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 25.1 ms: 1.07x slower                                                       |
| comprehensions             | 17.0 us                                                      | 18.2 us: 1.07x slower                                                       |
| richards_super             | 59.6 ms                                                      | 64.0 ms: 1.07x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 12.0 ms: 1.07x slower                                                       |
| k_core                     | 2.17 sec                                                     | 2.33 sec: 1.07x slower                                                      |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| 2to3                       | 293 ms                                                       | 316 ms: 1.08x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 3.70 ms: 1.08x slower                                                       |
| spectral_norm              | 97.0 ms                                                      | 105 ms: 1.09x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 237 us: 1.09x slower                                                        |
| sympy_expand               | 509 ms                                                       | 559 ms: 1.10x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.63 us: 1.10x slower                                                       |
| sympy_str                  | 298 ms                                                       | 328 ms: 1.10x slower                                                        |
| thrift                     | 901 us                                                       | 993 us: 1.10x slower                                                        |
| chaos                      | 60.2 ms                                                      | 66.4 ms: 1.10x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 171 ms: 1.11x slower                                                        |
| connected_components       | 432 ms                                                       | 485 ms: 1.12x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 362 us: 1.12x slower                                                        |
| meteor_contest             | 130 ms                                                       | 145 ms: 1.12x slower                                                        |
| shortest_path              | 460 ms                                                       | 517 ms: 1.12x slower                                                        |
| json_loads                 | 24.7 us                                                      | 27.9 us: 1.13x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 69.9 ms: 1.14x slower                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 99.6 ms: 1.15x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 65.8 ms: 1.15x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 30.3 ms: 1.15x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 105 ms: 1.16x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 116 ms: 1.18x slower                                                        |
| django_template            | 36.4 ms                                                      | 43.0 ms: 1.18x slower                                                       |
| raytrace                   | 273 ms                                                       | 323 ms: 1.18x slower                                                        |
| python_startup             | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 79.7 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 206 us: 1.22x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.95 ms: 1.25x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 93.8 ms: 1.28x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 11.7 ms: 1.31x slower                                                       |
| fannkuch                   | 363 ms                                                       | 484 ms: 1.33x slower                                                        |
| many_optionals             | 930 us                                                       | 1.28 ms: 1.37x slower                                                       |
| nbody                      | 89.3 ms                                                      | 127 ms: 1.43x slower                                                        |
| coverage                   | 80.0 ms                                                      | 117 ms: 1.46x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.40 ms: 1.49x slower                                                       |
| mako                       | 10.4 ms                                                      | 17.5 ms: 1.68x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 48.8 ms: 2.79x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 57.2 ms: 11.17x slower                                                      |
| telco                      | 8.79 ms                                                      | 175 ms: 19.91x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (4): pylint, logging_silent, hexiom, sphinx
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.055x slower

# HPT report

- Reliability score: 95.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.30x