# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.106x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 314 ms: 1.07x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.09 sec: 1.09x slower                                                      |
| html5lib       | 73.5 ms                                                      | 70.8 ms: 1.04x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 364 ms: 1.28x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 358 ms: 1.27x faster                                                        |
| async_tree_none            | 376 ms                                                       | 305 ms: 1.23x faster                                                        |
| async_tree_io              | 843 ms                                                       | 688 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 703 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 298 ms: 1.16x faster                                                        |
| async_generators           | 457 ms                                                       | 449 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 23.1 ms: 1.07x slower                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 655 ms: 1.08x slower                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 661 ms: 1.14x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 81.8 ms: 1.01x slower                                                       |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 99.2 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.24 ms: 1.13x faster                                                       |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 27.2 ms: 1.04x slower                                                       |
| regex_compile  | 143 ms                                                       | 153 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.34 sec: 1.05x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 241 us: 1.11x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 114 ms: 1.11x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 168 ms: 1.12x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 380 us: 1.18x slower                                                        |
| json_loads           | 24.7 us                                                      | 29.2 us: 1.19x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 73.8 ms: 1.21x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 108 ms: 1.25x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 14.2 ms: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.15x slower                                                                |

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
| genshi_text     | 26.2 ms                                                      | 27.5 ms: 1.05x slower                                                       |
| genshi_xml      | 57.1 ms                                                      | 59.8 ms: 1.05x slower                                                       |
| django_template | 36.4 ms                                                      | 42.5 ms: 1.17x slower                                                       |
| mako            | 10.4 ms                                                      | 13.2 ms: 1.28x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.56 sec: 1.63x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 364 ms: 1.28x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 358 ms: 1.27x faster                                                        |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                                        |
| async_tree_none            | 376 ms                                                       | 305 ms: 1.23x faster                                                        |
| deepcopy                   | 392 us                                                       | 320 us: 1.23x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 31.5 us: 1.23x faster                                                       |
| async_tree_io              | 843 ms                                                       | 688 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 703 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 298 ms: 1.16x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.24 ms: 1.13x faster                                                       |
| pyflate                    | 503 ms                                                       | 467 ms: 1.08x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 63.9 ms: 1.07x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.34 sec: 1.05x faster                                                      |
| generators                 | 33.6 ms                                                      | 32.4 ms: 1.04x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 70.8 ms: 1.04x faster                                                       |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                        |
| scimark_sor                | 123 ms                                                       | 119 ms: 1.03x faster                                                        |
| async_generators           | 457 ms                                                       | 449 ms: 1.02x faster                                                        |
| richards                   | 52.9 ms                                                      | 52.3 ms: 1.01x faster                                                       |
| richards_super             | 59.6 ms                                                      | 59.4 ms: 1.00x faster                                                       |
| connected_components       | 432 ms                                                       | 433 ms: 1.00x slower                                                        |
| shortest_path              | 460 ms                                                       | 462 ms: 1.00x slower                                                        |
| float                      | 81.3 ms                                                      | 81.8 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| djangocms                  | 65.3 us                                                      | 66.2 us: 1.01x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 3.47 ms: 1.02x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                       |
| regex_v8                   | 26.1 ms                                                      | 27.2 ms: 1.04x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 27.5 ms: 1.05x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 59.8 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 9.41 ms: 1.05x slower                                                       |
| json                       | 5.69 ms                                                      | 6.02 ms: 1.06x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.20 sec: 1.07x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 23.1 ms: 1.07x slower                                                       |
| 2to3                       | 293 ms                                                       | 314 ms: 1.07x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.34 sec: 1.07x slower                                                      |
| regex_compile              | 143 ms                                                       | 153 ms: 1.07x slower                                                        |
| meteor_contest             | 130 ms                                                       | 140 ms: 1.08x slower                                                        |
| telco                      | 8.79 ms                                                      | 9.52 ms: 1.08x slower                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 655 ms: 1.08x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 168 ms: 1.09x slower                                                        |
| docutils                   | 2.83 sec                                                     | 3.09 sec: 1.09x slower                                                      |
| bpe_tokeniser              | 5.09 sec                                                     | 5.62 sec: 1.10x slower                                                      |
| sympy_str                  | 298 ms                                                       | 330 ms: 1.11x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.04 ms: 1.11x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 241 us: 1.11x slower                                                        |
| nbody                      | 89.3 ms                                                      | 99.2 ms: 1.11x slower                                                       |
| comprehensions             | 17.0 us                                                      | 18.9 us: 1.11x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 114 ms: 1.11x slower                                                        |
| xml_etree_parse            | 150 ms                                                       | 168 ms: 1.12x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 3.00 ms: 1.12x slower                                                       |
| sympy_expand               | 509 ms                                                       | 571 ms: 1.12x slower                                                        |
| pathlib                    | 17.5 ms                                                      | 19.8 ms: 1.13x slower                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 661 ms: 1.14x slower                                                        |
| spectral_norm              | 97.0 ms                                                      | 111 ms: 1.14x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 76.0 ms: 1.15x slower                                                       |
| thrift                     | 901 us                                                       | 1.04 ms: 1.15x slower                                                       |
| logging_simple             | 6.39 us                                                      | 7.41 us: 1.16x slower                                                       |
| django_template            | 36.4 ms                                                      | 42.5 ms: 1.17x slower                                                       |
| sqlite_synth               | 2.91 us                                                      | 3.40 us: 1.17x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 380 us: 1.18x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 116 ms: 1.18x slower                                                        |
| chaos                      | 60.2 ms                                                      | 71.0 ms: 1.18x slower                                                       |
| scimark_fft                | 328 ms                                                       | 386 ms: 1.18x slower                                                        |
| json_loads                 | 24.7 us                                                      | 29.2 us: 1.19x slower                                                       |
| logging_format             | 6.94 us                                                      | 8.27 us: 1.19x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 108 ms: 1.19x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 87.9 ms: 1.20x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 73.8 ms: 1.21x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 5.73 ms: 1.21x slower                                                       |
| many_optionals             | 930 us                                                       | 1.13 ms: 1.21x slower                                                       |
| fannkuch                   | 363 ms                                                       | 444 ms: 1.22x slower                                                        |
| raytrace                   | 273 ms                                                       | 335 ms: 1.23x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 208 us: 1.23x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 108 ms: 1.25x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.15 sec: 1.25x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 1.06 sec: 1.25x slower                                                      |
| coverage                   | 80.0 ms                                                      | 101 ms: 1.27x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 14.2 ms: 1.27x slower                                                       |
| mako                       | 10.4 ms                                                      | 13.2 ms: 1.28x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 6.53 ms: 1.37x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 28.3 ms: 1.62x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 689 ns: 7.04x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.46 sec: 284.19x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmark hidden because not significant (6): asyncio_websockets, deepcopy_reduce, hexiom, k_core, sympy_integrate, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.106x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.10x