# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 6a6bae2
- commit date: 2024-06-04
- overall geometric mean: 1.43x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 406 ms: 1.48x slower                                                    |
| docutils       | 2.77 sec                                               | 3.44 sec: 1.24x slower                                                  |
| tornado_http   | 103 ms                                                 | 139 ms: 1.36x slower                                                    |
| Geometric mean | (ref)                                                  | 1.36x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 927 ms: 1.28x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 979 ms: 1.18x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 536 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 678 ms: 1.07x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 427 ms: 1.05x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 586 ms: 1.01x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (2): async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                    |
| float          | 84.7 ms                                                | 141 ms: 1.66x slower                                                    |
| nbody          | 97.0 ms                                                | 234 ms: 2.42x slower                                                    |
| Geometric mean | (ref)                                                  | 1.59x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                   |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                   |
| regex_compile  | 148 ms                                                 | 227 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                  | 1.14x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 5.08 us                                                | 4.90 us: 1.04x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.03x faster                                                    |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                   |
| unpickle             | 15.9 us                                                | 16.2 us: 1.02x slower                                                   |
| unpickle_list        | 5.29 us                                                | 5.73 us: 1.08x slower                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 118 ms: 1.11x slower                                                    |
| json_loads           | 28.5 us                                                | 31.8 us: 1.12x slower                                                   |
| pickle_dict          | 35.5 us                                                | 41.1 us: 1.16x slower                                                   |
| xml_etree_generate   | 89.2 ms                                                | 115 ms: 1.29x slower                                                    |
| json_dumps           | 10.4 ms                                                | 14.2 ms: 1.37x slower                                                   |
| tomli_loads          | 2.33 sec                                               | 3.38 sec: 1.45x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 92.8 ms: 1.50x slower                                                   |
| unpickle_pure_python | 230 us                                                 | 423 us: 1.84x slower                                                    |
| pickle_pure_python   | 324 us                                                 | 611 us: 1.89x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.24x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.18 ms: 1.32x slower                                                   |
| python_startup         | 9.55 ms                                                | 13.7 ms: 1.43x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.38x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 21.6 ms: 1.81x slower                                                   |
| django_template | 34.6 ms                                                | 62.9 ms: 1.82x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.81x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 3.79 ms                                                | 2.78 ms: 1.36x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 927 ms: 1.28x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 979 ms: 1.18x faster                                                    |
| bench_mp_pool              | 24.0 ms                                                | 20.4 ms: 1.17x faster                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.37 ms: 1.08x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 536 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 678 ms: 1.07x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 427 ms: 1.05x faster                                                    |
| pickle_list                | 5.08 us                                                | 4.90 us: 1.04x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.03x faster                                                    |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                    |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                   |
| async_tree_memoization     | 578 ms                                                 | 586 ms: 1.01x slower                                                    |
| pathlib                    | 19.3 ms                                                | 19.7 ms: 1.02x slower                                                   |
| unpickle                   | 15.9 us                                                | 16.2 us: 1.02x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                    |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| unpickle_list              | 5.29 us                                                | 5.73 us: 1.08x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 118 ms: 1.11x slower                                                    |
| json_loads                 | 28.5 us                                                | 31.8 us: 1.12x slower                                                   |
| json                       | 5.26 ms                                                | 5.98 ms: 1.14x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 3.25 us: 1.15x slower                                                   |
| pickle_dict                | 35.5 us                                                | 41.1 us: 1.16x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.13 sec: 1.19x slower                                                  |
| async_generators           | 463 ms                                                 | 565 ms: 1.22x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 600 ms: 1.22x slower                                                    |
| docutils                   | 2.77 sec                                               | 3.44 sec: 1.24x slower                                                  |
| generators                 | 31.2 ms                                                | 39.1 ms: 1.25x slower                                                   |
| xml_etree_generate         | 89.2 ms                                                | 115 ms: 1.29x slower                                                    |
| dulwich_log                | 68.5 ms                                                | 89.0 ms: 1.30x slower                                                   |
| mdp                        | 2.63 sec                                               | 3.42 sec: 1.30x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 9.18 ms: 1.32x slower                                                   |
| scimark_fft                | 382 ms                                                 | 506 ms: 1.33x slower                                                    |
| tornado_http               | 103 ms                                                 | 139 ms: 1.36x slower                                                    |
| comprehensions             | 21.8 us                                                | 29.7 us: 1.36x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 14.2 ms: 1.37x slower                                                   |
| meteor_contest             | 112 ms                                                 | 154 ms: 1.37x slower                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.94 ms: 1.37x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 29.5 ms: 1.38x slower                                                   |
| telco                      | 7.10 ms                                                | 9.83 ms: 1.39x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.65 sec: 1.40x slower                                                  |
| coroutines                 | 23.2 ms                                                | 33.0 ms: 1.43x slower                                                   |
| crypto_pyaes               | 81.9 ms                                                | 117 ms: 1.43x slower                                                    |
| python_startup             | 9.55 ms                                                | 13.7 ms: 1.43x slower                                                   |
| tomli_loads                | 2.33 sec                                               | 3.38 sec: 1.45x slower                                                  |
| nqueens                    | 83.3 ms                                                | 122 ms: 1.46x slower                                                    |
| sympy_str                  | 300 ms                                                 | 438 ms: 1.46x slower                                                    |
| 2to3                       | 274 ms                                                 | 406 ms: 1.48x slower                                                    |
| fannkuch                   | 417 ms                                                 | 626 ms: 1.50x slower                                                    |
| xml_etree_process          | 61.7 ms                                                | 92.8 ms: 1.50x slower                                                   |
| regex_compile              | 148 ms                                                 | 227 ms: 1.53x slower                                                    |
| sympy_sum                  | 169 ms                                                 | 262 ms: 1.55x slower                                                    |
| deepcopy_reduce            | 3.35 us                                                | 5.39 us: 1.61x slower                                                   |
| deepcopy                   | 371 us                                                 | 598 us: 1.61x slower                                                    |
| sympy_expand               | 478 ms                                                 | 778 ms: 1.63x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 182 ms: 1.65x slower                                                    |
| float                      | 84.7 ms                                                | 141 ms: 1.66x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 91.4 ms: 1.67x slower                                                   |
| logging_format             | 7.23 us                                                | 12.2 us: 1.68x slower                                                   |
| pyflate                    | 482 ms                                                 | 813 ms: 1.69x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 266 us: 1.69x slower                                                    |
| spectral_norm              | 115 ms                                                 | 195 ms: 1.70x slower                                                    |
| deepcopy_memo              | 40.7 us                                                | 69.8 us: 1.71x slower                                                   |
| logging_simple             | 6.46 us                                                | 11.1 us: 1.71x slower                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 130 ms: 1.73x slower                                                    |
| pprint_safe_repr           | 776 ms                                                 | 1.38 sec: 1.78x slower                                                  |
| mako                       | 11.9 ms                                                | 21.6 ms: 1.81x slower                                                   |
| pprint_pformat             | 1.57 sec                                               | 2.85 sec: 1.81x slower                                                  |
| django_template            | 34.6 ms                                                | 62.9 ms: 1.82x slower                                                   |
| richards                   | 45.8 ms                                                | 83.6 ms: 1.82x slower                                                   |
| unpickle_pure_python       | 230 us                                                 | 423 us: 1.84x slower                                                    |
| pickle_pure_python         | 324 us                                                 | 611 us: 1.89x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 3.22 ms: 1.91x slower                                                   |
| chaos                      | 67.0 ms                                                | 129 ms: 1.93x slower                                                    |
| logging_silent             | 104 ns                                                 | 203 ns: 1.95x slower                                                    |
| richards_super             | 51.5 ms                                                | 101 ms: 1.96x slower                                                    |
| hexiom                     | 6.41 ms                                                | 12.7 ms: 1.98x slower                                                   |
| raytrace                   | 312 ms                                                 | 628 ms: 2.01x slower                                                    |
| sqlglot_parse              | 1.36 ms                                                | 2.74 ms: 2.01x slower                                                   |
| scimark_sor                | 129 ms                                                 | 274 ms: 2.12x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 254 ms: 2.15x slower                                                    |
| go                         | 139 ms                                                 | 329 ms: 2.36x slower                                                    |
| deltablue                  | 3.72 ms                                                | 8.80 ms: 2.37x slower                                                   |
| nbody                      | 97.0 ms                                                | 234 ms: 2.42x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 3.15 ms: 3.74x slower                                                   |
| coverage                   | 72.7 ms                                                | 802 ms: 11.04x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.43x slower                                                            |

Benchmark hidden because not significant (2): async_tree_none, async_tree_cpu_io_mixed
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240604-3.14.0a0-6a6bae2-NOGIL/bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.26x

# Memory
- memory change: 1.12x