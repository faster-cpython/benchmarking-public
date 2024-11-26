# Results vs. 3.12.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.042x faster
- HPT reliability: 96.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 295 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.01x slower                                                  |
| tornado_http   | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 417 ms: 1.49x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 555 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 417 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 548 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 716 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 92.9 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 361 us: 1.01x faster                                                    |
| pickle               | 13.4 us                                                               | 13.6 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| pickle_dict          | 37.3 us                                                               | 38.3 us: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.5 us: 1.03x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.63 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, xml_etree_process, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.57 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 26.9 ms: 1.02x faster                                                   |
| django_template | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 417 ms: 1.49x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 555 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 417 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 548 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 334 us: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 716 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.48 us: 1.18x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 20.9 ms: 1.17x faster                                                   |
| raytrace                   | 353 ms                                                                | 303 ms: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.89 us: 1.11x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.56 us: 1.10x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 140 ms: 1.10x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| tornado_http               | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.08x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 58.9 ms: 1.05x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.4 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 295 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.7 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.2 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.3 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.9 ms: 1.02x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 556 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| async_generators           | 491 ms                                                                | 485 ms: 1.01x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 361 us: 1.01x faster                                                    |
| thrift                     | 937 us                                                                | 928 us: 1.01x faster                                                    |
| meteor_contest             | 112 ms                                                                | 111 ms: 1.00x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.89 sec: 1.01x slower                                                  |
| richards_super             | 58.5 ms                                                               | 58.9 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 923 ms: 1.01x slower                                                    |
| pyflate                    | 559 ms                                                                | 564 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 92.9 ms: 1.01x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 100 ms: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.01x slower                                                   |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.01x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.01x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.10 ms: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| django_template            | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.57 ms: 1.02x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.3 us: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.87 us: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.5 us: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.4 ms: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 458 ms: 1.03x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                   |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.56 ms: 1.06x slower                                                   |
| scimark_fft                | 418 ms                                                                | 443 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.63 us: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.08x slower                                                    |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.5 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.13 ms: 1.17x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.97 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (11): xml_etree_parse, genshi_xml, xml_etree_generate, asyncio_websockets, json, xml_etree_process, pickle_list, pylint, html5lib, bench_mp_pool, sqlglot_optimize
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.042x faster
# HPT report

- Reliability score: 96.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x