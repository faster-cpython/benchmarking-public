# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.075x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 382 ms: 1.24x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.9 ms: 1.11x slower                                                   |
| tornado_http   | 136 ms                                                                | 150 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 442 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 426 ms: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 556 ms: 1.33x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 589 ms: 1.32x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 748 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 735 ms: 1.20x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| regex_compile  | 137 ms                                                                | 196 ms: 1.42x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.20 us: 1.01x faster                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.4 us: 1.02x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 38.3 us: 1.03x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 267 us: 1.03x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.42 us: 1.04x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.3 us: 1.04x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 392 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 51.4 ms: 1.26x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.0 ms: 1.28x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 80.8 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 442 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 426 ms: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 556 ms: 1.33x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 589 ms: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 748 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 735 ms: 1.20x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                   |
| deepcopy                   | 446 us                                                                | 401 us: 1.11x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.83 us: 1.07x faster                                                   |
| float                      | 92.1 ms                                                               | 87.5 ms: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.05x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.5 us: 1.04x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.46 us: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.20 us: 1.02x faster                                                   |
| raytrace                   | 353 ms                                                                | 348 ms: 1.02x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.20 us: 1.01x faster                                                   |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                                   |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 148 ms: 1.02x slower                                                    |
| json_loads                 | 30.7 us                                                               | 31.4 us: 1.02x slower                                                   |
| json                       | 5.54 ms                                                               | 5.67 ms: 1.02x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.3 us: 1.03x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 267 us: 1.03x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.52 sec: 1.03x slower                                                  |
| thrift                     | 937 us                                                                | 970 us: 1.03x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 89.7 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                  |
| unpickle_list              | 6.17 us                                                               | 6.42 us: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 512 ms: 1.04x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.3 us: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.39 ms: 1.07x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.57 ms: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                    |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.6 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| scimark_fft                | 418 ms                                                                | 459 ms: 1.10x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| tornado_http               | 136 ms                                                                | 150 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.9 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.85 ms: 1.11x slower                                                   |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 629 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 508 ms: 1.15x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.16x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.10 ms: 1.16x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| pyflate                    | 559 ms                                                                | 657 ms: 1.17x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 213 us: 1.18x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 150 ms: 1.19x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.76 ms: 1.20x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.20x slower                                                   |
| go                         | 157 ms                                                                | 190 ms: 1.21x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.53 sec: 1.21x slower                                                  |
| sqlglot_transpile          | 1.83 ms                                                               | 2.23 ms: 1.22x slower                                                   |
| 2to3                       | 308 ms                                                                | 382 ms: 1.24x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.6 ms: 1.25x slower                                                   |
| django_template            | 40.7 ms                                                               | 51.4 ms: 1.26x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 126 ms: 1.27x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 35.0 ms: 1.28x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 78.5 ms: 1.28x slower                                                   |
| chaos                      | 71.4 ms                                                               | 92.2 ms: 1.29x slower                                                   |
| richards_super             | 58.5 ms                                                               | 75.9 ms: 1.30x slower                                                   |
| richards                   | 50.9 ms                                                               | 66.3 ms: 1.30x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 28.5 ms: 1.32x slower                                                   |
| sympy_str                  | 280 ms                                                                | 369 ms: 1.32x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                  |
| dulwich_log                | 62.0 ms                                                               | 82.0 ms: 1.32x slower                                                   |
| generators                 | 43.5 ms                                                               | 57.6 ms: 1.32x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 80.8 ms: 1.33x slower                                                   |
| pylint                     | 355 ms                                                                | 479 ms: 1.35x slower                                                    |
| sympy_expand               | 454 ms                                                                | 613 ms: 1.35x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                                  |
| sympy_sum                  | 154 ms                                                                | 211 ms: 1.37x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.61 sec: 1.39x slower                                                  |
| regex_compile              | 137 ms                                                                | 196 ms: 1.42x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.3 ms: 1.48x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, mako, asyncio_websockets, xml_etree_process
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.075x slower
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x