# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.03x faster
- HPT reliability: 97.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                  |
| html5lib       | 65.1 ms                                                               | 66.6 ms: 1.02x slower                                                   |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 397 ms: 1.45x faster                                                    |
| async_tree_none            | 624 ms                                                                | 434 ms: 1.44x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 552 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 531 ms: 1.39x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.10 sec: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 702 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 255 ms: 1.01x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                  |
| pickle_pure_python   | 365 us                                                                | 357 us: 1.02x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 33.0 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.90 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.4 ms: 1.18x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 397 ms: 1.45x faster                                                    |
| async_tree_none            | 624 ms                                                                | 434 ms: 1.44x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 552 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 531 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.1 us: 1.30x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.10 sec: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 702 ms: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.38 us: 1.21x faster                                                   |
| raytrace                   | 353 ms                                                                | 294 ms: 1.20x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.97 us: 1.10x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.81 ms: 1.08x faster                                                   |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.73 us: 1.08x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 82.1 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                                   |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.5 ms: 1.04x faster                                                   |
| sympy_str                  | 280 ms                                                                | 269 ms: 1.04x faster                                                    |
| dask                       | 376 ms                                                                | 362 ms: 1.04x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                                  |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 357 us: 1.02x faster                                                    |
| nqueens                    | 99.2 ms                                                               | 97.8 ms: 1.01x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.7 ms: 1.01x faster                                                   |
| async_generators           | 491 ms                                                                | 487 ms: 1.01x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 61.5 ms: 1.00x slower                                                   |
| regex_dna                  | 254 ms                                                                | 255 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.04 ms: 1.01x slower                                                   |
| go                         | 157 ms                                                                | 159 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.01x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 576 ms: 1.02x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                   |
| richards                   | 50.9 ms                                                               | 51.9 ms: 1.02x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                                   |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.33 ms: 1.02x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 66.6 ms: 1.02x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 941 ms: 1.03x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.74 ms: 1.04x slower                                                   |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| pyflate                    | 559 ms                                                                | 582 ms: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| thrift                     | 937 us                                                                | 979 us: 1.05x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                  |
| scimark_fft                | 418 ms                                                                | 440 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 467 ms: 1.05x slower                                                    |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.90 ms: 1.06x slower                                                   |
| spectral_norm              | 131 ms                                                                | 139 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.0 us: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.0 ms: 1.12x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.98 ms: 1.13x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.86 ms: 1.16x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.4 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.37 ms: 1.23x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (10): sqlglot_parse, 2to3, richards_super, asyncio_websockets, xml_etree_iterparse, meteor_contest, pylint, bench_mp_pool, genshi_xml, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: bpe_tokeniser

# HPT report

- Reliability score: 97.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x