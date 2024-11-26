# Results vs. 3.12.0

- fork: brandtbucher
- ref: off_by_one
- machine: linux-x86_64
- commit hash: e099186
- commit date: 2024-09-12
- overall geometric mean: 1.096x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                              |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                            |
| tornado_http   | 103 ms                                                 | 93.5 ms: 1.10x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.49x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.46x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 879 ms: 1.35x faster                                              |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                              |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.0 ms: 1.23x faster                                             |
| float          | 84.7 ms                                                | 69.7 ms: 1.22x faster                                             |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.15x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                             |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                              |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.13x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 79.4 ms: 1.12x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                             |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                              |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                             |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                             |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.04x faster                                              |
| json_dumps           | 10.4 ms                                                | 9.99 ms: 1.04x faster                                             |
| unpickle_list        | 5.29 us                                                | 5.22 us: 1.01x faster                                             |
| pickle_dict          | 35.5 us                                                | 35.8 us: 1.01x slower                                             |
| pickle               | 11.6 us                                                | 11.9 us: 1.02x slower                                             |
| pickle_list          | 5.08 us                                                | 5.22 us: 1.03x slower                                             |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                             |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.77 ms: 1.22x faster                                             |
| django_template | 34.6 ms                                                | 36.5 ms: 1.06x slower                                             |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.6 us: 1.53x faster                                             |
| async_tree_none            | 472 ms                                                 | 315 ms: 1.49x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.46x faster                                              |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 879 ms: 1.35x faster                                              |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                              |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                             |
| scimark_fft                | 382 ms                                                 | 304 ms: 1.25x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 65.9 ms: 1.24x faster                                             |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                             |
| nbody                      | 97.0 ms                                                | 79.0 ms: 1.23x faster                                             |
| mako                       | 11.9 ms                                                | 9.77 ms: 1.22x faster                                             |
| float                      | 84.7 ms                                                | 69.7 ms: 1.22x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.20x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.27 ms: 1.18x faster                                             |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                             |
| richards                   | 45.8 ms                                                | 38.9 ms: 1.18x faster                                             |
| spectral_norm              | 115 ms                                                 | 98.2 ms: 1.17x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                             |
| richards_super             | 51.5 ms                                                | 44.2 ms: 1.17x faster                                             |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                             |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                              |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.13x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 79.4 ms: 1.12x faster                                             |
| pyflate                    | 482 ms                                                 | 430 ms: 1.12x faster                                              |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                              |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.12x faster                                              |
| tornado_http               | 103 ms                                                 | 93.5 ms: 1.10x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                             |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                              |
| go                         | 139 ms                                                 | 130 ms: 1.08x faster                                              |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                             |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                              |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.07x faster                                              |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.07x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                            |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                             |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.04x faster                                              |
| json_dumps                 | 10.4 ms                                                | 9.99 ms: 1.04x faster                                             |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                            |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                             |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                             |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                             |
| dulwich_log                | 68.5 ms                                                | 67.6 ms: 1.01x faster                                             |
| unpickle_list              | 5.29 us                                                | 5.22 us: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                              |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                              |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                             |
| asyncio_tcp                | 491 ms                                                 | 487 ms: 1.01x faster                                              |
| bench_thread_pool          | 842 us                                                 | 836 us: 1.01x faster                                              |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                              |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                              |
| pickle_dict                | 35.5 us                                                | 35.8 us: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                            |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                             |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                              |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                              |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                            |
| nqueens                    | 83.3 ms                                                | 85.0 ms: 1.02x slower                                             |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                              |
| pickle                     | 11.6 us                                                | 11.9 us: 1.02x slower                                             |
| pickle_list                | 5.08 us                                                | 5.22 us: 1.03x slower                                             |
| gc_traversal               | 3.79 ms                                                | 3.94 ms: 1.04x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                              |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                              |
| django_template            | 34.6 ms                                                | 36.5 ms: 1.06x slower                                             |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                            |
| sqlglot_optimize           | 54.8 ms                                                | 58.0 ms: 1.06x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                             |
| hexiom                     | 6.41 ms                                                | 6.88 ms: 1.07x slower                                             |
| generators                 | 31.2 ms                                                | 33.5 ms: 1.07x slower                                             |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                             |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                             |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                             |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                             |
| unpack_sequence            | 54.0 ns                                                | 105 ns: 1.95x slower                                              |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                      |

Benchmark hidden because not significant (3): sympy_str, sqlglot_transpile, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-e099186-JIT/bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.096x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.05x