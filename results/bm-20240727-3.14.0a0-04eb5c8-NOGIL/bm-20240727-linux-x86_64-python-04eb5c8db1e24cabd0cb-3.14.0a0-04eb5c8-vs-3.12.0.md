# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.36x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 394 ms: 1.44x slower                                                  |
| docutils       | 2.77 sec                                               | 3.35 sec: 1.21x slower                                                |
| tornado_http   | 103 ms                                                 | 136 ms: 1.32x slower                                                  |
| Geometric mean | (ref)                                                  | 1.32x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 346 ms: 1.30x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 908 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 453 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 597 ms: 1.21x faster                                                  |
| async_tree_none            | 472 ms                                                 | 406 ms: 1.16x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 510 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 662 ms: 1.10x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 184 ms: 1.02x faster                                                  |
| float          | 84.7 ms                                                | 142 ms: 1.67x slower                                                  |
| nbody          | 97.0 ms                                                | 217 ms: 2.24x slower                                                  |
| Geometric mean | (ref)                                                  | 1.55x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                 |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.8 ms: 1.16x slower                                                 |
| regex_compile  | 148 ms                                                 | 217 ms: 1.46x slower                                                  |
| Geometric mean | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| json_loads           | 28.5 us                                                | 32.2 us: 1.13x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 111 ms: 1.24x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| tomli_loads          | 2.33 sec                                               | 3.22 sec: 1.38x slower                                                |
| xml_etree_process    | 61.7 ms                                                | 89.5 ms: 1.45x slower                                                 |
| unpickle_pure_python | 230 us                                                 | 399 us: 1.74x slower                                                  |
| pickle_pure_python   | 324 us                                                 | 571 us: 1.76x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.30x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.08 ms: 1.31x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.4 ms: 1.41x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 60.9 ms: 1.76x slower                                                 |
| mako            | 11.9 ms                                                | 21.1 ms: 1.78x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.77x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 2.89 ms: 1.31x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 346 ms: 1.30x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 908 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 453 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 597 ms: 1.21x faster                                                  |
| async_tree_none            | 472 ms                                                 | 406 ms: 1.16x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 510 ms: 1.13x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 662 ms: 1.10x faster                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.37 ms: 1.08x faster                                                 |
| pidigits                   | 187 ms                                                 | 184 ms: 1.02x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                 |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                  |
| json_loads                 | 28.5 us                                                | 32.2 us: 1.13x slower                                                 |
| json                       | 5.26 ms                                                | 5.99 ms: 1.14x slower                                                 |
| deepcopy                   | 371 us                                                 | 423 us: 1.14x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 567 ms: 1.16x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 26.8 ms: 1.16x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.08 sec: 1.16x slower                                                |
| docutils                   | 2.77 sec                                               | 3.35 sec: 1.21x slower                                                |
| generators                 | 31.2 ms                                                | 38.0 ms: 1.22x slower                                                 |
| async_generators           | 463 ms                                                 | 565 ms: 1.22x slower                                                  |
| scimark_fft                | 382 ms                                                 | 475 ms: 1.24x slower                                                  |
| xml_etree_generate         | 89.2 ms                                                | 111 ms: 1.24x slower                                                  |
| mdp                        | 2.63 sec                                               | 3.37 sec: 1.28x slower                                                |
| deepcopy_memo              | 40.7 us                                                | 52.3 us: 1.28x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 9.08 ms: 1.31x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.63 ms: 1.31x slower                                                 |
| meteor_contest             | 112 ms                                                 | 148 ms: 1.32x slower                                                  |
| comprehensions             | 21.8 us                                                | 28.7 us: 1.32x slower                                                 |
| deepcopy_reduce            | 3.35 us                                                | 4.42 us: 1.32x slower                                                 |
| tornado_http               | 103 ms                                                 | 136 ms: 1.32x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 28.7 ms: 1.34x slower                                                 |
| coroutines                 | 23.2 ms                                                | 31.2 ms: 1.35x slower                                                 |
| crypto_pyaes               | 81.9 ms                                                | 112 ms: 1.37x slower                                                  |
| tomli_loads                | 2.33 sec                                               | 3.22 sec: 1.38x slower                                                |
| pycparser                  | 1.18 sec                                               | 1.64 sec: 1.39x slower                                                |
| python_startup             | 9.55 ms                                                | 13.4 ms: 1.41x slower                                                 |
| telco                      | 7.10 ms                                                | 10.0 ms: 1.41x slower                                                 |
| sympy_str                  | 300 ms                                                 | 424 ms: 1.42x slower                                                  |
| nqueens                    | 83.3 ms                                                | 119 ms: 1.43x slower                                                  |
| 2to3                       | 274 ms                                                 | 394 ms: 1.44x slower                                                  |
| xml_etree_process          | 61.7 ms                                                | 89.5 ms: 1.45x slower                                                 |
| fannkuch                   | 417 ms                                                 | 608 ms: 1.46x slower                                                  |
| regex_compile              | 148 ms                                                 | 217 ms: 1.46x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 254 ms: 1.50x slower                                                  |
| coverage                   | 72.7 ms                                                | 110 ms: 1.52x slower                                                  |
| sympy_expand               | 478 ms                                                 | 753 ms: 1.57x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 177 ms: 1.60x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 254 us: 1.61x slower                                                  |
| pyflate                    | 482 ms                                                 | 777 ms: 1.61x slower                                                  |
| spectral_norm              | 115 ms                                                 | 186 ms: 1.62x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 88.8 ms: 1.62x slower                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 124 ms: 1.65x slower                                                  |
| logging_simple             | 6.46 us                                                | 10.7 us: 1.65x slower                                                 |
| logging_format             | 7.23 us                                                | 12.0 us: 1.66x slower                                                 |
| float                      | 84.7 ms                                                | 142 ms: 1.67x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 1.32 sec: 1.70x slower                                                |
| richards                   | 45.8 ms                                                | 78.0 ms: 1.70x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 2.72 sec: 1.73x slower                                                |
| unpickle_pure_python       | 230 us                                                 | 399 us: 1.74x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 571 us: 1.76x slower                                                  |
| django_template            | 34.6 ms                                                | 60.9 ms: 1.76x slower                                                 |
| logging_silent             | 104 ns                                                 | 185 ns: 1.77x slower                                                  |
| mako                       | 11.9 ms                                                | 21.1 ms: 1.78x slower                                                 |
| richards_super             | 51.5 ms                                                | 94.6 ms: 1.84x slower                                                 |
| chaos                      | 67.0 ms                                                | 124 ms: 1.86x slower                                                  |
| hexiom                     | 6.41 ms                                                | 12.0 ms: 1.88x slower                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 3.20 ms: 1.90x slower                                                 |
| raytrace                   | 312 ms                                                 | 593 ms: 1.90x slower                                                  |
| sqlglot_parse              | 1.36 ms                                                | 2.71 ms: 1.99x slower                                                 |
| scimark_sor                | 129 ms                                                 | 264 ms: 2.04x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 245 ms: 2.07x slower                                                  |
| go                         | 139 ms                                                 | 307 ms: 2.20x slower                                                  |
| deltablue                  | 3.72 ms                                                | 8.28 ms: 2.23x slower                                                 |
| nbody                      | 97.0 ms                                                | 217 ms: 2.24x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.03 ms: 3.60x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.36x slower                                                          |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.14x