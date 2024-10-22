# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_gc_fix_
- machine: linux-x86_64
- commit hash: ea7b940
- commit date: 2024-09-27
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 268 ms: 1.02x faster                                                            |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                          |
| tornado_http   | 103 ms                                                 | 91.1 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 656 ms: 1.80x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 650 ms: 1.78x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 342 ms: 1.68x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 278 ms: 1.62x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 365 ms: 1.58x faster                                                            |
| async_tree_none            | 472 ms                                                 | 300 ms: 1.57x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 498 ms: 1.46x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 521 ms: 1.39x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.61x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 89.6 ms: 1.08x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| float          | 84.7 ms                                                | 94.2 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                           |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                           |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.10x faster                                                          |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                                           |
| pickle_dict          | 35.5 us                                                | 33.6 us: 1.06x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                                            |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                            |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 87.9 ms: 1.01x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.01x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 61.9 ms: 1.00x slower                                                           |
| xml_etree_parse      | 159 ms                                                 | 163 ms: 1.02x slower                                                            |
| unpickle_list        | 5.29 us                                                | 5.41 us: 1.02x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 134 ms: 1.25x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 656 ms: 1.80x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 650 ms: 1.78x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 342 ms: 1.68x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 278 ms: 1.62x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 365 ms: 1.58x faster                                                            |
| async_tree_none            | 472 ms                                                 | 300 ms: 1.57x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 498 ms: 1.46x faster                                                            |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 521 ms: 1.39x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                           |
| unpack_sequence            | 54.0 ns                                                | 45.6 ns: 1.18x faster                                                           |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                            |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                            |
| logging_format             | 7.23 us                                                | 6.32 us: 1.14x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 71.6 ms: 1.14x faster                                                           |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                                           |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                           |
| tornado_http               | 103 ms                                                 | 91.1 ms: 1.13x faster                                                           |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                                           |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.10x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                                           |
| nbody                      | 97.0 ms                                                | 89.6 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 718 ms: 1.08x faster                                                            |
| scimark_fft                | 382 ms                                                 | 357 ms: 1.07x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 793 us: 1.06x faster                                                            |
| json                       | 5.26 ms                                                | 4.96 ms: 1.06x faster                                                           |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                          |
| pickle_dict                | 35.5 us                                                | 33.6 us: 1.06x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                                            |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                           |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                            |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 79.8 ms: 1.04x faster                                                           |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                            |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.25 ms: 1.03x faster                                                           |
| 2to3                       | 274 ms                                                 | 268 ms: 1.02x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 479 ms: 1.02x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 53.8 ms: 1.02x faster                                                           |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                           |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 87.9 ms: 1.01x faster                                                           |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                           |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                           |
| pickle_list                | 5.08 us                                                | 5.06 us: 1.01x faster                                                           |
| pyflate                    | 482 ms                                                 | 480 ms: 1.00x faster                                                            |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| xml_etree_process          | 61.7 ms                                                | 61.9 ms: 1.00x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                           |
| richards                   | 45.8 ms                                                | 46.5 ms: 1.02x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                                            |
| xml_etree_parse            | 159 ms                                                 | 163 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                            |
| unpickle_list              | 5.29 us                                                | 5.41 us: 1.02x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 3.89 ms: 1.02x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                           |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                            |
| float                      | 84.7 ms                                                | 94.2 ms: 1.11x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.70 ms: 1.15x slower                                                           |
| telco                      | 7.10 ms                                                | 8.33 ms: 1.17x slower                                                           |
| coverage                   | 72.7 ms                                                | 85.8 ms: 1.18x slower                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 134 ms: 1.25x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (3): bench_mp_pool, pycparser, logging_silent
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240927-3.14.0a0-ea7b940/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.96x