# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 360 ms: 1.17x slower                                         |
| chameleon      | 8.81 ms                                                               | 9.18 ms: 1.04x slower                                        |
| docutils       | 2.98 sec                                                              | 3.52 sec: 1.18x slower                                       |
| html5lib       | 65.1 ms                                                               | 71.7 ms: 1.10x slower                                        |
| tornado_http   | 136 ms                                                                | 139 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 508 ms: 1.23x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 620 ms: 1.19x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 485 ms: 1.19x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 671 ms: 1.16x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                       |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 818 ms: 1.11x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 806 ms: 1.10x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.16x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.7 ms: 1.04x faster                                        |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                         |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                         |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                         |
| regex_effbot   | 4.64 ms                                                               | 4.86 ms: 1.05x slower                                        |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                        |
| regex_compile  | 137 ms                                                                | 175 ms: 1.27x slower                                         |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.03x faster                                         |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.01x faster                                         |
| pickle_dict          | 37.3 us                                                               | 37.6 us: 1.01x slower                                        |
| pickle_list          | 5.25 us                                                               | 5.30 us: 1.01x slower                                        |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                       |
| xml_etree_generate   | 112 ms                                                                | 114 ms: 1.02x slower                                         |
| json_loads           | 30.7 us                                                               | 32.1 us: 1.05x slower                                        |
| unpickle_list        | 6.17 us                                                               | 6.58 us: 1.07x slower                                        |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                        |
| unpickle_pure_python | 260 us                                                                | 278 us: 1.07x slower                                         |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                        |
| pickle_pure_python   | 365 us                                                                | 398 us: 1.09x slower                                         |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                 |

