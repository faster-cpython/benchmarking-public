# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.041x slower
- HPT reliability: 88.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 312 ms: 1.09x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 524 ms: 2.01x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 552 ms: 1.89x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 229 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 290 ms: 1.86x faster                                                        |
| async_tree_none            | 452 ms                                                       | 259 ms: 1.74x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 316 ms: 1.72x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 462 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 491 ms: 1.42x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.74x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.0 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 125 ms: 1.42x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 226 ms: 1.06x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.3 ms: 1.02x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.52 ms: 1.01x faster                                                       |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.5 ms: 1.16x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 31.3 us: 1.04x faster                                                       |
| unpickle             | 14.8 us                                                      | 16.2 us: 1.09x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.88 us: 1.10x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 358 us: 1.12x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 97.6 ms: 1.13x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 239 us: 1.14x slower                                                        |
| pickle               | 10.5 us                                                      | 12.1 us: 1.15x slower                                                       |
| json_loads           | 24.4 us                                                      | 28.0 us: 1.15x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.54 us: 1.19x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 69.5 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.49x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.7 ms: 1.12x slower                                                       |
| mako            | 10.0 ms                                                      | 17.3 ms: 1.73x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.39x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 524 ms: 2.01x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 552 ms: 1.89x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 229 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 290 ms: 1.86x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.44 sec: 1.78x faster                                                      |
| async_tree_none            | 452 ms                                                       | 259 ms: 1.74x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 316 ms: 1.72x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 2.21 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 462 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 491 ms: 1.42x faster                                                        |
| deepcopy                   | 368 us                                                       | 297 us: 1.24x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 30.0 us: 1.22x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.5 ms: 1.22x faster                                                       |
| generators                 | 37.4 ms                                                      | 31.0 ms: 1.21x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 88.5 ms: 1.16x faster                                                       |
| go                         | 150 ms                                                       | 137 ms: 1.09x faster                                                        |
| float                      | 76.6 ms                                                      | 71.0 ms: 1.08x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.06x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 61.9 ms: 1.06x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.63 us: 1.05x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 31.3 us: 1.04x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 376 ms: 1.03x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| regex_v8                   | 23.6 ms                                                      | 23.3 ms: 1.02x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.32 us: 1.01x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.52 ms: 1.01x faster                                                       |
| docutils                   | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 22.8 ms: 1.01x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 53.9 ns: 1.01x slower                                                       |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                        |
| logging_simple             | 6.71 us                                                      | 6.81 us: 1.01x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 384 ms: 1.02x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 96.1 ns: 1.02x slower                                                       |
| logging_format             | 7.48 us                                                      | 7.62 us: 1.02x slower                                                       |
| chaos                      | 64.0 ms                                                      | 65.8 ms: 1.03x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.0 ms: 1.04x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 171 ms: 1.05x slower                                                        |
| scimark_fft                | 301 ms                                                       | 317 ms: 1.05x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 858 ms: 1.06x slower                                                        |
| pyflate                    | 439 ms                                                       | 467 ms: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.78 sec: 1.07x slower                                                      |
| sympy_str                  | 302 ms                                                       | 325 ms: 1.07x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.41 ms: 1.08x slower                                                       |
| json                       | 5.12 ms                                                      | 5.51 ms: 1.08x slower                                                       |
| raytrace                   | 298 ms                                                       | 321 ms: 1.08x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 99.6 ms: 1.09x slower                                                       |
| unpickle                   | 14.8 us                                                      | 16.2 us: 1.09x slower                                                       |
| 2to3                       | 285 ms                                                       | 312 ms: 1.09x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.56 ms: 1.10x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.88 us: 1.10x slower                                                       |
| django_template            | 38.2 ms                                                      | 42.7 ms: 1.12x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 77.4 ms: 1.12x slower                                                       |
| meteor_contest             | 128 ms                                                       | 144 ms: 1.12x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 358 us: 1.12x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 97.6 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 239 us: 1.14x slower                                                        |
| sympy_expand               | 484 ms                                                       | 553 ms: 1.14x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.1 us: 1.15x slower                                                       |
| json_loads                 | 24.4 us                                                      | 28.0 us: 1.15x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 114 ms: 1.15x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 93.5 ms: 1.16x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.88 sec: 1.18x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 107 ms: 1.19x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.54 us: 1.19x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 69.5 ms: 1.19x slower                                                       |
| async_generators           | 390 ms                                                       | 470 ms: 1.20x slower                                                        |
| richards                   | 45.7 ms                                                      | 55.3 ms: 1.21x slower                                                       |
| richards_super             | 51.3 ms                                                      | 63.9 ms: 1.25x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.00 ms: 1.26x slower                                                       |
| fannkuch                   | 350 ms                                                       | 450 ms: 1.29x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 6.32 ms: 1.33x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.63 ms: 1.34x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 207 us: 1.36x slower                                                        |
| nbody                      | 88.0 ms                                                      | 125 ms: 1.42x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.36 ms: 1.44x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                       |
| mako                       | 10.0 ms                                                      | 17.3 ms: 1.73x slower                                                       |
| coverage                   | 66.7 ms                                                      | 120 ms: 1.80x slower                                                        |
| telco                      | 6.96 ms                                                      | 167 ms: 24.00x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a-NOGIL/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 88.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.36x