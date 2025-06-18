# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.108x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 322 ms: 1.10x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.17 sec: 1.12x slower                                                      |
| html5lib       | 73.5 ms                                                      | 71.1 ms: 1.03x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.21 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 367 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 363 ms: 1.25x faster                                                        |
| async_tree_io              | 843 ms                                                       | 699 ms: 1.21x faster                                                        |
| async_tree_none            | 376 ms                                                       | 312 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 707 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 300 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 472 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 631 ms: 1.05x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 23.2 ms: 1.08x slower                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 635 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 75.3 ms: 1.08x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| nbody          | 89.3 ms                                                      | 109 ms: 1.22x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.34 ms: 1.10x faster                                                       |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                        |
| regex_compile  | 143 ms                                                       | 156 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.27 sec: 1.09x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 164 ms: 1.09x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 244 us: 1.12x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 116 ms: 1.13x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 71.5 ms: 1.17x slower                                                       |
| json_loads           | 24.7 us                                                      | 29.4 us: 1.19x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 391 us: 1.21x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 106 ms: 1.22x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 14.2 ms: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 9.41 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 28.1 ms: 1.07x slower                                                       |
| genshi_xml      | 57.1 ms                                                      | 61.2 ms: 1.07x slower                                                       |
| django_template | 36.4 ms                                                      | 43.2 ms: 1.19x slower                                                       |
| mako            | 10.4 ms                                                      | 12.9 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.56 sec: 1.63x faster                                                      |
| richards                   | 52.9 ms                                                      | 41.2 ms: 1.28x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 367 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 363 ms: 1.25x faster                                                        |
| richards_super             | 59.6 ms                                                      | 48.5 ms: 1.23x faster                                                       |
| async_tree_io              | 843 ms                                                       | 699 ms: 1.21x faster                                                        |
| async_tree_none            | 376 ms                                                       | 312 ms: 1.20x faster                                                        |
| deepcopy                   | 392 us                                                       | 328 us: 1.19x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 707 ms: 1.18x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 32.9 us: 1.18x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 300 ms: 1.15x faster                                                        |
| go                         | 162 ms                                                       | 143 ms: 1.13x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.34 ms: 1.10x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.27 sec: 1.09x faster                                                      |
| float                      | 81.3 ms                                                      | 75.3 ms: 1.08x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 63.8 ms: 1.07x faster                                                       |
| pyflate                    | 503 ms                                                       | 471 ms: 1.07x faster                                                        |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                      |
| html5lib                   | 73.5 ms                                                      | 71.1 ms: 1.03x faster                                                       |
| deltablue                  | 3.42 ms                                                      | 3.34 ms: 1.02x faster                                                       |
| connected_components       | 432 ms                                                       | 427 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.58 us: 1.01x slower                                                       |
| djangocms                  | 65.3 us                                                      | 66.3 us: 1.02x slower                                                       |
| scimark_sor                | 123 ms                                                       | 126 ms: 1.02x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                       |
| async_generators           | 457 ms                                                       | 472 ms: 1.03x slower                                                        |
| generators                 | 33.6 ms                                                      | 34.9 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 631 ms: 1.05x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.41 ms: 1.05x slower                                                       |
| json                       | 5.69 ms                                                      | 6.02 ms: 1.06x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 6.94 ms: 1.06x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 28.1 ms: 1.07x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.33 sec: 1.07x slower                                                      |
| genshi_xml                 | 57.1 ms                                                      | 61.2 ms: 1.07x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 23.2 ms: 1.08x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.21 sec: 1.08x slower                                                      |
| xml_etree_parse            | 150 ms                                                       | 164 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 635 ms: 1.09x slower                                                        |
| meteor_contest             | 130 ms                                                       | 142 ms: 1.09x slower                                                        |
| regex_compile              | 143 ms                                                       | 156 ms: 1.10x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.94 ms: 1.10x slower                                                       |
| 2to3                       | 293 ms                                                       | 322 ms: 1.10x slower                                                        |
| telco                      | 8.79 ms                                                      | 9.68 ms: 1.10x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 171 ms: 1.10x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.69 sec: 1.12x slower                                                      |
| docutils                   | 2.83 sec                                                     | 3.17 sec: 1.12x slower                                                      |
| unpickle_pure_python       | 217 us                                                       | 244 us: 1.12x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.06 ms: 1.13x slower                                                       |
| sympy_str                  | 298 ms                                                       | 337 ms: 1.13x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 116 ms: 1.13x slower                                                        |
| pathlib                    | 17.5 ms                                                      | 20.1 ms: 1.14x slower                                                       |
| thrift                     | 901 us                                                       | 1.04 ms: 1.15x slower                                                       |
| sqlite_synth               | 2.91 us                                                      | 3.36 us: 1.16x slower                                                       |
| sympy_expand               | 509 ms                                                       | 592 ms: 1.16x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 77.2 ms: 1.17x slower                                                       |
| scimark_fft                | 328 ms                                                       | 383 ms: 1.17x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 71.5 ms: 1.17x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 5.62 ms: 1.18x slower                                                       |
| logging_simple             | 6.39 us                                                      | 7.58 us: 1.19x slower                                                       |
| django_template            | 36.4 ms                                                      | 43.2 ms: 1.19x slower                                                       |
| json_loads                 | 24.7 us                                                      | 29.4 us: 1.19x slower                                                       |
| logging_format             | 6.94 us                                                      | 8.33 us: 1.20x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 391 us: 1.21x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 120 ms: 1.22x slower                                                        |
| nbody                      | 89.3 ms                                                      | 109 ms: 1.22x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.10 sec: 1.22x slower                                                      |
| spectral_norm              | 97.0 ms                                                      | 118 ms: 1.22x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 106 ms: 1.22x slower                                                        |
| chaos                      | 60.2 ms                                                      | 73.6 ms: 1.22x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.22x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 91.2 ms: 1.24x slower                                                       |
| raytrace                   | 273 ms                                                       | 339 ms: 1.24x slower                                                        |
| comprehensions             | 17.0 us                                                      | 21.2 us: 1.24x slower                                                       |
| pprint_safe_repr           | 843 ms                                                       | 1.05 sec: 1.25x slower                                                      |
| many_optionals             | 930 us                                                       | 1.16 ms: 1.25x slower                                                       |
| coverage                   | 80.0 ms                                                      | 99.8 ms: 1.25x slower                                                       |
| mako                       | 10.4 ms                                                      | 12.9 ms: 1.25x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 213 us: 1.26x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 14.2 ms: 1.28x slower                                                       |
| fannkuch                   | 363 ms                                                       | 486 ms: 1.34x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 6.40 ms: 1.34x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 28.3 ms: 1.62x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 685 ns: 7.00x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.57 sec: 307.16x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                                |

Benchmark hidden because not significant (4): asyncio_websockets, regex_v8, shortest_path, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.108x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.11x