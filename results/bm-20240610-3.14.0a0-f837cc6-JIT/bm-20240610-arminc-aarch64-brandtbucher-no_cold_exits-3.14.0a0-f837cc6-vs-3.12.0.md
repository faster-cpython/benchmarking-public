# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-aarch64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 356 ms: 1.16x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                 |
| html5lib       | 65.1 ms                                                               | 70.7 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 494 ms: 1.26x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 609 ms: 1.22x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 479 ms: 1.20x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 665 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 765 ms: 1.16x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 799 ms: 1.14x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.10x faster                                                 |
| Geometric mean             | (ref)                                                                 | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.1 ms: 1.02x faster                                                  |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 117 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 258 ms: 1.01x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                  |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.07x slower                                                  |
| regex_compile  | 137 ms                                                                | 176 ms: 1.28x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                   |
| pickle_list          | 5.25 us                                                               | 5.27 us: 1.00x slower                                                  |
| pickle_dict          | 37.3 us                                                               | 37.6 us: 1.01x slower                                                  |
| unpickle             | 18.5 us                                                               | 19.3 us: 1.05x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 275 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.67 us: 1.08x slower                                                  |
| pickle_pure_python   | 365 us                                                                | 413 us: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                           |

Benchmark hidden because not significant (4): pickle, tomli_loads, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                  |
| python_startup         | 11.4 ms                                                               | 12.8 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 12.9 ms: 1.00x faster                                                  |
| django_template | 40.7 ms                                                               | 49.1 ms: 1.21x slower                                                  |
| genshi_text     | 27.4 ms                                                               | 34.0 ms: 1.24x slower                                                  |
| genshi_xml      | 60.6 ms                                                               | 81.1 ms: 1.34x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.19x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 494 ms: 1.26x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 609 ms: 1.22x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 479 ms: 1.20x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 665 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 765 ms: 1.16x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 799 ms: 1.14x faster                                                   |
| generators                 | 43.5 ms                                                               | 38.2 ms: 1.14x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.10x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.10x faster                                                 |
| comprehensions             | 25.4 us                                                               | 23.1 us: 1.10x faster                                                  |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.89 us: 1.06x faster                                                  |
| logging_simple             | 7.63 us                                                               | 7.35 us: 1.04x faster                                                  |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                   |
| float                      | 92.1 ms                                                               | 90.1 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 48.8 us: 1.02x faster                                                  |
| mako                       | 12.9 ms                                                               | 12.9 ms: 1.00x faster                                                  |
| pickle_list                | 5.25 us                                                               | 5.27 us: 1.00x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 37.6 us: 1.01x slower                                                  |
| thrift                     | 937 us                                                                | 944 us: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.01x slower                                                  |
| regex_dna                  | 254 ms                                                                | 258 ms: 1.01x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 88.8 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.03x slower                                                 |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                  |
| dask                       | 376 ms                                                                | 390 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.92 us: 1.04x slower                                                  |
| async_generators           | 491 ms                                                                | 512 ms: 1.04x slower                                                   |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.04x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.3 us: 1.05x slower                                                  |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                  |
| unpickle_pure_python       | 260 us                                                                | 275 us: 1.06x slower                                                   |
| richards_super             | 58.5 ms                                                               | 62.1 ms: 1.06x slower                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.6 ms: 1.06x slower                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.07x slower                                                  |
| pyflate                    | 559 ms                                                                | 598 ms: 1.07x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                                  |
| fannkuch                   | 443 ms                                                                | 476 ms: 1.07x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.08x slower                                                 |
| unpickle_list              | 6.17 us                                                               | 6.67 us: 1.08x slower                                                  |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 70.7 ms: 1.09x slower                                                  |
| richards                   | 50.9 ms                                                               | 55.4 ms: 1.09x slower                                                  |
| logging_silent             | 127 ns                                                                | 139 ns: 1.09x slower                                                   |
| scimark_fft                | 418 ms                                                                | 460 ms: 1.10x slower                                                   |
| deepcopy                   | 446 us                                                                | 490 us: 1.10x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.03 ms: 1.11x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 630 ms: 1.11x slower                                                   |
| nbody                      | 105 ms                                                                | 117 ms: 1.11x slower                                                   |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.61 ms: 1.12x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.94 ms: 1.12x slower                                                  |
| python_startup             | 11.4 ms                                                               | 12.8 ms: 1.13x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 69.1 ms: 1.13x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 413 us: 1.13x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.65 us: 1.13x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 8.01 ms: 1.14x slower                                                  |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 70.6 ms: 1.14x slower                                                  |
| sympy_str                  | 280 ms                                                                | 319 ms: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 208 us: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                   |
| 2to3                       | 308 ms                                                                | 356 ms: 1.16x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 116 ms: 1.17x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.98 ms: 1.17x slower                                                  |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.18x slower                                                   |
| sympy_expand               | 454 ms                                                                | 534 ms: 1.18x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.18 ms: 1.18x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                 |
| pylint                     | 355 ms                                                                | 421 ms: 1.19x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 25.9 ms: 1.20x slower                                                  |
| django_template            | 40.7 ms                                                               | 49.1 ms: 1.21x slower                                                  |
| sympy_sum                  | 154 ms                                                                | 187 ms: 1.21x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.12 sec: 1.22x slower                                                 |
| create_gc_cycles           | 1.92 ms                                                               | 2.35 ms: 1.22x slower                                                  |
| chaos                      | 71.4 ms                                                               | 88.2 ms: 1.23x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                 |
| genshi_text                | 27.4 ms                                                               | 34.0 ms: 1.24x slower                                                  |
| scimark_lu                 | 146 ms                                                                | 183 ms: 1.26x slower                                                   |
| regex_compile              | 137 ms                                                                | 176 ms: 1.28x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.96 ms: 1.28x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 81.1 ms: 1.34x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                           |

Benchmark hidden because not significant (8): coroutines, pickle, tomli_loads, xml_etree_generate, mdp, asyncio_websockets, xml_etree_process, tornado_http
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.98x