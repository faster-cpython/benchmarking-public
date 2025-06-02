# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.202x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 365 ms: 1.28x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.29 sec: 1.15x slower                                                      |
| Geometric mean | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 614 ms: 1.72x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 642 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 336 ms: 1.61x faster                                                        |
| async_tree_none            | 452 ms                                                       | 296 ms: 1.53x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 360 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 608 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 638 ms: 1.09x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.46x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 81.7 ms: 1.07x slower                                                       |
| nbody          | 88.0 ms                                                      | 136 ms: 1.55x slower                                                        |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                       |
| regex_dna      | 239 ms                                                       | 242 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| regex_compile  | 144 ms                                                       | 178 ms: 1.24x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 167 ms: 1.16x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 39.9 us: 1.23x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.78 sec: 1.29x slower                                                      |
| unpickle_list        | 4.66 us                                                      | 6.08 us: 1.31x slower                                                       |
| pickle_list          | 4.43 us                                                      | 6.10 us: 1.38x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 299 us: 1.43x slower                                                        |
| unpickle             | 14.8 us                                                      | 21.2 us: 1.43x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 456 us: 1.43x slower                                                        |
| json_loads           | 24.4 us                                                      | 35.6 us: 1.46x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 126 ms: 1.47x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 87.2 ms: 1.49x slower                                                       |
| pickle               | 10.5 us                                                      | 15.8 us: 1.50x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 15.6 ms: 1.53x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.36x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.7 ms: 1.47x slower                                                       |
| python_startup         | 11.6 ms                                                      | 21.3 ms: 1.83x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.64x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 52.7 ms: 1.38x slower                                                       |
| mako            | 10.0 ms                                                      | 19.8 ms: 1.98x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.65x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 614 ms: 1.72x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 642 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 336 ms: 1.61x faster                                                        |
| async_tree_none            | 452 ms                                                       | 296 ms: 1.53x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 360 ms: 1.51x faster                                                        |
| mdp                        | 2.57 sec                                                     | 1.83 sec: 1.40x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 608 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 638 ms: 1.09x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 3.22 ms: 1.08x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                       |
| generators                 | 37.4 ms                                                      | 36.1 ms: 1.04x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 377 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.01x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.7 ms: 1.02x slower                                                       |
| go                         | 150 ms                                                       | 154 ms: 1.03x slower                                                        |
| deepcopy                   | 368 us                                                       | 383 us: 1.04x slower                                                        |
| comprehensions             | 21.9 us                                                      | 23.2 us: 1.06x slower                                                       |
| float                      | 76.6 ms                                                      | 81.7 ms: 1.07x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 20.2 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 57.3 ns: 1.08x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 3.07 us: 1.11x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 41.1 us: 1.12x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 426 ms: 1.13x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.40 sec: 1.13x slower                                                      |
| docutils                   | 2.87 sec                                                     | 3.29 sec: 1.15x slower                                                      |
| coroutines                 | 23.0 ms                                                      | 26.4 ms: 1.15x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 167 ms: 1.16x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 27.9 ms: 1.17x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| pyflate                    | 439 ms                                                       | 535 ms: 1.22x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 198 ms: 1.22x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 39.9 us: 1.23x slower                                                       |
| meteor_contest             | 128 ms                                                       | 158 ms: 1.23x slower                                                        |
| regex_compile              | 144 ms                                                       | 178 ms: 1.24x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 4.25 us: 1.26x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 7.57 ms: 1.27x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 4.14 ms: 1.28x slower                                                       |
| 2to3                       | 285 ms                                                       | 365 ms: 1.28x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.78 sec: 1.29x slower                                                      |
| sympy_str                  | 302 ms                                                       | 389 ms: 1.29x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.05 ms: 1.29x slower                                                       |
| chaos                      | 64.0 ms                                                      | 82.7 ms: 1.29x slower                                                       |
| logging_format             | 7.48 us                                                      | 9.76 us: 1.30x slower                                                       |
| logging_simple             | 6.71 us                                                      | 8.75 us: 1.30x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 6.08 us: 1.31x slower                                                       |
| json                       | 5.12 ms                                                      | 6.77 ms: 1.32x slower                                                       |
| raytrace                   | 298 ms                                                       | 396 ms: 1.33x slower                                                        |
| async_generators           | 390 ms                                                       | 529 ms: 1.36x slower                                                        |
| pickle_list                | 4.43 us                                                      | 6.10 us: 1.38x slower                                                       |
| django_template            | 38.2 ms                                                      | 52.7 ms: 1.38x slower                                                       |
| sympy_expand               | 484 ms                                                       | 674 ms: 1.39x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 126 ms: 1.40x slower                                                        |
| scimark_sor                | 109 ms                                                       | 153 ms: 1.40x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 299 us: 1.43x slower                                                        |
| unpickle                   | 14.8 us                                                      | 21.2 us: 1.43x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 456 us: 1.43x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 116 ms: 1.45x slower                                                        |
| json_loads                 | 24.4 us                                                      | 35.6 us: 1.46x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 12.7 ms: 1.47x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 126 ms: 1.47x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 101 ms: 1.47x slower                                                        |
| richards                   | 45.7 ms                                                      | 67.6 ms: 1.48x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 87.2 ms: 1.49x slower                                                       |
| pickle                     | 10.5 us                                                      | 15.8 us: 1.50x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 149 ms: 1.51x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 1.23 sec: 1.52x slower                                                      |
| scimark_fft                | 301 ms                                                       | 459 ms: 1.52x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 15.6 ms: 1.53x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.53 sec: 1.53x slower                                                      |
| richards_super             | 51.3 ms                                                      | 79.4 ms: 1.55x slower                                                       |
| nbody                      | 88.0 ms                                                      | 136 ms: 1.55x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.50 ms: 1.58x slower                                                       |
| fannkuch                   | 350 ms                                                       | 554 ms: 1.58x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 146 ms: 1.59x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 261 us: 1.72x slower                                                        |
| telco                      | 6.96 ms                                                      | 12.2 ms: 1.75x slower                                                       |
| python_startup             | 11.6 ms                                                      | 21.3 ms: 1.83x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 7.83 ms: 1.86x slower                                                       |
| mako                       | 10.0 ms                                                      | 19.8 ms: 1.98x slower                                                       |
| coverage                   | 66.7 ms                                                      | 135 ms: 2.03x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 791 ns: 8.38x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 62.1 ms: 13.04x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.28x slower                                                                |
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.202x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.37x