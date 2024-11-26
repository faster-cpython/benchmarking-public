# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                |
| tornado_http   | 103 ms                                                 | 90.8 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 390 ms: 1.48x faster                                                  |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 401 ms: 1.43x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 896 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 928 ms: 1.25x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.8 ms: 1.13x faster                                                 |
| float          | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.8 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| django_template | 34.6 ms                                                | 33.5 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 390 ms: 1.48x faster                                                  |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 401 ms: 1.43x faster                                                  |
| deepcopy                   | 371 us                                                 | 264 us: 1.41x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 896 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 928 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                 |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                  |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                                 |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                 |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| tornado_http               | 103 ms                                                 | 90.8 ms: 1.13x faster                                                 |
| nbody                      | 97.0 ms                                                | 85.8 ms: 1.13x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 72.4 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                 |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                 |
| float                      | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                                  |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| bench_thread_pool          | 842 us                                                 | 787 us: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                  |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.77 ms: 1.06x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                 |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                |
| django_template            | 34.6 ms                                                | 33.5 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                  |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                  |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 482 ms: 1.02x faster                                                  |
| pyflate                    | 482 ms                                                 | 478 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                  |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.8 ms: 1.16x slower                                                 |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                                 |
| telco                      | 7.10 ms                                                | 8.31 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (5): bench_mp_pool, json, richards, json_loads, richards_super
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.085x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x