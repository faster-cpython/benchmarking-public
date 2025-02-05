# Results vs. 3.12.0

- fork: python
- ref: 91b7f2e7f6593acefda4
- machine: linux-x86_64
- commit hash: 91b7f2e
- commit date: 2024-09-01
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                  |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| tornado_http   | 103 ms                                                 | 94.4 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 406 ms: 1.41x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 899 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 554 ms: 1.31x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.8 ms: 1.22x faster                                                 |
| float          | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                 |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.52 ms: 1.02x faster                                                 |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 77.6 ms: 1.15x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.1 ms: 1.12x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.97 ms: 1.19x faster                                                 |
| django_template | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.53x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                                  |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 406 ms: 1.41x faster                                                  |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 537 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 899 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 554 ms: 1.31x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 65.7 ms: 1.25x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                  |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.23x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                |
| nbody                      | 97.0 ms                                                | 79.8 ms: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| float                      | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 62.9 ms: 1.19x faster                                                 |
| mako                       | 11.9 ms                                                | 9.97 ms: 1.19x faster                                                 |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                 |
| richards                   | 45.8 ms                                                | 39.3 ms: 1.17x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.34 ms: 1.17x faster                                                 |
| spectral_norm              | 115 ms                                                 | 99.9 ms: 1.15x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 77.6 ms: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                 |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                  |
| richards_super             | 51.5 ms                                                | 45.4 ms: 1.13x faster                                                 |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.1 ms: 1.12x faster                                                 |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                  |
| tornado_http               | 103 ms                                                 | 94.4 ms: 1.09x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 718 ms: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.07x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                                |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.52 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                 |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.01x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 68.2 ms: 1.00x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 495 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                                 |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                  |
| nqueens                    | 83.3 ms                                                | 85.1 ms: 1.02x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                  |
| django_template            | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                 |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                  |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.07x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 58.4 ms: 1.07x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.86 ms: 1.07x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (5): bench_mp_pool, pycparser, json_loads, sympy_str, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240901-3.14.0a0-91b7f2e-JIT/bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.091x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x