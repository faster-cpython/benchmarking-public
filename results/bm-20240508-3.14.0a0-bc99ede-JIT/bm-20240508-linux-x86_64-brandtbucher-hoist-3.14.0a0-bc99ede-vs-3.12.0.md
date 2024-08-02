# Results vs. 3.12.0

- fork: brandtbucher
- ref: hoist
- machine: linux-x86_64
- commit hash: bc99ede
- commit date: 2024-05-08
- overall geometric mean: 1.00x slower
- HPT reliability: 97.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                         |
| chameleon      | 7.41 ms                                                | 7.07 ms: 1.05x faster                                        |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                       |
| tornado_http   | 103 ms                                                 | 97.4 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 344 ms: 1.31x faster                                         |
| async_tree_none            | 472 ms                                                 | 364 ms: 1.30x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.27x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                         |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 478 ms: 1.21x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                       |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.8 ms: 1.20x faster                                        |
| nbody          | 97.0 ms                                                | 86.0 ms: 1.13x faster                                        |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.66 ms: 1.01x slower                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                         |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                       |
| xml_etree_generate   | 89.2 ms                                                | 82.5 ms: 1.08x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 57.9 ms: 1.07x faster                                        |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                         |
| pickle_dict          | 35.5 us                                                | 33.9 us: 1.05x faster                                        |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                         |
| xml_etree_parse      | 159 ms                                                 | 153 ms: 1.04x faster                                         |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                         |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                        |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                        |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                        |
| unpickle             | 15.9 us                                                | 16.2 us: 1.02x slower                                        |
| unpickle_list        | 5.29 us                                                | 5.40 us: 1.02x slower                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.67 ms: 1.11x slower                                        |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.16x slower                                        |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.52 ms: 1.25x faster                                        |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                        |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                        |
| async_tree_none_tg         | 450 ms                                                 | 344 ms: 1.31x faster                                         |
| async_tree_none            | 472 ms                                                 | 364 ms: 1.30x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.27x faster                                         |
| mako                       | 11.9 ms                                                | 9.52 ms: 1.25x faster                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                         |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 478 ms: 1.21x faster                                         |
| float                      | 84.7 ms                                                | 70.8 ms: 1.20x faster                                        |
| scimark_fft                | 382 ms                                                 | 321 ms: 1.19x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 69.1 ms: 1.18x faster                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                        |
| spectral_norm              | 115 ms                                                 | 99.0 ms: 1.16x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                       |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                        |
| fannkuch                   | 417 ms                                                 | 368 ms: 1.13x faster                                         |
| logging_format             | 7.23 us                                                | 6.41 us: 1.13x faster                                        |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                        |
| nbody                      | 97.0 ms                                                | 86.0 ms: 1.13x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.55 ms: 1.11x faster                                        |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                         |
| pathlib                    | 19.3 ms                                                | 17.8 ms: 1.09x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 82.5 ms: 1.08x faster                                        |
| deepcopy_memo              | 40.7 us                                                | 37.7 us: 1.08x faster                                        |
| pyflate                    | 482 ms                                                 | 449 ms: 1.08x faster                                         |
| richards                   | 45.8 ms                                                | 42.7 ms: 1.07x faster                                        |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 57.9 ms: 1.07x faster                                        |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                         |
| richards_super             | 51.5 ms                                                | 48.8 ms: 1.06x faster                                        |
| tornado_http               | 103 ms                                                 | 97.4 ms: 1.05x faster                                        |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                         |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                        |
| chameleon                  | 7.41 ms                                                | 7.07 ms: 1.05x faster                                        |
| pickle_dict                | 35.5 us                                                | 33.9 us: 1.05x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 153 ms: 1.04x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                        |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                        |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                        |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.31 us: 1.01x faster                                        |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                       |
| async_generators           | 463 ms                                                 | 465 ms: 1.00x slower                                         |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                         |
| pickle_list                | 5.08 us                                                | 5.14 us: 1.01x slower                                        |
| gc_traversal               | 3.79 ms                                                | 3.84 ms: 1.01x slower                                        |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                        |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                         |
| regex_effbot               | 3.61 ms                                                | 3.66 ms: 1.01x slower                                        |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.01x slower                                         |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                        |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                        |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                         |
| deepcopy                   | 371 us                                                 | 378 us: 1.02x slower                                         |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                        |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                         |
| unpickle                   | 15.9 us                                                | 16.2 us: 1.02x slower                                        |
| unpickle_list              | 5.29 us                                                | 5.40 us: 1.02x slower                                        |
| dulwich_log                | 68.5 ms                                                | 70.1 ms: 1.02x slower                                        |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                         |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                         |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                         |
| bench_thread_pool          | 842 us                                                 | 868 us: 1.03x slower                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                       |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                        |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                        |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                         |
| hexiom                     | 6.41 ms                                                | 6.73 ms: 1.05x slower                                        |
| asyncio_tcp                | 491 ms                                                 | 515 ms: 1.05x slower                                         |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                         |
| nqueens                    | 83.3 ms                                                | 87.8 ms: 1.05x slower                                        |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                         |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                        |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                        |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                       |
| sympy_expand               | 478 ms                                                 | 511 ms: 1.07x slower                                         |
| gunicorn                   | 1.24 ms                                                | 1.35 ms: 1.09x slower                                        |
| aiohttp                    | 1.15 ms                                                | 1.26 ms: 1.09x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.67 ms: 1.11x slower                                        |
| typing_runtime_protocols   | 158 us                                                 | 177 us: 1.12x slower                                         |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.16x slower                                        |
| coverage                   | 72.7 ms                                                | 88.7 ms: 1.22x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.81 ms: 1.23x slower                                        |
| telco                      | 7.10 ms                                                | 171 ms: 24.14x slower                                        |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (4): json_dumps, scimark_sor, bench_mp_pool, deltablue
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240508-3.14.0a0-bc99ede-JIT/bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x