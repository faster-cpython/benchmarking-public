# Results vs. 3.12.0

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-aarch64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.03x faster
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                       |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                     |
| tornado_http   | 136 ms                                                                | 126 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 433 ms: 1.44x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 551 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.24x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 730 ms: 1.21x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.2 ms: 1.01x faster                                                      |
| nbody          | 105 ms                                                                | 109 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                       |
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                       |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                      |
| regex_v8       | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                       |
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                       |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                       |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                     |
| json_loads           | 30.7 us                                                               | 32.8 us: 1.07x slower                                                      |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                               |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                      |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.3 ms: 1.01x faster                                                      |
| django_template | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                      |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 433 ms: 1.44x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 551 ms: 1.34x faster                                                       |
| deepcopy                   | 446 us                                                                | 335 us: 1.33x faster                                                       |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                      |
| generators                 | 43.5 ms                                                               | 34.9 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.24x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                      |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 730 ms: 1.21x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                     |
| raytrace                   | 353 ms                                                                | 303 ms: 1.17x faster                                                       |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 4.10 us                                                               | 3.57 us: 1.15x faster                                                      |
| logging_simple             | 7.63 us                                                               | 6.98 us: 1.09x faster                                                      |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                       |
| logging_format             | 8.34 us                                                               | 7.68 us: 1.09x faster                                                      |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                       |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                       |
| tornado_http               | 136 ms                                                                | 126 ms: 1.07x faster                                                       |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.07x faster                                                      |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                      |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.06x faster                                                       |
| crypto_pyaes               | 86.6 ms                                                               | 82.5 ms: 1.05x faster                                                      |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                      |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                      |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                       |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                      |
| chaos                      | 71.4 ms                                                               | 68.8 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.0 ms: 1.04x faster                                                      |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                       |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                       |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                     |
| async_generators           | 491 ms                                                                | 483 ms: 1.02x faster                                                       |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                      |
| meteor_contest             | 112 ms                                                                | 110 ms: 1.01x faster                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 6.96 ms: 1.01x faster                                                      |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                       |
| float                      | 92.1 ms                                                               | 91.2 ms: 1.01x faster                                                      |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                       |
| genshi_text                | 27.4 ms                                                               | 27.3 ms: 1.01x faster                                                      |
| hexiom                     | 6.98 ms                                                               | 6.97 ms: 1.00x faster                                                      |
| sympy_expand               | 454 ms                                                                | 458 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 916 ms                                                                | 927 ms: 1.01x slower                                                       |
| richards_super             | 58.5 ms                                                               | 59.2 ms: 1.01x slower                                                      |
| asyncio_tcp                | 566 ms                                                                | 573 ms: 1.01x slower                                                       |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.03x slower                                                     |
| django_template            | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                      |
| json                       | 5.54 ms                                                               | 5.70 ms: 1.03x slower                                                      |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                       |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                      |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                       |
| richards                   | 50.9 ms                                                               | 52.8 ms: 1.04x slower                                                      |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.48 ms: 1.05x slower                                                      |
| nbody                      | 105 ms                                                                | 109 ms: 1.05x slower                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                      |
| regex_v8                   | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                      |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                                       |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                      |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                       |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                       |
| gc_traversal               | 4.40 ms                                                               | 4.98 ms: 1.13x slower                                                      |
| coverage                   | 87.3 ms                                                               | 99.2 ms: 1.14x slower                                                      |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                      |
| telco                      | 8.51 ms                                                               | 9.97 ms: 1.17x slower                                                      |
| create_gc_cycles           | 1.92 ms                                                               | 2.26 ms: 1.18x slower                                                      |
| go                         | 157 ms                                                                | 191 ms: 1.22x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                               |

Benchmark hidden because not significant (13): genshi_xml, pprint_pformat, asyncio_websockets, pyflate, pickle_pure_python, sqlglot_normalize, thrift, xml_etree_process, pidigits, nqueens, pylint, sqlglot_optimize, html5lib
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240824-3.14.0a0-bf9cfa8/bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8.json: bpe_tokeniser

# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x