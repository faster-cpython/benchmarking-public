# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.077x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 382 ms: 1.24x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.93 sec: 1.32x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                   |
| tornado_http   | 136 ms                                                                | 151 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 451 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 571 ms: 1.36x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 430 ms: 1.34x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 558 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 743 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.0 ms: 1.05x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 194 ms: 1.41x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 79.4 ms: 1.00x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 266 us: 1.02x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 382 us: 1.05x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.96 ms: 1.07x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.3 ms: 1.17x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 51.0 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.4 ms: 1.26x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 81.1 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 451 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 571 ms: 1.36x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 430 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 558 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 743 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                                   |
| deepcopy                   | 446 us                                                                | 400 us: 1.11x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.83 us: 1.07x faster                                                   |
| float                      | 92.1 ms                                                               | 88.0 ms: 1.05x faster                                                   |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.41 us: 1.03x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.13 us: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.3 ms: 1.02x faster                                                   |
| comprehensions             | 25.4 us                                                               | 25.0 us: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 79.4 ms: 1.00x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.45 sec: 1.01x slower                                                  |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| thrift                     | 937 us                                                                | 950 us: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 266 us: 1.02x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.03x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 89.4 ms: 1.03x slower                                                   |
| async_generators           | 491 ms                                                                | 507 ms: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.76 ms: 1.04x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 382 us: 1.05x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.34 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.96 ms: 1.07x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.59 ms: 1.08x slower                                                   |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.2 ms: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.81 ms: 1.10x slower                                                   |
| meteor_contest             | 112 ms                                                                | 123 ms: 1.10x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| scimark_fft                | 418 ms                                                                | 463 ms: 1.11x slower                                                    |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                    |
| tornado_http               | 136 ms                                                                | 151 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 635 ms: 1.12x slower                                                    |
| pyflate                    | 559 ms                                                                | 630 ms: 1.13x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.00 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.6 ms: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                    |
| fannkuch                   | 443 ms                                                                | 511 ms: 1.15x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.3 ms: 1.17x slower                                                   |
| go                         | 157 ms                                                                | 188 ms: 1.20x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.19 ms: 1.20x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 151 ms: 1.20x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.77 ms: 1.21x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.52 sec: 1.21x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.36 ms: 1.23x slower                                                   |
| 2to3                       | 308 ms                                                                | 382 ms: 1.24x slower                                                    |
| django_template            | 40.7 ms                                                               | 51.0 ms: 1.25x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.4 ms: 1.26x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 125 ms: 1.26x slower                                                    |
| chaos                      | 71.4 ms                                                               | 91.5 ms: 1.28x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 79.4 ms: 1.29x slower                                                   |
| sympy_str                  | 280 ms                                                                | 364 ms: 1.30x slower                                                    |
| richards_super             | 58.5 ms                                                               | 76.3 ms: 1.30x slower                                                   |
| generators                 | 43.5 ms                                                               | 56.9 ms: 1.31x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.93 sec: 1.32x slower                                                  |
| richards                   | 50.9 ms                                                               | 67.9 ms: 1.33x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 81.1 ms: 1.34x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 29.2 ms: 1.35x slower                                                   |
| sympy_expand               | 454 ms                                                                | 619 ms: 1.36x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 85.3 ms: 1.38x slower                                                   |
| pylint                     | 355 ms                                                                | 489 ms: 1.38x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 215 ms: 1.39x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.28 sec: 1.40x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.64 sec: 1.40x slower                                                  |
| regex_compile              | 137 ms                                                                | 194 ms: 1.41x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.3 ms: 1.48x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (4): raytrace, scimark_sor, xml_etree_parse, xml_etree_generate
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.077x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.02x