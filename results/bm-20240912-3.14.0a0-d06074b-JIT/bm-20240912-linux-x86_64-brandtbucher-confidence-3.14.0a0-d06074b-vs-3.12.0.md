# Results vs. 3.12.0

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d06074b
- commit date: 2024-09-12
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.00x faster                                              |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                            |
| tornado_http   | 103 ms                                                 | 94.9 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 384 ms: 1.50x faster                                              |
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.48x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 393 ms: 1.47x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 873 ms: 1.35x faster                                              |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                              |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.9 ms: 1.21x faster                                             |
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                             |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.14x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                              |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                              |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                             |
| regex_effbot   | 3.61 ms                                                | 3.82 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 76.9 ms: 1.16x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 54.6 ms: 1.13x faster                                             |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                             |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.06x faster                                              |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                              |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                             |
| unpickle_list        | 5.29 us                                                | 5.07 us: 1.04x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                             |
| pickle_dict          | 35.5 us                                                | 34.9 us: 1.02x faster                                             |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                             |
| pickle_list          | 5.08 us                                                | 5.24 us: 1.03x slower                                             |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                             |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.85 ms: 1.21x faster                                             |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 384 ms: 1.50x faster                                              |
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.48x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 393 ms: 1.47x faster                                              |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 873 ms: 1.35x faster                                              |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                              |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 66.0 ms: 1.24x faster                                             |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.11 ms: 1.23x faster                                             |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                             |
| nbody                      | 97.0 ms                                                | 79.9 ms: 1.21x faster                                             |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                             |
| mako                       | 11.9 ms                                                | 9.85 ms: 1.21x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.21x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                            |
| richards_super             | 51.5 ms                                                | 43.3 ms: 1.19x faster                                             |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                             |
| richards                   | 45.8 ms                                                | 39.3 ms: 1.17x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 76.9 ms: 1.16x faster                                             |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                             |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                              |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                             |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 54.6 ms: 1.13x faster                                             |
| pyflate                    | 482 ms                                                 | 430 ms: 1.12x faster                                              |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                              |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                              |
| unpickle                   | 15.9 us                                                | 14.4 us: 1.10x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 710 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                             |
| tornado_http               | 103 ms                                                 | 94.9 ms: 1.08x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                            |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.07x faster                                              |
| go                         | 139 ms                                                 | 131 ms: 1.07x faster                                              |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.06x faster                                              |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                              |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                              |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                             |
| json                       | 5.26 ms                                                | 5.01 ms: 1.05x faster                                             |
| unpickle_list              | 5.29 us                                                | 5.07 us: 1.04x faster                                             |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                             |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                             |
| pickle_dict                | 35.5 us                                                | 34.9 us: 1.02x faster                                             |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                              |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                              |
| bench_thread_pool          | 842 us                                                 | 838 us: 1.00x faster                                              |
| 2to3                       | 274 ms                                                 | 273 ms: 1.00x faster                                              |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                              |
| asyncio_tcp                | 491 ms                                                 | 494 ms: 1.01x slower                                              |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                            |
| nqueens                    | 83.3 ms                                                | 84.1 ms: 1.01x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                             |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                              |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                              |
| pickle_list                | 5.08 us                                                | 5.24 us: 1.03x slower                                             |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                             |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                              |
| sympy_expand               | 478 ms                                                 | 500 ms: 1.05x slower                                              |
| gc_traversal               | 3.79 ms                                                | 3.98 ms: 1.05x slower                                             |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.05x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                             |
| regex_effbot               | 3.61 ms                                                | 3.82 ms: 1.06x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 58.2 ms: 1.06x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                             |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.88 ms: 1.07x slower                                             |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                             |
| telco                      | 7.10 ms                                                | 8.00 ms: 1.13x slower                                             |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                             |
| unpack_sequence            | 54.0 ns                                                | 111 ns: 2.06x slower                                              |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                      |

Benchmark hidden because not significant (4): sympy_str, bench_mp_pool, sqlglot_transpile, logging_silent
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-d06074b-JIT/bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.05x