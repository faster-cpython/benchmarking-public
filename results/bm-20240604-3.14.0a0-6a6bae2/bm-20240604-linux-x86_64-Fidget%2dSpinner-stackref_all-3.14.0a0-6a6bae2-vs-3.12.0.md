# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 6a6bae2
- commit date: 2024-06-04
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                                    |
| tornado_http   | 103 ms                                                 | 94.0 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 337 ms: 1.33x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 902 ms: 1.31x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 440 ms: 1.31x faster                                                    |
| async_tree_none            | 472 ms                                                 | 373 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 470 ms: 1.23x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 946 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 621 ms: 1.17x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.1 ms: 1.10x faster                                                   |
| float          | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                   |
| pidigits       | 187 ms                                                 | 190 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                   |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                    |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.15 sec: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                    |
| unpickle             | 15.9 us                                                | 15.2 us: 1.05x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                    |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                   |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                   |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                   |
| unpickle_list        | 5.29 us                                                | 5.42 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                   |
| django_template | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 337 ms: 1.33x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 902 ms: 1.31x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 440 ms: 1.31x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                   |
| async_tree_none            | 472 ms                                                 | 373 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 470 ms: 1.23x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 946 ms: 1.22x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                   |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 621 ms: 1.17x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                                   |
| logging_format             | 7.23 us                                                | 6.36 us: 1.14x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.14x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.7 ms: 1.11x faster                                                   |
| nbody                      | 97.0 ms                                                | 88.1 ms: 1.10x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                                   |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                    |
| tornado_http               | 103 ms                                                 | 94.0 ms: 1.09x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                    |
| float                      | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.15 sec: 1.09x faster                                                  |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                    |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.05x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 65.0 ms: 1.05x faster                                                   |
| logging_silent             | 104 ns                                                 | 99.6 ns: 1.05x faster                                                   |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.05x faster                                                   |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                   |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                                   |
| async_generators           | 463 ms                                                 | 447 ms: 1.04x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 39.3 us: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                    |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 753 ms: 1.03x faster                                                    |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.94 ms: 1.02x faster                                                   |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                   |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                    |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                    |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                    |
| deepcopy                   | 371 us                                                 | 367 us: 1.01x faster                                                    |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 3.32 us: 1.01x faster                                                   |
| scimark_fft                | 382 ms                                                 | 379 ms: 1.01x faster                                                    |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                    |
| pickle_list                | 5.08 us                                                | 5.06 us: 1.00x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.00x slower                                                   |
| django_template            | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                    |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                   |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                   |
| go                         | 139 ms                                                 | 142 ms: 1.01x slower                                                    |
| pidigits                   | 187 ms                                                 | 190 ms: 1.02x slower                                                    |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                  |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                   |
| unpickle_list              | 5.29 us                                                | 5.42 us: 1.03x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 568 ms: 1.03x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                  |
| richards                   | 45.8 ms                                                | 47.7 ms: 1.04x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                    |
| sqlite_synth               | 2.83 us                                                | 2.97 us: 1.05x slower                                                   |
| richards_super             | 51.5 ms                                                | 54.0 ms: 1.05x slower                                                   |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                   |
| telco                      | 7.10 ms                                                | 8.36 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                   |
| coverage                   | 72.7 ms                                                | 92.5 ms: 1.27x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (6): dask, xml_etree_parse, bench_mp_pool, sqlglot_optimize, pickle_dict, docutils
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240604-3.14.0a0-6a6bae2/bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.97x