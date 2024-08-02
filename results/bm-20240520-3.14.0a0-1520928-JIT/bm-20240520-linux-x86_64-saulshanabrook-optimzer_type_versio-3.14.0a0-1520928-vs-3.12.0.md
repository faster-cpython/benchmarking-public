# Results vs. 3.12.0

- fork: saulshanabrook
- ref: optimzer_type_versio
- machine: linux-x86_64
- commit hash: 1520928
- commit date: 2024-05-20
- overall geometric mean: 1.04x faster
- HPT reliability: 96.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                          |
| chameleon      | 7.41 ms                                                | 7.04 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                        |
| tornado_http   | 103 ms                                                 | 97.0 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 337 ms: 1.33x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.29x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 951 ms: 1.24x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 467 ms: 1.24x faster                                                          |
| async_tree_none            | 472 ms                                                 | 382 ms: 1.24x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 588 ms: 1.23x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.3 ms: 1.19x faster                                                         |
| float          | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                         |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                         |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                          |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 83.0 ms: 1.07x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 153 ms: 1.04x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                                          |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                         |
| unpickle_list        | 5.29 us                                                | 5.33 us: 1.01x slower                                                         |
| pickle_dict          | 35.5 us                                                | 36.1 us: 1.02x slower                                                         |
| pickle               | 11.6 us                                                | 12.1 us: 1.05x slower                                                         |
| unpickle             | 15.9 us                                                | 16.7 us: 1.05x slower                                                         |
| pickle_list          | 5.08 us                                                | 5.38 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.63 ms: 1.10x slower                                                         |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.99 ms: 1.19x faster                                                         |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 337 ms: 1.33x faster                                                          |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.29x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 951 ms: 1.24x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 467 ms: 1.24x faster                                                          |
| async_tree_none            | 472 ms                                                 | 382 ms: 1.24x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 588 ms: 1.23x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                                          |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 62.7 ms: 1.20x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 68.5 ms: 1.19x faster                                                         |
| nbody                      | 97.0 ms                                                | 81.3 ms: 1.19x faster                                                         |
| mako                       | 11.9 ms                                                | 9.99 ms: 1.19x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                          |
| float                      | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                         |
| fannkuch                   | 417 ms                                                 | 361 ms: 1.16x faster                                                          |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                          |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                         |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                          |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.54 ms: 1.11x faster                                                         |
| richards                   | 45.8 ms                                                | 41.3 ms: 1.11x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 701 ms: 1.11x faster                                                          |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                          |
| richards_super             | 51.5 ms                                                | 47.5 ms: 1.09x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 37.7 us: 1.08x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 83.0 ms: 1.07x faster                                                         |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                                          |
| tornado_http               | 103 ms                                                 | 97.0 ms: 1.06x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                          |
| chameleon                  | 7.41 ms                                                | 7.04 ms: 1.05x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 153 ms: 1.04x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                                          |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                         |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                          |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.28 us: 1.02x faster                                                         |
| deepcopy                   | 371 us                                                 | 364 us: 1.02x faster                                                          |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                                          |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                          |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                         |
| unpickle_list              | 5.29 us                                                | 5.33 us: 1.01x slower                                                         |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                          |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                         |
| dulwich_log                | 68.5 ms                                                | 69.5 ms: 1.01x slower                                                         |
| pickle_dict                | 35.5 us                                                | 36.1 us: 1.02x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                         |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                          |
| dask                       | 372 ms                                                 | 380 ms: 1.02x slower                                                          |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 865 us: 1.03x slower                                                          |
| asyncio_websockets         | 551 ms                                                 | 568 ms: 1.03x slower                                                          |
| nqueens                    | 83.3 ms                                                | 85.9 ms: 1.03x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 3.92 ms: 1.03x slower                                                         |
| logging_silent             | 104 ns                                                 | 108 ns: 1.04x slower                                                          |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 57.0 ms: 1.04x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                          |
| scimark_lu                 | 118 ms                                                 | 123 ms: 1.04x slower                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                        |
| pickle                     | 11.6 us                                                | 12.1 us: 1.05x slower                                                         |
| unpickle                   | 15.9 us                                                | 16.7 us: 1.05x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.05x slower                                                         |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                         |
| scimark_sor                | 129 ms                                                 | 137 ms: 1.06x slower                                                          |
| pickle_list                | 5.08 us                                                | 5.38 us: 1.06x slower                                                         |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                          |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                          |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.07x slower                                                        |
| sympy_expand               | 478 ms                                                 | 512 ms: 1.07x slower                                                          |
| asyncio_tcp                | 491 ms                                                 | 526 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.63 ms: 1.10x slower                                                         |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                         |
| telco                      | 7.10 ms                                                | 8.23 ms: 1.16x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.23x slower                                                         |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.29x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (4): json, json_dumps, bench_mp_pool, deltablue
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, hexiom, mdp, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240520-3.14.0a0-1520928-JIT/bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x