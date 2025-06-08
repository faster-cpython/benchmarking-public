# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.204x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 363 ms: 1.27x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.24 sec: 1.13x slower                                                      |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 612 ms: 1.72x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 641 ms: 1.63x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.53x faster                                                        |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 627 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 656 ms: 1.06x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.45x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 81.2 ms: 1.06x slower                                                       |
| nbody          | 88.0 ms                                                      | 144 ms: 1.64x slower                                                        |
| Geometric mean | (ref)                                                        | 1.18x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.44 ms: 1.04x faster                                                       |
| regex_dna      | 239 ms                                                       | 249 ms: 1.05x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| regex_compile  | 144 ms                                                       | 178 ms: 1.24x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 168 ms: 1.17x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 39.0 us: 1.20x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.77 sec: 1.28x slower                                                      |
| unpickle_list        | 4.66 us                                                      | 6.39 us: 1.37x slower                                                       |
| pickle_list          | 4.43 us                                                      | 6.16 us: 1.39x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 296 us: 1.41x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 450 us: 1.41x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 127 ms: 1.47x slower                                                        |
| unpickle             | 14.8 us                                                      | 21.8 us: 1.47x slower                                                       |
| json_loads           | 24.4 us                                                      | 36.0 us: 1.48x slower                                                       |
| pickle               | 10.5 us                                                      | 15.7 us: 1.49x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 15.6 ms: 1.53x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 90.2 ms: 1.55x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.7 ms: 1.47x slower                                                       |
| python_startup         | 11.6 ms                                                      | 21.3 ms: 1.83x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.64x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 52.5 ms: 1.38x slower                                                       |
| mako            | 10.0 ms                                                      | 20.0 ms: 2.00x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.66x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 612 ms: 1.72x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 641 ms: 1.63x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.53x faster                                                        |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.83 sec: 1.40x faster                                                      |
| gc_traversal               | 3.48 ms                                                      | 3.01 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 627 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 656 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.44 ms: 1.04x faster                                                       |
| generators                 | 37.4 ms                                                      | 36.3 ms: 1.03x faster                                                       |
| go                         | 150 ms                                                       | 153 ms: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.7 ms: 1.04x slower                                                       |
| deepcopy                   | 368 us                                                       | 384 us: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.05x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 56.3 ns: 1.06x slower                                                       |
| float                      | 76.6 ms                                                      | 81.2 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| comprehensions             | 21.9 us                                                      | 23.5 us: 1.07x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 20.3 ms: 1.08x slower                                                       |
| coroutines                 | 23.0 ms                                                      | 24.9 ms: 1.08x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 422 ms: 1.12x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.38 sec: 1.12x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 3.12 us: 1.13x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.24 sec: 1.13x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 42.1 us: 1.14x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 27.7 ms: 1.16x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 168 ms: 1.17x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| pickle_dict                | 32.5 us                                                      | 39.0 us: 1.20x slower                                                       |
| pyflate                    | 439 ms                                                       | 534 ms: 1.22x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 198 ms: 1.22x slower                                                        |
| regex_compile              | 144 ms                                                       | 178 ms: 1.24x slower                                                        |
| meteor_contest             | 128 ms                                                       | 159 ms: 1.24x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 4.07 ms: 1.26x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 7.54 ms: 1.27x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.26 us: 1.27x slower                                                       |
| 2to3                       | 285 ms                                                       | 363 ms: 1.27x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.03 ms: 1.28x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.77 sec: 1.28x slower                                                      |
| sympy_str                  | 302 ms                                                       | 388 ms: 1.28x slower                                                        |
| logging_format             | 7.48 us                                                      | 9.63 us: 1.29x slower                                                       |
| logging_simple             | 6.71 us                                                      | 8.67 us: 1.29x slower                                                       |
| chaos                      | 64.0 ms                                                      | 83.2 ms: 1.30x slower                                                       |
| raytrace                   | 298 ms                                                       | 392 ms: 1.32x slower                                                        |
| json                       | 5.12 ms                                                      | 6.80 ms: 1.33x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 6.39 us: 1.37x slower                                                       |
| django_template            | 38.2 ms                                                      | 52.5 ms: 1.38x slower                                                       |
| sympy_expand               | 484 ms                                                       | 668 ms: 1.38x slower                                                        |
| async_generators           | 390 ms                                                       | 540 ms: 1.38x slower                                                        |
| scimark_sor                | 109 ms                                                       | 151 ms: 1.39x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 125 ms: 1.39x slower                                                        |
| pickle_list                | 4.43 us                                                      | 6.16 us: 1.39x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 296 us: 1.41x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 450 us: 1.41x slower                                                        |
| richards                   | 45.7 ms                                                      | 65.8 ms: 1.44x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 12.7 ms: 1.47x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 127 ms: 1.47x slower                                                        |
| unpickle                   | 14.8 us                                                      | 21.8 us: 1.47x slower                                                       |
| json_loads                 | 24.4 us                                                      | 36.0 us: 1.48x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 119 ms: 1.48x slower                                                        |
| pickle                     | 10.5 us                                                      | 15.7 us: 1.49x slower                                                       |
| richards_super             | 51.3 ms                                                      | 77.8 ms: 1.51x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 150 ms: 1.52x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 105 ms: 1.52x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 15.6 ms: 1.53x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.24 sec: 1.53x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 2.54 sec: 1.54x slower                                                      |
| xml_etree_process          | 58.4 ms                                                      | 90.2 ms: 1.55x slower                                                       |
| scimark_fft                | 301 ms                                                       | 469 ms: 1.56x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.50 ms: 1.58x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 145 ms: 1.59x slower                                                        |
| fannkuch                   | 350 ms                                                       | 571 ms: 1.63x slower                                                        |
| nbody                      | 88.0 ms                                                      | 144 ms: 1.64x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 258 us: 1.70x slower                                                        |
| telco                      | 6.96 ms                                                      | 12.2 ms: 1.75x slower                                                       |
| python_startup             | 11.6 ms                                                      | 21.3 ms: 1.83x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 8.21 ms: 1.95x slower                                                       |
| mako                       | 10.0 ms                                                      | 20.0 ms: 2.00x slower                                                       |
| coverage                   | 66.7 ms                                                      | 139 ms: 2.09x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 793 ns: 8.40x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 61.5 ms: 12.91x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.29x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.204x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.37x