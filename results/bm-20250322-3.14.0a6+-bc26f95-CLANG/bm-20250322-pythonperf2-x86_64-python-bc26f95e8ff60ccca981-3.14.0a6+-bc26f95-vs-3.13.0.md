# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 277 ms: 1.06x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| html5lib       | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 311 ms: 1.50x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 320 ms: 1.42x faster                                                         |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 615 ms: 1.35x faster                                                         |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 259 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 523 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 19.8 ms: 1.09x faster                                                        |
| async_generators           | 457 ms                                                       | 425 ms: 1.07x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 68.1 ms: 1.19x faster                                                        |
| nbody          | 89.3 ms                                                      | 86.6 ms: 1.03x faster                                                        |
| pidigits       | 252 ms                                                       | 291 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.05 ms: 1.20x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 23.7 ms: 1.10x faster                                                        |
| regex_dna      | 247 ms                                                       | 225 ms: 1.10x faster                                                         |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 55.8 ms: 1.10x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 79.3 ms: 1.09x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 209 us: 1.04x faster                                                         |
| pickle_pure_python   | 323 us                                                       | 316 us: 1.02x faster                                                         |
| json_loads           | 24.7 us                                                      | 25.4 us: 1.03x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 161 ms: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.2 ms: 1.02x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.3 ms: 1.18x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 51.7 ms: 1.10x faster                                                        |
| django_template | 36.4 ms                                                      | 33.6 ms: 1.08x faster                                                        |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 311 ms: 1.50x faster                                                         |
| deepcopy                   | 392 us                                                       | 268 us: 1.46x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 320 ms: 1.42x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 27.3 us: 1.41x faster                                                        |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 615 ms: 1.35x faster                                                         |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 259 ms: 1.34x faster                                                         |
| scimark_sor                | 123 ms                                                       | 92.9 ms: 1.33x faster                                                        |
| go                         | 162 ms                                                       | 124 ms: 1.31x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.74 us: 1.29x faster                                                        |
| pyflate                    | 503 ms                                                       | 409 ms: 1.23x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 78.9 ms: 1.23x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 81.1 ns: 1.21x faster                                                        |
| richards                   | 52.9 ms                                                      | 43.8 ms: 1.21x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.05 ms: 1.20x faster                                                        |
| float                      | 81.3 ms                                                      | 68.1 ms: 1.19x faster                                                        |
| richards_super             | 59.6 ms                                                      | 49.9 ms: 1.19x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| telco                      | 8.79 ms                                                      | 7.39 ms: 1.19x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.04 ms: 1.18x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 22.3 ms: 1.18x faster                                                        |
| scimark_fft                | 328 ms                                                       | 282 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 523 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 60.0 ms: 1.14x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.9 ms: 1.13x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 5.85 ms: 1.12x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 88.2 ms: 1.12x faster                                                        |
| coverage                   | 80.0 ms                                                      | 71.8 ms: 1.11x faster                                                        |
| json                       | 5.69 ms                                                      | 5.12 ms: 1.11x faster                                                        |
| pylint                     | 347 ms                                                       | 313 ms: 1.11x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 23.7 ms: 1.10x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 51.7 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 60.3 ms: 1.10x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 55.8 ms: 1.10x faster                                                        |
| regex_dna                  | 247 ms                                                       | 225 ms: 1.10x faster                                                         |
| thrift                     | 901 us                                                       | 826 us: 1.09x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 79.3 ms: 1.09x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 19.8 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.58 sec: 1.09x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.70 sec: 1.08x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 21.8 ms: 1.08x faster                                                        |
| django_template            | 36.4 ms                                                      | 33.6 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 782 ms: 1.08x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.17 ms: 1.08x faster                                                        |
| async_generators           | 457 ms                                                       | 425 ms: 1.07x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.5 ms: 1.06x faster                                                        |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| 2to3                       | 293 ms                                                       | 277 ms: 1.06x faster                                                         |
| sympy_str                  | 298 ms                                                       | 284 ms: 1.05x faster                                                         |
| sympy_expand               | 509 ms                                                       | 487 ms: 1.05x faster                                                         |
| logging_simple             | 6.39 us                                                      | 6.12 us: 1.05x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.05x faster                                                         |
| comprehensions             | 17.0 us                                                      | 16.3 us: 1.04x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.5 ms: 1.04x faster                                                        |
| raytrace                   | 273 ms                                                       | 262 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 209 us: 1.04x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.04x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| typing_runtime_protocols   | 169 us                                                       | 164 us: 1.03x faster                                                         |
| nbody                      | 89.3 ms                                                      | 86.6 ms: 1.03x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 88.0 ms: 1.03x faster                                                        |
| chaos                      | 60.2 ms                                                      | 58.5 ms: 1.03x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.76 us: 1.03x faster                                                        |
| pickle_pure_python         | 323 us                                                       | 316 us: 1.02x faster                                                         |
| shortest_path              | 460 ms                                                       | 454 ms: 1.01x faster                                                         |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                         |
| docutils                   | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.2 ms: 1.02x slower                                                        |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.02x slower                                                         |
| json_loads                 | 24.7 us                                                      | 25.4 us: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| mdp                        | 2.54 sec                                                     | 2.65 sec: 1.04x slower                                                       |
| fannkuch                   | 363 ms                                                       | 381 ms: 1.05x slower                                                         |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| xml_etree_parse            | 150 ms                                                       | 161 ms: 1.07x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.88 ms: 1.08x slower                                                        |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.09x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 81.3 ms: 1.11x slower                                                        |
| pidigits                   | 252 ms                                                       | 291 ms: 1.15x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 5.85 ms: 1.24x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.5 ms: 1.29x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.10 sec: 214.10x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (3): bench_thread_pool, xml_etree_iterparse, connected_components
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x