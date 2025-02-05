# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 99262b6
- commit date: 2024-09-19
- overall geometric mean: 1.061x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 318 ms: 1.16x slower                                                         |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.02x faster                                                       |
| tornado_http   | 103 ms                                                 | 110 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                         |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 892 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.3 ms: 1.19x faster                                                        |
| nbody          | 97.0 ms                                                | 85.5 ms: 1.13x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.62 ms: 1.00x slower                                                        |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                         |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                       |
| unpickle             | 15.9 us                                                | 14.5 us: 1.09x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                        |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.04x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                        |
| unpickle_list        | 5.29 us                                                | 5.26 us: 1.01x faster                                                        |
| pickle_dict          | 35.5 us                                                | 35.4 us: 1.00x faster                                                        |
| pickle               | 11.6 us                                                | 11.8 us: 1.01x slower                                                        |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                        |
| pickle_pure_python   | 324 us                                                 | 331 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| django_template | 34.6 ms                                                | 38.4 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.5 us: 1.48x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 390 ms: 1.47x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                         |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                         |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 892 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 67.5 ms: 1.21x faster                                                        |
| float                      | 84.7 ms                                                | 71.3 ms: 1.19x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                        |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                        |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                         |
| go                         | 139 ms                                                 | 122 ms: 1.14x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 65.9 ms: 1.14x faster                                                        |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                         |
| nbody                      | 97.0 ms                                                | 85.5 ms: 1.13x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.47 ms: 1.13x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.13x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                       |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                         |
| unpickle                   | 15.9 us                                                | 14.5 us: 1.09x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                         |
| chaos                      | 67.0 ms                                                | 62.5 ms: 1.07x faster                                                        |
| fannkuch                   | 417 ms                                                 | 389 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                                        |
| json                       | 5.26 ms                                                | 4.94 ms: 1.07x faster                                                        |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 732 ms: 1.06x faster                                                         |
| sympy_str                  | 300 ms                                                 | 284 ms: 1.06x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                       |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                         |
| scimark_fft                | 382 ms                                                 | 366 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.04x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.58 ms: 1.04x faster                                                        |
| pyflate                    | 482 ms                                                 | 466 ms: 1.04x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.02x faster                                                       |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                         |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                         |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                         |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| unpickle_list              | 5.29 us                                                | 5.26 us: 1.01x faster                                                        |
| pickle_dict                | 35.5 us                                                | 35.4 us: 1.00x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.62 ms: 1.00x slower                                                        |
| meteor_contest             | 112 ms                                                 | 113 ms: 1.00x slower                                                         |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.00x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                         |
| dulwich_log                | 68.5 ms                                                | 69.2 ms: 1.01x slower                                                        |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                         |
| pickle                     | 11.6 us                                                | 11.8 us: 1.01x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                        |
| pickle_list                | 5.08 us                                                | 5.17 us: 1.02x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                       |
| pickle_pure_python         | 324 us                                                 | 331 us: 1.02x slower                                                         |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                         |
| richards_super             | 51.5 ms                                                | 53.2 ms: 1.03x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 3.96 ms: 1.04x slower                                                        |
| nqueens                    | 83.3 ms                                                | 87.5 ms: 1.05x slower                                                        |
| richards                   | 45.8 ms                                                | 48.2 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                         |
| hexiom                     | 6.41 ms                                                | 6.81 ms: 1.06x slower                                                        |
| tornado_http               | 103 ms                                                 | 110 ms: 1.07x slower                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.83 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 60.1 ms: 1.10x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 928 us: 1.10x slower                                                         |
| django_template            | 34.6 ms                                                | 38.4 ms: 1.11x slower                                                        |
| telco                      | 7.10 ms                                                | 8.08 ms: 1.14x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                        |
| 2to3                       | 274 ms                                                 | 318 ms: 1.16x slower                                                         |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                        |
| generators                 | 31.2 ms                                                | 36.8 ms: 1.18x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 28.0 ms: 1.31x slower                                                        |
| unpack_sequence            | 54.0 ns                                                | 110 ns: 2.04x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240919-3.14.0a0-99262b6-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.061x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x