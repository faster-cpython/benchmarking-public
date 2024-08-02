# Results vs. 3.12.0

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-aarch64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.01x faster
- HPT reliability: 52.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| chameleon      | 8.81 ms                                                               | 8.93 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| html5lib       | 65.1 ms                                                               | 66.9 ms: 1.03x slower                                                    |
| tornado_http   | 136 ms                                                                | 131 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 492 ms: 1.27x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 599 ms: 1.24x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 642 ms: 1.21x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 479 ms: 1.20x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 758 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 783 ms: 1.17x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| regex_dna      | 254 ms                                                                | 257 ms: 1.01x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| pickle_pure_python   | 365 us                                                                | 359 us: 1.02x faster                                                     |
| pickle_list          | 5.25 us                                                               | 5.30 us: 1.01x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                    |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 116 ms: 1.03x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 82.2 ms: 1.04x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.56 us: 1.06x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                    |
| unpickle             | 18.5 us                                                               | 20.0 us: 1.08x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                    |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.6 ms: 1.01x slower                                                    |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                    |
| django_template | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 492 ms: 1.27x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 599 ms: 1.24x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 642 ms: 1.21x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 479 ms: 1.20x faster                                                     |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 758 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 783 ms: 1.17x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.6 ms: 1.16x faster                                                    |
| mypy2                      | 873 ms                                                                | 772 ms: 1.13x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.82 ms: 1.08x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.10 us: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.76 us: 1.08x faster                                                    |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 82.1 ms: 1.06x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.0 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                     |
| tornado_http               | 136 ms                                                                | 131 ms: 1.04x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 59.8 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.9 ms: 1.03x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 142 ms: 1.03x faster                                                     |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 359 us: 1.02x faster                                                     |
| async_generators           | 491 ms                                                                | 483 ms: 1.02x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 27.6 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.03 ms: 1.01x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.30 us: 1.01x slower                                                    |
| regex_dna                  | 254 ms                                                                | 257 ms: 1.01x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 8.93 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 928 ms: 1.01x slower                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 4.16 us: 1.01x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.16 ms: 1.01x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 50.4 us: 1.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 461 ms: 1.02x slower                                                     |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                     |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.23 sec: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                    |
| thrift                     | 937 us                                                                | 958 us: 1.02x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 62.8 ms: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 66.9 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                    |
| fannkuch                   | 443 ms                                                                | 457 ms: 1.03x slower                                                     |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 585 ms: 1.03x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 116 ms: 1.03x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.90 us: 1.04x slower                                                    |
| pyflate                    | 559 ms                                                                | 581 ms: 1.04x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 82.2 ms: 1.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.52 ms: 1.05x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                    |
| richards_super             | 58.5 ms                                                               | 61.9 ms: 1.06x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.56 us: 1.06x slower                                                    |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                                     |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                    |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                     |
| unpickle                   | 18.5 us                                                               | 20.0 us: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                    |
| richards                   | 50.9 ms                                                               | 55.6 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                     |
| gunicorn                   | 1.14 ms                                                               | 1.24 ms: 1.10x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.6 ms: 1.13x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.73 ms: 1.14x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.08 ms: 1.16x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.35 ms: 1.22x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (14): pylint, sqlglot_parse, dask, xml_etree_iterparse, xml_etree_parse, 2to3, asyncio_websockets, float, coroutines, nqueens, pprint_pformat, deepcopy, aiohttp, genshi_xml
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: flaskblogging

# HPT report

- Reliability score: 52.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x