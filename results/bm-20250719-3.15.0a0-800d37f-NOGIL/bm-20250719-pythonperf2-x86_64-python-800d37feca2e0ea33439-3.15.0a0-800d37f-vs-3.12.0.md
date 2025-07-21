# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.059x slower
- HPT reliability: 98.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 319 ms: 1.12x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 529 ms: 1.99x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 560 ms: 1.86x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 232 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 295 ms: 1.83x faster                                                        |
| async_tree_none            | 452 ms                                                       | 264 ms: 1.71x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 323 ms: 1.69x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 465 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 495 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.72x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.7 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 127 ms: 1.44x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                       |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                        |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.3 ms: 1.16x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.31 sec: 1.07x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 35.6 us: 1.09x slower                                                       |
| unpickle             | 14.8 us                                                      | 16.5 us: 1.12x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 239 us: 1.14x slower                                                        |
| json_loads           | 24.4 us                                                      | 28.0 us: 1.15x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 99.4 ms: 1.15x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 368 us: 1.16x slower                                                        |
| pickle               | 10.5 us                                                      | 12.3 us: 1.17x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 12.0 ms: 1.18x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.25 us: 1.18x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.56 us: 1.19x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 70.2 ms: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.6 ms: 1.35x slower                                                       |
| python_startup         | 11.6 ms                                                      | 19.5 ms: 1.68x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.50x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 43.1 ms: 1.13x slower                                                       |
| mako            | 10.0 ms                                                      | 17.2 ms: 1.72x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.40x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 529 ms: 1.99x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 560 ms: 1.86x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 232 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 295 ms: 1.83x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.45 sec: 1.77x faster                                                      |
| async_tree_none            | 452 ms                                                       | 264 ms: 1.71x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 323 ms: 1.69x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 2.26 ms: 1.54x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 465 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 495 ms: 1.41x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.3 ms: 1.24x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.0 us: 1.22x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 88.3 ms: 1.16x faster                                                       |
| deepcopy                   | 368 us                                                       | 321 us: 1.15x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.10x faster                                                       |
| go                         | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 33.9 us: 1.09x faster                                                       |
| float                      | 76.6 ms                                                      | 71.7 ms: 1.07x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 61.6 ms: 1.06x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.66 us: 1.04x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.8 ms: 1.01x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 384 ms: 1.02x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| logging_silent             | 94.4 ns                                                      | 96.8 ns: 1.03x slower                                                       |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| logging_simple             | 6.71 us                                                      | 6.94 us: 1.03x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.3 ms: 1.04x slower                                                       |
| logging_format             | 7.48 us                                                      | 7.78 us: 1.04x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.51 us: 1.04x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 55.7 ns: 1.05x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.2 ms: 1.05x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 172 ms: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.31 sec: 1.07x slower                                                      |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.07x slower                                                        |
| json                       | 5.12 ms                                                      | 5.50 ms: 1.07x slower                                                       |
| sympy_str                  | 302 ms                                                       | 326 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 474 ms: 1.08x slower                                                        |
| raytrace                   | 298 ms                                                       | 322 ms: 1.08x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 35.6 us: 1.09x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 884 ms: 1.09x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.53 ms: 1.10x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.82 sec: 1.10x slower                                                      |
| unpickle                   | 14.8 us                                                      | 16.5 us: 1.12x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 102 ms: 1.12x slower                                                        |
| 2to3                       | 285 ms                                                       | 319 ms: 1.12x slower                                                        |
| meteor_contest             | 128 ms                                                       | 144 ms: 1.12x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.65 ms: 1.13x slower                                                       |
| django_template            | 38.2 ms                                                      | 43.1 ms: 1.13x slower                                                       |
| sympy_expand               | 484 ms                                                       | 551 ms: 1.14x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 239 us: 1.14x slower                                                        |
| json_loads                 | 24.4 us                                                      | 28.0 us: 1.15x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 92.6 ms: 1.15x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 99.4 ms: 1.15x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 368 us: 1.16x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.3 us: 1.17x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 105 ms: 1.17x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 12.0 ms: 1.18x slower                                                       |
| scimark_fft                | 301 ms                                                       | 357 ms: 1.18x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.25 us: 1.18x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 81.8 ms: 1.19x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 117 ms: 1.19x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.89 sec: 1.19x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 5.56 us: 1.19x slower                                                       |
| richards                   | 45.7 ms                                                      | 54.7 ms: 1.20x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 70.2 ms: 1.20x slower                                                       |
| async_generators           | 390 ms                                                       | 475 ms: 1.22x slower                                                        |
| richards_super             | 51.3 ms                                                      | 63.2 ms: 1.23x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.97 ms: 1.24x slower                                                       |
| fannkuch                   | 350 ms                                                       | 460 ms: 1.31x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.6 ms: 1.35x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 208 us: 1.37x slower                                                        |
| nbody                      | 88.0 ms                                                      | 127 ms: 1.44x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.25 ms: 1.49x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.42 ms: 1.50x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.5 ms: 1.68x slower                                                       |
| mako                       | 10.0 ms                                                      | 17.2 ms: 1.72x slower                                                       |
| coverage                   | 66.7 ms                                                      | 116 ms: 1.74x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 57.3 ms: 12.04x slower                                                      |
| telco                      | 6.96 ms                                                      | 175 ms: 25.20x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.059x slower

# HPT report

- Reliability score: 98.83% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.35x