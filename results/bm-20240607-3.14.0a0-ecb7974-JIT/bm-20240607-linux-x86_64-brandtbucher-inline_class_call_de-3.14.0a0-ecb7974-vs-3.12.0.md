# Results vs. 3.12.0

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: ecb7974
- commit date: 2024-06-07
- overall geometric mean: 1.04x faster
- HPT reliability: 96.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                        |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                      |
| tornado_http   | 103 ms                                                 | 98.0 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 342 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 912 ms: 1.30x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 445 ms: 1.29x faster                                                        |
| async_tree_none            | 472 ms                                                 | 377 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 594 ms: 1.22x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 949 ms: 1.22x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 483 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 634 ms: 1.14x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.1 ms: 1.21x faster                                                       |
| float          | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                       |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                       |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                        |
| unpickle             | 15.9 us                                                | 15.0 us: 1.06x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 225 us: 1.02x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                       |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                       |
| pickle_dict          | 35.5 us                                                | 36.3 us: 1.02x slower                                                       |
| unpickle_list        | 5.29 us                                                | 5.43 us: 1.03x slower                                                       |
| pickle_list          | 5.08 us                                                | 5.33 us: 1.05x slower                                                       |
| pickle               | 11.6 us                                                | 12.3 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.64 ms: 1.10x slower                                                       |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                       |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 342 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 912 ms: 1.30x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 445 ms: 1.29x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                       |
| async_tree_none            | 472 ms                                                 | 377 ms: 1.25x faster                                                        |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 594 ms: 1.22x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 949 ms: 1.22x faster                                                        |
| nbody                      | 97.0 ms                                                | 80.1 ms: 1.21x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 62.5 ms: 1.20x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 68.4 ms: 1.20x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 483 ms: 1.20x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                      |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                       |
| fannkuch                   | 417 ms                                                 | 356 ms: 1.17x faster                                                        |
| float                      | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 634 ms: 1.14x faster                                                        |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.14x faster                                                       |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.51 ms: 1.12x faster                                                       |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.12x faster                                                       |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                        |
| richards                   | 45.8 ms                                                | 41.8 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                                        |
| richards_super             | 51.5 ms                                                | 47.6 ms: 1.08x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                        |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 38.3 us: 1.06x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.59 ms: 1.06x faster                                                       |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.06x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                       |
| tornado_http               | 103 ms                                                 | 98.0 ms: 1.05x faster                                                       |
| pyflate                    | 482 ms                                                 | 463 ms: 1.04x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                       |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                        |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 225 us: 1.02x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.32 us: 1.01x faster                                                       |
| deepcopy                   | 371 us                                                 | 369 us: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                        |
| dulwich_log                | 68.5 ms                                                | 69.2 ms: 1.01x slower                                                       |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                       |
| async_generators           | 463 ms                                                 | 470 ms: 1.02x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                       |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                                        |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                        |
| pickle_dict                | 35.5 us                                                | 36.3 us: 1.02x slower                                                       |
| unpickle_list              | 5.29 us                                                | 5.43 us: 1.03x slower                                                       |
| json                       | 5.26 ms                                                | 5.40 ms: 1.03x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                        |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                        |
| logging_silent             | 104 ns                                                 | 108 ns: 1.04x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 878 us: 1.04x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 512 ms: 1.04x slower                                                        |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.70 ms: 1.04x slower                                                       |
| nqueens                    | 83.3 ms                                                | 87.3 ms: 1.05x slower                                                       |
| pickle_list                | 5.08 us                                                | 5.33 us: 1.05x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                       |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                        |
| pickle                     | 11.6 us                                                | 12.3 us: 1.06x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                       |
| mdp                        | 2.63 sec                                               | 2.79 sec: 1.06x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                        |
| sympy_expand               | 478 ms                                                 | 514 ms: 1.07x slower                                                        |
| go                         | 139 ms                                                 | 151 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.10x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.64 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                                       |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                       |
| coverage                   | 72.7 ms                                                | 94.4 ms: 1.30x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (3): scimark_sor, bench_mp_pool, deltablue
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240607-3.14.0a0-ecb7974-JIT/bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x