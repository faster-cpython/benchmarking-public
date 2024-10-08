# Results vs. 3.12.0

- fork: python
- ref: d9efa45d7457b0dfea46
- machine: linux-x86_64
- commit hash: d9efa45
- commit date: 2024-07-25
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                  |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                |
| tornado_http   | 103 ms                                                 | 89.9 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 863 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.5 ms: 1.10x faster                                                 |
| float          | 84.7 ms                                                | 78.0 ms: 1.09x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                  |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                 |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.3 ms: 1.05x faster                                                 |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| django_template | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 527 ms: 1.38x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 863 ms: 1.37x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                 |
| raytrace                   | 312 ms                                                 | 257 ms: 1.21x faster                                                  |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.18x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                 |
| tornado_http               | 103 ms                                                 | 89.9 ms: 1.14x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 72.1 ms: 1.14x faster                                                 |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                                  |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                  |
| nbody                      | 97.0 ms                                                | 88.5 ms: 1.10x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                 |
| float                      | 84.7 ms                                                | 78.0 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.08x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 784 us: 1.07x faster                                                  |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                 |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| dask                       | 372 ms                                                 | 354 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                                  |
| logging_silent             | 104 ns                                                 | 99.6 ns: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.05x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 85.3 ms: 1.05x faster                                                 |
| nqueens                    | 83.3 ms                                                | 79.7 ms: 1.05x faster                                                 |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                  |
| scimark_fft                | 382 ms                                                 | 366 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| sympy_expand               | 478 ms                                                 | 462 ms: 1.03x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                                 |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.03x faster                                                  |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.94 ms: 1.02x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 482 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                |
| richards                   | 45.8 ms                                                | 45.1 ms: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.01x faster                                                  |
| django_template            | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                 |
| richards_super             | 51.5 ms                                                | 51.2 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.01x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                 |
| coverage                   | 72.7 ms                                                | 92.6 ms: 1.27x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (4): bench_mp_pool, pyflate, go, json_dumps
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240725-3.14.0a0-d9efa45/bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x