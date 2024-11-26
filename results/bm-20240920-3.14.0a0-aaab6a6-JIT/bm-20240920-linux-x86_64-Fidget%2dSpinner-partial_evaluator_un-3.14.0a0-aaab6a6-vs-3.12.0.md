# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: partial_evaluator_un
- machine: linux-x86_64
- commit hash: aaab6a6
- commit date: 2024-09-20
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.68x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                            |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                          |
| tornado_http   | 103 ms                                                 | 95.1 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                            |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 862 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                           |
| nbody          | 97.0 ms                                                | 81.1 ms: 1.20x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.05x faster                                                            |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                           |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                            |
| regex_effbot   | 3.61 ms                                                | 3.92 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 76.7 ms: 1.16x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 53.7 ms: 1.15x faster                                                           |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.1 ms: 1.09x faster                                                           |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                            |
| pickle_dict          | 35.5 us                                                | 34.4 us: 1.03x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                           |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.52x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                            |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                            |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 862 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.32x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 66.4 ms: 1.23x faster                                                           |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                           |
| float                      | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                           |
| mako                       | 11.9 ms                                                | 9.92 ms: 1.20x faster                                                           |
| nbody                      | 97.0 ms                                                | 81.1 ms: 1.20x faster                                                           |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                          |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 64.2 ms: 1.17x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 76.7 ms: 1.16x faster                                                           |
| richards                   | 45.8 ms                                                | 39.6 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.37 ms: 1.16x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 53.7 ms: 1.15x faster                                                           |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                           |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                            |
| richards_super             | 51.5 ms                                                | 45.7 ms: 1.13x faster                                                           |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                                            |
| unpickle                   | 15.9 us                                                | 14.4 us: 1.10x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                                           |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                            |
| tornado_http               | 103 ms                                                 | 95.1 ms: 1.08x faster                                                           |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.08x faster                                                            |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                                           |
| go                         | 139 ms                                                 | 132 ms: 1.05x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                            |
| regex_compile              | 148 ms                                                 | 142 ms: 1.05x faster                                                            |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                          |
| pickle_dict                | 35.5 us                                                | 34.4 us: 1.03x faster                                                           |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 754 ms: 1.03x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 67.2 ms: 1.02x faster                                                           |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                            |
| async_generators           | 463 ms                                                 | 456 ms: 1.02x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 835 us: 1.01x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                           |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.00x faster                                                            |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 497 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| pickle_list                | 5.08 us                                                | 5.17 us: 1.02x slower                                                           |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                           |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                            |
| nqueens                    | 83.3 ms                                                | 85.7 ms: 1.03x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 3.91 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                            |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                           |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                                            |
| generators                 | 31.2 ms                                                | 33.0 ms: 1.06x slower                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 58.4 ms: 1.06x slower                                                           |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                            |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.07x slower                                                           |
| hexiom                     | 6.41 ms                                                | 6.86 ms: 1.07x slower                                                           |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.92 ms: 1.08x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                           |
| coverage                   | 72.7 ms                                                | 84.2 ms: 1.16x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                           |
| unpack_sequence            | 54.0 ns                                                | 111 ns: 2.06x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (3): pickle, bench_mp_pool, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240920-3.14.0a0-aaab6a6-JIT/bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.087x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.68x