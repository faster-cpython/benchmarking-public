# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-aarch64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.016x faster
- HPT reliability: 87.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 304 ms: 1.01x faster                                           |
| chameleon      | 8.81 ms                                                               | 8.94 ms: 1.01x slower                                          |
| docutils       | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                         |
| tornado_http   | 136 ms                                                                | 130 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 488 ms: 1.28x faster                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 603 ms: 1.23x faster                                           |
| async_tree_none_tg         | 577 ms                                                                | 470 ms: 1.23x faster                                           |
| async_tree_memoization     | 777 ms                                                                | 644 ms: 1.21x faster                                           |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 790 ms: 1.15x faster                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.5 ms: 1.01x faster                                          |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                           |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                           |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                          |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 251 us: 1.03x faster                                           |
| pickle_pure_python   | 365 us                                                                | 354 us: 1.03x faster                                           |
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                         |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                           |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                           |
| pickle_list          | 5.25 us                                                               | 5.33 us: 1.02x slower                                          |
| pickle_dict          | 37.3 us                                                               | 37.9 us: 1.02x slower                                          |
| pickle               | 13.4 us                                                               | 13.6 us: 1.02x slower                                          |
| json_loads           | 30.7 us                                                               | 31.4 us: 1.02x slower                                          |
| unpickle_list        | 6.17 us                                                               | 6.58 us: 1.07x slower                                          |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                          |
| unpickle             | 18.5 us                                                               | 20.3 us: 1.10x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                          |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                          |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                          |
| django_template | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 488 ms: 1.28x faster                                           |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                          |
| async_tree_memoization_tg  | 740 ms                                                                | 603 ms: 1.23x faster                                           |
| async_tree_none_tg         | 577 ms                                                                | 470 ms: 1.23x faster                                           |
| async_tree_memoization     | 777 ms                                                                | 644 ms: 1.21x faster                                           |
| raytrace                   | 353 ms                                                                | 300 ms: 1.18x faster                                           |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 790 ms: 1.15x faster                                           |
| mypy2                      | 873 ms                                                                | 761 ms: 1.15x faster                                           |
| generators                 | 43.5 ms                                                               | 38.0 ms: 1.15x faster                                          |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                         |
| logging_simple             | 7.63 us                                                               | 6.96 us: 1.10x faster                                          |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                           |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                          |
| logging_format             | 8.34 us                                                               | 7.76 us: 1.08x faster                                          |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                           |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                          |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                          |
| crypto_pyaes               | 86.6 ms                                                               | 82.2 ms: 1.05x faster                                          |
| sympy_str                  | 280 ms                                                                | 266 ms: 1.05x faster                                           |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                          |
| tornado_http               | 136 ms                                                                | 130 ms: 1.04x faster                                           |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                           |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.04x faster                                         |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.03x faster                                           |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                          |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                          |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                          |
| pickle_pure_python         | 365 us                                                                | 354 us: 1.03x faster                                           |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                          |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                         |
| pyflate                    | 559 ms                                                                | 550 ms: 1.02x faster                                           |
| async_generators           | 491 ms                                                                | 483 ms: 1.02x faster                                           |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                           |
| 2to3                       | 308 ms                                                                | 304 ms: 1.01x faster                                           |
| mdp                        | 3.41 sec                                                              | 3.38 sec: 1.01x faster                                         |
| float                      | 92.1 ms                                                               | 91.5 ms: 1.01x faster                                          |
| hexiom                     | 6.98 ms                                                               | 7.00 ms: 1.00x slower                                          |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                           |
| sympy_expand               | 454 ms                                                                | 456 ms: 1.01x slower                                           |
| coroutines                 | 29.0 ms                                                               | 29.2 ms: 1.01x slower                                          |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                           |
| json                       | 5.54 ms                                                               | 5.60 ms: 1.01x slower                                          |
| genshi_text                | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                          |
| chameleon                  | 8.81 ms                                                               | 8.94 ms: 1.01x slower                                          |
| pickle_list                | 5.25 us                                                               | 5.33 us: 1.02x slower                                          |
| pickle_dict                | 37.3 us                                                               | 37.9 us: 1.02x slower                                          |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                           |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.02x slower                                          |
| deepcopy                   | 446 us                                                                | 453 us: 1.02x slower                                           |
| richards_super             | 58.5 ms                                                               | 59.5 ms: 1.02x slower                                          |
| thrift                     | 937 us                                                                | 956 us: 1.02x slower                                           |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                         |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                           |
| sqlglot_optimize           | 61.3 ms                                                               | 62.6 ms: 1.02x slower                                          |
| sqlglot_normalize          | 126 ms                                                                | 129 ms: 1.02x slower                                           |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.02x slower                                         |
| json_loads                 | 30.7 us                                                               | 31.4 us: 1.02x slower                                          |
| pprint_safe_repr           | 916 ms                                                                | 942 ms: 1.03x slower                                           |
| sqlite_synth               | 3.77 us                                                               | 3.88 us: 1.03x slower                                          |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                          |
| fannkuch                   | 443 ms                                                                | 458 ms: 1.03x slower                                           |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                          |
| aiohttp                    | 1.16 ms                                                               | 1.20 ms: 1.03x slower                                          |
| deepcopy_memo              | 49.6 us                                                               | 51.4 us: 1.04x slower                                          |
| docutils                   | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                         |
| richards                   | 50.9 ms                                                               | 52.9 ms: 1.04x slower                                          |
| asyncio_tcp                | 566 ms                                                                | 592 ms: 1.05x slower                                           |
| django_template            | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                          |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                          |
| unpickle_list              | 6.17 us                                                               | 6.58 us: 1.07x slower                                          |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                           |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                           |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.67 ms: 1.08x slower                                          |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                           |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                           |
| gunicorn                   | 1.14 ms                                                               | 1.23 ms: 1.09x slower                                          |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                          |
| bench_mp_pool              | 7.05 ms                                                               | 7.75 ms: 1.10x slower                                          |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                          |
| unpickle                   | 18.5 us                                                               | 20.3 us: 1.10x slower                                          |
| spectral_norm              | 131 ms                                                                | 145 ms: 1.11x slower                                           |
| gc_traversal               | 4.40 ms                                                               | 4.92 ms: 1.12x slower                                          |
| coverage                   | 87.3 ms                                                               | 98.7 ms: 1.13x slower                                          |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                          |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                          |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (10): regex_dna, dask, nqueens, xml_etree_parse, deepcopy_reduce, asyncio_websockets, xml_etree_process, genshi_xml, pylint, html5lib
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: bpe_tokeniser, flaskblogging, unpack_sequence

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 87.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x