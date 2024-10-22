# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.04x slower
- HPT reliability: 97.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 424 ms: 1.47x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 412 ms: 1.40x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 555 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 552 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 721 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.22x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 93.0 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 259 ms: 1.02x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.99 ms: 1.08x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.27 us: 1.00x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 31.2 us: 1.02x slower                                                   |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.05x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_pure_python, pickle_dict, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 42.2 ms: 1.04x slower                                                   |
| mako            | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 424 ms: 1.47x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 412 ms: 1.40x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 555 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 552 ms: 1.34x faster                                                    |
| deepcopy                   | 446 us                                                                | 335 us: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.1 us: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 721 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.22x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.16x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                   |
| raytrace                   | 353 ms                                                                | 305 ms: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 140 ms: 1.10x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 133 ms: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.72 us: 1.08x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.11 us: 1.07x faster                                                   |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 58.6 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.92 ms: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                                   |
| async_generators           | 491 ms                                                                | 476 ms: 1.03x faster                                                    |
| chaos                      | 71.4 ms                                                               | 69.4 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.8 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                  |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| thrift                     | 937 us                                                                | 920 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| nqueens                    | 99.2 ms                                                               | 98.0 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 907 ms: 1.01x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.27 us: 1.00x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.00x slower                                                  |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                  |
| float                      | 92.1 ms                                                               | 93.0 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.81 us: 1.01x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.3 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.02x slower                                                  |
| json_loads                 | 30.7 us                                                               | 31.2 us: 1.02x slower                                                   |
| regex_dna                  | 254 ms                                                                | 259 ms: 1.02x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                                   |
| scimark_fft                | 418 ms                                                                | 427 ms: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| logging_silent             | 127 ns                                                                | 130 ns: 1.02x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.37 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                   |
| pyflate                    | 559 ms                                                                | 579 ms: 1.04x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.2 ms: 1.04x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                   |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 468 ms: 1.05x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.05x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.99 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.45 ms: 1.11x slower                                                   |
| python_startup             | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.3 ms: 1.14x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.02 ms: 1.14x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 4.42 sec: 627.18x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (17): sqlglot_parse, xml_etree_iterparse, asyncio_tcp, pickle_pure_python, bench_thread_pool, html5lib, pylint, json, genshi_xml, pickle_dict, pprint_pformat, xml_etree_generate, meteor_contest, asyncio_websockets, genshi_text, xml_etree_process, sqlglot_optimize
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 97.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x