# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.03x faster
- HPT reliability: 98.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 296 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                  |
| tornado_http   | 136 ms                                                                | 125 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 424 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 555 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 248 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 256 us: 1.01x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 38.2 us: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.6 us: 1.03x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.05x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.55 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_iterparse, xml_etree_generate, pickle_list, pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.4 ms: 1.02x faster                                                   |
| genshi_text     | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| django_template | 40.7 ms                                                               | 42.5 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 424 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 563 ms: 1.38x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                                    |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 555 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.8 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.48 us: 1.18x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 20.9 ms: 1.18x faster                                                   |
| raytrace                   | 353 ms                                                                | 305 ms: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.98 us: 1.09x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.63 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| tornado_http               | 136 ms                                                                | 125 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| sympy_str                  | 280 ms                                                                | 263 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.1 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.94 ms: 1.05x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 296 ms: 1.04x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.77 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| chaos                      | 71.4 ms                                                               | 69.6 ms: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 248 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                  |
| async_generators           | 491 ms                                                                | 481 ms: 1.02x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 59.4 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 256 us: 1.01x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.9 ms: 1.01x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 61.7 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.89 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| pyflate                    | 559 ms                                                                | 564 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                  |
| sympy_expand               | 454 ms                                                                | 459 ms: 1.01x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.14 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.2 us: 1.02x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.9 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.19 ms: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.6 us: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.41 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.5 ms: 1.04x slower                                                   |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 441 ms: 1.05x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.05x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.00 us: 1.06x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.55 us: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.1 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.12 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.5 ms: 1.23x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (17): asyncio_tcp, sqlglot_parse, html5lib, nqueens, xml_etree_iterparse, thrift, json, xml_etree_generate, pickle_list, meteor_contest, asyncio_websockets, asyncio_tcp_ssl, pickle_pure_python, pprint_safe_repr, sqlglot_normalize, pylint, xml_etree_process
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 98.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x