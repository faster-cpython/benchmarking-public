# Results vs. 3.12.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-aarch64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 385 ms: 1.25x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.72 sec: 1.25x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.9 ms: 1.11x slower                                                   |
| tornado_http   | 136 ms                                                                | 145 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 444 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 424 ms: 1.36x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 743 ms: 1.19x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.8 ms: 1.03x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 253 ms: 1.00x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.4 ms: 1.11x slower                                                   |
| regex_compile  | 137 ms                                                                | 185 ms: 1.35x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.21 us: 1.01x faster                                                   |
| json_loads           | 30.7 us                                                               | 31.1 us: 1.01x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 264 us: 1.02x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.33 us: 1.03x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.2 us: 1.04x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 82.5 ms: 1.04x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 397 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 51.0 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 84.1 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 444 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 424 ms: 1.36x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.3 us: 1.30x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 743 ms: 1.19x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                   |
| deepcopy                   | 446 us                                                                | 402 us: 1.11x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.05x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.5 us: 1.04x faster                                                   |
| float                      | 92.1 ms                                                               | 89.8 ms: 1.03x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.01 us: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.51 us: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.01x faster                                                   |
| raytrace                   | 353 ms                                                                | 349 ms: 1.01x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.21 us: 1.01x faster                                                   |
| json                       | 5.54 ms                                                               | 5.50 ms: 1.01x faster                                                   |
| regex_dna                  | 254 ms                                                                | 253 ms: 1.00x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.1 us: 1.01x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 264 us: 1.02x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| unpickle_list              | 6.17 us                                                               | 6.33 us: 1.03x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 150 ms: 1.03x slower                                                    |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 966 us: 1.03x slower                                                    |
| async_generators           | 491 ms                                                                | 507 ms: 1.03x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.2 us: 1.04x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 90.1 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 82.5 ms: 1.04x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                                  |
| deltablue                  | 4.12 ms                                                               | 4.35 ms: 1.06x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.9 ms: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| tornado_http               | 136 ms                                                                | 145 ms: 1.07x slower                                                    |
| scimark_fft                | 418 ms                                                                | 449 ms: 1.07x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 397 us: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.9 ms: 1.11x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.41 ms: 1.11x slower                                                   |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.4 ms: 1.11x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 628 ms: 1.11x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.91 ms: 1.11x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.8 ms: 1.12x slower                                                   |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                    |
| fannkuch                   | 443 ms                                                                | 505 ms: 1.14x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.02 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| pyflate                    | 559 ms                                                                | 638 ms: 1.14x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 208 us: 1.15x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.71 ms: 1.17x slower                                                   |
| go                         | 157 ms                                                                | 186 ms: 1.18x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.49 sec: 1.18x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.20 ms: 1.21x slower                                                   |
| richards_super             | 58.5 ms                                                               | 71.8 ms: 1.23x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 156 ms: 1.24x slower                                                    |
| chaos                      | 71.4 ms                                                               | 88.8 ms: 1.24x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.72 sec: 1.25x slower                                                  |
| 2to3                       | 308 ms                                                                | 385 ms: 1.25x slower                                                    |
| django_template            | 40.7 ms                                                               | 51.0 ms: 1.25x slower                                                   |
| richards                   | 50.9 ms                                                               | 64.1 ms: 1.26x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 125 ms: 1.26x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                                   |
| sympy_expand               | 454 ms                                                                | 587 ms: 1.30x slower                                                    |
| sympy_str                  | 280 ms                                                                | 363 ms: 1.30x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 80.8 ms: 1.30x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 82.1 ms: 1.34x slower                                                   |
| regex_compile              | 137 ms                                                                | 185 ms: 1.35x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 29.2 ms: 1.35x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                                  |
| generators                 | 43.5 ms                                                               | 59.5 ms: 1.37x slower                                                   |
| pylint                     | 355 ms                                                                | 487 ms: 1.37x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.61 sec: 1.38x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 84.1 ms: 1.39x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 215 ms: 1.39x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.1 ms: 1.44x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 2.04 sec: 289.62x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.14x slower                                                            |

Benchmark hidden because not significant (3): logging_format, sqlite_synth, xml_etree_generate
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.97x