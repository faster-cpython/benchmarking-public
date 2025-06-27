# Results vs. 3.12.0

- fork: python
- ref: a4625d597f9fc2d083fb
- machine: linux-x86_64
- commit hash: a4625d5
- commit date: 2025-06-26
- overall geometric mean: 1.071x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 280 ms: 1.02x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 631 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.60x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.6 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 260 ms: 1.02x faster                                                        |
| nbody          | 88.0 ms                                                      | 92.3 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.09x faster                                                        |
| regex_dna      | 239 ms                                                       | 221 ms: 1.08x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.1 ms: 1.03x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 83.4 ms: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                       |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 631 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.60x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                        |
| deepcopy                   | 368 us                                                       | 273 us: 1.35x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.3 us: 1.34x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 28.5 us: 1.29x faster                                                       |
| go                         | 150 ms                                                       | 119 ms: 1.26x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.1 ms: 1.24x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.94 us: 1.15x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 60.6 ms: 1.14x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.64 us: 1.13x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.01 us: 1.12x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.6 ms: 1.10x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 21.9 ms: 1.09x faster                                                       |
| pyflate                    | 439 ms                                                       | 402 ms: 1.09x faster                                                        |
| chaos                      | 64.0 ms                                                      | 58.8 ms: 1.09x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 149 ms: 1.09x faster                                                        |
| regex_compile              | 144 ms                                                       | 133 ms: 1.09x faster                                                        |
| float                      | 76.6 ms                                                      | 70.6 ms: 1.08x faster                                                       |
| regex_dna                  | 239 ms                                                       | 221 ms: 1.08x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                       |
| meteor_contest             | 128 ms                                                       | 119 ms: 1.07x faster                                                        |
| raytrace                   | 298 ms                                                       | 279 ms: 1.07x faster                                                        |
| sympy_str                  | 302 ms                                                       | 284 ms: 1.06x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.3 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                                      |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.0 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 779 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 83.4 ms: 1.03x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 77.9 ms: 1.03x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.1 ms: 1.03x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                       |
| pidigits                   | 265 ms                                                       | 260 ms: 1.02x faster                                                        |
| 2to3                       | 285 ms                                                       | 280 ms: 1.02x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.18 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.02x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                                      |
| richards                   | 45.7 ms                                                      | 45.4 ms: 1.01x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 93.8 ns: 1.01x faster                                                       |
| hexiom                     | 5.96 ms                                                      | 5.93 ms: 1.00x faster                                                       |
| sympy_expand               | 484 ms                                                       | 483 ms: 1.00x faster                                                        |
| richards_super             | 51.3 ms                                                      | 51.7 ms: 1.01x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 90.8 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| scimark_fft                | 301 ms                                                       | 307 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                        |
| fannkuch                   | 350 ms                                                       | 363 ms: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                       |
| nbody                      | 88.0 ms                                                      | 92.3 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 163 us: 1.08x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                       |
| async_generators           | 390 ms                                                       | 427 ms: 1.09x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.64 ms: 1.10x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.77 ms: 1.13x slower                                                       |
| coverage                   | 66.7 ms                                                      | 82.8 ms: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.31x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.83 ms: 1.78x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_process, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250626-3.15.0a0-a4625d5/bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.12x