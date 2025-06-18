# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.130x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 322 ms: 1.13x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.17 sec: 1.10x slower                                                      |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 544 ms                                                       | 363 ms: 1.50x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 699 ms: 1.49x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 707 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 367 ms: 1.47x faster                                                        |
| async_tree_none            | 452 ms                                                       | 312 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.43x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 631 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 635 ms: 1.10x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 75.3 ms: 1.02x faster                                                       |
| nbody          | 88.0 ms                                                      | 109 ms: 1.24x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.34 ms: 1.07x faster                                                       |
| regex_compile  | 144 ms                                                       | 156 ms: 1.09x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.27 sec: 1.05x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 35.5 us: 1.09x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 116 ms: 1.13x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 164 ms: 1.14x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 244 us: 1.16x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.59 us: 1.20x slower                                                       |
| json_loads           | 24.4 us                                                      | 29.4 us: 1.21x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 71.5 ms: 1.23x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 106 ms: 1.23x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 391 us: 1.23x slower                                                        |
| unpickle             | 14.8 us                                                      | 18.6 us: 1.25x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.93 us: 1.34x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 14.2 ms: 1.39x slower                                                       |
| pickle               | 10.5 us                                                      | 14.9 us: 1.42x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.41 ms: 1.09x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 43.2 ms: 1.13x slower                                                       |
| mako            | 10.0 ms                                                      | 12.9 ms: 1.29x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.56 sec: 1.64x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 363 ms: 1.50x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 699 ms: 1.49x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 707 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 367 ms: 1.47x faster                                                        |
| async_tree_none            | 452 ms                                                       | 312 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.43x faster                                                        |
| deepcopy                   | 368 us                                                       | 328 us: 1.12x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 32.9 us: 1.12x faster                                                       |
| richards                   | 45.7 ms                                                      | 41.2 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 631 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 635 ms: 1.10x faster                                                        |
| generators                 | 37.4 ms                                                      | 34.9 ms: 1.07x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.34 ms: 1.07x faster                                                       |
| richards_super             | 51.3 ms                                                      | 48.5 ms: 1.06x faster                                                       |
| go                         | 150 ms                                                       | 143 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| comprehensions             | 21.9 us                                                      | 21.2 us: 1.03x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 63.8 ms: 1.03x faster                                                       |
| float                      | 76.6 ms                                                      | 75.3 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 23.2 ms: 1.01x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 24.3 ms: 1.01x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.34 ms: 1.03x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.27 sec: 1.05x slower                                                      |
| sympy_sum                  | 162 ms                                                       | 171 ms: 1.05x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.58 us: 1.06x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 20.1 ms: 1.06x slower                                                       |
| pyflate                    | 439 ms                                                       | 471 ms: 1.07x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.33 sec: 1.08x slower                                                      |
| regex_compile              | 144 ms                                                       | 156 ms: 1.09x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.41 ms: 1.09x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 35.5 us: 1.09x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.17 sec: 1.10x slower                                                      |
| meteor_contest             | 128 ms                                                       | 142 ms: 1.11x slower                                                        |
| logging_format             | 7.48 us                                                      | 8.33 us: 1.11x slower                                                       |
| sympy_str                  | 302 ms                                                       | 337 ms: 1.12x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 77.2 ms: 1.12x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.06 ms: 1.12x slower                                                       |
| 2to3                       | 285 ms                                                       | 322 ms: 1.13x slower                                                        |
| logging_simple             | 6.71 us                                                      | 7.58 us: 1.13x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 116 ms: 1.13x slower                                                        |
| django_template            | 38.2 ms                                                      | 43.2 ms: 1.13x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 91.2 ms: 1.13x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 60.4 ns: 1.14x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 164 ms: 1.14x slower                                                        |
| raytrace                   | 298 ms                                                       | 339 ms: 1.14x slower                                                        |
| chaos                      | 64.0 ms                                                      | 73.6 ms: 1.15x slower                                                       |
| scimark_sor                | 109 ms                                                       | 126 ms: 1.16x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 244 us: 1.16x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.94 ms: 1.17x slower                                                       |
| json                       | 5.12 ms                                                      | 6.02 ms: 1.18x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.59 us: 1.20x slower                                                       |
| json_loads                 | 24.4 us                                                      | 29.4 us: 1.21x slower                                                       |
| async_generators           | 390 ms                                                       | 472 ms: 1.21x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 3.36 us: 1.21x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 120 ms: 1.21x slower                                                        |
| sympy_expand               | 484 ms                                                       | 592 ms: 1.22x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 71.5 ms: 1.23x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 106 ms: 1.23x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 391 us: 1.23x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.23x slower                                                        |
| nbody                      | 88.0 ms                                                      | 109 ms: 1.24x slower                                                        |
| unpickle                   | 14.8 us                                                      | 18.6 us: 1.25x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.10 sec: 1.27x slower                                                      |
| scimark_fft                | 301 ms                                                       | 383 ms: 1.27x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 118 ms: 1.29x slower                                                        |
| mako                       | 10.0 ms                                                      | 12.9 ms: 1.29x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.05 sec: 1.30x slower                                                      |
| pickle_list                | 4.43 us                                                      | 5.93 us: 1.34x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 14.2 ms: 1.39x slower                                                       |
| fannkuch                   | 350 ms                                                       | 486 ms: 1.39x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.68 ms: 1.39x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 213 us: 1.40x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                       |
| pickle                     | 10.5 us                                                      | 14.9 us: 1.42x slower                                                       |
| coverage                   | 66.7 ms                                                      | 99.8 ms: 1.50x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.40 ms: 1.52x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.62 ms: 1.61x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.94 ms: 1.85x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 685 ns: 7.26x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.57 sec: 330.27x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.19x slower                                                                |

Benchmark hidden because not significant (3): asyncio_websockets, regex_dna, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.130x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.14x