# Results vs. 3.12.0

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: linux-aarch64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.03x faster
- HPT reliability: 93.18%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                  |
| html5lib       | 65.1 ms                                                               | 66.8 ms: 1.03x slower                                                   |
| tornado_http   | 136 ms                                                                | 125 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 407 ms: 1.42x faster                                                    |
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 569 ms: 1.36x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.12 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 710 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 734 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                    |
| regex_dna      | 254 ms                                                                | 258 ms: 1.01x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                  |
| pickle_pure_python   | 365 us                                                                | 357 us: 1.02x faster                                                    |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.80 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 407 ms: 1.42x faster                                                    |
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 569 ms: 1.36x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.8 us: 1.28x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.12 sec: 1.26x faster                                                  |
| generators                 | 43.5 ms                                                               | 34.8 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 710 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 734 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.23x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.37 us: 1.22x faster                                                   |
| raytrace                   | 353 ms                                                                | 295 ms: 1.20x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.68 us: 1.09x faster                                                   |
| tornado_http               | 136 ms                                                                | 125 ms: 1.09x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.80 ms: 1.08x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.05 us: 1.08x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.71 ms: 1.07x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 57.9 ms: 1.07x faster                                                   |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.8 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.7 ms: 1.06x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.25 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| dask                       | 376 ms                                                                | 360 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.2 ms: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                                  |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 357 us: 1.02x faster                                                    |
| nqueens                    | 99.2 ms                                                               | 97.1 ms: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| async_generators           | 491 ms                                                                | 486 ms: 1.01x faster                                                    |
| meteor_contest             | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| pyflate                    | 559 ms                                                                | 562 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.0 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 61.9 ms: 1.01x slower                                                   |
| sympy_expand               | 454 ms                                                                | 459 ms: 1.01x slower                                                    |
| regex_dna                  | 254 ms                                                                | 258 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.02x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.09 ms: 1.02x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 936 ms: 1.02x slower                                                    |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.68 ms: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.3 ms: 1.03x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 66.8 ms: 1.03x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                  |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 587 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.80 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.52 ms: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 442 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| fannkuch                   | 443 ms                                                                | 478 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 198 us: 1.10x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.54 ms: 1.12x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.2 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.08 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.20x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (10): xml_etree_iterparse, pylint, thrift, bench_mp_pool, xml_etree_process, asyncio_websockets, genshi_xml, xml_etree_generate, genshi_text, sqlglot_normalize
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: bpe_tokeniser

# HPT report

- Reliability score: 93.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x