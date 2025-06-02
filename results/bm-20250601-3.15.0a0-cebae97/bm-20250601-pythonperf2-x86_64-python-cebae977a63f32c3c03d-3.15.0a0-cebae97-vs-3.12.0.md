# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.118x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 311 ms: 1.09x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 544 ms                                                       | 358 ms: 1.52x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 689 ms: 1.51x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 702 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 364 ms: 1.48x faster                                                        |
| async_tree_none            | 452 ms                                                       | 307 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 297 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 655 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 662 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                       |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.36 ms: 1.06x faster                                                       |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                        |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.5 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.38 sec: 1.10x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 36.4 us: 1.12x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 117 ms: 1.14x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 239 us: 1.14x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 168 ms: 1.17x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.47 us: 1.17x slower                                                       |
| unpickle             | 14.8 us                                                      | 17.6 us: 1.19x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 378 us: 1.19x slower                                                        |
| json_loads           | 24.4 us                                                      | 29.1 us: 1.19x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 107 ms: 1.24x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 72.6 ms: 1.24x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.92 us: 1.34x slower                                                       |
| pickle               | 10.5 us                                                      | 14.7 us: 1.39x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 14.4 ms: 1.41x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.40 ms: 1.09x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.2 ms: 1.10x slower                                                       |
| mako            | 10.0 ms                                                      | 13.7 ms: 1.37x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.23x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.55 sec: 1.66x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 358 ms: 1.52x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 689 ms: 1.51x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 702 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 364 ms: 1.48x faster                                                        |
| async_tree_none            | 452 ms                                                       | 307 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 297 ms: 1.45x faster                                                        |
| go                         | 150 ms                                                       | 127 ms: 1.18x faster                                                        |
| generators                 | 37.4 ms                                                      | 31.7 ms: 1.18x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.6 us: 1.18x faster                                                       |
| deepcopy                   | 368 us                                                       | 317 us: 1.16x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 32.2 us: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 655 ms: 1.06x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.36 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 662 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 63.1 ms: 1.04x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.8 ms: 1.01x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.62 sec: 1.02x slower                                                      |
| pathlib                    | 18.9 ms                                                      | 19.5 ms: 1.03x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 169 ms: 1.04x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.52 us: 1.04x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 55.5 ns: 1.04x slower                                                       |
| float                      | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                       |
| coroutines                 | 23.0 ms                                                      | 24.4 ms: 1.06x slower                                                       |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.46 ms: 1.07x slower                                                       |
| pyflate                    | 439 ms                                                       | 469 ms: 1.07x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.33 sec: 1.08x slower                                                      |
| meteor_contest             | 128 ms                                                       | 139 ms: 1.08x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 9.40 ms: 1.09x slower                                                       |
| sympy_str                  | 302 ms                                                       | 330 ms: 1.09x slower                                                        |
| 2to3                       | 285 ms                                                       | 311 ms: 1.09x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.50 ms: 1.09x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.04 ms: 1.09x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 87.9 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 76.1 ms: 1.10x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.38 sec: 1.10x slower                                                      |
| django_template            | 38.2 ms                                                      | 42.2 ms: 1.10x slower                                                       |
| raytrace                   | 298 ms                                                       | 331 ms: 1.11x slower                                                        |
| logging_format             | 7.48 us                                                      | 8.33 us: 1.11x slower                                                       |
| chaos                      | 64.0 ms                                                      | 71.5 ms: 1.12x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 36.4 us: 1.12x slower                                                       |
| logging_simple             | 6.71 us                                                      | 7.55 us: 1.13x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 117 ms: 1.14x slower                                                        |
| async_generators           | 390 ms                                                       | 444 ms: 1.14x slower                                                        |
| scimark_sor                | 109 ms                                                       | 124 ms: 1.14x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 239 us: 1.14x slower                                                        |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                        |
| json                       | 5.12 ms                                                      | 5.93 ms: 1.16x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.5 ms: 1.16x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 168 ms: 1.17x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.47 us: 1.17x slower                                                       |
| richards                   | 45.7 ms                                                      | 53.9 ms: 1.18x slower                                                       |
| sympy_expand               | 484 ms                                                       | 571 ms: 1.18x slower                                                        |
| richards_super             | 51.3 ms                                                      | 60.8 ms: 1.18x slower                                                       |
| unpickle                   | 14.8 us                                                      | 17.6 us: 1.19x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 378 us: 1.19x slower                                                        |
| json_loads                 | 24.4 us                                                      | 29.1 us: 1.19x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 108 ms: 1.20x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 3.40 us: 1.23x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 107 ms: 1.24x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 72.6 ms: 1.24x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 123 ms: 1.25x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 114 ms: 1.25x slower                                                        |
| scimark_fft                | 301 ms                                                       | 383 ms: 1.27x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.11 sec: 1.28x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.03 sec: 1.28x slower                                                      |
| fannkuch                   | 350 ms                                                       | 463 ms: 1.32x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.92 us: 1.34x slower                                                       |
| mako                       | 10.0 ms                                                      | 13.7 ms: 1.37x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 210 us: 1.38x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.64 ms: 1.38x slower                                                       |
| pickle                     | 10.5 us                                                      | 14.7 us: 1.39x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 14.4 ms: 1.41x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                       |
| coverage                   | 66.7 ms                                                      | 98.2 ms: 1.47x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.46 ms: 1.53x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.65 ms: 1.62x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.99 ms: 1.88x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 676 ns: 7.16x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.00 sec: 209.94x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.18x slower                                                                |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.118x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.11x