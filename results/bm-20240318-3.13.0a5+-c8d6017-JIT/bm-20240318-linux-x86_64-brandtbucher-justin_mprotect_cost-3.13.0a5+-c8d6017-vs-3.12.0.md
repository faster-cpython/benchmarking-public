# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: linux-x86_64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.00x slower
- HPT reliability: 90.15%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                         |
| chameleon      | 7.41 ms                                                | 6.84 ms: 1.08x faster                                                        |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                       |
| tornado_http   | 103 ms                                                 | 99.0 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 447 ms: 1.06x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 458 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 740 ms: 1.02x slower                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 589 ms: 1.03x slower                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                       |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.5 ms: 1.05x faster                                                        |
| nbody          | 97.0 ms                                                | 94.2 ms: 1.03x faster                                                        |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.85 ms: 1.07x slower                                                        |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                                         |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                       |
| unpickle             | 15.9 us                                                | 14.6 us: 1.08x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                         |
| unpickle_list        | 5.29 us                                                | 5.02 us: 1.05x faster                                                        |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                                        |
| pickle_list          | 5.08 us                                                | 4.92 us: 1.03x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                        |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 87.6 ms: 1.02x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.01x slower                                                        |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                         |
| unpickle_pure_python | 230 us                                                 | 239 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.23x slower                                                        |
| python_startup_no_site | 6.94 ms                                                | 10.3 ms: 1.49x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                        |
| django_template | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 111 us: 1.43x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                        |
| scimark_fft                | 382 ms                                                 | 340 ms: 1.12x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                       |
| logging_format             | 7.23 us                                                | 6.48 us: 1.12x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.88 us: 1.10x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 3.05 us: 1.10x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 75.4 ms: 1.09x faster                                                        |
| chameleon                  | 7.41 ms                                                | 6.84 ms: 1.08x faster                                                        |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.08x faster                                                        |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                         |
| deepcopy                   | 371 us                                                 | 349 us: 1.06x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 71.0 ms: 1.06x faster                                                        |
| raytrace                   | 312 ms                                                 | 295 ms: 1.06x faster                                                         |
| async_tree_none            | 472 ms                                                 | 447 ms: 1.06x faster                                                         |
| unpickle_list              | 5.29 us                                                | 5.02 us: 1.05x faster                                                        |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                         |
| float                      | 84.7 ms                                                | 80.5 ms: 1.05x faster                                                        |
| sympy_str                  | 300 ms                                                 | 285 ms: 1.05x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 161 ms: 1.05x faster                                                         |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 38.9 us: 1.05x faster                                                        |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                                        |
| chaos                      | 67.0 ms                                                | 64.4 ms: 1.04x faster                                                        |
| tornado_http               | 103 ms                                                 | 99.0 ms: 1.04x faster                                                        |
| pathlib                    | 19.3 ms                                                | 18.7 ms: 1.04x faster                                                        |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                         |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                        |
| pickle_list                | 5.08 us                                                | 4.92 us: 1.03x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                        |
| nbody                      | 97.0 ms                                                | 94.2 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                                        |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                         |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                        |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 87.6 ms: 1.02x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.02x faster                                                        |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                         |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 21.2 ms: 1.01x faster                                                        |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.01x slower                                                        |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                                         |
| django_template            | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                        |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                         |
| sympy_expand               | 478 ms                                                 | 486 ms: 1.02x slower                                                         |
| richards                   | 45.8 ms                                                | 46.7 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 450 ms                                                 | 458 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 740 ms: 1.02x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 859 us: 1.02x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                                         |
| pyflate                    | 482 ms                                                 | 495 ms: 1.03x slower                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 589 ms: 1.03x slower                                                         |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 56.3 ms: 1.03x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                         |
| dulwich_log                | 68.5 ms                                                | 70.5 ms: 1.03x slower                                                        |
| richards_super             | 51.5 ms                                                | 53.0 ms: 1.03x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 3.92 ms: 1.03x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                       |
| unpickle_pure_python       | 230 us                                                 | 239 us: 1.04x slower                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                       |
| gunicorn                   | 1.24 ms                                                | 1.30 ms: 1.05x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.55 ms: 1.05x slower                                                        |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.05x slower                                                        |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.05x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.85 ms: 1.07x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.26 sec: 1.07x slower                                                       |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.84 sec: 1.08x slower                                                       |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 129 ms: 1.09x slower                                                         |
| hexiom                     | 6.41 ms                                                | 7.05 ms: 1.10x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.12x slower                                                        |
| go                         | 139 ms                                                 | 158 ms: 1.13x slower                                                         |
| telco                      | 7.10 ms                                                | 8.33 ms: 1.17x slower                                                        |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.23x slower                                                        |
| coverage                   | 72.7 ms                                                | 96.9 ms: 1.33x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 10.3 ms: 1.49x slower                                                        |
| unpack_sequence            | 54.0 ns                                                | 89.2 ns: 1.65x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (10): pprint_safe_repr, async_tree_cpu_io_mixed, pickle, bench_mp_pool, async_tree_memoization, async_generators, dask, sqlite_synth, pprint_pformat, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 90.15% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.17x