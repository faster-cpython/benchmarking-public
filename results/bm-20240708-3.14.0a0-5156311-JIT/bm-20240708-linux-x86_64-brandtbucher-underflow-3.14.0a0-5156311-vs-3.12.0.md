# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 5156311
- commit date: 2024-07-08
- overall geometric mean: 1.07x faster
- HPT reliability: 99.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                             |
| docutils       | 2.77 sec                                               | 3.02 sec: 1.09x slower                                           |
| tornado_http   | 103 ms                                                 | 97.6 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.48x faster                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 852 ms: 1.39x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                             |
| async_tree_io              | 1.16 sec                                               | 887 ms: 1.30x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                             |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 78.9 ms: 1.23x faster                                            |
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                             |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                            |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                             |
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                           |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 82.5 ms: 1.08x faster                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 57.8 ms: 1.07x faster                                            |
| json_loads           | 28.5 us                                                | 27.5 us: 1.04x faster                                            |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                            |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.72 ms: 1.22x faster                                            |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                            |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.48x faster                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.44x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 852 ms: 1.39x faster                                             |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                             |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.33x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                             |
| async_tree_io              | 1.16 sec                                               | 887 ms: 1.30x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 58.1 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                             |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                             |
| nbody                      | 97.0 ms                                                | 78.9 ms: 1.23x faster                                            |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                            |
| mako                       | 11.9 ms                                                | 9.72 ms: 1.22x faster                                            |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.80 us: 1.19x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                            |
| fannkuch                   | 417 ms                                                 | 352 ms: 1.18x faster                                             |
| chaos                      | 67.0 ms                                                | 57.6 ms: 1.16x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                             |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                            |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                             |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.43 ms: 1.14x faster                                            |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.13x faster                                            |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                           |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                             |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 82.5 ms: 1.08x faster                                            |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                            |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                             |
| richards_super             | 51.5 ms                                                | 48.1 ms: 1.07x faster                                            |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                            |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                            |
| tornado_http               | 103 ms                                                 | 97.6 ms: 1.05x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                             |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.04x faster                                            |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                           |
| bench_thread_pool          | 842 us                                                 | 827 us: 1.02x faster                                             |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                            |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                           |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                             |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.55 ms: 1.02x slower                                            |
| sqlglot_optimize           | 54.8 ms                                                | 56.1 ms: 1.02x slower                                            |
| asyncio_tcp                | 491 ms                                                 | 503 ms: 1.03x slower                                             |
| sympy_str                  | 300 ms                                                 | 307 ms: 1.03x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                            |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                             |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                            |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                           |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                             |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                             |
| sympy_sum                  | 169 ms                                                 | 179 ms: 1.06x slower                                             |
| dulwich_log                | 68.5 ms                                                | 72.6 ms: 1.06x slower                                            |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                             |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                            |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                            |
| sympy_expand               | 478 ms                                                 | 518 ms: 1.08x slower                                             |
| docutils                   | 2.77 sec                                               | 3.02 sec: 1.09x slower                                           |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.10x slower                                             |
| logging_silent             | 104 ns                                                 | 115 ns: 1.10x slower                                             |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                            |
| deltablue                  | 3.72 ms                                                | 4.14 ms: 1.11x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                            |
| coverage                   | 72.7 ms                                                | 94.1 ms: 1.29x slower                                            |
| generators                 | 31.2 ms                                                | 43.2 ms: 1.38x slower                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                     |

Benchmark hidden because not significant (6): dask, nqueens, bench_mp_pool, pycparser, regex_effbot, scimark_sor
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240708-3.14.0a0-5156311-JIT/bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.22% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x