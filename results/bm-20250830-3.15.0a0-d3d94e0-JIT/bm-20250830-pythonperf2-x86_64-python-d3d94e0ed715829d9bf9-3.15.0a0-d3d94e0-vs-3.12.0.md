# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 611 ms: 1.70x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 622 ms: 1.69x faster                                                        |
| async_tree_none            | 452 ms                                                       | 270 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 325 ms: 1.67x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 498 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 63.1 ms: 1.21x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 104 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_dna      | 239 ms                                                       | 224 ms: 1.07x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.53 ms: 1.01x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 79.6 ms: 1.08x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 195 us: 1.07x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 54.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.3 ms: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.1 ms: 1.02x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 32.9 us: 1.01x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.11 us: 1.10x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.92 us: 1.11x slower                                                       |
| pickle               | 10.5 us                                                      | 12.3 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                       |
| mako            | 10.0 ms                                                      | 9.89 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 611 ms: 1.70x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 622 ms: 1.69x faster                                                        |
| async_tree_none            | 452 ms                                                       | 270 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 325 ms: 1.67x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 498 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                        |
| richards                   | 45.7 ms                                                      | 34.0 ms: 1.35x faster                                                       |
| deepcopy                   | 368 us                                                       | 276 us: 1.33x faster                                                        |
| richards_super             | 51.3 ms                                                      | 38.5 ms: 1.33x faster                                                       |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 28.5 us: 1.29x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| float                      | 76.6 ms                                                      | 63.1 ms: 1.21x faster                                                       |
| go                         | 150 ms                                                       | 125 ms: 1.20x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 77.6 ms: 1.18x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.52 us: 1.15x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.84 ms: 1.14x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                      |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.96 us: 1.13x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.02 us: 1.12x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 58.9 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.50 sec: 1.10x faster                                                      |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| pyflate                    | 439 ms                                                       | 402 ms: 1.09x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 741 ms: 1.09x faster                                                        |
| chaos                      | 64.0 ms                                                      | 58.7 ms: 1.09x faster                                                       |
| django_template            | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 79.6 ms: 1.08x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.2 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 195 us: 1.07x faster                                                        |
| regex_dna                  | 239 ms                                                       | 224 ms: 1.07x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 50.0 ns: 1.06x faster                                                       |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.06x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 54.9 ms: 1.06x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 93.7 ms: 1.05x faster                                                       |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 76.8 ms: 1.05x faster                                                       |
| meteor_contest             | 128 ms                                                       | 122 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.3 ms: 1.05x faster                                                       |
| raytrace                   | 298 ms                                                       | 285 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.20 sec: 1.03x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 92.2 ns: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 370 ms: 1.02x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.1 ms: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.01x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.89 ms: 1.01x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.53 ms: 1.01x faster                                                       |
| scimark_fft                | 301 ms                                                       | 298 ms: 1.01x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 32.9 us: 1.01x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.09 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 91.9 ms: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 495 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.46 ms: 1.07x slower                                                       |
| fannkuch                   | 350 ms                                                       | 379 ms: 1.08x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.11 us: 1.10x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.92 us: 1.11x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.12x slower                                                        |
| async_generators           | 390 ms                                                       | 437 ms: 1.12x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.3 us: 1.17x slower                                                       |
| nbody                      | 88.0 ms                                                      | 104 ms: 1.18x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.04 ms: 1.20x slower                                                       |
| coverage                   | 66.7 ms                                                      | 81.3 ms: 1.22x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.84 ms: 1.79x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.46 ms: 1.86x slower                                                       |
| telco                      | 6.96 ms                                                      | 159 ms: 22.89x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.28 sec: 268.19x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (4): scimark_monte_carlo, asyncio_tcp_ssl, 2to3, bench_thread_pool
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x