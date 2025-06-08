# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.191x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 363 ms: 1.24x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.24 sec: 1.15x slower                                                      |
| html5lib       | 73.5 ms                                                      | 76.6 ms: 1.04x slower                                                       |
| sphinx         | 1.12 sec                                                     | 1.32 sec: 1.18x slower                                                      |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 612 ms: 1.36x faster                                                        |
| async_tree_io              | 843 ms                                                       | 641 ms: 1.32x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                        |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 627 ms: 1.08x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 656 ms: 1.09x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 24.9 ms: 1.16x slower                                                       |
| async_generators           | 457 ms                                                       | 540 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| nbody          | 89.3 ms                                                      | 144 ms: 1.61x slower                                                        |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.44 ms: 1.07x faster                                                       |
| regex_dna      | 247 ms                                                       | 249 ms: 1.01x slower                                                        |
| regex_v8       | 26.1 ms                                                      | 26.8 ms: 1.03x slower                                                       |
| regex_compile  | 143 ms                                                       | 178 ms: 1.25x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 168 ms: 1.12x slower                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.77 sec: 1.12x slower                                                      |
| unpickle_pure_python | 217 us                                                       | 296 us: 1.36x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 450 us: 1.39x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 15.6 ms: 1.40x slower                                                       |
| json_loads           | 24.7 us                                                      | 36.0 us: 1.46x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 127 ms: 1.46x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 90.2 ms: 1.48x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.31x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 21.3 ms: 1.34x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 12.7 ms: 1.42x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.38x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 78.1 ms: 1.37x slower                                                       |
| genshi_text     | 26.2 ms                                                      | 36.9 ms: 1.41x slower                                                       |
| django_template | 36.4 ms                                                      | 52.5 ms: 1.44x slower                                                       |
| mako            | 10.4 ms                                                      | 20.0 ms: 1.93x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.52x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 3.01 ms: 1.57x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                        |
| mdp                        | 2.54 sec                                                     | 1.83 sec: 1.39x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 612 ms: 1.36x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.03 ms: 1.32x faster                                                       |
| async_tree_io              | 843 ms                                                       | 641 ms: 1.32x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                        |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.44 ms: 1.07x faster                                                       |
| go                         | 162 ms                                                       | 153 ms: 1.06x faster                                                        |
| deepcopy                   | 392 us                                                       | 384 us: 1.02x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 67.7 ms: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| regex_dna                  | 247 ms                                                       | 249 ms: 1.01x slower                                                        |
| regex_v8                   | 26.1 ms                                                      | 26.8 ms: 1.03x slower                                                       |
| html5lib                   | 73.5 ms                                                      | 76.6 ms: 1.04x slower                                                       |
| pyflate                    | 503 ms                                                       | 534 ms: 1.06x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| sqlite_synth               | 2.91 us                                                      | 3.12 us: 1.07x slower                                                       |
| generators                 | 33.6 ms                                                      | 36.3 ms: 1.08x slower                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 627 ms: 1.08x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 656 ms: 1.09x slower                                                        |
| deepcopy_memo              | 38.6 us                                                      | 42.1 us: 1.09x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.38 sec: 1.11x slower                                                      |
| xml_etree_parse            | 150 ms                                                       | 168 ms: 1.12x slower                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.77 sec: 1.12x slower                                                      |
| k_core                     | 2.17 sec                                                     | 2.44 sec: 1.12x slower                                                      |
| pylint                     | 347 ms                                                       | 392 ms: 1.13x slower                                                        |
| docutils                   | 2.83 sec                                                     | 3.24 sec: 1.15x slower                                                      |
| hexiom                     | 6.55 ms                                                      | 7.54 ms: 1.15x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 24.9 ms: 1.16x slower                                                       |
| connected_components       | 432 ms                                                       | 500 ms: 1.16x slower                                                        |
| pathlib                    | 17.5 ms                                                      | 20.3 ms: 1.16x slower                                                       |
| shortest_path              | 460 ms                                                       | 535 ms: 1.16x slower                                                        |
| sphinx                     | 1.12 sec                                                     | 1.32 sec: 1.18x slower                                                      |
| sympy_integrate            | 23.6 ms                                                      | 27.7 ms: 1.18x slower                                                       |
| async_generators           | 457 ms                                                       | 540 ms: 1.18x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 4.07 ms: 1.19x slower                                                       |
| json                       | 5.69 ms                                                      | 6.80 ms: 1.20x slower                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 4.26 us: 1.20x slower                                                       |
| meteor_contest             | 130 ms                                                       | 159 ms: 1.23x slower                                                        |
| scimark_sor                | 123 ms                                                       | 151 ms: 1.23x slower                                                        |
| 2to3                       | 293 ms                                                       | 363 ms: 1.24x slower                                                        |
| richards                   | 52.9 ms                                                      | 65.8 ms: 1.24x slower                                                       |
| regex_compile              | 143 ms                                                       | 178 ms: 1.25x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.35 sec: 1.25x slower                                                      |
| sympy_sum                  | 155 ms                                                       | 198 ms: 1.28x slower                                                        |
| sympy_str                  | 298 ms                                                       | 388 ms: 1.30x slower                                                        |
| richards_super             | 59.6 ms                                                      | 77.8 ms: 1.31x slower                                                       |
| many_optionals             | 930 us                                                       | 1.22 ms: 1.31x slower                                                       |
| sympy_expand               | 509 ms                                                       | 668 ms: 1.31x slower                                                        |
| python_startup             | 15.9 ms                                                      | 21.3 ms: 1.34x slower                                                       |
| logging_simple             | 6.39 us                                                      | 8.67 us: 1.36x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 296 us: 1.36x slower                                                        |
| thrift                     | 901 us                                                       | 1.23 ms: 1.36x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 78.1 ms: 1.37x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 125 ms: 1.38x slower                                                        |
| comprehensions             | 17.0 us                                                      | 23.5 us: 1.38x slower                                                       |
| chaos                      | 60.2 ms                                                      | 83.2 ms: 1.38x slower                                                       |
| telco                      | 8.79 ms                                                      | 12.2 ms: 1.39x slower                                                       |
| logging_format             | 6.94 us                                                      | 9.63 us: 1.39x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 450 us: 1.39x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 15.6 ms: 1.40x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 36.9 ms: 1.41x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 12.7 ms: 1.42x slower                                                       |
| scimark_fft                | 328 ms                                                       | 469 ms: 1.43x slower                                                        |
| raytrace                   | 273 ms                                                       | 392 ms: 1.44x slower                                                        |
| django_template            | 36.4 ms                                                      | 52.5 ms: 1.44x slower                                                       |
| json_loads                 | 24.7 us                                                      | 36.0 us: 1.46x slower                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 127 ms: 1.46x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 1.24 sec: 1.47x slower                                                      |
| xml_etree_process          | 61.2 ms                                                      | 90.2 ms: 1.48x slower                                                       |
| pprint_pformat             | 1.72 sec                                                     | 2.54 sec: 1.48x slower                                                      |
| spectral_norm              | 97.0 ms                                                      | 145 ms: 1.50x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 150 ms: 1.52x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 258 us: 1.52x slower                                                        |
| fannkuch                   | 363 ms                                                       | 571 ms: 1.57x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 105 ms: 1.58x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.50 ms: 1.59x slower                                                       |
| nbody                      | 89.3 ms                                                      | 144 ms: 1.61x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 119 ms: 1.62x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 8.21 ms: 1.72x slower                                                       |
| coverage                   | 80.0 ms                                                      | 139 ms: 1.74x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 31.9 ms: 1.82x slower                                                       |
| mako                       | 10.4 ms                                                      | 20.0 ms: 1.93x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 793 ns: 8.10x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 61.5 ms: 12.01x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.26x slower                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, float
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.191x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.32x