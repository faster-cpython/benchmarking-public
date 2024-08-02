# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 091375e
- commit date: 2024-07-03
- overall geometric mean: 1.07x faster
- HPT reliability: 99.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                             |
| docutils       | 2.77 sec                                               | 3.01 sec: 1.09x slower                                           |
| tornado_http   | 103 ms                                                 | 97.7 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                             |
| async_tree_io              | 1.16 sec                                               | 870 ms: 1.33x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                             |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.9 ms: 1.21x faster                                            |
| float          | 84.7 ms                                                | 70.2 ms: 1.21x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                             |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                            |
| regex_dna      | 212 ms                                                 | 230 ms: 1.09x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 200 us: 1.15x faster                                             |
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                           |
| xml_etree_generate   | 89.2 ms                                                | 80.9 ms: 1.10x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                             |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 57.5 ms: 1.07x faster                                            |
| json_loads           | 28.5 us                                                | 27.3 us: 1.05x faster                                            |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.86 ms: 1.21x faster                                            |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                            |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.51x faster                                             |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                             |
| deepcopy                   | 371 us                                                 | 274 us: 1.36x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                             |
| async_tree_io              | 1.16 sec                                               | 870 ms: 1.33x faster                                             |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 57.4 ms: 1.31x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 66.9 ms: 1.22x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                            |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                             |
| nbody                      | 97.0 ms                                                | 79.9 ms: 1.21x faster                                            |
| mako                       | 11.9 ms                                                | 9.86 ms: 1.21x faster                                            |
| float                      | 84.7 ms                                                | 70.2 ms: 1.21x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.30 ms: 1.18x faster                                            |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                             |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                            |
| logging_format             | 7.23 us                                                | 6.27 us: 1.15x faster                                            |
| fannkuch                   | 417 ms                                                 | 362 ms: 1.15x faster                                             |
| unpickle_pure_python       | 230 us                                                 | 200 us: 1.15x faster                                             |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                           |
| pyflate                    | 482 ms                                                 | 427 ms: 1.13x faster                                             |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                            |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 80.9 ms: 1.10x faster                                            |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                             |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                             |
| regex_compile              | 148 ms                                                 | 138 ms: 1.08x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                            |
| xml_etree_process          | 61.7 ms                                                | 57.5 ms: 1.07x faster                                            |
| logging_silent             | 104 ns                                                 | 98.4 ns: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                            |
| tornado_http               | 103 ms                                                 | 97.7 ms: 1.05x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                             |
| json_loads                 | 28.5 us                                                | 27.3 us: 1.05x faster                                            |
| richards_super             | 51.5 ms                                                | 49.7 ms: 1.04x faster                                            |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                           |
| richards                   | 45.8 ms                                                | 44.6 ms: 1.03x faster                                            |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.02x faster                                            |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                           |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                             |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                             |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                           |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                             |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.01x slower                                            |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                             |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                             |
| go                         | 139 ms                                                 | 143 ms: 1.02x slower                                             |
| nqueens                    | 83.3 ms                                                | 85.4 ms: 1.03x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.59 ms: 1.03x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                            |
| sympy_str                  | 300 ms                                                 | 309 ms: 1.03x slower                                             |
| asyncio_tcp                | 491 ms                                                 | 508 ms: 1.04x slower                                             |
| dulwich_log                | 68.5 ms                                                | 71.8 ms: 1.05x slower                                            |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                            |
| sqlglot_optimize           | 54.8 ms                                                | 57.6 ms: 1.05x slower                                            |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                             |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                             |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                            |
| sqlglot_normalize          | 110 ms                                                 | 119 ms: 1.08x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 23.2 ms: 1.08x slower                                            |
| sympy_expand               | 478 ms                                                 | 517 ms: 1.08x slower                                             |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.09x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                             |
| docutils                   | 2.77 sec                                               | 3.01 sec: 1.09x slower                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| deltablue                  | 3.72 ms                                                | 4.10 ms: 1.10x slower                                            |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                            |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                            |
| generators                 | 31.2 ms                                                | 48.4 ms: 1.55x slower                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                     |

Benchmark hidden because not significant (5): dask, pprint_pformat, regex_effbot, bench_mp_pool, json_dumps
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240703-3.14.0a0-091375e-JIT/bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.54% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x