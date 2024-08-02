# Results vs. 3.12.0

- fork: nohlson
- ref: enable_no_impact_def
- machine: linux-x86_64
- commit hash: 98d9ea0
- commit date: 2024-06-20
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.03x faster                                                   |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                 |
| tornado_http   | 103 ms                                                 | 91.6 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 327 ms: 1.38x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                   |
| async_tree_none            | 472 ms                                                 | 366 ms: 1.29x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 452 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 572 ms: 1.27x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 974 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 612 ms: 1.19x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.6 ms: 1.11x faster                                                  |
| nbody          | 97.0 ms                                                | 91.9 ms: 1.06x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.13x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                  |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.14 sec: 1.09x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                  |
| pickle               | 11.6 us                                                | 11.3 us: 1.03x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.37 us: 1.02x slower                                                  |
| pickle_dict          | 35.5 us                                                | 36.6 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (3): unpickle, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                  |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                  |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 327 ms: 1.38x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                  |
| async_tree_none            | 472 ms                                                 | 366 ms: 1.29x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 452 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 572 ms: 1.27x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                  |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 974 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 612 ms: 1.19x faster                                                   |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                  |
| regex_compile              | 148 ms                                                 | 132 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                  |
| tornado_http               | 103 ms                                                 | 91.6 ms: 1.12x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.12x faster                                                   |
| float                      | 84.7 ms                                                | 76.6 ms: 1.11x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 74.5 ms: 1.10x faster                                                  |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                   |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.14 sec: 1.09x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 69.8 ms: 1.08x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 789 us: 1.07x faster                                                   |
| fannkuch                   | 417 ms                                                 | 392 ms: 1.06x faster                                                   |
| async_generators           | 463 ms                                                 | 436 ms: 1.06x faster                                                   |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                  |
| nqueens                    | 83.3 ms                                                | 78.5 ms: 1.06x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                   |
| nbody                      | 97.0 ms                                                | 91.9 ms: 1.06x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.60 ms: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                 |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| dask                       | 372 ms                                                 | 358 ms: 1.04x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                  |
| 2to3                       | 274 ms                                                 | 265 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| pickle                     | 11.6 us                                                | 11.3 us: 1.03x faster                                                  |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                   |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.02x faster                                                   |
| asyncio_tcp                | 491 ms                                                 | 482 ms: 1.02x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 54.0 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                  |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.02 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                   |
| pyflate                    | 482 ms                                                 | 484 ms: 1.00x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.11 us: 1.01x slower                                                  |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                   |
| unpickle_list              | 5.29 us                                                | 5.37 us: 1.02x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.03x slower                                                  |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                   |
| pickle_dict                | 35.5 us                                                | 36.6 us: 1.03x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                 |
| richards                   | 45.8 ms                                                | 48.0 ms: 1.05x slower                                                  |
| richards_super             | 51.5 ms                                                | 54.3 ms: 1.05x slower                                                  |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                  |
| telco                      | 7.10 ms                                                | 8.29 ms: 1.17x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                  |
| coverage                   | 72.7 ms                                                | 92.1 ms: 1.27x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (5): unpickle, json_dumps, json_loads, bench_mp_pool, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240620-3.14.0a0-98d9ea0/bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x