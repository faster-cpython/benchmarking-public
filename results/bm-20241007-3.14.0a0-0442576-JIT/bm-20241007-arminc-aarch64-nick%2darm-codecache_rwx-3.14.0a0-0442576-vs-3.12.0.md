# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 365 ms: 1.19x slower                                                 |
| docutils       | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                               |
| html5lib       | 65.1 ms                                                               | 70.6 ms: 1.09x slower                                                |
| tornado_http   | 136 ms                                                                | 149 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 442 ms: 1.41x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 427 ms: 1.35x faster                                                 |
| async_tree_memoization     | 777 ms                                                                | 585 ms: 1.33x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 754 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 732 ms: 1.21x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                               |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.2 ms: 1.02x faster                                                |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 263 ms: 1.03x slower                                                 |
| regex_effbot   | 4.64 ms                                                               | 5.00 ms: 1.08x slower                                                |
| regex_v8       | 28.3 ms                                                               | 31.3 ms: 1.10x slower                                                |
| regex_compile  | 137 ms                                                                | 174 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 109 ms: 1.02x faster                                                 |
| pickle_list          | 5.25 us                                                               | 5.19 us: 1.01x faster                                                |
| xml_etree_process    | 79.0 ms                                                               | 79.4 ms: 1.01x slower                                                |
| json_loads           | 30.7 us                                                               | 31.1 us: 1.01x slower                                                |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                               |
| unpickle_pure_python | 260 us                                                                | 265 us: 1.02x slower                                                 |
| pickle               | 13.4 us                                                               | 13.8 us: 1.02x slower                                                |
| unpickle_list        | 6.17 us                                                               | 6.37 us: 1.03x slower                                                |
| unpickle             | 18.5 us                                                               | 19.1 us: 1.04x slower                                                |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                |
| pickle_pure_python   | 365 us                                                                | 395 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                         |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.16x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                |
| genshi_text     | 27.4 ms                                                               | 33.1 ms: 1.21x slower                                                |
| django_template | 40.7 ms                                                               | 51.2 ms: 1.26x slower                                                |
| genshi_xml      | 60.6 ms                                                               | 78.1 ms: 1.29x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.19x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 442 ms: 1.41x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 427 ms: 1.35x faster                                                 |
| async_tree_memoization     | 777 ms                                                                | 585 ms: 1.33x faster                                                 |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 754 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 732 ms: 1.21x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                               |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                |
| deepcopy                   | 446 us                                                                | 402 us: 1.11x faster                                                 |
| deepcopy_reduce            | 4.10 us                                                               | 3.94 us: 1.04x faster                                                |
| comprehensions             | 25.4 us                                                               | 24.6 us: 1.03x faster                                                |
| logging_format             | 8.34 us                                                               | 8.10 us: 1.03x faster                                                |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.02x faster                                                 |
| raytrace                   | 353 ms                                                                | 345 ms: 1.02x faster                                                 |
| float                      | 92.1 ms                                                               | 90.2 ms: 1.02x faster                                                |
| logging_simple             | 7.63 us                                                               | 7.49 us: 1.02x faster                                                |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                |
| pickle_list                | 5.25 us                                                               | 5.19 us: 1.01x faster                                                |
| xml_etree_process          | 79.0 ms                                                               | 79.4 ms: 1.01x slower                                                |
| scimark_sor                | 150 ms                                                                | 151 ms: 1.01x slower                                                 |
| mdp                        | 3.41 sec                                                              | 3.45 sec: 1.01x slower                                               |
| asyncio_websockets         | 658 ms                                                                | 665 ms: 1.01x slower                                                 |
| json_loads                 | 30.7 us                                                               | 31.1 us: 1.01x slower                                                |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                               |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                |
| unpickle_pure_python       | 260 us                                                                | 265 us: 1.02x slower                                                 |
| crypto_pyaes               | 86.6 ms                                                               | 88.6 ms: 1.02x slower                                                |
| thrift                     | 937 us                                                                | 959 us: 1.02x slower                                                 |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.02x slower                                                |
| unpickle_list              | 6.17 us                                                               | 6.37 us: 1.03x slower                                                |
| regex_dna                  | 254 ms                                                                | 263 ms: 1.03x slower                                                 |
| unpickle                   | 18.5 us                                                               | 19.1 us: 1.04x slower                                                |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.2 ms: 1.04x slower                                                |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                 |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                 |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.04x slower                                                |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                               |
| python_startup_no_site     | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                |
| deltablue                  | 4.12 ms                                                               | 4.34 ms: 1.05x slower                                                |
| async_generators           | 491 ms                                                                | 517 ms: 1.05x slower                                                 |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                 |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                                 |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                |
| regex_effbot               | 4.64 ms                                                               | 5.00 ms: 1.08x slower                                                |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                 |
| html5lib                   | 65.1 ms                                                               | 70.6 ms: 1.09x slower                                                |
| tornado_http               | 136 ms                                                                | 149 ms: 1.10x slower                                                 |
| meteor_contest             | 112 ms                                                                | 123 ms: 1.10x slower                                                 |
| asyncio_tcp                | 566 ms                                                                | 622 ms: 1.10x slower                                                 |
| telco                      | 8.51 ms                                                               | 9.37 ms: 1.10x slower                                                |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.83 ms: 1.10x slower                                                |
| regex_v8                   | 28.3 ms                                                               | 31.3 ms: 1.10x slower                                                |
| pyflate                    | 559 ms                                                                | 620 ms: 1.11x slower                                                 |
| richards                   | 50.9 ms                                                               | 56.9 ms: 1.12x slower                                                |
| coverage                   | 87.3 ms                                                               | 98.2 ms: 1.12x slower                                                |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.13x slower                                                 |
| fannkuch                   | 443 ms                                                                | 504 ms: 1.14x slower                                                 |
| typing_runtime_protocols   | 181 us                                                                | 205 us: 1.14x slower                                                 |
| sqlglot_parse              | 1.46 ms                                                               | 1.68 ms: 1.14x slower                                                |
| richards_super             | 58.5 ms                                                               | 67.3 ms: 1.15x slower                                                |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.16x slower                                                |
| go                         | 157 ms                                                                | 182 ms: 1.16x slower                                                 |
| pycparser                  | 1.26 sec                                                              | 1.47 sec: 1.17x slower                                               |
| 2to3                       | 308 ms                                                                | 365 ms: 1.19x slower                                                 |
| gc_traversal               | 4.40 ms                                                               | 5.21 ms: 1.19x slower                                                |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.19x slower                                                 |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                |
| docutils                   | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                               |
| genshi_text                | 27.4 ms                                                               | 33.1 ms: 1.21x slower                                                |
| sqlglot_transpile          | 1.83 ms                                                               | 2.21 ms: 1.21x slower                                                |
| chaos                      | 71.4 ms                                                               | 86.4 ms: 1.21x slower                                                |
| nqueens                    | 99.2 ms                                                               | 123 ms: 1.24x slower                                                 |
| sympy_str                  | 280 ms                                                                | 346 ms: 1.24x slower                                                 |
| sqlglot_optimize           | 61.3 ms                                                               | 76.1 ms: 1.24x slower                                                |
| django_template            | 40.7 ms                                                               | 51.2 ms: 1.26x slower                                                |
| sympy_expand               | 454 ms                                                                | 573 ms: 1.26x slower                                                 |
| regex_compile              | 137 ms                                                                | 174 ms: 1.27x slower                                                 |
| genshi_xml                 | 60.6 ms                                                               | 78.1 ms: 1.29x slower                                                |
| pylint                     | 355 ms                                                                | 459 ms: 1.30x slower                                                 |
| dulwich_log                | 62.0 ms                                                               | 81.3 ms: 1.31x slower                                                |
| sympy_integrate            | 21.6 ms                                                               | 28.5 ms: 1.32x slower                                                |
| pprint_safe_repr           | 916 ms                                                                | 1.22 sec: 1.34x slower                                               |
| pprint_pformat             | 1.88 sec                                                              | 2.54 sec: 1.35x slower                                               |
| generators                 | 43.5 ms                                                               | 58.8 ms: 1.35x slower                                                |
| sympy_sum                  | 154 ms                                                                | 210 ms: 1.36x slower                                                 |
| hexiom                     | 6.98 ms                                                               | 9.90 ms: 1.42x slower                                                |
| bench_mp_pool              | 7.05 ms                                                               | 2.94 sec: 417.29x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                         |

Benchmark hidden because not significant (5): xml_etree_parse, json, xml_etree_iterparse, pidigits, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.98x