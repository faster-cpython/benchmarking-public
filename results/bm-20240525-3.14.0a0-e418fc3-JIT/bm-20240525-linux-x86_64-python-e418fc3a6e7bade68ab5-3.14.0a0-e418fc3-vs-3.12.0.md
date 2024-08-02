# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.04x faster
- HPT reliability: 98.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                  |
| chameleon      | 7.41 ms                                                | 7.04 ms: 1.05x faster                                                 |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.06x slower                                                |
| tornado_http   | 103 ms                                                 | 97.0 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 334 ms: 1.35x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 942 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 466 ms: 1.24x faster                                                  |
| async_tree_none            | 472 ms                                                 | 385 ms: 1.23x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 957 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                 |
| float          | 84.7 ms                                                | 72.2 ms: 1.17x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                 |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 81.8 ms: 1.09x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 224 us: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pickle_dict          | 35.5 us                                                | 35.9 us: 1.01x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.34 us: 1.01x slower                                                 |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                 |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                 |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                 |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 334 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 942 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 466 ms: 1.24x faster                                                  |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                  |
| async_tree_none            | 472 ms                                                 | 385 ms: 1.23x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 67.4 ms: 1.21x faster                                                 |
| mako                       | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 62.1 ms: 1.21x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 957 ms: 1.21x faster                                                  |
| nbody                      | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.21 ms: 1.20x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                  |
| float                      | 84.7 ms                                                | 72.2 ms: 1.17x faster                                                 |
| fannkuch                   | 417 ms                                                 | 356 ms: 1.17x faster                                                  |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                                 |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                 |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                 |
| richards                   | 45.8 ms                                                | 41.7 ms: 1.10x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 81.8 ms: 1.09x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                  |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| richards_super             | 51.5 ms                                                | 48.0 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                  |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                  |
| tornado_http               | 103 ms                                                 | 97.0 ms: 1.06x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 38.6 us: 1.05x faster                                                 |
| chameleon                  | 7.41 ms                                                | 7.04 ms: 1.05x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                 |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 224 us: 1.02x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                |
| deepcopy                   | 371 us                                                 | 365 us: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                 |
| pickle_dict                | 35.5 us                                                | 35.9 us: 1.01x slower                                                 |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.34 us: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 69.3 ms: 1.01x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                 |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.56 ms: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 56.4 ms: 1.03x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 867 us: 1.03x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                 |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 122 ms: 1.04x slower                                                  |
| nqueens                    | 83.3 ms                                                | 86.6 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 520 ms: 1.06x slower                                                  |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.06x slower                                                |
| sympy_expand               | 478 ms                                                 | 509 ms: 1.06x slower                                                  |
| scimark_sor                | 129 ms                                                 | 138 ms: 1.07x slower                                                  |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.10x slower                                                  |
| telco                      | 7.10 ms                                                | 8.12 ms: 1.14x slower                                                 |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.84 ms: 1.24x slower                                                 |
| coverage                   | 72.7 ms                                                | 94.0 ms: 1.29x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (7): unpickle, pickle_list, async_generators, deepcopy_reduce, deltablue, bench_mp_pool, dask
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.07% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x