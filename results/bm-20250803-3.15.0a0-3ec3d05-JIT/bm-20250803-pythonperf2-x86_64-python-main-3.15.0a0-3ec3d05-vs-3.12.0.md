# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ec3d05
- commit date: 2025-08-03
- overall geometric mean: 1.034x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                        |
| docutils       | 2.87 sec                                                     | 2.94 sec: 1.02x slower                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 628 ms: 1.66x faster                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 637 ms: 1.65x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                        |
| async_tree_none            | 452 ms                                                       | 281 ms: 1.61x faster                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.60x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 76.6 ms                                                      | 64.6 ms: 1.19x faster                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                        |
| nbody          | 88.0 ms                                                      | 99.1 ms: 1.13x slower                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                        |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                        |
| regex_v8       | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                       |
| regex_effbot   | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.92 sec: 1.12x faster                                      |
| unpickle_pure_python | 210 us                                                       | 194 us: 1.08x faster                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.5 ms: 1.07x faster                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.5 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.8 ms: 1.05x faster                                       |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                        |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                        |
| json_loads           | 24.4 us                                                      | 26.5 us: 1.09x slower                                       |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.33x slower                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.5 ms: 1.07x faster                                       |
| mako            | 10.0 ms                                                      | 9.78 ms: 1.02x faster                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.28 sec: 2.00x faster                                      |
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 628 ms: 1.66x faster                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 637 ms: 1.65x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                        |
| async_tree_none            | 452 ms                                                       | 281 ms: 1.61x faster                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.60x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                        |
| deepcopy                   | 368 us                                                       | 280 us: 1.32x faster                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.1 us: 1.31x faster                                       |
| richards                   | 45.7 ms                                                      | 35.4 ms: 1.29x faster                                       |
| generators                 | 37.4 ms                                                      | 29.5 ms: 1.27x faster                                       |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                       |
| richards_super             | 51.3 ms                                                      | 41.4 ms: 1.24x faster                                       |
| float                      | 76.6 ms                                                      | 64.6 ms: 1.19x faster                                       |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                        |
| spectral_norm              | 91.6 ms                                                      | 79.7 ms: 1.15x faster                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.98 us: 1.13x faster                                       |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                       |
| tomli_loads                | 2.16 sec                                                     | 1.92 sec: 1.12x faster                                      |
| logging_format             | 7.48 us                                                      | 6.69 us: 1.12x faster                                       |
| deltablue                  | 3.24 ms                                                      | 2.91 ms: 1.11x faster                                       |
| dulwich_log                | 65.4 ms                                                      | 58.8 ms: 1.11x faster                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.50 sec: 1.10x faster                                      |
| logging_simple             | 6.71 us                                                      | 6.10 us: 1.10x faster                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.8 ms: 1.10x faster                                       |
| pprint_safe_repr           | 807 ms                                                       | 741 ms: 1.09x faster                                        |
| chaos                      | 64.0 ms                                                      | 59.0 ms: 1.08x faster                                       |
| unpickle_pure_python       | 210 us                                                       | 194 us: 1.08x faster                                        |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.08x faster                                        |
| pyflate                    | 439 ms                                                       | 408 ms: 1.08x faster                                        |
| django_template            | 38.2 ms                                                      | 35.5 ms: 1.07x faster                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.5 ms: 1.07x faster                                       |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                        |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.5 ms: 1.06x faster                                       |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.5 ms: 1.05x faster                                       |
| regex_dna                  | 239 ms                                                       | 227 ms: 1.05x faster                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.8 ms: 1.05x faster                                       |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                        |
| crypto_pyaes               | 80.3 ms                                                      | 77.6 ms: 1.04x faster                                       |
| scimark_lu                 | 98.8 ms                                                      | 95.4 ms: 1.04x faster                                       |
| raytrace                   | 298 ms                                                       | 288 ms: 1.04x faster                                        |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                       |
| mako                       | 10.0 ms                                                      | 9.78 ms: 1.02x faster                                       |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                        |
| regex_v8                   | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                       |
| scimark_fft                | 301 ms                                                       | 297 ms: 1.01x faster                                        |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                        |
| logging_silent             | 94.4 ns                                                      | 93.7 ns: 1.01x faster                                       |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                        |
| nqueens                    | 89.9 ms                                                      | 90.8 ms: 1.01x slower                                       |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                       |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                      |
| regex_effbot               | 3.57 ms                                                      | 3.64 ms: 1.02x slower                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                       |
| docutils                   | 2.87 sec                                                     | 2.94 sec: 1.02x slower                                      |
| sympy_expand               | 484 ms                                                       | 498 ms: 1.03x slower                                        |
| hexiom                     | 5.96 ms                                                      | 6.21 ms: 1.04x slower                                       |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                        |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                       |
| fannkuch                   | 350 ms                                                       | 376 ms: 1.07x slower                                        |
| json_loads                 | 24.4 us                                                      | 26.5 us: 1.09x slower                                       |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                       |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.12x slower                                        |
| nbody                      | 88.0 ms                                                      | 99.1 ms: 1.13x slower                                       |
| async_generators           | 390 ms                                                       | 440 ms: 1.13x slower                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.96 ms: 1.18x slower                                       |
| coverage                   | 66.7 ms                                                      | 80.7 ms: 1.21x slower                                       |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.33x slower                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                       |
| gc_traversal               | 3.48 ms                                                      | 6.51 ms: 1.87x slower                                       |
| telco                      | 6.96 ms                                                      | 158 ms: 22.76x slower                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                |
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250803-3.15.0a0-3ec3d05-JIT/bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x