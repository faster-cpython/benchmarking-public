# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 275 ms: 1.07x faster                                                         |
| html5lib       | 73.5 ms                                                      | 65.9 ms: 1.12x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.06 sec: 1.06x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 317 ms: 1.47x faster                                                         |
| async_tree_none            | 376 ms                                                       | 272 ms: 1.38x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 606 ms: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 615 ms: 1.37x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 261 ms: 1.32x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 539 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 525 ms: 1.11x faster                                                         |
| async_generators           | 457 ms                                                       | 416 ms: 1.10x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 66.4 ms: 1.23x faster                                                        |
| nbody          | 89.3 ms                                                      | 83.5 ms: 1.07x faster                                                        |
| pidigits       | 252 ms                                                       | 292 ms: 1.16x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 2.95 ms: 1.25x faster                                                        |
| regex_dna      | 247 ms                                                       | 219 ms: 1.13x faster                                                         |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.00 sec: 1.23x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 54.2 ms: 1.13x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 77.3 ms: 1.12x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 199 us: 1.09x faster                                                         |
| pickle_pure_python   | 323 us                                                       | 314 us: 1.03x faster                                                         |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.6 us: 1.08x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 162 ms: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 9.13 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 21.7 ms: 1.21x faster                                                        |
| django_template | 36.4 ms                                                      | 32.2 ms: 1.13x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 51.8 ms: 1.10x faster                                                        |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 258 us: 1.52x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 317 ms: 1.47x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 26.8 us: 1.44x faster                                                        |
| async_tree_none            | 376 ms                                                       | 272 ms: 1.38x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 606 ms: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 615 ms: 1.37x faster                                                         |
| scimark_sor                | 123 ms                                                       | 91.4 ms: 1.35x faster                                                        |
| go                         | 162 ms                                                       | 121 ms: 1.34x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 72.4 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 261 ms: 1.32x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.70 us: 1.31x faster                                                        |
| richards                   | 52.9 ms                                                      | 41.4 ms: 1.28x faster                                                        |
| pyflate                    | 503 ms                                                       | 395 ms: 1.27x faster                                                         |
| richards_super             | 59.6 ms                                                      | 47.0 ms: 1.27x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 2.95 ms: 1.25x faster                                                        |
| scimark_fft                | 328 ms                                                       | 266 ms: 1.23x faster                                                         |
| logging_silent             | 97.9 ns                                                      | 79.6 ns: 1.23x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.00 sec: 1.23x faster                                                       |
| float                      | 81.3 ms                                                      | 66.4 ms: 1.23x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 21.7 ms: 1.21x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.53 ms: 1.17x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 5.68 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.17 ms: 1.14x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 86.3 ms: 1.14x faster                                                        |
| thrift                     | 901 us                                                       | 792 us: 1.14x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 58.3 ms: 1.13x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.52 sec: 1.13x faster                                                       |
| pylint                     | 347 ms                                                       | 306 ms: 1.13x faster                                                         |
| django_template            | 36.4 ms                                                      | 32.2 ms: 1.13x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.8 ms: 1.13x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 54.2 ms: 1.13x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.51 sec: 1.13x faster                                                       |
| regex_dna                  | 247 ms                                                       | 219 ms: 1.13x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 752 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 539 ms: 1.12x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 77.3 ms: 1.12x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 65.9 ms: 1.12x faster                                                        |
| comprehensions             | 17.0 us                                                      | 15.3 us: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 525 ms: 1.11x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.09 ms: 1.11x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 51.8 ms: 1.10x faster                                                        |
| async_generators           | 457 ms                                                       | 416 ms: 1.10x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 199 us: 1.09x faster                                                         |
| coverage                   | 80.0 ms                                                      | 73.1 ms: 1.09x faster                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 54.3 ms: 1.09x faster                                                        |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                         |
| sqlglot_normalize          | 119 ms                                                       | 110 ms: 1.09x faster                                                         |
| typing_runtime_protocols   | 169 us                                                       | 155 us: 1.09x faster                                                         |
| sympy_expand               | 509 ms                                                       | 469 ms: 1.09x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.29 ms: 1.08x faster                                                        |
| chaos                      | 60.2 ms                                                      | 55.8 ms: 1.08x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.92 us: 1.08x faster                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.66 ms: 1.08x faster                                                        |
| raytrace                   | 273 ms                                                       | 253 ms: 1.08x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.3 ms: 1.08x faster                                                        |
| json                       | 5.69 ms                                                      | 5.29 ms: 1.07x faster                                                        |
| sympy_str                  | 298 ms                                                       | 278 ms: 1.07x faster                                                         |
| nbody                      | 89.3 ms                                                      | 83.5 ms: 1.07x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 139 ms: 1.07x faster                                                         |
| 2to3                       | 293 ms                                                       | 275 ms: 1.07x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 22.1 ms: 1.06x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 85.4 ms: 1.06x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.74 us: 1.06x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 146 ms: 1.06x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.06 sec: 1.06x faster                                                       |
| bench_thread_pool          | 942 us                                                       | 892 us: 1.06x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.3 ms: 1.06x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 64.9 ms: 1.05x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.61 us: 1.05x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| fannkuch                   | 363 ms                                                       | 351 ms: 1.03x faster                                                         |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                         |
| pickle_pure_python         | 323 us                                                       | 314 us: 1.03x faster                                                         |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.02x faster                                                       |
| connected_components       | 432 ms                                                       | 424 ms: 1.02x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| meteor_contest             | 130 ms                                                       | 129 ms: 1.00x faster                                                         |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.13 ms: 1.02x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 74.8 ms: 1.02x slower                                                        |
| mdp                        | 2.54 sec                                                     | 2.61 sec: 1.03x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| many_optionals             | 930 us                                                       | 986 us: 1.06x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.85 ms: 1.06x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.6 us: 1.08x slower                                                        |
| xml_etree_parse            | 150 ms                                                       | 162 ms: 1.08x slower                                                         |
| gc_traversal               | 4.74 ms                                                      | 5.47 ms: 1.15x slower                                                        |
| pidigits                   | 252 ms                                                       | 292 ms: 1.16x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 21.9 ms: 1.25x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 961 ms: 187.72x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): docutils, xml_etree_iterparse
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.06x