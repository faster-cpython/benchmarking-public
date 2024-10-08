# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_exit_leaks
- machine: linux-x86_64
- commit hash: 984ca75
- commit date: 2024-10-01
- overall geometric mean: 1.06x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                       |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                     |
| tornado_http   | 103 ms                                                 | 95.7 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 880 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                      |
| float          | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                      |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 97.5 ms: 1.10x faster                                                      |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                       |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.05x faster                                                       |
| pickle_dict          | 35.5 us                                                | 34.7 us: 1.02x faster                                                      |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                      |
| pickle               | 11.6 us                                                | 11.7 us: 1.00x slower                                                      |
| unpickle_list        | 5.29 us                                                | 5.33 us: 1.01x slower                                                      |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                      |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.87 ms: 1.21x faster                                                      |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                                      |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                       |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 880 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 65.7 ms: 1.25x faster                                                      |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.24x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                     |
| mako                       | 11.9 ms                                                | 9.87 ms: 1.21x faster                                                      |
| nbody                      | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 62.5 ms: 1.20x faster                                                      |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                      |
| float                      | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.16x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.37 ms: 1.16x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                      |
| richards                   | 45.8 ms                                                | 40.0 ms: 1.15x faster                                                      |
| richards_super             | 51.5 ms                                                | 45.1 ms: 1.14x faster                                                      |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                      |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                       |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                      |
| fannkuch                   | 417 ms                                                 | 376 ms: 1.11x faster                                                       |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 97.5 ms: 1.10x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                       |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                       |
| tornado_http               | 103 ms                                                 | 95.7 ms: 1.07x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                      |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                                       |
| json                       | 5.26 ms                                                | 5.02 ms: 1.05x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.05x faster                                                       |
| pyflate                    | 482 ms                                                 | 462 ms: 1.05x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                     |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                      |
| pickle_dict                | 35.5 us                                                | 34.7 us: 1.02x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                     |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                      |
| pickle                     | 11.6 us                                                | 11.7 us: 1.00x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 494 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                     |
| unpickle_list              | 5.29 us                                                | 5.33 us: 1.01x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                      |
| sympy_str                  | 300 ms                                                 | 305 ms: 1.02x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                      |
| pickle_list                | 5.08 us                                                | 5.18 us: 1.02x slower                                                      |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                       |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                                       |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 3.99 ms: 1.05x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                     |
| telco                      | 7.10 ms                                                | 7.49 ms: 1.06x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 117 ms: 1.06x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 894 us: 1.06x slower                                                       |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                       |
| nqueens                    | 83.3 ms                                                | 88.6 ms: 1.06x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.92 ms: 1.08x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 23.5 ms: 1.10x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 60.5 ms: 1.10x slower                                                      |
| generators                 | 31.2 ms                                                | 34.9 ms: 1.12x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                                      |
| unpack_sequence            | 54.0 ns                                                | 108 ns: 2.01x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 60.7 ms: 2.53x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (1): logging_silent
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241001-3.14.0a0-984ca75-JIT/bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x