# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.043x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.95 sec: 1.04x slower                                                       |
| html5lib       | 73.5 ms                                                      | 67.9 ms: 1.08x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 339 ms: 1.37x faster                                                         |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 650 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 352 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 651 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 280 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 434 ms: 1.05x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 394 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.1 ms: 1.16x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 101 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.11 ms: 1.18x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 25.0 ms: 1.05x faster                                                        |
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                         |
| regex_dna      | 247 ms                                                       | 241 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 55.5 ms: 1.10x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 79.3 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 95.9 ms: 1.07x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.06x faster                                                         |
| pickle_pure_python   | 323 us                                                       | 334 us: 1.03x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.8 ms: 1.06x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.6 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 24.2 ms: 1.09x faster                                                        |
| mako           | 10.4 ms                                                      | 9.79 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 339 ms: 1.37x faster                                                         |
| deepcopy                   | 392 us                                                       | 286 us: 1.37x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.4 us: 1.32x faster                                                        |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 650 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 352 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 651 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 280 ms: 1.23x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.23x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.11 ms: 1.18x faster                                                        |
| float                      | 81.3 ms                                                      | 70.1 ms: 1.16x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.59 ms: 1.16x faster                                                        |
| richards                   | 52.9 ms                                                      | 45.8 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                         |
| generators                 | 33.6 ms                                                      | 29.1 ms: 1.16x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 84.8 ms: 1.14x faster                                                        |
| richards_super             | 59.6 ms                                                      | 52.1 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                         |
| pyflate                    | 503 ms                                                       | 447 ms: 1.13x faster                                                         |
| scimark_sor                | 123 ms                                                       | 109 ms: 1.13x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 55.5 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.64 sec: 1.10x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 79.3 ms: 1.09x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.2 ms: 1.09x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.9 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.1 ms: 1.08x faster                                                        |
| scimark_fft                | 328 ms                                                       | 304 ms: 1.08x faster                                                         |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                         |
| go                         | 162 ms                                                       | 151 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.9 ms: 1.07x faster                                                        |
| connected_components       | 432 ms                                                       | 405 ms: 1.07x faster                                                         |
| shortest_path              | 460 ms                                                       | 434 ms: 1.06x faster                                                         |
| mako                       | 10.4 ms                                                      | 9.79 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.06x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                                        |
| async_generators           | 457 ms                                                       | 434 ms: 1.05x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.77 us: 1.05x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.07 sec: 1.05x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 25.0 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                         |
| json                       | 5.69 ms                                                      | 5.48 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                        |
| thrift                     | 901 us                                                       | 872 us: 1.03x faster                                                         |
| pprint_safe_repr           | 843 ms                                                       | 819 ms: 1.03x faster                                                         |
| logging_simple             | 6.39 us                                                      | 6.23 us: 1.03x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.77 us: 1.02x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.68 sec: 1.02x faster                                                       |
| regex_dna                  | 247 ms                                                       | 241 ms: 1.02x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 67.1 ms: 1.02x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.01x faster                                                        |
| 2to3                       | 293 ms                                                       | 290 ms: 1.01x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.40 ms: 1.00x slower                                                        |
| sympy_expand               | 509 ms                                                       | 512 ms: 1.00x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 3.45 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.82 ms: 1.01x slower                                                        |
| coverage                   | 80.0 ms                                                      | 80.8 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 60.0 ms: 1.01x slower                                                        |
| chaos                      | 60.2 ms                                                      | 61.0 ms: 1.01x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 394 ms: 1.02x slower                                                         |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| mdp                        | 2.54 sec                                                     | 2.59 sec: 1.02x slower                                                       |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.03x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 334 us: 1.03x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 975 us: 1.04x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.95 sec: 1.04x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.8 ms: 1.06x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 77.5 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 180 us: 1.06x slower                                                         |
| fannkuch                   | 363 ms                                                       | 387 ms: 1.06x slower                                                         |
| hexiom                     | 6.55 ms                                                      | 7.05 ms: 1.08x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.6 us: 1.08x slower                                                        |
| raytrace                   | 273 ms                                                       | 296 ms: 1.08x slower                                                         |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.09x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 99.6 ms: 1.10x slower                                                        |
| comprehensions             | 17.0 us                                                      | 19.2 us: 1.13x slower                                                        |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.13x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.32x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.29 ms: 1.33x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.23 sec: 240.88x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (9): genshi_xml, django_template, logging_silent, create_gc_cycles, sqlglot_normalize, sympy_sum, sympy_str, sqlglot_transpile, sympy_integrate
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x