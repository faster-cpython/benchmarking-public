# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 359 ms: 1.16x slower                                                    |
| chameleon      | 8.81 ms                                                               | 10.2 ms: 1.16x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                  |
| html5lib       | 65.1 ms                                                               | 74.4 ms: 1.14x slower                                                   |
| tornado_http   | 136 ms                                                                | 138 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 529 ms: 1.18x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 640 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 501 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 697 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 809 ms: 1.09x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.30 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 850 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| float          | 92.1 ms                                                               | 117 ms: 1.27x slower                                                    |
| nbody          | 105 ms                                                                | 151 ms: 1.44x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 257 ms: 1.01x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 171 ms: 1.25x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 5.25 us                                                               | 5.32 us: 1.01x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.05x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.51 us: 1.06x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 162 ms: 1.08x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 88.2 ms: 1.12x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 128 ms: 1.14x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 3.25 sec: 1.25x slower                                                  |
| pickle_pure_python   | 365 us                                                                | 467 us: 1.28x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 367 us: 1.41x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.11x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.57 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.8 ms: 1.12x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 50.1 ms: 1.23x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 78.5 ms: 1.30x slower                                                   |
| mako            | 12.9 ms                                                               | 17.3 ms: 1.34x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 37.6 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.31x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 529 ms: 1.18x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 640 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 501 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 697 ms: 1.11x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.3 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 809 ms: 1.09x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.30 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 850 ms: 1.07x faster                                                    |
| generators                 | 43.5 ms                                                               | 40.7 ms: 1.07x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.01 us: 1.04x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.36 us: 1.04x faster                                                   |
| raytrace                   | 353 ms                                                                | 348 ms: 1.02x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.32 us: 1.01x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| regex_dna                  | 254 ms                                                                | 257 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| tornado_http               | 136 ms                                                                | 138 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.23 sec: 1.02x slower                                                  |
| python_startup_no_site     | 8.37 ms                                                               | 8.57 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| dask                       | 376 ms                                                                | 389 ms: 1.03x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 588 ms: 1.04x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.93 us: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 515 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.83 ms: 1.05x slower                                                   |
| thrift                     | 937 us                                                                | 987 us: 1.05x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.60 sec: 1.05x slower                                                  |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.05x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.51 us: 1.06x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.8 ms: 1.06x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 66.1 ms: 1.07x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 162 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.40 sec: 1.11x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 88.2 ms: 1.12x slower                                                   |
| python_startup             | 11.4 ms                                                               | 12.8 ms: 1.12x slower                                                   |
| pylint                     | 355 ms                                                                | 401 ms: 1.13x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 176 ms: 1.14x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 128 ms: 1.14x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 74.4 ms: 1.14x slower                                                   |
| sympy_str                  | 280 ms                                                                | 321 ms: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 10.2 ms: 1.16x slower                                                   |
| 2to3                       | 308 ms                                                                | 359 ms: 1.16x slower                                                    |
| sympy_expand               | 454 ms                                                                | 533 ms: 1.17x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.19x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 72.9 ms: 1.19x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.88 us: 1.19x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.28 ms: 1.20x slower                                                   |
| meteor_contest             | 112 ms                                                                | 135 ms: 1.20x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.62 ms: 1.22x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 106 ms: 1.22x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.6 ms: 1.23x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.1 ms: 1.23x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.26 ms: 1.24x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.81 ms: 1.24x slower                                                   |
| deepcopy                   | 446 us                                                                | 553 us: 1.24x slower                                                    |
| regex_compile              | 137 ms                                                                | 171 ms: 1.25x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.39 ms: 1.25x slower                                                   |
| chaos                      | 71.4 ms                                                               | 89.4 ms: 1.25x slower                                                   |
| comprehensions             | 25.4 us                                                               | 31.8 us: 1.25x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 3.25 sec: 1.25x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 226 us: 1.25x slower                                                    |
| float                      | 92.1 ms                                                               | 117 ms: 1.27x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.8 ms: 1.27x slower                                                   |
| richards_super             | 58.5 ms                                                               | 74.7 ms: 1.28x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 467 us: 1.28x slower                                                    |
| go                         | 157 ms                                                                | 202 ms: 1.29x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 5.31 ms: 1.29x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 78.5 ms: 1.30x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.47 sec: 1.31x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.21 sec: 1.32x slower                                                  |
| scimark_fft                | 418 ms                                                                | 558 ms: 1.33x slower                                                    |
| mako                       | 12.9 ms                                                               | 17.3 ms: 1.34x slower                                                   |
| richards                   | 50.9 ms                                                               | 68.2 ms: 1.34x slower                                                   |
| fannkuch                   | 443 ms                                                                | 598 ms: 1.35x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.35 ms: 1.35x slower                                                   |
| scimark_sor                | 150 ms                                                                | 202 ms: 1.35x slower                                                    |
| pyflate                    | 559 ms                                                                | 760 ms: 1.36x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 136 ms: 1.37x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 37.6 ms: 1.37x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 119 ms: 1.40x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 367 us: 1.41x slower                                                    |
| nbody                      | 105 ms                                                                | 151 ms: 1.44x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 211 ms: 1.45x slower                                                    |
| spectral_norm              | 131 ms                                                                | 194 ms: 1.48x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 75.9 us: 1.53x slower                                                   |
| logging_silent             | 127 ns                                                                | 197 ns: 1.56x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 11.3 ms: 1.62x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.15x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.93x