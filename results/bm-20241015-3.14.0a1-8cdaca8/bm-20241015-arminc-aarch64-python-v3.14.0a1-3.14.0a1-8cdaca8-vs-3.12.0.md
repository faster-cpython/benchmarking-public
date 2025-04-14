# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.029x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 293 ms: 1.05x faster                                         |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                       |
| tornado_http   | 136 ms                                                                | 125 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 438 ms: 1.42x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 538 ms: 1.38x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 447 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 743 ms: 1.23x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 724 ms: 1.22x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.21 sec: 1.16x faster                                       |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| float          | 92.1 ms                                                               | 95.4 ms: 1.04x slower                                        |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                         |
| regex_dna      | 254 ms                                                                | 243 ms: 1.04x faster                                         |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                        |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 191 ms: 1.02x faster                                         |
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                         |
| pickle_list          | 5.25 us                                                               | 5.22 us: 1.00x faster                                        |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                        |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                       |
| json_loads           | 30.7 us                                                               | 31.2 us: 1.02x slower                                        |
| xml_etree_process    | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                        |
| unpickle             | 18.5 us                                                               | 19.1 us: 1.04x slower                                        |
| pickle               | 13.4 us                                                               | 13.9 us: 1.04x slower                                        |
| unpickle_list        | 6.17 us                                                               | 6.60 us: 1.07x slower                                        |
| json_dumps           | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                        |
| python_startup         | 11.4 ms                                                               | 14.5 ms: 1.28x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.15x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 61.6 ms: 1.02x slower                                        |
| django_template | 40.7 ms                                                               | 42.1 ms: 1.04x slower                                        |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 438 ms: 1.42x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 538 ms: 1.38x faster                                         |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                         |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                        |
| async_tree_none_tg         | 577 ms                                                                | 447 ms: 1.29x faster                                         |
| generators                 | 43.5 ms                                                               | 34.8 ms: 1.25x faster                                        |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 743 ms: 1.23x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 724 ms: 1.22x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.21 sec: 1.16x faster                                       |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                        |
| go                         | 157 ms                                                                | 136 ms: 1.16x faster                                         |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                        |
| raytrace                   | 353 ms                                                                | 311 ms: 1.14x faster                                         |
| logging_simple             | 7.63 us                                                               | 6.82 us: 1.12x faster                                        |
| sympy_sum                  | 154 ms                                                                | 138 ms: 1.12x faster                                         |
| logging_format             | 8.34 us                                                               | 7.51 us: 1.11x faster                                        |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                         |
| scimark_lu                 | 146 ms                                                                | 133 ms: 1.10x faster                                         |
| dulwich_log                | 62.0 ms                                                               | 57.0 ms: 1.09x faster                                        |
| tornado_http               | 136 ms                                                                | 125 ms: 1.08x faster                                         |
| sympy_str                  | 280 ms                                                                | 261 ms: 1.07x faster                                         |
| crypto_pyaes               | 86.6 ms                                                               | 80.9 ms: 1.07x faster                                        |
| 2to3                       | 308 ms                                                                | 293 ms: 1.05x faster                                         |
| regex_dna                  | 254 ms                                                                | 243 ms: 1.04x faster                                         |
| deltablue                  | 4.12 ms                                                               | 3.95 ms: 1.04x faster                                        |
| sqlglot_transpile          | 1.83 ms                                                               | 1.75 ms: 1.04x faster                                        |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                        |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.04x faster                                       |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                        |
| chaos                      | 71.4 ms                                                               | 69.3 ms: 1.03x faster                                        |
| async_generators           | 491 ms                                                                | 479 ms: 1.02x faster                                         |
| asyncio_tcp                | 566 ms                                                                | 554 ms: 1.02x faster                                         |
| xml_etree_parse            | 195 ms                                                                | 191 ms: 1.02x faster                                         |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                         |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                       |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.7 ms: 1.02x faster                                        |
| json                       | 5.54 ms                                                               | 5.46 ms: 1.01x faster                                        |
| meteor_contest             | 112 ms                                                                | 110 ms: 1.01x faster                                         |
| pprint_safe_repr           | 916 ms                                                                | 909 ms: 1.01x faster                                         |
| pprint_pformat             | 1.88 sec                                                              | 1.87 sec: 1.01x faster                                       |
| pickle_list                | 5.25 us                                                               | 5.22 us: 1.00x faster                                        |
| hexiom                     | 6.98 ms                                                               | 6.97 ms: 1.00x faster                                        |
| sqlglot_normalize          | 126 ms                                                                | 126 ms: 1.00x slower                                         |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                       |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| sqlglot_optimize           | 61.3 ms                                                               | 61.8 ms: 1.01x slower                                        |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                        |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                       |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                       |
| json_loads                 | 30.7 us                                                               | 31.2 us: 1.02x slower                                        |
| genshi_xml                 | 60.6 ms                                                               | 61.6 ms: 1.02x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                        |
| sqlite_synth               | 3.77 us                                                               | 3.86 us: 1.02x slower                                        |
| richards_super             | 58.5 ms                                                               | 60.0 ms: 1.03x slower                                        |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                        |
| scimark_fft                | 418 ms                                                                | 433 ms: 1.03x slower                                         |
| django_template            | 40.7 ms                                                               | 42.1 ms: 1.04x slower                                        |
| unpickle                   | 18.5 us                                                               | 19.1 us: 1.04x slower                                        |
| pickle                     | 13.4 us                                                               | 13.9 us: 1.04x slower                                        |
| float                      | 92.1 ms                                                               | 95.4 ms: 1.04x slower                                        |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                         |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.46 ms: 1.04x slower                                        |
| pyflate                    | 559 ms                                                                | 585 ms: 1.05x slower                                         |
| richards                   | 50.9 ms                                                               | 53.4 ms: 1.05x slower                                        |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                         |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                        |
| fannkuch                   | 443 ms                                                                | 469 ms: 1.06x slower                                         |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                        |
| unpickle_list              | 6.17 us                                                               | 6.60 us: 1.07x slower                                        |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                         |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.08x slower                                         |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                         |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                        |
| coverage                   | 87.3 ms                                                               | 97.6 ms: 1.12x slower                                        |
| telco                      | 8.51 ms                                                               | 9.54 ms: 1.12x slower                                        |
| json_dumps                 | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                        |
| python_startup             | 11.4 ms                                                               | 14.5 ms: 1.28x slower                                        |
| gc_traversal               | 4.40 ms                                                               | 6.25 ms: 1.42x slower                                        |
| create_gc_cycles           | 1.92 ms                                                               | 3.67 ms: 1.92x slower                                        |
| bench_mp_pool              | 7.05 ms                                                               | 4.94 sec: 700.52x slower                                     |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                 |

Benchmark hidden because not significant (12): coroutines, nqueens, thrift, html5lib, xml_etree_iterparse, bench_thread_pool, pylint, asyncio_websockets, pickle_pure_python, genshi_text, sympy_expand, xml_etree_generate
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x