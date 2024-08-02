# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: c73f8ac
- commit date: 2024-06-04
- overall geometric mean: 1.02x faster
- HPT reliability: 96.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                    |
| docutils       | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                  |
| tornado_http   | 103 ms                                                 | 94.6 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 342 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 446 ms: 1.29x faster                                                    |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 473 ms: 1.22x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 950 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 600 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 632 ms: 1.15x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.0 ms: 1.07x faster                                                   |
| nbody          | 97.0 ms                                                | 92.2 ms: 1.05x faster                                                   |
| pidigits       | 187 ms                                                 | 190 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                   |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.23 sec: 1.04x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 87.5 ms: 1.02x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 227 us: 1.01x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 61.1 ms: 1.01x faster                                                   |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                    |
| pickle_dict          | 35.5 us                                                | 36.2 us: 1.02x slower                                                   |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                   |
| json_loads           | 28.5 us                                                | 29.2 us: 1.02x slower                                                   |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.35 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 12.0 ms: 1.00x slower                                                   |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 342 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 446 ms: 1.29x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                   |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 473 ms: 1.22x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 950 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 600 ms: 1.21x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                   |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 632 ms: 1.15x faster                                                    |
| logging_format             | 7.23 us                                                | 6.48 us: 1.12x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.35 ms: 1.11x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.84 us: 1.11x faster                                                   |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                    |
| tornado_http               | 103 ms                                                 | 94.6 ms: 1.08x faster                                                   |
| chaos                      | 67.0 ms                                                | 62.0 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 69.9 ms: 1.07x faster                                                   |
| float                      | 84.7 ms                                                | 79.0 ms: 1.07x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 76.6 ms: 1.07x faster                                                   |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                                    |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                   |
| nbody                      | 97.0 ms                                                | 92.2 ms: 1.05x faster                                                   |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.04x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.23 sec: 1.04x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.0 ms: 1.04x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                                    |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                    |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                    |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 87.5 ms: 1.02x faster                                                   |
| scimark_fft                | 382 ms                                                 | 376 ms: 1.02x faster                                                    |
| nqueens                    | 83.3 ms                                                | 82.1 ms: 1.01x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.01x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 227 us: 1.01x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.00 ms: 1.01x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 61.1 ms: 1.01x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                  |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                    |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                    |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                                    |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                                   |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.38 ms: 1.00x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 838 us: 1.00x faster                                                    |
| mako                       | 11.9 ms                                                | 12.0 ms: 1.00x slower                                                   |
| pprint_safe_repr           | 776 ms                                                 | 780 ms: 1.01x slower                                                    |
| deepcopy_reduce            | 3.35 us                                                | 3.36 us: 1.01x slower                                                   |
| deepcopy                   | 371 us                                                 | 373 us: 1.01x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                    |
| deepcopy_memo              | 40.7 us                                                | 41.0 us: 1.01x slower                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.58 sec: 1.01x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                   |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                    |
| pidigits                   | 187 ms                                                 | 190 ms: 1.02x slower                                                    |
| pickle_dict                | 35.5 us                                                | 36.2 us: 1.02x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                   |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                                    |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.2 us: 1.02x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                   |
| json                       | 5.26 ms                                                | 5.39 ms: 1.03x slower                                                   |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                    |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.94 us: 1.04x slower                                                   |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 3.95 ms: 1.04x slower                                                   |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                  |
| richards                   | 45.8 ms                                                | 48.2 ms: 1.05x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.35 us: 1.05x slower                                                   |
| richards_super             | 51.5 ms                                                | 54.4 ms: 1.06x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                   |
| telco                      | 7.10 ms                                                | 8.45 ms: 1.19x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                   |
| coverage                   | 72.7 ms                                                | 92.5 ms: 1.27x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, dask, scimark_lu
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240604-3.14.0a0-c73f8ac/bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x