# Results vs. 3.12.0

- fork: python
- ref: ec9d12be9648ee60a2eb
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.00x faster
- HPT reliability: 95.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                  |
| chameleon      | 7.41 ms                                                | 7.00 ms: 1.06x faster                                                 |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                |
| tornado_http   | 103 ms                                                 | 97.6 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 365 ms: 1.29x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 349 ms: 1.29x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 459 ms: 1.25x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 943 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 597 ms: 1.22x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 986 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 627 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.9 ms: 1.20x faster                                                 |
| float          | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                 |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 83.1 ms: 1.07x faster                                                 |
| pickle_dict          | 35.5 us                                                | 33.5 us: 1.06x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 152 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                  |
| unpickle             | 15.9 us                                                | 15.6 us: 1.02x faster                                                 |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| json_loads           | 28.5 us                                                | 29.1 us: 1.02x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.44 us: 1.03x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.47 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.63 ms: 1.10x slower                                                 |
| python_startup         | 9.55 ms                                                | 11.0 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.56 ms: 1.24x faster                                                 |
| django_template | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                 |
| async_tree_none            | 472 ms                                                 | 365 ms: 1.29x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 349 ms: 1.29x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 459 ms: 1.25x faster                                                  |
| mako                       | 11.9 ms                                                | 9.56 ms: 1.24x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 943 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 597 ms: 1.22x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 67.9 ms: 1.21x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 480 ms: 1.20x faster                                                  |
| nbody                      | 97.0 ms                                                | 80.9 ms: 1.20x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 986 ms: 1.20x faster                                                  |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 63.4 ms: 1.19x faster                                                 |
| float                      | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 627 ms: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.49 ms: 1.13x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.73 us: 1.13x faster                                                 |
| fannkuch                   | 417 ms                                                 | 371 ms: 1.12x faster                                                  |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                  |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                  |
| richards                   | 45.8 ms                                                | 41.8 ms: 1.10x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 708 ms: 1.10x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.7 ms: 1.09x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.6 ms: 1.08x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 37.9 us: 1.07x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 83.1 ms: 1.07x faster                                                 |
| regex_compile              | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| pickle_dict                | 35.5 us                                                | 33.5 us: 1.06x faster                                                 |
| chameleon                  | 7.41 ms                                                | 7.00 ms: 1.06x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                  |
| tornado_http               | 103 ms                                                 | 97.6 ms: 1.05x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 152 ms: 1.05x faster                                                  |
| pyflate                    | 482 ms                                                 | 459 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                  |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                 |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.6 us: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| sympy_str                  | 300 ms                                                 | 301 ms: 1.01x slower                                                  |
| async_generators           | 463 ms                                                 | 466 ms: 1.01x slower                                                  |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                                  |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 69.6 ms: 1.02x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                  |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                                  |
| deepcopy                   | 371 us                                                 | 378 us: 1.02x slower                                                  |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                  |
| json_loads                 | 28.5 us                                                | 29.1 us: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 3.87 ms: 1.02x slower                                                 |
| json                       | 5.26 ms                                                | 5.39 ms: 1.02x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.44 us: 1.03x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 56.5 ms: 1.03x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                  |
| nqueens                    | 83.3 ms                                                | 87.0 ms: 1.04x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                 |
| django_template            | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                 |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.05x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 522 ms: 1.06x slower                                                  |
| sympy_expand               | 478 ms                                                 | 510 ms: 1.07x slower                                                  |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                |
| pickle_list                | 5.08 us                                                | 5.47 us: 1.08x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.63 ms: 1.10x slower                                                 |
| python_startup             | 9.55 ms                                                | 11.0 ms: 1.15x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.83 ms: 1.24x slower                                                 |
| coverage                   | 72.7 ms                                                | 95.1 ms: 1.31x slower                                                 |
| telco                      | 7.10 ms                                                | 173 ms: 24.34x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (4): bench_mp_pool, json_dumps, deltablue, deepcopy_reduce
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x