# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.188x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 365 ms: 1.25x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.29 sec: 1.16x slower                                                      |
| html5lib       | 73.5 ms                                                      | 76.6 ms: 1.04x slower                                                       |
| sphinx         | 1.12 sec                                                     | 1.32 sec: 1.18x slower                                                      |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 336 ms: 1.39x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 614 ms: 1.35x faster                                                        |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| async_tree_none            | 376 ms                                                       | 296 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 360 ms: 1.26x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 377 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 608 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 638 ms: 1.06x slower                                                        |
| async_generators           | 457 ms                                                       | 529 ms: 1.16x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 26.4 ms: 1.22x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 251 ms: 1.01x faster                                                        |
| float          | 81.3 ms                                                      | 81.7 ms: 1.00x slower                                                       |
| nbody          | 89.3 ms                                                      | 136 ms: 1.53x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.40 ms: 1.08x faster                                                       |
| regex_dna      | 247 ms                                                       | 242 ms: 1.02x faster                                                        |
| regex_compile  | 143 ms                                                       | 178 ms: 1.25x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 167 ms: 1.11x slower                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.78 sec: 1.13x slower                                                      |
| unpickle_pure_python | 217 us                                                       | 299 us: 1.37x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 15.6 ms: 1.40x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 456 us: 1.41x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 87.2 ms: 1.43x slower                                                       |
| json_loads           | 24.7 us                                                      | 35.6 us: 1.44x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 126 ms: 1.46x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.31x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 21.3 ms: 1.34x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 12.7 ms: 1.41x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 72.9 ms: 1.28x slower                                                       |
| genshi_text     | 26.2 ms                                                      | 35.7 ms: 1.36x slower                                                       |
| django_template | 36.4 ms                                                      | 52.7 ms: 1.45x slower                                                       |
| mako            | 10.4 ms                                                      | 19.8 ms: 1.91x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.48x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 3.22 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 336 ms: 1.39x faster                                                        |
| mdp                        | 2.54 sec                                                     | 1.83 sec: 1.39x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 614 ms: 1.35x faster                                                        |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.05 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| async_tree_none            | 376 ms                                                       | 296 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 360 ms: 1.26x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.40 ms: 1.08x faster                                                       |
| go                         | 162 ms                                                       | 154 ms: 1.05x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 377 ms: 1.03x faster                                                        |
| deepcopy                   | 392 us                                                       | 383 us: 1.02x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 66.7 ms: 1.02x faster                                                       |
| regex_dna                  | 247 ms                                                       | 242 ms: 1.02x faster                                                        |
| pidigits                   | 252 ms                                                       | 251 ms: 1.01x faster                                                        |
| float                      | 81.3 ms                                                      | 81.7 ms: 1.00x slower                                                       |
| html5lib                   | 73.5 ms                                                      | 76.6 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 608 ms: 1.04x slower                                                        |
| sqlite_synth               | 2.91 us                                                      | 3.07 us: 1.06x slower                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 638 ms: 1.06x slower                                                        |
| pyflate                    | 503 ms                                                       | 535 ms: 1.06x slower                                                        |
| deepcopy_memo              | 38.6 us                                                      | 41.1 us: 1.06x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| generators                 | 33.6 ms                                                      | 36.1 ms: 1.07x slower                                                       |
| xml_etree_parse            | 150 ms                                                       | 167 ms: 1.11x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.40 sec: 1.12x slower                                                      |
| k_core                     | 2.17 sec                                                     | 2.44 sec: 1.12x slower                                                      |
| tomli_loads                | 2.46 sec                                                     | 2.78 sec: 1.13x slower                                                      |
| pylint                     | 347 ms                                                       | 396 ms: 1.14x slower                                                        |
| connected_components       | 432 ms                                                       | 494 ms: 1.14x slower                                                        |
| pathlib                    | 17.5 ms                                                      | 20.2 ms: 1.15x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 7.57 ms: 1.16x slower                                                       |
| async_generators           | 457 ms                                                       | 529 ms: 1.16x slower                                                        |
| docutils                   | 2.83 sec                                                     | 3.29 sec: 1.16x slower                                                      |
| shortest_path              | 460 ms                                                       | 536 ms: 1.16x slower                                                        |
| sphinx                     | 1.12 sec                                                     | 1.32 sec: 1.18x slower                                                      |
| sympy_integrate            | 23.6 ms                                                      | 27.9 ms: 1.19x slower                                                       |
| json                       | 5.69 ms                                                      | 6.77 ms: 1.19x slower                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 4.25 us: 1.20x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 4.14 ms: 1.21x slower                                                       |
| meteor_contest             | 130 ms                                                       | 158 ms: 1.22x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 26.4 ms: 1.22x slower                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 6.27 sec: 1.23x slower                                                      |
| scimark_sor                | 123 ms                                                       | 153 ms: 1.24x slower                                                        |
| 2to3                       | 293 ms                                                       | 365 ms: 1.25x slower                                                        |
| regex_compile              | 143 ms                                                       | 178 ms: 1.25x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 72.9 ms: 1.28x slower                                                       |
| richards                   | 52.9 ms                                                      | 67.6 ms: 1.28x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 198 ms: 1.28x slower                                                        |
| sympy_str                  | 298 ms                                                       | 389 ms: 1.30x slower                                                        |
| many_optionals             | 930 us                                                       | 1.22 ms: 1.31x slower                                                       |
| sympy_expand               | 509 ms                                                       | 674 ms: 1.32x slower                                                        |
| richards_super             | 59.6 ms                                                      | 79.4 ms: 1.33x slower                                                       |
| python_startup             | 15.9 ms                                                      | 21.3 ms: 1.34x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 35.7 ms: 1.36x slower                                                       |
| comprehensions             | 17.0 us                                                      | 23.2 us: 1.37x slower                                                       |
| thrift                     | 901 us                                                       | 1.23 ms: 1.37x slower                                                       |
| logging_simple             | 6.39 us                                                      | 8.75 us: 1.37x slower                                                       |
| chaos                      | 60.2 ms                                                      | 82.7 ms: 1.37x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 299 us: 1.37x slower                                                        |
| telco                      | 8.79 ms                                                      | 12.2 ms: 1.39x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 126 ms: 1.39x slower                                                        |
| scimark_fft                | 328 ms                                                       | 459 ms: 1.40x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 15.6 ms: 1.40x slower                                                       |
| logging_format             | 6.94 us                                                      | 9.76 us: 1.41x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 456 us: 1.41x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 12.7 ms: 1.41x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 87.2 ms: 1.43x slower                                                       |
| json_loads                 | 24.7 us                                                      | 35.6 us: 1.44x slower                                                       |
| django_template            | 36.4 ms                                                      | 52.7 ms: 1.45x slower                                                       |
| raytrace                   | 273 ms                                                       | 396 ms: 1.45x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 1.23 sec: 1.46x slower                                                      |
| xml_etree_generate         | 86.5 ms                                                      | 126 ms: 1.46x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.53 sec: 1.47x slower                                                      |
| spectral_norm              | 97.0 ms                                                      | 146 ms: 1.50x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 149 ms: 1.51x slower                                                        |
| fannkuch                   | 363 ms                                                       | 554 ms: 1.52x slower                                                        |
| nbody                      | 89.3 ms                                                      | 136 ms: 1.53x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 101 ms: 1.53x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 261 us: 1.55x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 116 ms: 1.59x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.50 ms: 1.59x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 7.83 ms: 1.64x slower                                                       |
| coverage                   | 80.0 ms                                                      | 135 ms: 1.69x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 32.1 ms: 1.84x slower                                                       |
| mako                       | 10.4 ms                                                      | 19.8 ms: 1.91x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 791 ns: 8.08x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 62.1 ms: 12.13x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.26x slower                                                                |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.188x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.32x