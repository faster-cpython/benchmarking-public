# Results vs. 3.13.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.063x faster
- HPT reliability: 95.79%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| sphinx         | 617 ms                                                      | 638 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 390 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 226 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.1 ms: 1.15x faster                                                      |
| nbody          | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                      |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.0 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.02x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.34 ms: 1.02x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.7 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 20.3 ms                                                     | 24.0 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 488 us: 17.34x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| mdp                        | 1.43 sec                                                    | 811 ms: 1.76x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.29x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 390 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| float                      | 50.8 ms                                                     | 44.1 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                      |
| go                         | 84.7 ms                                                     | 77.5 ms: 1.09x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.53 ms: 1.03x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.0 ms: 1.03x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 61.9 ms: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.0 ms: 1.02x faster                                                      |
| nbody                      | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                      |
| sympy_expand               | 286 ms                                                      | 288 ms: 1.01x slower                                                       |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.5 ms: 1.01x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| pyflate                    | 283 ms                                                      | 287 ms: 1.01x slower                                                       |
| async_generators           | 223 ms                                                      | 226 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 493 ms: 1.02x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.02x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.7 ns: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.34 ms: 1.02x slower                                                      |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.02x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 2.94 sec: 1.02x slower                                                     |
| crypto_pyaes               | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                      |
| shortest_path              | 355 ms                                                      | 366 ms: 1.03x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 638 ms: 1.03x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.2 ms: 1.04x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.00 us: 1.04x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.02 sec: 1.05x slower                                                     |
| logging_format             | 6.18 us                                                     | 6.49 us: 1.05x slower                                                      |
| connected_components       | 320 ms                                                      | 336 ms: 1.05x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 59.7 ms: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 857 us: 1.06x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.7 ms: 1.06x slower                                                      |
| fannkuch                   | 252 ms                                                      | 267 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.5 ms: 1.07x slower                                                      |
| coverage                   | 45.3 ms                                                     | 48.8 ms: 1.08x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.19 ms: 1.09x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 62.1 ms: 1.11x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.21 ms: 1.12x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.13 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 95.9 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 177 ms: 1.16x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.56x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (9): pylint, meteor_contest, genshi_text, sympy_integrate, mako, scimark_fft, genshi_xml, pycparser, html5lib
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 95.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown