# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                        |
| async_tree_none            | 452 ms                                                       | 268 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 626 ms: 1.68x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 325 ms: 1.67x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 269 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 498 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 68.5 ms: 1.12x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 93.2 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_dna      | 239 ms                                                       | 226 ms: 1.06x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.99 sec: 1.08x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 96.8 ms: 1.06x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.5 ms: 1.02x faster                                                       |
| json_dumps           | 10.2 ms                                                      | 10.2 ms: 1.00x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| pickle_dict          | 32.5 us                                                      | 33.7 us: 1.03x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.97 us: 1.07x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.07 us: 1.15x slower                                                       |
| pickle               | 10.5 us                                                      | 12.1 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.7 ms: 1.10x faster                                                       |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                        |
| async_tree_none            | 452 ms                                                       | 268 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 626 ms: 1.68x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 325 ms: 1.67x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 269 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 498 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.37x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.1 us: 1.36x faster                                                       |
| deepcopy                   | 368 us                                                       | 276 us: 1.34x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.7 us: 1.33x faster                                                       |
| go                         | 150 ms                                                       | 117 ms: 1.28x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.9 ms: 1.25x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 43.1 ns: 1.23x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.36 us: 1.18x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 59.6 ms: 1.16x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.84 us: 1.15x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.98 us: 1.13x faster                                                       |
| float                      | 76.6 ms                                                      | 68.5 ms: 1.12x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 58.5 ms: 1.12x faster                                                       |
| chaos                      | 64.0 ms                                                      | 58.1 ms: 1.10x faster                                                       |
| django_template            | 38.2 ms                                                      | 34.7 ms: 1.10x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 21.8 ms: 1.10x faster                                                       |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 1.99 sec: 1.08x faster                                                      |
| pyflate                    | 439 ms                                                       | 406 ms: 1.08x faster                                                        |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 74.8 ms: 1.07x faster                                                       |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.07x faster                                                        |
| sympy_str                  | 302 ms                                                       | 283 ms: 1.07x faster                                                        |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 96.8 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.06x faster                                                      |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.06x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 93.7 ms: 1.05x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 87.4 ms: 1.05x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 773 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.1 ms: 1.04x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.16 ms: 1.02x faster                                                       |
| hexiom                     | 5.96 ms                                                      | 5.84 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.02x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 92.8 ns: 1.02x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 57.5 ms: 1.02x faster                                                       |
| richards_super             | 51.3 ms                                                      | 50.6 ms: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.2 ms: 1.00x faster                                                       |
| sympy_expand               | 484 ms                                                       | 486 ms: 1.00x slower                                                        |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 92.1 ms: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 33.7 us: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.36 ms: 1.05x slower                                                       |
| nbody                      | 88.0 ms                                                      | 93.2 ms: 1.06x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.97 us: 1.07x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                       |
| async_generators           | 390 ms                                                       | 421 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.07 us: 1.15x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.1 us: 1.15x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.92 ms: 1.17x slower                                                       |
| coverage                   | 66.7 ms                                                      | 82.7 ms: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.31x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.93 ms: 1.84x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.43 ms: 1.85x slower                                                       |
| telco                      | 6.96 ms                                                      | 157 ms: 22.60x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.50 sec: 314.36x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (2): docutils, bench_thread_pool
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x