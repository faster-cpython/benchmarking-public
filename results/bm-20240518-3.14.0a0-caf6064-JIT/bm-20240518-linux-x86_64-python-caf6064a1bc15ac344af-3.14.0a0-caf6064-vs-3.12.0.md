# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.01x faster
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                  |
| chameleon      | 7.41 ms                                                | 7.06 ms: 1.05x faster                                                 |
| docutils       | 2.77 sec                                               | 2.94 sec: 1.06x slower                                                |
| tornado_http   | 103 ms                                                 | 96.6 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 363 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 455 ms: 1.26x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 945 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 596 ms: 1.22x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 479 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 986 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 625 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.4 ms: 1.21x faster                                                 |
| float          | 84.7 ms                                                | 71.9 ms: 1.18x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                 |
| regex_dna      | 212 ms                                                 | 209 ms: 1.02x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 82.4 ms: 1.08x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                  |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                                 |
| pickle_dict          | 35.5 us                                                | 34.2 us: 1.04x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                  |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.38 us: 1.02x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.57 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (2): pickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.62 ms: 1.24x faster                                                 |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                 |
| async_tree_none            | 472 ms                                                 | 363 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 455 ms: 1.26x faster                                                  |
| mako                       | 11.9 ms                                                | 9.62 ms: 1.24x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 945 ms: 1.22x faster                                                  |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 596 ms: 1.22x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 479 ms: 1.21x faster                                                  |
| nbody                      | 97.0 ms                                                | 80.4 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 986 ms: 1.20x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 63.1 ms: 1.19x faster                                                 |
| float                      | 84.7 ms                                                | 71.9 ms: 1.18x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                 |
| fannkuch                   | 417 ms                                                 | 359 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 625 ms: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.45 ms: 1.14x faster                                                 |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.14x faster                                                 |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                 |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                                  |
| richards                   | 45.8 ms                                                | 42.1 ms: 1.09x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 82.4 ms: 1.08x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 37.7 us: 1.08x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                                  |
| richards_super             | 51.5 ms                                                | 48.0 ms: 1.07x faster                                                 |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                 |
| tornado_http               | 103 ms                                                 | 96.6 ms: 1.06x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                  |
| chameleon                  | 7.41 ms                                                | 7.06 ms: 1.05x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                 |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                 |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                 |
| pickle_dict                | 35.5 us                                                | 34.2 us: 1.04x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.02x faster                                                  |
| deepcopy                   | 371 us                                                 | 366 us: 1.01x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.31 us: 1.01x faster                                                 |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                  |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.84 ms: 1.01x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 69.5 ms: 1.01x slower                                                 |
| dask                       | 372 ms                                                 | 378 ms: 1.02x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.38 us: 1.02x slower                                                 |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 860 us: 1.02x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                  |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                  |
| scimark_sor                | 129 ms                                                 | 133 ms: 1.03x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.68 ms: 1.04x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                                 |
| nqueens                    | 83.3 ms                                                | 87.3 ms: 1.05x slower                                                 |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                  |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                 |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.94 sec: 1.06x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 522 ms: 1.06x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.10x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.57 us: 1.10x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.24x slower                                                 |
| coverage                   | 72.7 ms                                                | 95.9 ms: 1.32x slower                                                 |
| telco                      | 7.10 ms                                                | 172 ms: 24.20x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (7): pickle, async_generators, deltablue, bench_mp_pool, sympy_str, coroutines, json_dumps
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.60% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x