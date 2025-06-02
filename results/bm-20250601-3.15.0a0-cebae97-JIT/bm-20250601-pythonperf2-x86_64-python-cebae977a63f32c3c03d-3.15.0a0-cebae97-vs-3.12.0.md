# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.269x faster
- HPT reliability: 98.65%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 320 ms: 1.12x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.17 sec: 1.11x slower                                                      |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 696 ms: 1.50x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 705 ms: 1.49x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 368 ms: 1.47x faster                                                        |
| async_tree_none            | 452 ms                                                       | 314 ms: 1.44x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 301 ms: 1.43x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 677 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 680 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 72.7 ms: 1.05x faster                                                       |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 107 ms: 1.22x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.32 ms: 1.08x faster                                                       |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.3 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.31 sec: 1.07x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 35.3 us: 1.08x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 164 ms: 1.14x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 239 us: 1.14x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 380 us: 1.19x slower                                                        |
| unpickle             | 14.8 us                                                      | 17.7 us: 1.20x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.59 us: 1.20x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 70.1 ms: 1.20x slower                                                       |
| json_loads           | 24.4 us                                                      | 29.4 us: 1.21x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 104 ms: 1.21x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.97 us: 1.35x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 14.2 ms: 1.38x slower                                                       |
| pickle               | 10.5 us                                                      | 14.6 us: 1.39x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.44 ms: 1.09x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                       |
| mako            | 10.0 ms                                                      | 13.5 ms: 1.35x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.22x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pprint_pformat             | 1.65 sec                                                     | 1.83 us: 905480.58x faster                                                  |
| pprint_safe_repr           | 807 ms                                                       | 1.12 us: 720721.05x faster                                                  |
| mdp                        | 2.57 sec                                                     | 1.57 sec: 1.64x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 696 ms: 1.50x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 705 ms: 1.49x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 365 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 368 ms: 1.47x faster                                                        |
| async_tree_none            | 452 ms                                                       | 314 ms: 1.44x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 301 ms: 1.43x faster                                                        |
| deepcopy                   | 368 us                                                       | 320 us: 1.15x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 32.0 us: 1.15x faster                                                       |
| generators                 | 37.4 ms                                                      | 33.0 ms: 1.13x faster                                                       |
| richards                   | 45.7 ms                                                      | 40.6 ms: 1.13x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.32 ms: 1.08x faster                                                       |
| richards_super             | 51.3 ms                                                      | 47.9 ms: 1.07x faster                                                       |
| go                         | 150 ms                                                       | 141 ms: 1.06x faster                                                        |
| float                      | 76.6 ms                                                      | 72.7 ms: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| comprehensions             | 21.9 us                                                      | 21.1 us: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 677 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 680 ms: 1.03x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 64.0 ms: 1.02x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.20 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                       |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                        |
| coroutines                 | 23.0 ms                                                      | 23.9 ms: 1.04x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 19.8 ms: 1.05x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.54 us: 1.05x slower                                                       |
| pyflate                    | 439 ms                                                       | 462 ms: 1.05x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 172 ms: 1.06x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.31 sec: 1.07x slower                                                      |
| pycparser                  | 1.23 sec                                                     | 1.34 sec: 1.08x slower                                                      |
| pickle_dict                | 32.5 us                                                      | 35.3 us: 1.08x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.44 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 76.3 ms: 1.11x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.17 sec: 1.11x slower                                                      |
| bench_thread_pool          | 950 us                                                       | 1.05 ms: 1.11x slower                                                       |
| sympy_str                  | 302 ms                                                       | 336 ms: 1.11x slower                                                        |
| django_template            | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| 2to3                       | 285 ms                                                       | 320 ms: 1.12x slower                                                        |
| scimark_sor                | 109 ms                                                       | 123 ms: 1.13x slower                                                        |
| meteor_contest             | 128 ms                                                       | 146 ms: 1.14x slower                                                        |
| raytrace                   | 298 ms                                                       | 339 ms: 1.14x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 164 ms: 1.14x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 239 us: 1.14x slower                                                        |
| chaos                      | 64.0 ms                                                      | 73.4 ms: 1.15x slower                                                       |
| logging_format             | 7.48 us                                                      | 8.59 us: 1.15x slower                                                       |
| logging_simple             | 6.71 us                                                      | 7.73 us: 1.15x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.3 ms: 1.16x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.93 ms: 1.16x slower                                                       |
| json                       | 5.12 ms                                                      | 5.98 ms: 1.17x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 93.9 ms: 1.17x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 63.1 ns: 1.19x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 380 us: 1.19x slower                                                        |
| unpickle                   | 14.8 us                                                      | 17.7 us: 1.20x slower                                                       |
| async_generators           | 390 ms                                                       | 468 ms: 1.20x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.59 us: 1.20x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 70.1 ms: 1.20x slower                                                       |
| json_loads                 | 24.4 us                                                      | 29.4 us: 1.21x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 104 ms: 1.21x slower                                                        |
| sympy_expand               | 484 ms                                                       | 586 ms: 1.21x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 3.36 us: 1.21x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 121 ms: 1.22x slower                                                        |
| nbody                      | 88.0 ms                                                      | 107 ms: 1.22x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.23x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 118 ms: 1.29x slower                                                        |
| scimark_fft                | 301 ms                                                       | 397 ms: 1.32x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.97 us: 1.35x slower                                                       |
| mako                       | 10.0 ms                                                      | 13.5 ms: 1.35x slower                                                       |
| fannkuch                   | 350 ms                                                       | 479 ms: 1.37x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 14.2 ms: 1.38x slower                                                       |
| telco                      | 6.96 ms                                                      | 9.67 ms: 1.39x slower                                                       |
| pickle                     | 10.5 us                                                      | 14.6 us: 1.39x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 216 us: 1.42x slower                                                        |
| coverage                   | 66.7 ms                                                      | 96.4 ms: 1.45x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.30 ms: 1.50x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.70 ms: 1.64x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.99 ms: 1.88x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 668 ns: 7.08x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.17 sec: 455.99x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.16x faster                                                                |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.269x faster

# HPT report

- Reliability score: 98.65% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x