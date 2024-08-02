# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 144a6fa
- commit date: 2024-05-11
- overall geometric mean: 1.06x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                                    |
| chameleon      | 7.41 ms                                                | 7.80 ms: 1.05x slower                                                   |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.04x slower                                                  |
| tornado_http   | 103 ms                                                 | 97.8 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 362 ms: 1.24x faster                                                    |
| async_tree_none            | 472 ms                                                 | 382 ms: 1.24x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 476 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 602 ms: 1.21x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 960 ms: 1.20x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 1.01 sec: 1.17x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 499 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 636 ms: 1.14x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                    |
| float          | 84.7 ms                                                | 86.7 ms: 1.02x slower                                                   |
| nbody          | 97.0 ms                                                | 105 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                    |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                    |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_dict          | 35.5 us                                                | 33.9 us: 1.05x faster                                                   |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                                   |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                   |
| xml_etree_parse      | 159 ms                                                 | 163 ms: 1.02x slower                                                    |
| json_loads           | 28.5 us                                                | 29.1 us: 1.02x slower                                                   |
| pickle_pure_python   | 324 us                                                 | 335 us: 1.03x slower                                                    |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 112 ms: 1.04x slower                                                    |
| xml_etree_generate   | 89.2 ms                                                | 93.4 ms: 1.05x slower                                                   |
| unpickle_list        | 5.29 us                                                | 5.55 us: 1.05x slower                                                   |
| xml_etree_process    | 61.7 ms                                                | 65.1 ms: 1.06x slower                                                   |
| unpickle_pure_python | 230 us                                                 | 243 us: 1.06x slower                                                    |
| pickle_list          | 5.08 us                                                | 5.41 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 12.7 ms: 1.07x slower                                                   |
| django_template | 34.6 ms                                                | 38.2 ms: 1.10x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 362 ms: 1.24x faster                                                    |
| async_tree_none            | 472 ms                                                 | 382 ms: 1.24x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 476 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 602 ms: 1.21x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 960 ms: 1.20x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 1.01 sec: 1.17x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 499 ms: 1.16x faster                                                    |
| comprehensions             | 21.8 us                                                | 19.0 us: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 636 ms: 1.14x faster                                                    |
| pathlib                    | 19.3 ms                                                | 17.9 ms: 1.08x faster                                                   |
| raytrace                   | 312 ms                                                 | 289 ms: 1.08x faster                                                    |
| logging_format             | 7.23 us                                                | 6.72 us: 1.08x faster                                                   |
| logging_simple             | 6.46 us                                                | 6.06 us: 1.07x faster                                                   |
| tornado_http               | 103 ms                                                 | 97.8 ms: 1.05x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 78.1 ms: 1.05x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 161 ms: 1.05x faster                                                    |
| pickle_dict                | 35.5 us                                                | 33.9 us: 1.05x faster                                                   |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.60 ms: 1.03x faster                                                   |
| sympy_str                  | 300 ms                                                 | 291 ms: 1.03x faster                                                    |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                    |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 21.2 ms: 1.01x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 68.3 ms: 1.00x faster                                                   |
| generators                 | 31.2 ms                                                | 31.3 ms: 1.00x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.00x slower                                                   |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                  |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 76.7 ms: 1.02x slower                                                   |
| xml_etree_parse            | 159 ms                                                 | 163 ms: 1.02x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.1 us: 1.02x slower                                                   |
| dask                       | 372 ms                                                 | 380 ms: 1.02x slower                                                    |
| float                      | 84.7 ms                                                | 86.7 ms: 1.02x slower                                                   |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                    |
| sympy_expand               | 478 ms                                                 | 491 ms: 1.03x slower                                                    |
| meteor_contest             | 112 ms                                                 | 115 ms: 1.03x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 865 us: 1.03x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                    |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                   |
| pickle_pure_python         | 324 us                                                 | 335 us: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.04x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 112 ms: 1.04x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.76 ms: 1.05x slower                                                   |
| xml_etree_generate         | 89.2 ms                                                | 93.4 ms: 1.05x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.97 us: 1.05x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                                    |
| unpickle_list              | 5.29 us                                                | 5.55 us: 1.05x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 516 ms: 1.05x slower                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                   |
| chameleon                  | 7.41 ms                                                | 7.80 ms: 1.05x slower                                                   |
| xml_etree_process          | 61.7 ms                                                | 65.1 ms: 1.06x slower                                                   |
| spectral_norm              | 115 ms                                                 | 121 ms: 1.06x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                   |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                    |
| unpickle_pure_python       | 230 us                                                 | 243 us: 1.06x slower                                                    |
| json                       | 5.26 ms                                                | 5.57 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 58.1 ms: 1.06x slower                                                   |
| pyflate                    | 482 ms                                                 | 512 ms: 1.06x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.82 ms: 1.06x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.41 us: 1.06x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.26 sec: 1.07x slower                                                  |
| mako                       | 11.9 ms                                                | 12.7 ms: 1.07x slower                                                   |
| nqueens                    | 83.3 ms                                                | 89.1 ms: 1.07x slower                                                   |
| logging_silent             | 104 ns                                                 | 112 ns: 1.08x slower                                                    |
| fannkuch                   | 417 ms                                                 | 449 ms: 1.08x slower                                                    |
| deepcopy_reduce            | 3.35 us                                                | 3.60 us: 1.08x slower                                                   |
| deepcopy                   | 371 us                                                 | 401 us: 1.08x slower                                                    |
| scimark_fft                | 382 ms                                                 | 414 ms: 1.08x slower                                                    |
| nbody                      | 97.0 ms                                                | 105 ms: 1.08x slower                                                    |
| scimark_sor                | 129 ms                                                 | 141 ms: 1.09x slower                                                    |
| pprint_safe_repr           | 776 ms                                                 | 853 ms: 1.10x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                   |
| django_template            | 34.6 ms                                                | 38.2 ms: 1.10x slower                                                   |
| deepcopy_memo              | 40.7 us                                                | 45.1 us: 1.11x slower                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.74 sec: 1.11x slower                                                  |
| richards                   | 45.8 ms                                                | 51.2 ms: 1.12x slower                                                   |
| go                         | 139 ms                                                 | 158 ms: 1.13x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 178 us: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.72 ms: 1.13x slower                                                   |
| richards_super             | 51.5 ms                                                | 58.5 ms: 1.13x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                   |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.28x slower                                                   |
| telco                      | 7.10 ms                                                | 185 ms: 26.02x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                            |

Benchmark hidden because not significant (4): chaos, regex_effbot, bench_mp_pool, tomli_loads
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240511-3.14.0a0-144a6fa/bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.97x