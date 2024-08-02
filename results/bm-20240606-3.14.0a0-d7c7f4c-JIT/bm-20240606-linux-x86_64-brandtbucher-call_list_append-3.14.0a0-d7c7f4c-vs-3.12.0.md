# Results vs. 3.12.0

- fork: brandtbucher
- ref: call_list_append
- machine: linux-x86_64
- commit hash: d7c7f4c
- commit date: 2024-06-06
- overall geometric mean: 1.04x faster
- HPT reliability: 98.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                    |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                  |
| tornado_http   | 103 ms                                                 | 97.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 343 ms: 1.31x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 446 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 929 ms: 1.27x faster                                                    |
| async_tree_none            | 472 ms                                                 | 384 ms: 1.23x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 474 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 602 ms: 1.21x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 999 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 640 ms: 1.13x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.5 ms: 1.17x faster                                                   |
| float          | 84.7 ms                                                | 72.6 ms: 1.17x faster                                                   |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                   |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 57.7 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                    |
| pickle_dict          | 35.5 us                                                | 34.7 us: 1.02x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 225 us: 1.02x faster                                                    |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.01x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                   |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                   |
| unpickle_list        | 5.29 us                                                | 5.37 us: 1.02x slower                                                   |
| pickle               | 11.6 us                                                | 12.0 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.60 ms: 1.10x slower                                                   |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                   |
| django_template | 34.6 ms                                                | 37.3 ms: 1.08x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 343 ms: 1.31x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 446 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 929 ms: 1.27x faster                                                    |
| async_tree_none            | 472 ms                                                 | 384 ms: 1.23x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 474 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 602 ms: 1.21x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                  |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                   |
| scimark_fft                | 382 ms                                                 | 324 ms: 1.18x faster                                                    |
| nbody                      | 97.0 ms                                                | 82.5 ms: 1.17x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                   |
| fannkuch                   | 417 ms                                                 | 356 ms: 1.17x faster                                                    |
| float                      | 84.7 ms                                                | 72.6 ms: 1.17x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 70.2 ms: 1.17x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 999 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 640 ms: 1.13x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.71 us: 1.13x faster                                                   |
| logging_format             | 7.23 us                                                | 6.42 us: 1.13x faster                                                   |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                                    |
| chaos                      | 67.0 ms                                                | 60.3 ms: 1.11x faster                                                   |
| richards                   | 45.8 ms                                                | 41.8 ms: 1.10x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.64 ms: 1.09x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                   |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.09x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                    |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 57.7 ms: 1.07x faster                                                   |
| richards_super             | 51.5 ms                                                | 48.4 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 38.4 us: 1.06x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                    |
| tornado_http               | 103 ms                                                 | 97.1 ms: 1.06x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.7 us: 1.02x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 225 us: 1.02x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.01x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                   |
| generators                 | 31.2 ms                                                | 30.9 ms: 1.01x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.01x slower                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                    |
| sympy_str                  | 300 ms                                                 | 301 ms: 1.01x slower                                                    |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.14 us: 1.01x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                    |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                   |
| async_generators           | 463 ms                                                 | 469 ms: 1.01x slower                                                    |
| unpickle_list              | 5.29 us                                                | 5.37 us: 1.02x slower                                                   |
| deepcopy                   | 371 us                                                 | 378 us: 1.02x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 3.87 ms: 1.02x slower                                                   |
| nqueens                    | 83.3 ms                                                | 85.0 ms: 1.02x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                    |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                    |
| dask                       | 372 ms                                                 | 381 ms: 1.02x slower                                                    |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 568 ms: 1.03x slower                                                    |
| pickle                     | 11.6 us                                                | 12.0 us: 1.03x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.66 ms: 1.04x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 57.0 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.87 sec: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                                    |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 518 ms: 1.05x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                    |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                    |
| sympy_expand               | 478 ms                                                 | 512 ms: 1.07x slower                                                    |
| django_template            | 34.6 ms                                                | 37.3 ms: 1.08x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.60 ms: 1.10x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                    |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                   |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                   |
| coverage                   | 72.7 ms                                                | 93.5 ms: 1.29x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (5): unpickle, deepcopy_reduce, scimark_sor, bench_mp_pool, deltablue
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240606-3.14.0a0-d7c7f4c-JIT/bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.61% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x