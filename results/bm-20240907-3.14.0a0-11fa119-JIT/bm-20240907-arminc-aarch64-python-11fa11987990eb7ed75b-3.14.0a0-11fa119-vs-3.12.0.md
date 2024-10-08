# Results vs. 3.12.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 380 ms: 1.23x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.2 ms: 1.08x slower                                                   |
| tornado_http   | 136 ms                                                                | 147 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 457 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 570 ms: 1.36x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 429 ms: 1.34x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 555 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 748 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.15 sec: 1.22x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.1 ms: 1.03x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| regex_compile  | 137 ms                                                                | 188 ms: 1.37x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.01x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 78.7 ms: 1.00x faster                                                   |
| pickle_list          | 5.25 us                                                               | 5.28 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.26 us: 1.01x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 265 us: 1.02x slower                                                    |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 393 us: 1.08x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.90 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.1 ms: 1.24x slower                                                   |
| django_template | 40.7 ms                                                               | 51.4 ms: 1.26x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 80.1 ms: 1.32x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 457 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 570 ms: 1.36x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 429 ms: 1.34x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 555 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.3 us: 1.33x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 748 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.15 sec: 1.22x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| deepcopy                   | 446 us                                                                | 388 us: 1.15x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.80 us: 1.08x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| float                      | 92.1 ms                                                               | 89.1 ms: 1.03x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.6 us: 1.03x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.09 us: 1.03x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.42 us: 1.03x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.01x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.01x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 78.7 ms: 1.00x faster                                                   |
| pickle_list                | 5.25 us                                                               | 5.28 us: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.26 us: 1.01x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                  |
| unpickle_pure_python       | 260 us                                                                | 265 us: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| async_generators           | 491 ms                                                                | 504 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| crypto_pyaes               | 86.6 ms                                                               | 89.3 ms: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.89 us: 1.03x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 971 us: 1.04x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.34 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| json                       | 5.54 ms                                                               | 5.88 ms: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.90 ms: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                    |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.2 ms: 1.08x slower                                                   |
| tornado_http               | 136 ms                                                                | 147 ms: 1.09x slower                                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| scimark_fft                | 418 ms                                                                | 460 ms: 1.10x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.82 ms: 1.10x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 93.7 ms: 1.10x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 625 ms: 1.10x slower                                                    |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.82 ms: 1.11x slower                                                   |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.11x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 4.93 ms: 1.12x slower                                                   |
| pyflate                    | 559 ms                                                                | 627 ms: 1.12x slower                                                    |
| fannkuch                   | 443 ms                                                                | 504 ms: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 99.8 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.73 ms: 1.18x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 214 us: 1.19x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.19x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.49 sec: 1.19x slower                                                  |
| go                         | 157 ms                                                                | 188 ms: 1.20x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.19 ms: 1.20x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| 2to3                       | 308 ms                                                                | 380 ms: 1.23x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.1 ms: 1.24x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 124 ms: 1.25x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 77.7 ms: 1.25x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 77.4 ms: 1.26x slower                                                   |
| django_template            | 40.7 ms                                                               | 51.4 ms: 1.26x slower                                                   |
| chaos                      | 71.4 ms                                                               | 91.4 ms: 1.28x slower                                                   |
| richards_super             | 58.5 ms                                                               | 75.0 ms: 1.28x slower                                                   |
| sympy_str                  | 280 ms                                                                | 366 ms: 1.31x slower                                                    |
| richards                   | 50.9 ms                                                               | 66.8 ms: 1.31x slower                                                   |
| pylint                     | 355 ms                                                                | 466 ms: 1.31x slower                                                    |
| generators                 | 43.5 ms                                                               | 57.3 ms: 1.32x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 28.5 ms: 1.32x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 80.1 ms: 1.32x slower                                                   |
| sympy_expand               | 454 ms                                                                | 606 ms: 1.34x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                                  |
| regex_compile              | 137 ms                                                                | 188 ms: 1.37x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.59 sec: 1.38x slower                                                  |
| sympy_sum                  | 154 ms                                                                | 214 ms: 1.38x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.46x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (5): raytrace, regex_dna, scimark_sor, pickle_dict, asyncio_websockets
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x