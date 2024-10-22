# Results vs. 3.12.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-aarch64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.03x faster
- HPT reliability: 96.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                |
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                              |
| tornado_http   | 136 ms                                                                | 126 ms: 1.08x faster                                                |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                        |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 427 ms: 1.46x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.38x faster                                                |
| async_tree_memoization     | 777 ms                                                                | 562 ms: 1.38x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 734 ms: 1.24x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                              |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                |
| float          | 92.1 ms                                                               | 94.2 ms: 1.02x slower                                               |
| nbody          | 105 ms                                                                | 109 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                |
| regex_effbot   | 4.64 ms                                                               | 5.01 ms: 1.08x slower                                               |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                |
| pickle_list          | 5.25 us                                                               | 5.19 us: 1.01x faster                                               |
| pickle_pure_python   | 365 us                                                                | 368 us: 1.01x slower                                                |
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                              |
| pickle_dict          | 37.3 us                                                               | 37.9 us: 1.01x slower                                               |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                               |
| json_loads           | 30.7 us                                                               | 31.4 us: 1.02x slower                                               |
| unpickle_list        | 6.17 us                                                               | 6.38 us: 1.03x slower                                               |
| unpickle             | 18.5 us                                                               | 19.3 us: 1.05x slower                                               |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.65 ms: 1.03x slower                                               |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                               |
| django_template | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                        |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 427 ms: 1.46x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.38x faster                                                |
| async_tree_memoization     | 777 ms                                                                | 562 ms: 1.38x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                |
| deepcopy_memo              | 49.6 us                                                               | 37.3 us: 1.33x faster                                               |
| deepcopy                   | 446 us                                                                | 337 us: 1.32x faster                                                |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                               |
| generators                 | 43.5 ms                                                               | 34.8 ms: 1.25x faster                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 734 ms: 1.24x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                              |
| pathlib                    | 24.5 ms                                                               | 20.9 ms: 1.17x faster                                               |
| raytrace                   | 353 ms                                                                | 301 ms: 1.17x faster                                                |
| deepcopy_reduce            | 4.10 us                                                               | 3.57 us: 1.15x faster                                               |
| go                         | 157 ms                                                                | 137 ms: 1.15x faster                                                |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.09x faster                                                |
| logging_format             | 8.34 us                                                               | 7.72 us: 1.08x faster                                               |
| tornado_http               | 136 ms                                                                | 126 ms: 1.08x faster                                                |
| logging_simple             | 7.63 us                                                               | 7.15 us: 1.07x faster                                               |
| dulwich_log                | 62.0 ms                                                               | 58.4 ms: 1.06x faster                                               |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                               |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                               |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.7 ms: 1.05x faster                                               |
| sympy_integrate            | 21.6 ms                                                               | 20.5 ms: 1.05x faster                                               |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                               |
| chaos                      | 71.4 ms                                                               | 68.1 ms: 1.05x faster                                               |
| crypto_pyaes               | 86.6 ms                                                               | 82.9 ms: 1.04x faster                                               |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                               |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.03x faster                                              |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                              |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                               |
| async_generators           | 491 ms                                                                | 482 ms: 1.02x faster                                                |
| pickle_list                | 5.25 us                                                               | 5.19 us: 1.01x faster                                               |
| pickle_pure_python         | 365 us                                                                | 368 us: 1.01x slower                                                |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                              |
| pprint_safe_repr           | 916 ms                                                                | 923 ms: 1.01x slower                                                |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                              |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.01x slower                                              |
| pickle_dict                | 37.3 us                                                               | 37.9 us: 1.01x slower                                               |
| sqlite_synth               | 3.77 us                                                               | 3.82 us: 1.01x slower                                               |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.02x slower                                                |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                              |
| richards_super             | 58.5 ms                                                               | 59.5 ms: 1.02x slower                                               |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                               |
| float                      | 92.1 ms                                                               | 94.2 ms: 1.02x slower                                               |
| json_loads                 | 30.7 us                                                               | 31.4 us: 1.02x slower                                               |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.39 ms: 1.03x slower                                               |
| unpickle_list              | 6.17 us                                                               | 6.38 us: 1.03x slower                                               |
| python_startup_no_site     | 8.37 ms                                                               | 8.65 ms: 1.03x slower                                               |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                               |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.03x slower                                               |
| pyflate                    | 559 ms                                                                | 579 ms: 1.04x slower                                                |
| logging_silent             | 127 ns                                                                | 131 ns: 1.04x slower                                                |
| nbody                      | 105 ms                                                                | 109 ms: 1.04x slower                                                |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                                |
| unpickle                   | 18.5 us                                                               | 19.3 us: 1.05x slower                                               |
| django_template            | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                               |
| scimark_fft                | 418 ms                                                                | 440 ms: 1.05x slower                                                |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                |
| regex_effbot               | 4.64 ms                                                               | 5.01 ms: 1.08x slower                                               |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                               |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                               |
| coverage                   | 87.3 ms                                                               | 97.0 ms: 1.11x slower                                               |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                               |
| gc_traversal               | 4.40 ms                                                               | 5.13 ms: 1.17x slower                                               |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                               |
| create_gc_cycles           | 1.92 ms                                                               | 2.37 ms: 1.24x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                        |

Benchmark hidden because not significant (18): xml_etree_parse, genshi_xml, regex_dna, meteor_contest, asyncio_tcp, json, asyncio_websockets, xml_etree_process, xml_etree_generate, html5lib, thrift, genshi_text, bench_mp_pool, xml_etree_iterparse, hexiom, pylint, sqlglot_optimize, sqlglot_normalize
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 96.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x