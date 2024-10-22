# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.02x faster
- HPT reliability: 76.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                  |
| html5lib       | 65.1 ms                                                               | 68.2 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 437 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 407 ms: 1.42x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 562 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 707 ms: 1.25x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 93.0 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                                  |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 360 us: 1.01x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 79.6 ms: 1.01x slower                                                   |
| json_loads           | 30.7 us                                                               | 33.3 us: 1.09x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.5 ms: 1.18x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                                   |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 437 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 407 ms: 1.42x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 562 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                    |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.27x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 39.3 us: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 707 ms: 1.25x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.39 us: 1.21x faster                                                   |
| raytrace                   | 353 ms                                                                | 299 ms: 1.18x faster                                                    |
| generators                 | 43.5 ms                                                               | 38.0 ms: 1.14x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.92 us: 1.10x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.64 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 128 ms: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.84 ms: 1.07x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.06x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.7 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                                   |
| sympy_str                  | 280 ms                                                                | 271 ms: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 150 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.8 ms: 1.03x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                                  |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                    |
| dask                       | 376 ms                                                                | 368 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.36 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 360 us: 1.01x faster                                                    |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 79.6 ms: 1.01x slower                                                   |
| float                      | 92.1 ms                                                               | 93.0 ms: 1.01x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 100 ms: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.13 ms: 1.02x slower                                                   |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.9 ms: 1.02x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.9 ms: 1.03x slower                                                   |
| sympy_expand               | 454 ms                                                                | 465 ms: 1.03x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 129 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                   |
| pyflate                    | 559 ms                                                                | 578 ms: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 969 us: 1.03x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.95 sec: 1.04x slower                                                  |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 952 ms: 1.04x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 64.6 ms: 1.04x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 592 ms: 1.05x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 68.2 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.53 ms: 1.05x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                   |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.3 us: 1.09x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 4.98 ms: 1.13x slower                                                   |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.5 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (12): pylint, xml_etree_iterparse, 2to3, meteor_contest, coroutines, tornado_http, sympy_integrate, bench_mp_pool, asyncio_websockets, async_generators, genshi_xml, xml_etree_generate
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: bpe_tokeniser

# HPT report

- Reliability score: 76.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x