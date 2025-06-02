# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.230x faster
- HPT reliability: 98.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 320 ms: 1.09x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.17 sec: 1.12x slower                                                      |
| html5lib       | 73.5 ms                                                      | 70.9 ms: 1.04x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.22 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 368 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 365 ms: 1.24x faster                                                        |
| async_tree_io              | 843 ms                                                       | 696 ms: 1.21x faster                                                        |
| async_tree_none            | 376 ms                                                       | 314 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 705 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 301 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 468 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 23.9 ms: 1.11x slower                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 677 ms: 1.12x slower                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 680 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 72.7 ms: 1.12x faster                                                       |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 107 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.32 ms: 1.11x faster                                                       |
| regex_dna      | 247 ms                                                       | 243 ms: 1.02x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 27.3 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.31 sec: 1.07x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 164 ms: 1.09x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 239 us: 1.10x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 70.1 ms: 1.15x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 380 us: 1.18x slower                                                        |
| json_loads           | 24.7 us                                                      | 29.4 us: 1.19x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 104 ms: 1.20x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 14.2 ms: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.5 ms: 1.04x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 9.44 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 63.0 ms: 1.10x slower                                                       |
| genshi_text     | 26.2 ms                                                      | 29.2 ms: 1.11x slower                                                       |
| django_template | 36.4 ms                                                      | 42.4 ms: 1.17x slower                                                       |
| mako            | 10.4 ms                                                      | 13.5 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.17x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pprint_pformat             | 1.72 sec                                                     | 1.83 us: 940913.45x faster                                                  |
| pprint_safe_repr           | 843 ms                                                       | 1.12 us: 752291.49x faster                                                  |
| mdp                        | 2.54 sec                                                     | 1.57 sec: 1.62x faster                                                      |
| richards                   | 52.9 ms                                                      | 40.6 ms: 1.30x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 368 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 365 ms: 1.24x faster                                                        |
| richards_super             | 59.6 ms                                                      | 47.9 ms: 1.24x faster                                                       |
| deepcopy                   | 392 us                                                       | 320 us: 1.23x faster                                                        |
| async_tree_io              | 843 ms                                                       | 696 ms: 1.21x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 32.0 us: 1.21x faster                                                       |
| async_tree_none            | 376 ms                                                       | 314 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 705 ms: 1.18x faster                                                        |
| go                         | 162 ms                                                       | 141 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 301 ms: 1.15x faster                                                        |
| float                      | 81.3 ms                                                      | 72.7 ms: 1.12x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.32 ms: 1.11x faster                                                       |
| pyflate                    | 503 ms                                                       | 462 ms: 1.09x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.20 ms: 1.07x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.31 sec: 1.07x faster                                                      |
| dulwich_log                | 68.2 ms                                                      | 64.0 ms: 1.06x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 70.9 ms: 1.04x faster                                                       |
| connected_components       | 432 ms                                                       | 419 ms: 1.03x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                      |
| generators                 | 33.6 ms                                                      | 33.0 ms: 1.02x faster                                                       |
| shortest_path              | 460 ms                                                       | 452 ms: 1.02x faster                                                        |
| regex_dna                  | 247 ms                                                       | 243 ms: 1.02x faster                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| djangocms                  | 65.3 us                                                      | 66.3 us: 1.02x slower                                                       |
| async_generators           | 457 ms                                                       | 468 ms: 1.02x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.5 ms: 1.04x slower                                                       |
| regex_v8                   | 26.1 ms                                                      | 27.3 ms: 1.05x slower                                                       |
| json                       | 5.69 ms                                                      | 5.98 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 9.44 ms: 1.05x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 6.93 ms: 1.06x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.34 sec: 1.07x slower                                                      |
| sphinx                     | 1.12 sec                                                     | 1.22 sec: 1.08x slower                                                      |
| xml_etree_parse            | 150 ms                                                       | 164 ms: 1.09x slower                                                        |
| 2to3                       | 293 ms                                                       | 320 ms: 1.09x slower                                                        |
| telco                      | 8.79 ms                                                      | 9.67 ms: 1.10x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 239 us: 1.10x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 63.0 ms: 1.10x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 23.9 ms: 1.11x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 172 ms: 1.11x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 29.2 ms: 1.11x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.99 ms: 1.12x slower                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 5.68 sec: 1.12x slower                                                      |
| bench_thread_pool          | 942 us                                                       | 1.05 ms: 1.12x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 677 ms: 1.12x slower                                                        |
| docutils                   | 2.83 sec                                                     | 3.17 sec: 1.12x slower                                                      |
| meteor_contest             | 130 ms                                                       | 146 ms: 1.12x slower                                                        |
| sympy_str                  | 298 ms                                                       | 336 ms: 1.13x slower                                                        |
| pathlib                    | 17.5 ms                                                      | 19.8 ms: 1.13x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 70.1 ms: 1.15x slower                                                       |
| sympy_expand               | 509 ms                                                       | 586 ms: 1.15x slower                                                        |
| thrift                     | 901 us                                                       | 1.04 ms: 1.15x slower                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 76.3 ms: 1.15x slower                                                       |
| sqlite_synth               | 2.91 us                                                      | 3.36 us: 1.16x slower                                                       |
| django_template            | 36.4 ms                                                      | 42.4 ms: 1.17x slower                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 680 ms: 1.17x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 380 us: 1.18x slower                                                        |
| json_loads                 | 24.7 us                                                      | 29.4 us: 1.19x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 5.70 ms: 1.20x slower                                                       |
| nbody                      | 89.3 ms                                                      | 107 ms: 1.20x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 104 ms: 1.20x slower                                                        |
| coverage                   | 80.0 ms                                                      | 96.4 ms: 1.21x slower                                                       |
| logging_simple             | 6.39 us                                                      | 7.73 us: 1.21x slower                                                       |
| scimark_fft                | 328 ms                                                       | 397 ms: 1.21x slower                                                        |
| spectral_norm              | 97.0 ms                                                      | 118 ms: 1.22x slower                                                        |
| chaos                      | 60.2 ms                                                      | 73.4 ms: 1.22x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.22x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 121 ms: 1.22x slower                                                        |
| many_optionals             | 930 us                                                       | 1.15 ms: 1.23x slower                                                       |
| logging_format             | 6.94 us                                                      | 8.59 us: 1.24x slower                                                       |
| comprehensions             | 17.0 us                                                      | 21.1 us: 1.24x slower                                                       |
| raytrace                   | 273 ms                                                       | 339 ms: 1.24x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 14.2 ms: 1.27x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 216 us: 1.28x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 93.9 ms: 1.28x slower                                                       |
| mako                       | 10.4 ms                                                      | 13.5 ms: 1.30x slower                                                       |
| fannkuch                   | 363 ms                                                       | 479 ms: 1.32x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 6.30 ms: 1.32x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 28.6 ms: 1.64x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 668 ns: 6.83x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 2.17 sec: 424.08x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.17x faster                                                                |

Benchmark hidden because not significant (4): deepcopy_reduce, scimark_sor, asyncio_websockets, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.230x faster

# HPT report

- Reliability score: 98.86% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x