# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.038x faster
- HPT reliability: 97.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                           |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                         |
| tornado_http   | 136 ms                                                                | 126 ms: 1.07x faster                                           |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 417 ms: 1.49x faster                                           |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                           |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.37x faster                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 552 ms: 1.34x faster                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 736 ms: 1.24x faster                                           |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 721 ms: 1.23x faster                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                           |
| float          | 92.1 ms                                                               | 94.9 ms: 1.03x slower                                          |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                           |
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                           |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                          |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                           |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                           |
| pickle_pure_python   | 365 us                                                                | 360 us: 1.01x faster                                           |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                           |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                          |
| xml_etree_process    | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                          |
| pickle               | 13.4 us                                                               | 13.6 us: 1.01x slower                                          |
| tomli_loads          | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                         |
| json_loads           | 30.7 us                                                               | 31.8 us: 1.04x slower                                          |
| unpickle_list        | 6.17 us                                                               | 6.42 us: 1.04x slower                                          |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                          |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (2): pickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                          |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                          |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                   |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 417 ms: 1.49x faster                                           |
| async_tree_memoization     | 777 ms                                                                | 553 ms: 1.40x faster                                           |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.37x faster                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 552 ms: 1.34x faster                                           |
| deepcopy                   | 446 us                                                                | 335 us: 1.33x faster                                           |
| deepcopy_memo              | 49.6 us                                                               | 39.2 us: 1.27x faster                                          |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 736 ms: 1.24x faster                                           |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                          |
| generators                 | 43.5 ms                                                               | 35.4 ms: 1.23x faster                                          |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 721 ms: 1.23x faster                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                         |
| raytrace                   | 353 ms                                                                | 302 ms: 1.17x faster                                           |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.15x faster                                          |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.15x faster                                          |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                           |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                           |
| logging_format             | 8.34 us                                                               | 7.71 us: 1.08x faster                                          |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                           |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                           |
| logging_simple             | 7.63 us                                                               | 7.11 us: 1.07x faster                                          |
| tornado_http               | 136 ms                                                                | 126 ms: 1.07x faster                                           |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                          |
| crypto_pyaes               | 86.6 ms                                                               | 82.4 ms: 1.05x faster                                          |
| dulwich_log                | 62.0 ms                                                               | 59.1 ms: 1.05x faster                                          |
| deltablue                  | 4.12 ms                                                               | 3.94 ms: 1.05x faster                                          |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                           |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                           |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                           |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.0 ms: 1.04x faster                                          |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                          |
| bench_thread_pool          | 1.31 ms                                                               | 1.26 ms: 1.04x faster                                          |
| chaos                      | 71.4 ms                                                               | 69.2 ms: 1.03x faster                                          |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                          |
| async_generators           | 491 ms                                                                | 480 ms: 1.02x faster                                           |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                           |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                         |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.02x faster                                         |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                           |
| pickle_pure_python         | 365 us                                                                | 360 us: 1.01x faster                                           |
| thrift                     | 937 us                                                                | 926 us: 1.01x faster                                           |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                           |
| pprint_safe_repr           | 916 ms                                                                | 911 ms: 1.01x faster                                           |
| pyflate                    | 559 ms                                                                | 563 ms: 1.01x slower                                           |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                           |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                          |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                         |
| xml_etree_process          | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                          |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.01x slower                                          |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.01x slower                                           |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.01x slower                                           |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.02x slower                                          |
| richards_super             | 58.5 ms                                                               | 59.4 ms: 1.02x slower                                          |
| json                       | 5.54 ms                                                               | 5.68 ms: 1.03x slower                                          |
| tomli_loads                | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                         |
| sqlite_synth               | 3.77 us                                                               | 3.88 us: 1.03x slower                                          |
| hexiom                     | 6.98 ms                                                               | 7.18 ms: 1.03x slower                                          |
| django_template            | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                          |
| float                      | 92.1 ms                                                               | 94.9 ms: 1.03x slower                                          |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                          |
| richards                   | 50.9 ms                                                               | 52.8 ms: 1.04x slower                                          |
| json_loads                 | 30.7 us                                                               | 31.8 us: 1.04x slower                                          |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                          |
| unpickle_list              | 6.17 us                                                               | 6.42 us: 1.04x slower                                          |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.45 ms: 1.04x slower                                          |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                           |
| fannkuch                   | 443 ms                                                                | 465 ms: 1.05x slower                                           |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                          |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                           |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                           |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                          |
| typing_runtime_protocols   | 181 us                                                                | 192 us: 1.06x slower                                           |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                          |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                           |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                          |
| coverage                   | 87.3 ms                                                               | 97.9 ms: 1.12x slower                                          |
| gc_traversal               | 4.40 ms                                                               | 5.04 ms: 1.15x slower                                          |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                          |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                          |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                   |

Benchmark hidden because not significant (13): asyncio_tcp, html5lib, coroutines, pickle_list, xml_etree_generate, pprint_pformat, nqueens, genshi_text, sqlglot_normalize, asyncio_websockets, bench_mp_pool, genshi_xml, pylint
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.038x faster
# HPT report

- Reliability score: 97.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x