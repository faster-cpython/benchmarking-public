# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.056x slower
- HPT reliability: 96.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 318 ms: 1.11x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 532 ms: 1.98x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 562 ms: 1.85x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 233 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 294 ms: 1.83x faster                                                        |
| async_tree_none            | 452 ms                                                       | 264 ms: 1.71x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 321 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 465 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 495 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.72x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 74.1 ms: 1.03x faster                                                       |
| nbody          | 88.0 ms                                                      | 125 ms: 1.42x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 231 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                       |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.2 ms: 1.17x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                      |
| pickle_dict          | 32.5 us                                                      | 33.3 us: 1.02x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 96.6 ms: 1.12x slower                                                       |
| unpickle             | 14.8 us                                                      | 16.7 us: 1.13x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.01 us: 1.13x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 238 us: 1.14x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 374 us: 1.18x slower                                                        |
| pickle               | 10.5 us                                                      | 12.5 us: 1.18x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.52 us: 1.18x slower                                                       |
| json_loads           | 24.4 us                                                      | 29.0 us: 1.19x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 69.9 ms: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.49x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 43.6 ms: 1.14x slower                                                       |
| mako            | 10.0 ms                                                      | 17.5 ms: 1.75x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.41x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 532 ms: 1.98x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 562 ms: 1.85x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 233 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 294 ms: 1.83x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.45 sec: 1.78x faster                                                      |
| async_tree_none            | 452 ms                                                       | 264 ms: 1.71x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 321 ms: 1.70x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 2.22 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 465 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 495 ms: 1.41x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.5 ms: 1.23x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 88.2 ms: 1.17x faster                                                       |
| deepcopy                   | 368 us                                                       | 326 us: 1.13x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.0 ms: 1.11x faster                                                       |
| go                         | 150 ms                                                       | 139 ms: 1.08x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.59 us: 1.07x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 61.3 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 35.1 us: 1.05x faster                                                       |
| float                      | 76.6 ms                                                      | 74.1 ms: 1.03x faster                                                       |
| regex_dna                  | 239 ms                                                       | 231 ms: 1.03x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.68 us: 1.00x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.55 us: 1.01x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 382 ms: 1.01x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| unpack_sequence            | 53.2 ns                                                      | 54.3 ns: 1.02x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 33.3 us: 1.02x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 3.47 us: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.3 ns: 1.03x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 24.9 ms: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 67.2 ms: 1.05x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 171 ms: 1.05x slower                                                        |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| pyflate                    | 439 ms                                                       | 472 ms: 1.08x slower                                                        |
| sympy_str                  | 302 ms                                                       | 326 ms: 1.08x slower                                                        |
| json                       | 5.12 ms                                                      | 5.53 ms: 1.08x slower                                                       |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 877 ms: 1.09x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.49 ms: 1.09x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.81 sec: 1.09x slower                                                      |
| raytrace                   | 298 ms                                                       | 331 ms: 1.11x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                       |
| 2to3                       | 285 ms                                                       | 318 ms: 1.11x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.63 ms: 1.12x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 96.6 ms: 1.12x slower                                                       |
| unpickle                   | 14.8 us                                                      | 16.7 us: 1.13x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 104 ms: 1.13x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.01 us: 1.13x slower                                                       |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 238 us: 1.14x slower                                                        |
| django_template            | 38.2 ms                                                      | 43.6 ms: 1.14x slower                                                       |
| sympy_expand               | 484 ms                                                       | 555 ms: 1.15x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 79.4 ms: 1.15x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 92.6 ms: 1.15x slower                                                       |
| scimark_fft                | 301 ms                                                       | 352 ms: 1.17x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.17x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 374 us: 1.18x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 106 ms: 1.18x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.5 us: 1.18x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.52 us: 1.18x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.89 sec: 1.19x slower                                                      |
| json_loads                 | 24.4 us                                                      | 29.0 us: 1.19x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 69.9 ms: 1.20x slower                                                       |
| async_generators           | 390 ms                                                       | 470 ms: 1.20x slower                                                        |
| richards                   | 45.7 ms                                                      | 55.5 ms: 1.21x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.98 ms: 1.25x slower                                                       |
| richards_super             | 51.3 ms                                                      | 64.1 ms: 1.25x slower                                                       |
| fannkuch                   | 350 ms                                                       | 458 ms: 1.31x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 212 us: 1.40x slower                                                        |
| nbody                      | 88.0 ms                                                      | 125 ms: 1.42x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.11 ms: 1.45x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.39 ms: 1.47x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                       |
| coverage                   | 66.7 ms                                                      | 116 ms: 1.74x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.5 ms: 1.75x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 58.0 ms: 12.18x slower                                                      |
| telco                      | 6.96 ms                                                      | 174 ms: 24.92x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.056x slower

# HPT report

- Reliability score: 96.88% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.35x