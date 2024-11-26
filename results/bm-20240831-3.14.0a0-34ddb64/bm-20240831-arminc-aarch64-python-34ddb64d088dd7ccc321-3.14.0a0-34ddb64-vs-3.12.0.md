# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.043x faster
- HPT reliability: 99.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                  |
| html5lib       | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                   |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 422 ms: 1.48x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 559 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 544 ms: 1.36x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.12 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 722 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 356 us: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                   |
| django_template | 40.7 ms                                                               | 41.4 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 422 ms: 1.48x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 559 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 544 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 337 us: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.12 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.0 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 722 ms: 1.22x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.8 us: 1.22x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.16 sec: 1.21x faster                                                  |
| raytrace                   | 353 ms                                                                | 301 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.51 us: 1.17x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.0 ms: 1.17x faster                                                   |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.91 us: 1.10x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                    |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.64 us: 1.09x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                    |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 58.7 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.92 ms: 1.05x faster                                                   |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.6 ms: 1.04x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 83.3 ms: 1.04x faster                                                   |
| async_generators           | 491 ms                                                                | 474 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.03x faster                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.5 ms: 1.03x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 551 ms: 1.03x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 356 us: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.3 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 63.7 ms: 1.02x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                  |
| genshi_xml                 | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.00 ms: 1.01x faster                                                   |
| thrift                     | 937 us                                                                | 931 us: 1.01x faster                                                    |
| float                      | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| pyflate                    | 559 ms                                                                | 567 ms: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.4 ms: 1.02x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.04 sec: 1.02x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 62.5 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.13 ms: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.70 ms: 1.03x slower                                                   |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.40 ms: 1.03x slower                                                   |
| richards_super             | 58.5 ms                                                               | 60.7 ms: 1.04x slower                                                   |
| nbody                      | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 465 ms: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                   |
| richards                   | 50.9 ms                                                               | 54.3 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.1 ms: 1.13x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.99 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.76 ms: 1.15x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (10): xml_etree_iterparse, meteor_contest, regex_dna, pprint_safe_repr, asyncio_websockets, genshi_text, xml_etree_process, nqueens, xml_etree_generate, pylint
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.043x faster
# HPT report

- Reliability score: 99.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x