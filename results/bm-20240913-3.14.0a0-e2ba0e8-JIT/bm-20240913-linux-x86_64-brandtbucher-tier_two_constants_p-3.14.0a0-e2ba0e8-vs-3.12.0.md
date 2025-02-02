# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_constants_p
- machine: linux-x86_64
- commit hash: e2ba0e8
- commit date: 2024-09-13
- overall geometric mean: 1.085x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                        |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                      |
| tornado_http   | 103 ms                                                 | 95.1 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                        |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 400 ms: 1.45x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 888 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.6 ms: 1.22x faster                                                       |
| nbody          | 97.0 ms                                                | 81.7 ms: 1.19x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.05x faster                                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 76.9 ms: 1.16x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 54.1 ms: 1.14x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                       |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                        |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                       |
| pickle_dict          | 35.5 us                                                | 34.6 us: 1.03x faster                                                       |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                                       |
| unpickle_list        | 5.29 us                                                | 5.34 us: 1.01x slower                                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.73 ms: 1.22x faster                                                       |
| django_template | 34.6 ms                                                | 35.8 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                        |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 400 ms: 1.45x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                        |
| deepcopy                   | 371 us                                                 | 277 us: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 554 ms: 1.31x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 888 ms: 1.30x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                       |
| mako                       | 11.9 ms                                                | 9.73 ms: 1.22x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 67.3 ms: 1.22x faster                                                       |
| float                      | 84.7 ms                                                | 69.6 ms: 1.22x faster                                                       |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                       |
| nbody                      | 97.0 ms                                                | 81.7 ms: 1.19x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 63.3 ms: 1.19x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                      |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 76.9 ms: 1.16x faster                                                       |
| richards                   | 45.8 ms                                                | 39.6 ms: 1.16x faster                                                       |
| spectral_norm              | 115 ms                                                 | 99.6 ms: 1.15x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.1 ms: 1.14x faster                                                       |
| richards_super             | 51.5 ms                                                | 45.1 ms: 1.14x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                       |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.47 ms: 1.13x faster                                                       |
| fannkuch                   | 417 ms                                                 | 374 ms: 1.12x faster                                                        |
| raytrace                   | 312 ms                                                 | 280 ms: 1.11x faster                                                        |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                       |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                        |
| tornado_http               | 103 ms                                                 | 95.1 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                                        |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                        |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                       |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                        |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                        |
| regex_compile              | 148 ms                                                 | 142 ms: 1.05x faster                                                        |
| json                       | 5.26 ms                                                | 5.02 ms: 1.05x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                       |
| pickle_dict                | 35.5 us                                                | 34.6 us: 1.03x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                       |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                        |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 68.3 ms: 1.00x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                                        |
| pickle_list                | 5.08 us                                                | 5.11 us: 1.01x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                        |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                        |
| unpickle_list              | 5.29 us                                                | 5.34 us: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.01x slower                                                       |
| pickle                     | 11.6 us                                                | 11.8 us: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                       |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 502 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                      |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                        |
| nqueens                    | 83.3 ms                                                | 86.5 ms: 1.04x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                                        |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                                       |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 58.7 ms: 1.07x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| hexiom                     | 6.41 ms                                                | 7.05 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 8.07 ms: 1.14x slower                                                       |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                       |
| unpack_sequence            | 54.0 ns                                                | 108 ns: 2.00x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                |

Benchmark hidden because not significant (3): regex_effbot, sqlglot_parse, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240913-3.14.0a0-e2ba0e8-JIT/bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.085x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.07x