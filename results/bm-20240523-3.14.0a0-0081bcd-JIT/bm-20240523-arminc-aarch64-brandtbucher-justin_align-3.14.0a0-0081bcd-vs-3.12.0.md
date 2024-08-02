# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_align
- machine: linux-aarch64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 353 ms: 1.15x slower                                                  |
| chameleon      | 8.81 ms                                                               | 9.09 ms: 1.03x slower                                                 |
| docutils       | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                |
| html5lib       | 65.1 ms                                                               | 70.4 ms: 1.08x slower                                                 |
| tornado_http   | 136 ms                                                                | 138 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 509 ms: 1.23x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 485 ms: 1.19x faster                                                  |
| async_tree_memoization_tg  | 740 ms                                                                | 628 ms: 1.18x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.22 sec: 1.15x faster                                                |
| async_tree_memoization     | 777 ms                                                                | 676 ms: 1.15x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.26 sec: 1.12x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 831 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 807 ms: 1.10x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.15x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.0 ms: 1.01x faster                                                 |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                  |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                  |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                 |
| regex_v8       | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                 |
| regex_compile  | 137 ms                                                                | 165 ms: 1.20x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 110 ms: 1.02x faster                                                  |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                |
| pickle               | 13.4 us                                                               | 13.6 us: 1.02x slower                                                 |
| unpickle_list        | 6.17 us                                                               | 6.35 us: 1.03x slower                                                 |
| unpickle_pure_python | 260 us                                                                | 272 us: 1.05x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                                 |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                 |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                 |
| pickle_pure_python   | 365 us                                                                | 403 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                          |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_iterparse, pickle_list, pickle_dict, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.9 ms: 1.30x slower                                                 |
| python_startup         | 11.4 ms                                                               | 14.9 ms: 1.31x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 12.6 ms: 1.02x faster                                                 |
| genshi_text     | 27.4 ms                                                               | 33.2 ms: 1.21x slower                                                 |
| django_template | 40.7 ms                                                               | 49.3 ms: 1.21x slower                                                 |
| genshi_xml      | 60.6 ms                                                               | 80.0 ms: 1.32x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.17x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 509 ms: 1.23x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 485 ms: 1.19x faster                                                  |
| async_tree_memoization_tg  | 740 ms                                                                | 628 ms: 1.18x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.22 sec: 1.15x faster                                                |
| async_tree_memoization     | 777 ms                                                                | 676 ms: 1.15x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                 |
| generators                 | 43.5 ms                                                               | 38.5 ms: 1.13x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 1.26 sec: 1.12x faster                                                |
| comprehensions             | 25.4 us                                                               | 23.0 us: 1.10x faster                                                 |
| raytrace                   | 353 ms                                                                | 321 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 831 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 807 ms: 1.10x faster                                                  |
| logging_simple             | 7.63 us                                                               | 7.22 us: 1.06x faster                                                 |
| logging_format             | 8.34 us                                                               | 7.89 us: 1.06x faster                                                 |
| mako                       | 12.9 ms                                                               | 12.6 ms: 1.02x faster                                                 |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 48.7 us: 1.02x faster                                                 |
| fannkuch                   | 443 ms                                                                | 437 ms: 1.01x faster                                                  |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                  |
| float                      | 92.1 ms                                                               | 91.0 ms: 1.01x faster                                                 |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                 |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                                |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                  |
| json                       | 5.54 ms                                                               | 5.62 ms: 1.01x slower                                                 |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.02x slower                                                 |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                                 |
| tornado_http               | 136 ms                                                                | 138 ms: 1.02x slower                                                  |
| unpickle_list              | 6.17 us                                                               | 6.35 us: 1.03x slower                                                 |
| richards_super             | 58.5 ms                                                               | 60.2 ms: 1.03x slower                                                 |
| chameleon                  | 8.81 ms                                                               | 9.09 ms: 1.03x slower                                                 |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.03x slower                                                 |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                  |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                                  |
| thrift                     | 937 us                                                                | 975 us: 1.04x slower                                                  |
| dask                       | 376 ms                                                                | 393 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 260 us                                                                | 272 us: 1.05x slower                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                                |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                 |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                 |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                 |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.0 ms: 1.06x slower                                                 |
| regex_v8                   | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                 |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                                |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                 |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                  |
| sqlglot_parse              | 1.46 ms                                                               | 1.58 ms: 1.08x slower                                                 |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                  |
| scimark_fft                | 418 ms                                                                | 451 ms: 1.08x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 70.4 ms: 1.08x slower                                                 |
| pyflate                    | 559 ms                                                                | 613 ms: 1.10x slower                                                  |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.10x slower                                                  |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                 |
| pickle_pure_python         | 365 us                                                                | 403 us: 1.10x slower                                                  |
| deepcopy                   | 446 us                                                                | 492 us: 1.10x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.87 ms: 1.11x slower                                                 |
| deltablue                  | 4.12 ms                                                               | 4.57 ms: 1.11x slower                                                 |
| asyncio_tcp                | 566 ms                                                                | 629 ms: 1.11x slower                                                  |
| go                         | 157 ms                                                                | 176 ms: 1.12x slower                                                  |
| sympy_str                  | 280 ms                                                                | 313 ms: 1.12x slower                                                  |
| dulwich_log                | 62.0 ms                                                               | 69.5 ms: 1.12x slower                                                 |
| sqlglot_optimize           | 61.3 ms                                                               | 68.9 ms: 1.12x slower                                                 |
| deepcopy_reduce            | 4.10 us                                                               | 4.61 us: 1.12x slower                                                 |
| typing_runtime_protocols   | 181 us                                                                | 204 us: 1.13x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                  |
| 2to3                       | 308 ms                                                                | 353 ms: 1.15x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 114 ms: 1.15x slower                                                  |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                  |
| telco                      | 8.51 ms                                                               | 9.90 ms: 1.16x slower                                                 |
| sympy_sum                  | 154 ms                                                                | 181 ms: 1.17x slower                                                  |
| pylint                     | 355 ms                                                                | 415 ms: 1.17x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.07 sec: 1.17x slower                                                |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                  |
| sympy_expand               | 454 ms                                                                | 532 ms: 1.17x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 8.28 ms: 1.17x slower                                                 |
| pprint_pformat             | 1.88 sec                                                              | 2.22 sec: 1.18x slower                                                |
| docutils                   | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                |
| sympy_integrate            | 21.6 ms                                                               | 25.6 ms: 1.19x slower                                                 |
| chaos                      | 71.4 ms                                                               | 85.6 ms: 1.20x slower                                                 |
| gc_traversal               | 4.40 ms                                                               | 5.27 ms: 1.20x slower                                                 |
| regex_compile              | 137 ms                                                                | 165 ms: 1.20x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 33.2 ms: 1.21x slower                                                 |
| django_template            | 40.7 ms                                                               | 49.3 ms: 1.21x slower                                                 |
| scimark_lu                 | 146 ms                                                                | 179 ms: 1.23x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 2.37 ms: 1.24x slower                                                 |
| hexiom                     | 6.98 ms                                                               | 8.67 ms: 1.24x slower                                                 |
| python_startup_no_site     | 8.37 ms                                                               | 10.9 ms: 1.30x slower                                                 |
| python_startup             | 11.4 ms                                                               | 14.9 ms: 1.31x slower                                                 |
| genshi_xml                 | 60.6 ms                                                               | 80.0 ms: 1.32x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                          |

Benchmark hidden because not significant (7): xml_etree_parse, xml_etree_iterparse, pickle_list, crypto_pyaes, pickle_dict, xml_etree_process, coroutines
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x