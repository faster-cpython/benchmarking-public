# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.106x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 320 ms: 1.09x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.14 sec: 1.11x slower                                                      |
| html5lib       | 73.5 ms                                                      | 70.7 ms: 1.04x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.22 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 367 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 364 ms: 1.25x faster                                                        |
| async_tree_io              | 843 ms                                                       | 694 ms: 1.21x faster                                                        |
| async_tree_none            | 376 ms                                                       | 313 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 705 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 299 ms: 1.16x faster                                                        |
| async_generators           | 457 ms                                                       | 475 ms: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 24.0 ms: 1.11x slower                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 672 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 675 ms: 1.16x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 72.3 ms: 1.13x faster                                                       |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 108 ms: 1.21x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.29 ms: 1.12x faster                                                       |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                        |
| regex_compile  | 143 ms                                                       | 156 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.33 sec: 1.06x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 238 us: 1.09x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 170 ms: 1.13x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 71.4 ms: 1.17x slower                                                       |
| json_loads           | 24.7 us                                                      | 29.2 us: 1.18x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 385 us: 1.19x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 105 ms: 1.21x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 14.5 ms: 1.30x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.5 ms: 1.04x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 9.43 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 28.9 ms: 1.10x slower                                                       |
| genshi_xml      | 57.1 ms                                                      | 64.1 ms: 1.12x slower                                                       |
| django_template | 36.4 ms                                                      | 43.0 ms: 1.18x slower                                                       |
| mako            | 10.4 ms                                                      | 13.4 ms: 1.29x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.17x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.59 sec: 1.60x faster                                                      |
| richards                   | 52.9 ms                                                      | 41.1 ms: 1.29x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 367 ms: 1.27x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 364 ms: 1.25x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 31.5 us: 1.23x faster                                                       |
| richards_super             | 59.6 ms                                                      | 48.6 ms: 1.23x faster                                                       |
| async_tree_io              | 843 ms                                                       | 694 ms: 1.21x faster                                                        |
| deepcopy                   | 392 us                                                       | 326 us: 1.20x faster                                                        |
| async_tree_none            | 376 ms                                                       | 313 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 705 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 299 ms: 1.16x faster                                                        |
| go                         | 162 ms                                                       | 143 ms: 1.14x faster                                                        |
| float                      | 81.3 ms                                                      | 72.3 ms: 1.13x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.29 ms: 1.12x faster                                                       |
| pyflate                    | 503 ms                                                       | 466 ms: 1.08x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 63.7 ms: 1.07x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.33 sec: 1.06x faster                                                      |
| html5lib                   | 73.5 ms                                                      | 70.7 ms: 1.04x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                      |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.34 ms: 1.02x faster                                                       |
| shortest_path              | 460 ms                                                       | 454 ms: 1.01x faster                                                        |
| connected_components       | 432 ms                                                       | 427 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| djangocms                  | 65.3 us                                                      | 66.3 us: 1.02x slower                                                       |
| generators                 | 33.6 ms                                                      | 34.8 ms: 1.04x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.5 ms: 1.04x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 24.4 ms: 1.04x slower                                                       |
| async_generators           | 457 ms                                                       | 475 ms: 1.04x slower                                                        |
| scimark_sor                | 123 ms                                                       | 129 ms: 1.05x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.43 ms: 1.05x slower                                                       |
| json                       | 5.69 ms                                                      | 6.04 ms: 1.06x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.33 sec: 1.07x slower                                                      |
| hexiom                     | 6.55 ms                                                      | 7.03 ms: 1.07x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.22 sec: 1.08x slower                                                      |
| create_gc_cycles           | 2.68 ms                                                      | 2.92 ms: 1.09x slower                                                       |
| regex_compile              | 143 ms                                                       | 156 ms: 1.09x slower                                                        |
| 2to3                       | 293 ms                                                       | 320 ms: 1.09x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 238 us: 1.09x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 28.9 ms: 1.10x slower                                                       |
| telco                      | 8.79 ms                                                      | 9.72 ms: 1.11x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 172 ms: 1.11x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 24.0 ms: 1.11x slower                                                       |
| meteor_contest             | 130 ms                                                       | 144 ms: 1.11x slower                                                        |
| docutils                   | 2.83 sec                                                     | 3.14 sec: 1.11x slower                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 672 ms: 1.11x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.70 sec: 1.12x slower                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 64.1 ms: 1.12x slower                                                       |
| bench_thread_pool          | 942 us                                                       | 1.06 ms: 1.12x slower                                                       |
| xml_etree_parse            | 150 ms                                                       | 170 ms: 1.13x slower                                                        |
| sympy_str                  | 298 ms                                                       | 338 ms: 1.13x slower                                                        |
| pathlib                    | 17.5 ms                                                      | 20.0 ms: 1.14x slower                                                       |
| sqlite_synth               | 2.91 us                                                      | 3.35 us: 1.15x slower                                                       |
| sympy_expand               | 509 ms                                                       | 588 ms: 1.16x slower                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 675 ms: 1.16x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 77.0 ms: 1.16x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 71.4 ms: 1.17x slower                                                       |
| thrift                     | 901 us                                                       | 1.06 ms: 1.18x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 5.59 ms: 1.18x slower                                                       |
| django_template            | 36.4 ms                                                      | 43.0 ms: 1.18x slower                                                       |
| json_loads                 | 24.7 us                                                      | 29.2 us: 1.18x slower                                                       |
| chaos                      | 60.2 ms                                                      | 71.7 ms: 1.19x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 385 us: 1.19x slower                                                        |
| scimark_fft                | 328 ms                                                       | 392 ms: 1.20x slower                                                        |
| logging_simple             | 6.39 us                                                      | 7.69 us: 1.20x slower                                                       |
| scimark_lu                 | 98.7 ms                                                      | 119 ms: 1.20x slower                                                        |
| nbody                      | 89.3 ms                                                      | 108 ms: 1.21x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 105 ms: 1.21x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.10 sec: 1.22x slower                                                      |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.22x slower                                                        |
| logging_format             | 6.94 us                                                      | 8.51 us: 1.23x slower                                                       |
| raytrace                   | 273 ms                                                       | 337 ms: 1.24x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 1.04 sec: 1.24x slower                                                      |
| many_optionals             | 930 us                                                       | 1.16 ms: 1.24x slower                                                       |
| comprehensions             | 17.0 us                                                      | 21.3 us: 1.25x slower                                                       |
| spectral_norm              | 97.0 ms                                                      | 122 ms: 1.26x slower                                                        |
| coverage                   | 80.0 ms                                                      | 101 ms: 1.26x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 93.4 ms: 1.27x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 216 us: 1.28x slower                                                        |
| mako                       | 10.4 ms                                                      | 13.4 ms: 1.29x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 14.5 ms: 1.30x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 6.34 ms: 1.33x slower                                                       |
| fannkuch                   | 363 ms                                                       | 483 ms: 1.33x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 28.6 ms: 1.64x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 677 ns: 6.92x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 2.14 sec: 417.84x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                                |

Benchmark hidden because not significant (4): deepcopy_reduce, regex_v8, asyncio_websockets, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.106x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x