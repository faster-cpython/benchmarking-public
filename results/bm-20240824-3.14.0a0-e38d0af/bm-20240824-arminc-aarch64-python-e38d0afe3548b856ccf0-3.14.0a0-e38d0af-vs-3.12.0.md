# Results vs. 3.12.0

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-aarch64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.034x faster
- HPT reliability: 86.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 295 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.06 sec: 1.02x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.0 ms: 1.03x slower                                                   |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 427 ms: 1.46x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 729 ms: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 731 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 109 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.83 ms: 1.04x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 42.1 ms: 1.04x slower                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 427 ms: 1.46x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 729 ms: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.2 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 731 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| raytrace                   | 353 ms                                                                | 303 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.54 us: 1.16x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.96 us: 1.10x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.74 us: 1.08x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                   |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.75 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 295 ms: 1.05x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 83.1 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.6 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.43 ms: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                   |
| async_generators           | 491 ms                                                                | 485 ms: 1.01x faster                                                    |
| pyflate                    | 559 ms                                                                | 562 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 100 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.02x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.4 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.10 ms: 1.02x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 936 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.02x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.06 sec: 1.02x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 67.0 ms: 1.03x slower                                                   |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.1 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.44 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.83 ms: 1.04x slower                                                   |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| nbody                      | 105 ms                                                                | 109 ms: 1.05x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.3 ms: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.89 ms: 1.11x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.9 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.84 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.20x slower                                                   |
| go                         | 157 ms                                                                | 192 ms: 1.22x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (14): xml_etree_iterparse, pycparser, thrift, pickle_pure_python, xml_etree_generate, float, meteor_contest, genshi_xml, asyncio_websockets, bench_mp_pool, asyncio_tcp, xml_etree_process, pylint, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240824-3.14.0a0-e38d0af/bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 86.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x