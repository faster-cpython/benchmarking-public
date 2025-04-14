# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.049x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 335 ms: 1.14x slower                                                         |
| docutils       | 2.83 sec                                                     | 2.95 sec: 1.04x slower                                                       |
| sphinx         | 1.12 sec                                                     | 1.19 sec: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 580 ms: 1.43x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                         |
| async_tree_io              | 843 ms                                                       | 619 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.30x faster                                                         |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 365 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 496 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 534 ms: 1.13x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                         |
| async_generators           | 457 ms                                                       | 467 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 73.3 ms: 1.11x faster                                                        |
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| nbody          | 89.3 ms                                                      | 129 ms: 1.45x slower                                                         |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                        |
| regex_dna      | 247 ms                                                       | 242 ms: 1.02x faster                                                         |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 90.1 ms: 1.14x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                         |
| tomli_loads          | 2.46 sec                                                     | 2.40 sec: 1.03x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 238 us: 1.09x slower                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 97.1 ms: 1.12x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 69.8 ms: 1.14x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 379 us: 1.17x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 13.3 ms: 1.19x slower                                                        |
| json_loads           | 24.7 us                                                      | 32.1 us: 1.30x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 18.7 ms: 1.18x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.32x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 62.7 ms: 1.10x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 29.4 ms: 1.12x slower                                                        |
| django_template | 36.4 ms                                                      | 45.2 ms: 1.24x slower                                                        |
| mako            | 10.4 ms                                                      | 17.7 ms: 1.71x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.27x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.06 ms: 2.30x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 580 ms: 1.43x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 1.96 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 619 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.30x faster                                                         |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 365 ms: 1.24x faster                                                         |
| deepcopy                   | 392 us                                                       | 332 us: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 496 ms: 1.17x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 90.1 ms: 1.14x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.57 us: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 534 ms: 1.13x faster                                                         |
| float                      | 81.3 ms                                                      | 73.3 ms: 1.11x faster                                                        |
| go                         | 162 ms                                                       | 148 ms: 1.10x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 36.3 us: 1.06x faster                                                        |
| generators                 | 33.6 ms                                                      | 31.7 ms: 1.06x faster                                                        |
| scimark_sor                | 123 ms                                                       | 117 ms: 1.05x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| pyflate                    | 503 ms                                                       | 486 ms: 1.04x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.40 sec: 1.03x faster                                                       |
| regex_dna                  | 247 ms                                                       | 242 ms: 1.02x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                         |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 96.8 ms: 1.00x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.15 sec: 1.01x slower                                                       |
| async_generators           | 457 ms                                                       | 467 ms: 1.02x slower                                                         |
| dulwich_log                | 68.2 ms                                                      | 69.9 ms: 1.02x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 100 ns: 1.03x slower                                                         |
| telco                      | 8.79 ms                                                      | 9.09 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 872 ms: 1.03x slower                                                         |
| pycparser                  | 1.24 sec                                                     | 1.29 sec: 1.04x slower                                                       |
| scimark_fft                | 328 ms                                                       | 341 ms: 1.04x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.95 sec: 1.04x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.19 sec: 1.06x slower                                                       |
| json                       | 5.69 ms                                                      | 6.03 ms: 1.06x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 127 ms: 1.07x slower                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.84 sec: 1.07x slower                                                       |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                                         |
| unpickle_pure_python       | 217 us                                                       | 238 us: 1.09x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.78 sec: 1.09x slower                                                       |
| richards                   | 52.9 ms                                                      | 58.0 ms: 1.10x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 62.7 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 65.3 ms: 1.10x slower                                                        |
| k_core                     | 2.17 sec                                                     | 2.39 sec: 1.10x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 7.23 ms: 1.10x slower                                                        |
| sympy_expand               | 509 ms                                                       | 565 ms: 1.11x slower                                                         |
| logging_simple             | 6.39 us                                                      | 7.11 us: 1.11x slower                                                        |
| richards_super             | 59.6 ms                                                      | 66.5 ms: 1.12x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 29.4 ms: 1.12x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 97.1 ms: 1.12x slower                                                        |
| thrift                     | 901 us                                                       | 1.01 ms: 1.12x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 175 ms: 1.13x slower                                                         |
| sympy_str                  | 298 ms                                                       | 337 ms: 1.13x slower                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.7 ms: 1.13x slower                                                        |
| connected_components       | 432 ms                                                       | 492 ms: 1.14x slower                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 2.04 ms: 1.14x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.92 us: 1.14x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 69.8 ms: 1.14x slower                                                        |
| 2to3                       | 293 ms                                                       | 335 ms: 1.14x slower                                                         |
| sympy_integrate            | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                        |
| shortest_path              | 460 ms                                                       | 530 ms: 1.15x slower                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 172 ms: 1.16x slower                                                         |
| comprehensions             | 17.0 us                                                      | 19.9 us: 1.17x slower                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.64 ms: 1.17x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 379 us: 1.17x slower                                                         |
| chaos                      | 60.2 ms                                                      | 70.7 ms: 1.17x slower                                                        |
| python_startup             | 15.9 ms                                                      | 18.7 ms: 1.18x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 117 ms: 1.18x slower                                                         |
| meteor_contest             | 130 ms                                                       | 154 ms: 1.19x slower                                                         |
| many_optionals             | 930 us                                                       | 1.11 ms: 1.19x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 13.3 ms: 1.19x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.77 ms: 1.21x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 110 ms: 1.21x slower                                                         |
| raytrace                   | 273 ms                                                       | 338 ms: 1.24x slower                                                         |
| django_template            | 36.4 ms                                                      | 45.2 ms: 1.24x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 83.0 ms: 1.25x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 93.3 ms: 1.27x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 217 us: 1.28x slower                                                         |
| fannkuch                   | 363 ms                                                       | 468 ms: 1.29x slower                                                         |
| json_loads                 | 24.7 us                                                      | 32.1 us: 1.30x slower                                                        |
| coverage                   | 80.0 ms                                                      | 104 ms: 1.30x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 11.8 ms: 1.32x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 4.52 ms: 1.32x slower                                                        |
| nbody                      | 89.3 ms                                                      | 129 ms: 1.45x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 25.4 ms: 1.45x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.46 ms: 1.55x slower                                                        |
| mako                       | 10.4 ms                                                      | 17.7 ms: 1.71x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 49.0 ms: 9.56x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (3): html5lib, deepcopy_reduce, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x slower

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.24x