Benchmark hidden because not significant (2): pickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.9 ms: 1.30x slower                                        |
| python_startup         | 11.4 ms                                                               | 15.3 ms: 1.35x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                        |
| django_template | 40.7 ms                                                               | 49.6 ms: 1.22x slower                                        |
| genshi_text     | 27.4 ms                                                               | 35.4 ms: 1.29x slower                                        |
| genshi_xml      | 60.6 ms                                                               | 83.4 ms: 1.38x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 508 ms: 1.23x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 620 ms: 1.19x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 485 ms: 1.19x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 671 ms: 1.16x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                       |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 818 ms: 1.11x faster                                         |
| raytrace                   | 353 ms                                                                | 321 ms: 1.10x faster                                         |
| generators                 | 43.5 ms                                                               | 39.6 ms: 1.10x faster                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 806 ms: 1.10x faster                                         |
| comprehensions             | 25.4 us                                                               | 23.2 us: 1.09x faster                                        |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                        |
| logging_simple             | 7.63 us                                                               | 7.31 us: 1.04x faster                                        |
| float                      | 92.1 ms                                                               | 88.7 ms: 1.04x faster                                        |
| logging_format             | 8.34 us                                                               | 8.05 us: 1.04x faster                                        |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.03x faster                                         |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                         |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.01x faster                                         |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                        |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                        |
| pickle_dict                | 37.3 us                                                               | 37.6 us: 1.01x slower                                        |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                         |
| pickle_list                | 5.25 us                                                               | 5.30 us: 1.01x slower                                        |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                       |
| xml_etree_generate         | 112 ms                                                                | 114 ms: 1.02x slower                                         |
| tornado_http               | 136 ms                                                                | 139 ms: 1.02x slower                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                       |
| crypto_pyaes               | 86.6 ms                                                               | 89.1 ms: 1.03x slower                                        |
| thrift                     | 937 us                                                                | 965 us: 1.03x slower                                         |
| async_generators           | 491 ms                                                                | 508 ms: 1.04x slower                                         |
| json                       | 5.54 ms                                                               | 5.74 ms: 1.04x slower                                        |
| chameleon                  | 8.81 ms                                                               | 9.18 ms: 1.04x slower                                        |
| dask                       | 376 ms                                                                | 393 ms: 1.04x slower                                         |
| fannkuch                   | 443 ms                                                                | 463 ms: 1.04x slower                                         |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.0 ms: 1.05x slower                                        |
| regex_effbot               | 4.64 ms                                                               | 4.86 ms: 1.05x slower                                        |
| json_loads                 | 30.7 us                                                               | 32.1 us: 1.05x slower                                        |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.05x slower                                         |
| unpickle_list              | 6.17 us                                                               | 6.58 us: 1.07x slower                                        |
| pyflate                    | 559 ms                                                                | 596 ms: 1.07x slower                                         |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                        |
| unpickle_pure_python       | 260 us                                                                | 278 us: 1.07x slower                                         |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                        |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.07x slower                                       |
| sqlglot_parse              | 1.46 ms                                                               | 1.58 ms: 1.08x slower                                        |
| richards_super             | 58.5 ms                                                               | 63.4 ms: 1.08x slower                                        |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                        |
| pickle_pure_python         | 365 us                                                                | 398 us: 1.09x slower                                         |
| asyncio_tcp                | 566 ms                                                                | 618 ms: 1.09x slower                                         |
| sqlglot_transpile          | 1.83 ms                                                               | 2.00 ms: 1.10x slower                                        |
| scimark_fft                | 418 ms                                                                | 459 ms: 1.10x slower                                         |
| html5lib                   | 65.1 ms                                                               | 71.7 ms: 1.10x slower                                        |
| richards                   | 50.9 ms                                                               | 56.2 ms: 1.10x slower                                        |
| aiohttp                    | 1.16 ms                                                               | 1.28 ms: 1.10x slower                                        |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                         |
| logging_silent             | 127 ns                                                                | 141 ns: 1.11x slower                                         |
| deltablue                  | 4.12 ms                                                               | 4.58 ms: 1.11x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.94 ms: 1.12x slower                                        |
| coverage                   | 87.3 ms                                                               | 98.1 ms: 1.12x slower                                        |
| deepcopy                   | 446 us                                                                | 502 us: 1.13x slower                                         |
| sqlglot_optimize           | 61.3 ms                                                               | 69.8 ms: 1.14x slower                                        |
| spectral_norm              | 131 ms                                                                | 149 ms: 1.14x slower                                         |
| deepcopy_reduce            | 4.10 us                                                               | 4.68 us: 1.14x slower                                        |
| go                         | 157 ms                                                                | 180 ms: 1.14x slower                                         |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                         |
| dulwich_log                | 62.0 ms                                                               | 71.0 ms: 1.15x slower                                        |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.15x slower                                         |
| sympy_str                  | 280 ms                                                                | 321 ms: 1.15x slower                                         |
| gc_traversal               | 4.40 ms                                                               | 5.08 ms: 1.16x slower                                        |
| scimark_sor                | 150 ms                                                                | 174 ms: 1.16x slower                                         |
| pylint                     | 355 ms                                                                | 414 ms: 1.17x slower                                         |
| bench_mp_pool              | 7.05 ms                                                               | 8.24 ms: 1.17x slower                                        |
| 2to3                       | 308 ms                                                                | 360 ms: 1.17x slower                                         |
| nqueens                    | 99.2 ms                                                               | 117 ms: 1.18x slower                                         |
| sympy_integrate            | 21.6 ms                                                               | 25.5 ms: 1.18x slower                                        |
| docutils                   | 2.98 sec                                                              | 3.52 sec: 1.18x slower                                       |
| sympy_sum                  | 154 ms                                                                | 183 ms: 1.18x slower                                         |
| sympy_expand               | 454 ms                                                                | 538 ms: 1.19x slower                                         |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                        |
| gunicorn                   | 1.14 ms                                                               | 1.36 ms: 1.20x slower                                        |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                       |
| django_template            | 40.7 ms                                                               | 49.6 ms: 1.22x slower                                        |
| chaos                      | 71.4 ms                                                               | 87.1 ms: 1.22x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.31 sec: 1.23x slower                                       |
| create_gc_cycles           | 1.92 ms                                                               | 2.38 ms: 1.24x slower                                        |
| scimark_lu                 | 146 ms                                                                | 183 ms: 1.25x slower                                         |
| regex_compile              | 137 ms                                                                | 175 ms: 1.27x slower                                         |
| hexiom                     | 6.98 ms                                                               | 8.89 ms: 1.27x slower                                        |
| genshi_text                | 27.4 ms                                                               | 35.4 ms: 1.29x slower                                        |
| python_startup_no_site     | 8.37 ms                                                               | 10.9 ms: 1.30x slower                                        |
| python_startup             | 11.4 ms                                                               | 15.3 ms: 1.35x slower                                        |
| genshi_xml                 | 60.6 ms                                                               | 83.4 ms: 1.38x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                 |

Benchmark hidden because not significant (8): coroutines, deepcopy_memo, asyncio_websockets, sqlite_synth, mdp, pickle, xml_etree_process, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x