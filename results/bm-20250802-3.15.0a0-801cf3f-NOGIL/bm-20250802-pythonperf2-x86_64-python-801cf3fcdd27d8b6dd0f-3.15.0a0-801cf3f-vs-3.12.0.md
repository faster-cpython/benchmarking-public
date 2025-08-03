# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.057x slower
- HPT reliability: 97.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 316 ms: 1.11x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 528 ms: 1.99x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 558 ms: 1.87x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 232 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 294 ms: 1.84x faster                                                        |
| async_tree_none            | 452 ms                                                       | 263 ms: 1.72x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 320 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 467 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 495 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.72x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.4 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 127 ms: 1.45x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.55 ms: 1.01x faster                                                       |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 87.5 ms: 1.17x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 33.8 us: 1.04x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.30 sec: 1.06x slower                                                      |
| unpickle             | 14.8 us                                                      | 16.5 us: 1.11x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 237 us: 1.13x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 362 us: 1.14x slower                                                        |
| json_loads           | 24.4 us                                                      | 27.9 us: 1.14x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.10 us: 1.15x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 99.6 ms: 1.16x slower                                                       |
| pickle               | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 12.0 ms: 1.17x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.51 us: 1.18x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 69.9 ms: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.49x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 43.0 ms: 1.13x slower                                                       |
| mako            | 10.0 ms                                                      | 17.5 ms: 1.74x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.40x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 528 ms: 1.99x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 558 ms: 1.87x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 232 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 294 ms: 1.84x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.45 sec: 1.77x faster                                                      |
| async_tree_none            | 452 ms                                                       | 263 ms: 1.72x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 320 ms: 1.70x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 2.22 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 467 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 495 ms: 1.41x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.9 ms: 1.25x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.20x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 87.5 ms: 1.17x faster                                                       |
| deepcopy                   | 368 us                                                       | 315 us: 1.17x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.8 ms: 1.13x faster                                                       |
| go                         | 150 ms                                                       | 139 ms: 1.08x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 34.2 us: 1.08x faster                                                       |
| float                      | 76.6 ms                                                      | 71.4 ms: 1.07x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.60 us: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 62.1 ms: 1.05x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 376 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.55 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 381 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| logging_simple             | 6.71 us                                                      | 6.79 us: 1.01x slower                                                       |
| logging_format             | 7.48 us                                                      | 7.63 us: 1.02x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 54.5 ns: 1.02x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.48 us: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.03x slower                                                      |
| logging_silent             | 94.4 ns                                                      | 97.8 ns: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.4 ms: 1.04x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 33.8 us: 1.04x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.1 ms: 1.05x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 171 ms: 1.06x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.30 sec: 1.06x slower                                                      |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                        |
| raytrace                   | 298 ms                                                       | 323 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 476 ms: 1.08x slower                                                        |
| sympy_str                  | 302 ms                                                       | 328 ms: 1.09x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 878 ms: 1.09x slower                                                        |
| json                       | 5.12 ms                                                      | 5.62 ms: 1.10x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.82 sec: 1.10x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 6.56 ms: 1.10x slower                                                       |
| 2to3                       | 285 ms                                                       | 316 ms: 1.11x slower                                                        |
| unpickle                   | 14.8 us                                                      | 16.5 us: 1.11x slower                                                       |
| django_template            | 38.2 ms                                                      | 43.0 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 237 us: 1.13x slower                                                        |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 362 us: 1.14x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.70 ms: 1.14x slower                                                       |
| json_loads                 | 24.4 us                                                      | 27.9 us: 1.14x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 105 ms: 1.15x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.10 us: 1.15x slower                                                       |
| sympy_expand               | 484 ms                                                       | 559 ms: 1.16x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 79.7 ms: 1.16x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 99.6 ms: 1.16x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| scimark_fft                | 301 ms                                                       | 349 ms: 1.16x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 105 ms: 1.17x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 93.8 ms: 1.17x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 12.0 ms: 1.17x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.87 sec: 1.18x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 5.51 us: 1.18x slower                                                       |
| async_generators           | 390 ms                                                       | 463 ms: 1.19x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 69.9 ms: 1.20x slower                                                       |
| richards                   | 45.7 ms                                                      | 55.6 ms: 1.22x slower                                                       |
| richards_super             | 51.3 ms                                                      | 64.0 ms: 1.25x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.03 ms: 1.28x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 206 us: 1.36x slower                                                        |
| fannkuch                   | 350 ms                                                       | 484 ms: 1.38x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.95 ms: 1.41x slower                                                       |
| nbody                      | 88.0 ms                                                      | 127 ms: 1.45x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.40 ms: 1.47x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                       |
| mako                       | 10.0 ms                                                      | 17.5 ms: 1.74x slower                                                       |
| coverage                   | 66.7 ms                                                      | 117 ms: 1.76x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 57.2 ms: 12.01x slower                                                      |
| telco                      | 6.96 ms                                                      | 175 ms: 25.13x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                |
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x slower

# HPT report

- Reliability score: 97.30% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.35x