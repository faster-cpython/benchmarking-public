# Results vs. 3.12.0

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: linux-aarch64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.03x faster
- HPT reliability: 96.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 296 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| tornado_http   | 136 ms                                                                | 128 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 420 ms: 1.48x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 551 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 546 ms: 1.36x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 728 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.85 ms: 1.04x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 357 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.6 ms: 1.01x slower                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| django_template | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 420 ms: 1.48x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 551 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 546 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.0 ms: 1.24x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 728 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 20.8 ms: 1.18x faster                                                   |
| raytrace                   | 353 ms                                                                | 302 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.17x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.95 us: 1.10x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.67 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.07x faster                                                   |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                    |
| tornado_http               | 136 ms                                                                | 128 ms: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.9 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 296 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.8 ms: 1.04x faster                                                   |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.8 ms: 1.03x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.43 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 357 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| thrift                     | 937 us                                                                | 927 us: 1.01x faster                                                    |
| pyflate                    | 559 ms                                                                | 563 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 27.6 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 62.4 ms: 1.02x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.6 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.16 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.43 ms: 1.04x slower                                                   |
| nbody                      | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.85 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.4 ms: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 440 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.83 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.9 ms: 1.12x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.68 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| go                         | 157 ms                                                                | 193 ms: 1.23x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (15): asyncio_tcp, genshi_xml, async_generators, float, nqueens, asyncio_websockets, meteor_contest, pprint_pformat, pprint_safe_repr, bench_mp_pool, xml_etree_iterparse, pylint, xml_etree_generate, xml_etree_process, html5lib
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240826-3.14.0a0-fe85a82/bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82.json: bpe_tokeniser

# HPT report

- Reliability score: 96.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x