# Results vs. 3.12.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-aarch64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.03x faster
- HPT reliability: 89.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                  |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 421 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 562 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 720 ms: 1.27x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 92.9 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 110 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 191 ms: 1.02x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.20 us: 1.01x faster                                                   |
| pickle_dict          | 37.3 us                                                               | 38.0 us: 1.02x slower                                                   |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 373 us: 1.02x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 81.6 ms: 1.03x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.40 us: 1.04x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                                   |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 421 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 562 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 553 ms: 1.34x faster                                                    |
| deepcopy                   | 446 us                                                                | 337 us: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.5 us: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 720 ms: 1.27x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.9 ms: 1.25x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| raytrace                   | 353 ms                                                                | 301 ms: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.1 ms: 1.16x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.57 us: 1.15x faster                                                   |
| go                         | 157 ms                                                                | 139 ms: 1.13x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.87 ms: 1.06x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.18 us: 1.06x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.90 us: 1.06x faster                                                   |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.75 ms: 1.05x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.2 ms: 1.05x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.1 ms: 1.04x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                                    |
| async_generators           | 491 ms                                                                | 479 ms: 1.02x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 191 ms: 1.02x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| mdp                        | 3.41 sec                                                              | 3.37 sec: 1.01x faster                                                  |
| pickle_list                | 5.25 us                                                               | 5.20 us: 1.01x faster                                                   |
| nqueens                    | 99.2 ms                                                               | 98.4 ms: 1.01x faster                                                   |
| thrift                     | 937 us                                                                | 931 us: 1.01x faster                                                    |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| json                       | 5.54 ms                                                               | 5.59 ms: 1.01x slower                                                   |
| float                      | 92.1 ms                                                               | 92.9 ms: 1.01x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.81 us: 1.01x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 926 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.01x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 38.0 us: 1.02x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.4 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 373 us: 1.02x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.17 ms: 1.03x slower                                                   |
| richards_super             | 58.5 ms                                                               | 60.1 ms: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 81.6 ms: 1.03x slower                                                   |
| pyflate                    | 559 ms                                                                | 580 ms: 1.04x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.40 us: 1.04x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.8 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 462 ms: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.47 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| nbody                      | 105 ms                                                                | 110 ms: 1.06x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 192 us: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.6 ms: 1.12x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.09 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.27 ms: 1.18x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.2 ms: 1.20x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (13): sqlglot_parse, xml_etree_iterparse, coroutines, genshi_xml, genshi_text, meteor_contest, asyncio_tcp, xml_etree_generate, regex_dna, asyncio_websockets, bench_mp_pool, html5lib, pylint
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 89.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x