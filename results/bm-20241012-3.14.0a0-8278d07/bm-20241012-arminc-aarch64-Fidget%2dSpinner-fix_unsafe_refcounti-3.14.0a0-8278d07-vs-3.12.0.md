# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-aarch64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.039x faster
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 293 ms: 1.05x faster                                                              |
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                                            |
| html5lib       | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                             |
| tornado_http   | 136 ms                                                                | 126 ms: 1.07x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 422 ms: 1.48x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 551 ms: 1.41x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 709 ms: 1.29x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 710 ms: 1.24x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.13 sec: 1.24x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.22x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                              |
| float          | 92.1 ms                                                               | 93.9 ms: 1.02x slower                                                             |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                              |
| regex_effbot   | 4.64 ms                                                               | 4.97 ms: 1.07x slower                                                             |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                              |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                              |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                              |
| pickle_pure_python   | 365 us                                                                | 358 us: 1.02x faster                                                              |
| pickle               | 13.4 us                                                               | 13.6 us: 1.01x slower                                                             |
| json_loads           | 30.7 us                                                               | 31.2 us: 1.02x slower                                                             |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                            |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                                             |
| unpickle_list        | 6.17 us                                                               | 6.51 us: 1.05x slower                                                             |
| json_dumps           | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (4): pickle_list, xml_etree_process, xml_etree_generate, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                             |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                                             |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                             |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 422 ms: 1.48x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 551 ms: 1.41x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                              |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 709 ms: 1.29x faster                                                              |
| generators                 | 43.5 ms                                                               | 34.6 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 710 ms: 1.24x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.13 sec: 1.24x faster                                                            |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.22x faster                                                             |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.22x faster                                                            |
| deepcopy_reduce            | 4.10 us                                                               | 3.46 us: 1.19x faster                                                             |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.15x faster                                                             |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                              |
| raytrace                   | 353 ms                                                                | 312 ms: 1.13x faster                                                              |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                              |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.08x faster                                                              |
| logging_format             | 8.34 us                                                               | 7.72 us: 1.08x faster                                                             |
| tornado_http               | 136 ms                                                                | 126 ms: 1.07x faster                                                              |
| crypto_pyaes               | 86.6 ms                                                               | 81.4 ms: 1.06x faster                                                             |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                              |
| logging_simple             | 7.63 us                                                               | 7.19 us: 1.06x faster                                                             |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                             |
| 2to3                       | 308 ms                                                                | 293 ms: 1.05x faster                                                              |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 59.3 ms: 1.05x faster                                                             |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                             |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                                             |
| async_generators           | 491 ms                                                                | 475 ms: 1.03x faster                                                              |
| html5lib                   | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                             |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                              |
| chaos                      | 71.4 ms                                                               | 69.6 ms: 1.03x faster                                                             |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                            |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.02x faster                                                             |
| pickle_pure_python         | 365 us                                                                | 358 us: 1.02x faster                                                              |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                             |
| meteor_contest             | 112 ms                                                                | 110 ms: 1.01x faster                                                              |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.01x faster                                                            |
| thrift                     | 937 us                                                                | 926 us: 1.01x faster                                                              |
| pprint_safe_repr           | 916 ms                                                                | 908 ms: 1.01x faster                                                              |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.00x slower                                                            |
| hexiom                     | 6.98 ms                                                               | 7.03 ms: 1.01x slower                                                             |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.01x slower                                                             |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                              |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                              |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                                            |
| richards_super             | 58.5 ms                                                               | 59.4 ms: 1.02x slower                                                             |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.02x slower                                                             |
| json_loads                 | 30.7 us                                                               | 31.2 us: 1.02x slower                                                             |
| float                      | 92.1 ms                                                               | 93.9 ms: 1.02x slower                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                            |
| json                       | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                             |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                              |
| richards                   | 50.9 ms                                                               | 52.6 ms: 1.03x slower                                                             |
| scimark_fft                | 418 ms                                                                | 432 ms: 1.03x slower                                                              |
| pyflate                    | 559 ms                                                                | 580 ms: 1.04x slower                                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.44 ms: 1.04x slower                                                             |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                              |
| django_template            | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                                             |
| sqlite_synth               | 3.77 us                                                               | 3.95 us: 1.05x slower                                                             |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                                             |
| unpickle_list              | 6.17 us                                                               | 6.51 us: 1.05x slower                                                             |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                             |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                              |
| spectral_norm              | 131 ms                                                                | 139 ms: 1.07x slower                                                              |
| regex_effbot               | 4.64 ms                                                               | 4.97 ms: 1.07x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                                              |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                              |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.35 ms: 1.10x slower                                                             |
| coverage                   | 87.3 ms                                                               | 98.1 ms: 1.12x slower                                                             |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 5.22 ms: 1.19x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 2.39 ms: 1.24x slower                                                             |
| bench_mp_pool              | 7.05 ms                                                               | 5.94 sec: 841.75x slower                                                          |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                                      |

Benchmark hidden because not significant (13): asyncio_tcp, genshi_text, genshi_xml, pickle_list, pprint_pformat, xml_etree_process, regex_dna, asyncio_websockets, xml_etree_generate, nqueens, sympy_expand, pylint, pickle_dict
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.039x faster
# HPT report

- Reliability score: 99.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x