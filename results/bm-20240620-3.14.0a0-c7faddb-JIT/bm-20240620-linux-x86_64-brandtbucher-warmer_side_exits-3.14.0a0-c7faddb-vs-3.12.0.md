# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: c7faddb
- commit date: 2024-06-20
- overall geometric mean: 1.06x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.00x slower                                                     |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.05x slower                                                   |
| tornado_http   | 103 ms                                                 | 94.0 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 422 ms: 1.36x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 882 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 563 ms: 1.29x faster                                                     |
| async_tree_none            | 472 ms                                                 | 368 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 452 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 594 ms: 1.22x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                    |
| nbody          | 97.0 ms                                                | 81.2 ms: 1.19x faster                                                    |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.95 ms: 1.10x slower                                                    |
| regex_dna      | 212 ms                                                 | 233 ms: 1.10x slower                                                     |
| regex_v8       | 23.1 ms                                                | 26.3 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 296 us: 1.10x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 57.3 ms: 1.08x faster                                                    |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                                     |
| pickle_dict          | 35.5 us                                                | 34.5 us: 1.03x faster                                                    |
| unpickle_list        | 5.29 us                                                | 5.20 us: 1.02x faster                                                    |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.02x faster                                                    |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                    |
| pickle               | 11.6 us                                                | 11.9 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.41 ms: 1.07x slower                                                    |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.80 ms: 1.21x faster                                                    |
| django_template | 34.6 ms                                                | 36.5 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 28.5 us: 1.43x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 422 ms: 1.36x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 882 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                                     |
| deepcopy                   | 371 us                                                 | 278 us: 1.34x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 563 ms: 1.29x faster                                                     |
| async_tree_none            | 472 ms                                                 | 368 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 452 ms: 1.28x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.8 ms: 1.23x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 61.4 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 594 ms: 1.22x faster                                                     |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                     |
| mako                       | 11.9 ms                                                | 9.80 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                    |
| fannkuch                   | 417 ms                                                 | 345 ms: 1.21x faster                                                     |
| float                      | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                    |
| nbody                      | 97.0 ms                                                | 81.2 ms: 1.19x faster                                                    |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.18x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.36 ms: 1.16x faster                                                    |
| pyflate                    | 482 ms                                                 | 425 ms: 1.14x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                                    |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                     |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 296 us: 1.10x faster                                                     |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                     |
| tornado_http               | 103 ms                                                 | 94.0 ms: 1.09x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 57.3 ms: 1.08x faster                                                    |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                    |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                    |
| pickle_dict                | 35.5 us                                                | 34.5 us: 1.03x faster                                                    |
| richards                   | 45.8 ms                                                | 44.6 ms: 1.03x faster                                                    |
| richards_super             | 51.5 ms                                                | 50.5 ms: 1.02x faster                                                    |
| dask                       | 372 ms                                                 | 366 ms: 1.02x faster                                                     |
| unpickle_list              | 5.29 us                                                | 5.20 us: 1.02x faster                                                    |
| pickle_list                | 5.08 us                                                | 5.01 us: 1.02x faster                                                    |
| bench_thread_pool          | 842 us                                                 | 830 us: 1.01x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 67.9 ms: 1.01x faster                                                    |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                                     |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                    |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                                     |
| asyncio_tcp                | 491 ms                                                 | 489 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                   |
| 2to3                       | 274 ms                                                 | 276 ms: 1.00x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                     |
| nqueens                    | 83.3 ms                                                | 84.2 ms: 1.01x slower                                                    |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                   |
| pickle                     | 11.6 us                                                | 11.9 us: 1.02x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.57 ms: 1.02x slower                                                    |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.03x slower                                                     |
| deltablue                  | 3.72 ms                                                | 3.85 ms: 1.04x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.05x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 57.7 ms: 1.05x slower                                                    |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                                     |
| django_template            | 34.6 ms                                                | 36.5 ms: 1.06x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.01 ms: 1.06x slower                                                    |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.41 ms: 1.07x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                     |
| regex_effbot               | 3.61 ms                                                | 3.95 ms: 1.10x slower                                                    |
| regex_dna                  | 212 ms                                                 | 233 ms: 1.10x slower                                                     |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 26.3 ms: 1.14x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                    |
| coverage                   | 72.7 ms                                                | 94.2 ms: 1.30x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (4): sqlite_synth, bench_mp_pool, json, json_dumps
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240620-3.14.0a0-c7faddb-JIT/bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x