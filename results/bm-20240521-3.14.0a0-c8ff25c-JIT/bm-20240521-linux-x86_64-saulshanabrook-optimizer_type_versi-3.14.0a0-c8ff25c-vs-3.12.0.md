# Results vs. 3.12.0

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: c8ff25c
- commit date: 2024-05-21
- overall geometric mean: 1.04x faster
- HPT reliability: 98.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                                          |
| chameleon      | 7.41 ms                                                | 7.04 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                        |
| tornado_http   | 103 ms                                                 | 97.0 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 330 ms: 1.36x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 441 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 934 ms: 1.27x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 456 ms: 1.27x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 578 ms: 1.26x faster                                                          |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 937 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 609 ms: 1.19x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.6 ms: 1.19x faster                                                         |
| float          | 84.7 ms                                                | 72.6 ms: 1.17x faster                                                         |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                         |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                         |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 82.4 ms: 1.08x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                          |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 152 ms: 1.05x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.03x faster                                                          |
| unpickle             | 15.9 us                                                | 15.4 us: 1.03x faster                                                         |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                         |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                         |
| unpickle_list        | 5.29 us                                                | 5.37 us: 1.02x slower                                                         |
| pickle_dict          | 35.5 us                                                | 36.3 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (2): json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                         |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.17x faster                                                         |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 330 ms: 1.36x faster                                                          |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 441 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 934 ms: 1.27x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 456 ms: 1.27x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 578 ms: 1.26x faster                                                          |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 937 ms: 1.23x faster                                                          |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 62.1 ms: 1.21x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 67.8 ms: 1.21x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 609 ms: 1.19x faster                                                          |
| nbody                      | 97.0 ms                                                | 81.6 ms: 1.19x faster                                                         |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.17x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                         |
| fannkuch                   | 417 ms                                                 | 356 ms: 1.17x faster                                                          |
| float                      | 84.7 ms                                                | 72.6 ms: 1.17x faster                                                         |
| spectral_norm              | 115 ms                                                 | 100.0 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.45 ms: 1.14x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.70 us: 1.13x faster                                                         |
| logging_format             | 7.23 us                                                | 6.40 us: 1.13x faster                                                         |
| raytrace                   | 312 ms                                                 | 280 ms: 1.12x faster                                                          |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 702 ms: 1.10x faster                                                          |
| richards                   | 45.8 ms                                                | 41.8 ms: 1.10x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 82.4 ms: 1.08x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 37.7 us: 1.08x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                          |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                                          |
| richards_super             | 51.5 ms                                                | 48.0 ms: 1.07x faster                                                         |
| pyflate                    | 482 ms                                                 | 453 ms: 1.07x faster                                                          |
| tornado_http               | 103 ms                                                 | 97.0 ms: 1.06x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                          |
| chameleon                  | 7.41 ms                                                | 7.04 ms: 1.05x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 152 ms: 1.05x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.03x faster                                                          |
| unpickle                   | 15.9 us                                                | 15.4 us: 1.03x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.29 us: 1.02x faster                                                         |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.74 ms: 1.01x faster                                                         |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                         |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                         |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                         |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                          |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                          |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                          |
| dulwich_log                | 68.5 ms                                                | 69.3 ms: 1.01x slower                                                         |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                                          |
| unpickle_list              | 5.29 us                                                | 5.37 us: 1.02x slower                                                         |
| pickle_dict                | 35.5 us                                                | 36.3 us: 1.02x slower                                                         |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                          |
| nqueens                    | 83.3 ms                                                | 85.5 ms: 1.03x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                          |
| bench_thread_pool          | 842 us                                                 | 866 us: 1.03x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                          |
| sqlglot_optimize           | 54.8 ms                                                | 56.6 ms: 1.03x slower                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 123 ms: 1.04x slower                                                          |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                         |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                         |
| asyncio_tcp                | 491 ms                                                 | 520 ms: 1.06x slower                                                          |
| sympy_expand               | 478 ms                                                 | 509 ms: 1.06x slower                                                          |
| scimark_sor                | 129 ms                                                 | 138 ms: 1.07x slower                                                          |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                          |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                         |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                         |
| telco                      | 7.10 ms                                                | 8.22 ms: 1.16x slower                                                         |
| generators                 | 31.2 ms                                                | 36.3 ms: 1.16x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                         |
| coverage                   | 72.7 ms                                                | 93.0 ms: 1.28x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (8): json_dumps, sqlite_synth, bench_mp_pool, async_generators, pickle_list, deltablue, dask, deepcopy
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, hexiom, mdp, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240521-3.14.0a0-c8ff25c-JIT/bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.42% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x