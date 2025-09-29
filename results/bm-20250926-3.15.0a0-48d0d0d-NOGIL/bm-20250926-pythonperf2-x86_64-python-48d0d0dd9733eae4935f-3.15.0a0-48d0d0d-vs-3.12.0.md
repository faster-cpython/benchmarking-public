# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.049x slower
- HPT reliability: 94.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 312 ms: 1.10x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 523 ms: 2.01x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 555 ms: 1.88x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 230 ms: 1.87x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 291 ms: 1.86x faster                                                        |
| async_tree_none            | 452 ms                                                       | 261 ms: 1.73x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 320 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 465 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 494 ms: 1.41x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.73x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.8 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 126 ms: 1.43x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 231 ms: 1.03x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.6 ms: 1.00x faster                                                       |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.3 ms: 1.17x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 31.9 us: 1.02x faster                                                       |
| unpickle             | 14.8 us                                                      | 16.5 us: 1.11x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.00 us: 1.13x slower                                                       |
| json_loads           | 24.4 us                                                      | 27.6 us: 1.13x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 364 us: 1.14x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 99.0 ms: 1.15x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 241 us: 1.15x slower                                                        |
| pickle               | 10.5 us                                                      | 12.1 us: 1.15x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.54 us: 1.19x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 70.8 ms: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 19.2 ms: 1.65x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.50x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 43.2 ms: 1.13x slower                                                       |
| mako            | 10.0 ms                                                      | 17.3 ms: 1.73x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.40x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 523 ms: 2.01x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 555 ms: 1.88x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 230 ms: 1.87x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 291 ms: 1.86x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.45 sec: 1.77x faster                                                      |
| async_tree_none            | 452 ms                                                       | 261 ms: 1.73x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 320 ms: 1.70x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 2.19 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 465 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 494 ms: 1.41x faster                                                        |
| deepcopy                   | 368 us                                                       | 300 us: 1.23x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.5 ms: 1.22x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 30.6 us: 1.20x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.3 us: 1.20x faster                                                       |
| generators                 | 37.4 ms                                                      | 31.8 ms: 1.18x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 88.3 ms: 1.17x faster                                                       |
| go                         | 150 ms                                                       | 139 ms: 1.08x faster                                                        |
| float                      | 76.6 ms                                                      | 71.8 ms: 1.07x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 61.3 ms: 1.07x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.62 us: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 371 ms: 1.04x faster                                                        |
| regex_dna                  | 239 ms                                                       | 231 ms: 1.03x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 31.9 us: 1.02x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.6 ms: 1.00x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                      |
| unpack_sequence            | 53.2 ns                                                      | 54.2 ns: 1.02x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.4 ms: 1.04x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                                       |
| logging_simple             | 6.71 us                                                      | 6.97 us: 1.04x slower                                                       |
| logging_format             | 7.48 us                                                      | 7.82 us: 1.04x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.0 ms: 1.05x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 170 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                       |
| scimark_sor                | 109 ms                                                       | 116 ms: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| raytrace                   | 298 ms                                                       | 319 ms: 1.07x slower                                                        |
| sympy_str                  | 302 ms                                                       | 325 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 474 ms: 1.08x slower                                                        |
| scimark_fft                | 301 ms                                                       | 328 ms: 1.09x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.52 ms: 1.09x slower                                                       |
| 2to3                       | 285 ms                                                       | 312 ms: 1.10x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.10x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 894 ms: 1.11x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.60 ms: 1.11x slower                                                       |
| unpickle                   | 14.8 us                                                      | 16.5 us: 1.11x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.85 sec: 1.12x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                       |
| pickle_list                | 4.43 us                                                      | 5.00 us: 1.13x slower                                                       |
| django_template            | 38.2 ms                                                      | 43.2 ms: 1.13x slower                                                       |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                                        |
| json_loads                 | 24.4 us                                                      | 27.6 us: 1.13x slower                                                       |
| sympy_expand               | 484 ms                                                       | 552 ms: 1.14x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 91.7 ms: 1.14x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 364 us: 1.14x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 99.0 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 241 us: 1.15x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.1 us: 1.15x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 105 ms: 1.17x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.18x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 81.7 ms: 1.18x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.54 us: 1.19x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.89 sec: 1.19x slower                                                      |
| xml_etree_process          | 58.4 ms                                                      | 70.8 ms: 1.21x slower                                                       |
| richards                   | 45.7 ms                                                      | 55.8 ms: 1.22x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.94 ms: 1.22x slower                                                       |
| async_generators           | 390 ms                                                       | 480 ms: 1.23x slower                                                        |
| richards_super             | 51.3 ms                                                      | 64.3 ms: 1.25x slower                                                       |
| fannkuch                   | 350 ms                                                       | 456 ms: 1.30x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 6.32 ms: 1.33x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.72 ms: 1.36x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 209 us: 1.38x slower                                                        |
| nbody                      | 88.0 ms                                                      | 126 ms: 1.43x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.37 ms: 1.44x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.2 ms: 1.65x slower                                                       |
| mako                       | 10.0 ms                                                      | 17.3 ms: 1.73x slower                                                       |
| coverage                   | 66.7 ms                                                      | 120 ms: 1.79x slower                                                        |
| telco                      | 6.96 ms                                                      | 172 ms: 24.74x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (4): tomli_loads, regex_effbot, deepcopy_reduce, pycparser
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.049x slower

# HPT report

- Reliability score: 94.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.37x