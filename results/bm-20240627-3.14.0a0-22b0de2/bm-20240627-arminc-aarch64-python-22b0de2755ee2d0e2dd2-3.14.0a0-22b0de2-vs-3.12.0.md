# Results vs. 3.12.0

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: linux-aarch64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.03x faster
- HPT reliability: 87.20%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.3 ms: 1.03x slower                                                   |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 410 ms: 1.41x faster                                                    |
| async_tree_none            | 624 ms                                                                | 444 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 579 ms: 1.34x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.06 sec: 1.33x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.09 sec: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 729 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 710 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.6 ms: 1.00x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.07x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 358 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| xml_etree_process    | 79.0 ms                                                               | 80.5 ms: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 33.3 us: 1.09x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 61.5 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 42.2 ms: 1.04x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 28.8 ms: 1.05x slower                                                   |
| mako            | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 410 ms: 1.41x faster                                                    |
| async_tree_none            | 624 ms                                                                | 444 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 579 ms: 1.34x faster                                                    |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.06 sec: 1.33x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 38.3 us: 1.30x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.09 sec: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 729 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 710 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| raytrace                   | 353 ms                                                                | 298 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.48 us: 1.18x faster                                                   |
| generators                 | 43.5 ms                                                               | 37.6 ms: 1.16x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.07 us: 1.08x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.77 us: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                   |
| regex_compile              | 137 ms                                                                | 129 ms: 1.07x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.5 ms: 1.06x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.05x faster                                                   |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.3 ms: 1.05x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.4 ms: 1.04x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.75 ms: 1.04x faster                                                   |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.9 ms: 1.03x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 358 us: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| float                      | 92.1 ms                                                               | 91.6 ms: 1.00x faster                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 61.5 ms: 1.02x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.5 ms: 1.02x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.7 ms: 1.02x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 29.6 ms: 1.02x slower                                                   |
| fannkuch                   | 443 ms                                                                | 453 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.7 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.13 ms: 1.02x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 579 ms: 1.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 464 ms: 1.02x slower                                                    |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                                    |
| thrift                     | 937 us                                                                | 961 us: 1.03x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 129 ms: 1.03x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 67.3 ms: 1.03x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.2 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                  |
| json                       | 5.54 ms                                                               | 5.80 ms: 1.05x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 28.8 ms: 1.05x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 964 ms: 1.05x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.99 sec: 1.06x slower                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| richards                   | 50.9 ms                                                               | 54.2 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.59 ms: 1.06x slower                                                   |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                    |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| scimark_fft                | 418 ms                                                                | 451 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.3 us: 1.09x slower                                                   |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 199 us: 1.10x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 4.90 ms: 1.12x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.92 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (12): pylint, dask, bench_mp_pool, nqueens, xml_etree_iterparse, async_generators, asyncio_websockets, 2to3, meteor_contest, xml_etree_generate, pyflate, regex_dna
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240627-3.14.0a0-22b0de2/bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json: bpe_tokeniser

# HPT report

- Reliability score: 87.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x