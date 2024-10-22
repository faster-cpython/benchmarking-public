# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 374 ms: 1.22x slower                                             |
| docutils       | 2.98 sec                                                              | 3.63 sec: 1.22x slower                                           |
| html5lib       | 65.1 ms                                                               | 71.3 ms: 1.10x slower                                            |
| tornado_http   | 136 ms                                                                | 142 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 426 ms: 1.35x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 591 ms: 1.31x faster                                             |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 752 ms: 1.21x faster                                             |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 744 ms: 1.19x faster                                             |
| Geometric mean             | (ref)                                                                 | 1.27x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.0 ms: 1.02x faster                                            |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                             |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                             |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                            |
| regex_v8       | 28.3 ms                                                               | 31.4 ms: 1.11x slower                                            |
| regex_compile  | 137 ms                                                                | 181 ms: 1.32x slower                                             |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 110 ms: 1.02x faster                                             |
| pickle_list          | 5.25 us                                                               | 5.21 us: 1.01x faster                                            |
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                           |
| xml_etree_iterparse  | 150 ms                                                                | 152 ms: 1.01x slower                                             |
| json_loads           | 30.7 us                                                               | 31.0 us: 1.01x slower                                            |
| xml_etree_process    | 79.0 ms                                                               | 80.0 ms: 1.01x slower                                            |
| pickle               | 13.4 us                                                               | 13.6 us: 1.02x slower                                            |
| pickle_dict          | 37.3 us                                                               | 38.1 us: 1.02x slower                                            |
| unpickle_pure_python | 260 us                                                                | 267 us: 1.03x slower                                             |
| unpickle             | 18.5 us                                                               | 19.2 us: 1.04x slower                                            |
| unpickle_list        | 6.17 us                                                               | 6.40 us: 1.04x slower                                            |
| pickle_pure_python   | 365 us                                                                | 384 us: 1.05x slower                                             |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                            |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                            |
| genshi_text     | 27.4 ms                                                               | 34.8 ms: 1.27x slower                                            |
| django_template | 40.7 ms                                                               | 51.9 ms: 1.28x slower                                            |
| genshi_xml      | 60.6 ms                                                               | 83.0 ms: 1.37x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 426 ms: 1.35x faster                                             |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 591 ms: 1.31x faster                                             |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 752 ms: 1.21x faster                                             |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 744 ms: 1.19x faster                                             |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                            |
| deepcopy                   | 446 us                                                                | 405 us: 1.10x faster                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.85 us: 1.06x faster                                            |
| logging_format             | 8.34 us                                                               | 8.02 us: 1.04x faster                                            |
| comprehensions             | 25.4 us                                                               | 24.5 us: 1.04x faster                                            |
| logging_simple             | 7.63 us                                                               | 7.40 us: 1.03x faster                                            |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                             |
| float                      | 92.1 ms                                                               | 90.0 ms: 1.02x faster                                            |
| raytrace                   | 353 ms                                                                | 347 ms: 1.02x faster                                             |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                             |
| coroutines                 | 29.0 ms                                                               | 28.7 ms: 1.01x faster                                            |
| pickle_list                | 5.25 us                                                               | 5.21 us: 1.01x faster                                            |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                           |
| xml_etree_iterparse        | 150 ms                                                                | 152 ms: 1.01x slower                                             |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                             |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                             |
| sqlite_synth               | 3.77 us                                                               | 3.81 us: 1.01x slower                                            |
| json_loads                 | 30.7 us                                                               | 31.0 us: 1.01x slower                                            |
| xml_etree_process          | 79.0 ms                                                               | 80.0 ms: 1.01x slower                                            |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.02x slower                                            |
| crypto_pyaes               | 86.6 ms                                                               | 88.1 ms: 1.02x slower                                            |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                            |
| pickle_dict                | 37.3 us                                                               | 38.1 us: 1.02x slower                                            |
| mdp                        | 3.41 sec                                                              | 3.50 sec: 1.02x slower                                           |
| thrift                     | 937 us                                                                | 960 us: 1.03x slower                                             |
| unpickle_pure_python       | 260 us                                                                | 267 us: 1.03x slower                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.5 ms: 1.03x slower                                            |
| scimark_lu                 | 146 ms                                                                | 150 ms: 1.03x slower                                             |
| async_generators           | 491 ms                                                                | 507 ms: 1.03x slower                                             |
| unpickle                   | 18.5 us                                                               | 19.2 us: 1.04x slower                                            |
| unpickle_list              | 6.17 us                                                               | 6.40 us: 1.04x slower                                            |
| tornado_http               | 136 ms                                                                | 142 ms: 1.05x slower                                             |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                            |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                             |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                           |
| pickle_pure_python         | 365 us                                                                | 384 us: 1.05x slower                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                            |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                            |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                             |
| deltablue                  | 4.12 ms                                                               | 4.38 ms: 1.06x slower                                            |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                            |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.79 ms: 1.10x slower                                            |
| html5lib                   | 65.1 ms                                                               | 71.3 ms: 1.10x slower                                            |
| asyncio_tcp                | 566 ms                                                                | 622 ms: 1.10x slower                                             |
| pyflate                    | 559 ms                                                                | 617 ms: 1.10x slower                                             |
| regex_v8                   | 28.3 ms                                                               | 31.4 ms: 1.11x slower                                            |
| spectral_norm              | 131 ms                                                                | 145 ms: 1.11x slower                                             |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.11x slower                                             |
| scimark_sor                | 150 ms                                                                | 167 ms: 1.12x slower                                             |
| fannkuch                   | 443 ms                                                                | 503 ms: 1.13x slower                                             |
| coverage                   | 87.3 ms                                                               | 99.2 ms: 1.14x slower                                            |
| sqlglot_parse              | 1.46 ms                                                               | 1.68 ms: 1.15x slower                                            |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                            |
| telco                      | 8.51 ms                                                               | 9.86 ms: 1.16x slower                                            |
| typing_runtime_protocols   | 181 us                                                                | 211 us: 1.17x slower                                             |
| pycparser                  | 1.26 sec                                                              | 1.47 sec: 1.17x slower                                           |
| richards                   | 50.9 ms                                                               | 60.3 ms: 1.18x slower                                            |
| gc_traversal               | 4.40 ms                                                               | 5.21 ms: 1.19x slower                                            |
| go                         | 157 ms                                                                | 189 ms: 1.20x slower                                             |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.21x slower                                            |
| richards_super             | 58.5 ms                                                               | 70.7 ms: 1.21x slower                                            |
| 2to3                       | 308 ms                                                                | 374 ms: 1.22x slower                                             |
| sqlglot_transpile          | 1.83 ms                                                               | 2.22 ms: 1.22x slower                                            |
| docutils                   | 2.98 sec                                                              | 3.63 sec: 1.22x slower                                           |
| dulwich_log                | 62.0 ms                                                               | 76.0 ms: 1.23x slower                                            |
| nqueens                    | 99.2 ms                                                               | 122 ms: 1.23x slower                                             |
| sqlglot_normalize          | 126 ms                                                                | 155 ms: 1.23x slower                                             |
| chaos                      | 71.4 ms                                                               | 88.3 ms: 1.24x slower                                            |
| genshi_text                | 27.4 ms                                                               | 34.8 ms: 1.27x slower                                            |
| django_template            | 40.7 ms                                                               | 51.9 ms: 1.28x slower                                            |
| sympy_str                  | 280 ms                                                                | 358 ms: 1.28x slower                                             |
| sympy_expand               | 454 ms                                                                | 591 ms: 1.30x slower                                             |
| sqlglot_optimize           | 61.3 ms                                                               | 80.2 ms: 1.31x slower                                            |
| pprint_safe_repr           | 916 ms                                                                | 1.20 sec: 1.31x slower                                           |
| regex_compile              | 137 ms                                                                | 181 ms: 1.32x slower                                             |
| pprint_pformat             | 1.88 sec                                                              | 2.50 sec: 1.33x slower                                           |
| pylint                     | 355 ms                                                                | 472 ms: 1.33x slower                                             |
| sympy_integrate            | 21.6 ms                                                               | 28.8 ms: 1.33x slower                                            |
| generators                 | 43.5 ms                                                               | 59.3 ms: 1.36x slower                                            |
| genshi_xml                 | 60.6 ms                                                               | 83.0 ms: 1.37x slower                                            |
| sympy_sum                  | 154 ms                                                                | 214 ms: 1.38x slower                                             |
| hexiom                     | 6.98 ms                                                               | 10.1 ms: 1.45x slower                                            |
| bench_mp_pool              | 7.05 ms                                                               | 1.89 sec: 268.49x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x