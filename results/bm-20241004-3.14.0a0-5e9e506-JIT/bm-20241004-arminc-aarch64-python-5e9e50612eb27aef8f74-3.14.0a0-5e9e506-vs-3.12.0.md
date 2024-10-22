# Results vs. 3.12.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-aarch64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 386 ms: 1.25x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.71 sec: 1.24x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.9 ms: 1.11x slower                                                   |
| tornado_http   | 136 ms                                                                | 148 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                    |
| async_tree_none            | 624 ms                                                                | 459 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 728 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 765 ms: 1.19x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.20 sec: 1.17x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.27x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 94.3 ms: 1.02x slower                                                   |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 5.00 ms: 1.08x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 180 ms: 1.31x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.29 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 152 ms: 1.01x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 267 us: 1.03x slower                                                    |
| json_loads           | 30.7 us                                                               | 31.6 us: 1.03x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 81.3 ms: 1.03x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.3 us: 1.04x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.56 us: 1.06x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 393 us: 1.08x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 14.6 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| django_template | 40.7 ms                                                               | 52.2 ms: 1.28x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 84.4 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                    |
| async_tree_none            | 624 ms                                                                | 459 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 728 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 765 ms: 1.19x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.20 sec: 1.17x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                   |
| deepcopy                   | 446 us                                                                | 407 us: 1.10x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.94 us: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| comprehensions             | 25.4 us                                                               | 25.0 us: 1.02x faster                                                   |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.29 us: 1.01x slower                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 152 ms: 1.01x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 665 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| thrift                     | 937 us                                                                | 955 us: 1.02x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.02x slower                                                  |
| float                      | 92.1 ms                                                               | 94.3 ms: 1.02x slower                                                   |
| scimark_sor                | 150 ms                                                                | 153 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 267 us: 1.03x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.51 sec: 1.03x slower                                                  |
| json_loads                 | 30.7 us                                                               | 31.6 us: 1.03x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 81.3 ms: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.89 us: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                   |
| async_generators           | 491 ms                                                                | 508 ms: 1.04x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 89.8 ms: 1.04x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.3 us: 1.04x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.5 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 134 ns: 1.06x slower                                                    |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.56 us: 1.06x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 603 ms: 1.07x slower                                                    |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.40 ms: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 5.00 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| tornado_http               | 136 ms                                                                | 148 ms: 1.09x slower                                                    |
| pyflate                    | 559 ms                                                                | 616 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.9 ms: 1.11x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.91 ms: 1.12x slower                                                   |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.12x slower                                                    |
| fannkuch                   | 443 ms                                                                | 503 ms: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 99.7 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.78 ms: 1.15x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.69 ms: 1.15x slower                                                   |
| spectral_norm              | 131 ms                                                                | 152 ms: 1.16x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 211 us: 1.17x slower                                                    |
| go                         | 157 ms                                                                | 184 ms: 1.17x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.17 ms: 1.19x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.51 sec: 1.20x slower                                                  |
| chaos                      | 71.4 ms                                                               | 87.0 ms: 1.22x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.71 sec: 1.24x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 157 ms: 1.24x slower                                                    |
| 2to3                       | 308 ms                                                                | 386 ms: 1.25x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 125 ms: 1.26x slower                                                    |
| richards_super             | 58.5 ms                                                               | 74.9 ms: 1.28x slower                                                   |
| python_startup             | 11.4 ms                                                               | 14.6 ms: 1.28x slower                                                   |
| sympy_str                  | 280 ms                                                                | 359 ms: 1.28x slower                                                    |
| django_template            | 40.7 ms                                                               | 52.2 ms: 1.28x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 80.1 ms: 1.29x slower                                                   |
| richards                   | 50.9 ms                                                               | 66.2 ms: 1.30x slower                                                   |
| regex_compile              | 137 ms                                                                | 180 ms: 1.31x slower                                                    |
| sympy_expand               | 454 ms                                                                | 597 ms: 1.32x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 82.8 ms: 1.35x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.24 sec: 1.35x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 29.2 ms: 1.35x slower                                                   |
| generators                 | 43.5 ms                                                               | 59.1 ms: 1.36x slower                                                   |
| pylint                     | 355 ms                                                                | 492 ms: 1.39x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 214 ms: 1.39x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.11 ms: 1.39x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 84.4 ms: 1.39x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.63 sec: 1.40x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.46x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.57 ms: 1.86x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 1.43 sec: 203.21x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.15x slower                                                            |

Benchmark hidden because not significant (6): coroutines, raytrace, logging_format, regex_dna, xml_etree_generate, logging_simple
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: bpe_tokeniser, sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x