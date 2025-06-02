# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.097x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 311 ms: 1.06x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.12 sec: 1.10x slower                                                      |
| html5lib       | 73.5 ms                                                      | 71.6 ms: 1.03x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.21 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 364 ms: 1.28x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 358 ms: 1.27x faster                                                        |
| async_tree_none            | 376 ms                                                       | 307 ms: 1.22x faster                                                        |
| async_tree_io              | 843 ms                                                       | 689 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 702 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 297 ms: 1.16x faster                                                        |
| async_generators           | 457 ms                                                       | 444 ms: 1.03x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 655 ms: 1.09x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 24.4 ms: 1.13x slower                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 662 ms: 1.14x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 80.6 ms: 1.01x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| nbody          | 89.3 ms                                                      | 101 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.36 ms: 1.09x faster                                                       |
| regex_dna      | 247 ms                                                       | 243 ms: 1.02x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 27.5 ms: 1.05x slower                                                       |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.38 sec: 1.03x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 239 us: 1.10x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 168 ms: 1.12x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 117 ms: 1.14x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 378 us: 1.17x slower                                                        |
| json_loads           | 24.7 us                                                      | 29.1 us: 1.18x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 72.6 ms: 1.19x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 107 ms: 1.23x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 14.4 ms: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 9.40 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 27.7 ms: 1.06x slower                                                       |
| genshi_xml      | 57.1 ms                                                      | 60.5 ms: 1.06x slower                                                       |
| django_template | 36.4 ms                                                      | 42.2 ms: 1.16x slower                                                       |
| mako            | 10.4 ms                                                      | 13.7 ms: 1.32x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.55 sec: 1.64x faster                                                      |
| go                         | 162 ms                                                       | 127 ms: 1.28x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 364 ms: 1.28x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 358 ms: 1.27x faster                                                        |
| deepcopy                   | 392 us                                                       | 317 us: 1.24x faster                                                        |
| async_tree_none            | 376 ms                                                       | 307 ms: 1.22x faster                                                        |
| async_tree_io              | 843 ms                                                       | 689 ms: 1.22x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 32.2 us: 1.20x faster                                                       |
| async_tree_io_tg           | 831 ms                                                       | 702 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 297 ms: 1.16x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.36 ms: 1.09x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 63.1 ms: 1.08x faster                                                       |
| pyflate                    | 503 ms                                                       | 469 ms: 1.07x faster                                                        |
| generators                 | 33.6 ms                                                      | 31.7 ms: 1.06x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.38 sec: 1.03x faster                                                      |
| async_generators           | 457 ms                                                       | 444 ms: 1.03x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 71.6 ms: 1.03x faster                                                       |
| regex_dna                  | 247 ms                                                       | 243 ms: 1.02x faster                                                        |
| float                      | 81.3 ms                                                      | 80.6 ms: 1.01x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.50 ms: 1.01x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.52 us: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| scimark_sor                | 123 ms                                                       | 124 ms: 1.01x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 3.46 ms: 1.01x slower                                                       |
| richards                   | 52.9 ms                                                      | 53.9 ms: 1.02x slower                                                       |
| richards_super             | 59.6 ms                                                      | 60.8 ms: 1.02x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                       |
| json                       | 5.69 ms                                                      | 5.93 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 9.40 ms: 1.05x slower                                                       |
| regex_v8                   | 26.1 ms                                                      | 27.5 ms: 1.05x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 27.7 ms: 1.06x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 60.5 ms: 1.06x slower                                                       |
| 2to3                       | 293 ms                                                       | 311 ms: 1.06x slower                                                        |
| meteor_contest             | 130 ms                                                       | 139 ms: 1.07x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.33 sec: 1.07x slower                                                      |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| sphinx                     | 1.12 sec                                                     | 1.21 sec: 1.08x slower                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 655 ms: 1.09x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 169 ms: 1.09x slower                                                        |
| comprehensions             | 17.0 us                                                      | 18.6 us: 1.09x slower                                                       |
| telco                      | 8.79 ms                                                      | 9.64 ms: 1.10x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 239 us: 1.10x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.04 ms: 1.10x slower                                                       |
| docutils                   | 2.83 sec                                                     | 3.12 sec: 1.10x slower                                                      |
| sympy_str                  | 298 ms                                                       | 330 ms: 1.11x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.65 sec: 1.11x slower                                                      |
| create_gc_cycles           | 2.68 ms                                                      | 2.99 ms: 1.11x slower                                                       |
| pathlib                    | 17.5 ms                                                      | 19.5 ms: 1.11x slower                                                       |
| xml_etree_parse            | 150 ms                                                       | 168 ms: 1.12x slower                                                        |
| sympy_expand               | 509 ms                                                       | 571 ms: 1.12x slower                                                        |
| thrift                     | 901 us                                                       | 1.01 ms: 1.13x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 24.4 ms: 1.13x slower                                                       |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.13x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 117 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 662 ms: 1.14x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 76.1 ms: 1.15x slower                                                       |
| django_template            | 36.4 ms                                                      | 42.2 ms: 1.16x slower                                                       |
| scimark_fft                | 328 ms                                                       | 383 ms: 1.17x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 378 us: 1.17x slower                                                        |
| sqlite_synth               | 2.91 us                                                      | 3.40 us: 1.17x slower                                                       |
| spectral_norm              | 97.0 ms                                                      | 114 ms: 1.18x slower                                                        |
| json_loads                 | 24.7 us                                                      | 29.1 us: 1.18x slower                                                       |
| logging_simple             | 6.39 us                                                      | 7.55 us: 1.18x slower                                                       |
| chaos                      | 60.2 ms                                                      | 71.5 ms: 1.19x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 72.6 ms: 1.19x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 108 ms: 1.19x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 5.65 ms: 1.19x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 87.9 ms: 1.20x slower                                                       |
| logging_format             | 6.94 us                                                      | 8.33 us: 1.20x slower                                                       |
| raytrace                   | 273 ms                                                       | 331 ms: 1.21x slower                                                        |
| many_optionals             | 930 us                                                       | 1.14 ms: 1.22x slower                                                       |
| pprint_pformat             | 1.72 sec                                                     | 2.11 sec: 1.23x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 1.03 sec: 1.23x slower                                                      |
| coverage                   | 80.0 ms                                                      | 98.2 ms: 1.23x slower                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 107 ms: 1.23x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 210 us: 1.24x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 123 ms: 1.25x slower                                                        |
| fannkuch                   | 363 ms                                                       | 463 ms: 1.28x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 14.4 ms: 1.29x slower                                                       |
| mako                       | 10.4 ms                                                      | 13.7 ms: 1.32x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 6.46 ms: 1.35x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 28.2 ms: 1.61x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 676 ns: 6.91x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.00 sec: 195.25x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmark hidden because not significant (5): connected_components, shortest_path, djangocms, pylint, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.097x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.08x