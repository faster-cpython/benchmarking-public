# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 357 ms: 1.16x slower                                                     |
| chameleon      | 8.81 ms                                                               | 10.3 ms: 1.16x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.60 sec: 1.21x slower                                                   |
| html5lib       | 65.1 ms                                                               | 73.8 ms: 1.13x slower                                                    |
| tornado_http   | 136 ms                                                                | 139 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 522 ms: 1.19x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 637 ms: 1.16x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 505 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.14x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 685 ms: 1.13x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.27 sec: 1.11x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 827 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 807 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.13x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 236 ms: 1.02x slower                                                     |
| float          | 92.1 ms                                                               | 119 ms: 1.29x slower                                                     |
| nbody          | 105 ms                                                                | 152 ms: 1.46x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 258 ms: 1.02x slower                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                    |
| regex_compile  | 137 ms                                                                | 172 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_list          | 5.25 us                                                               | 5.31 us: 1.01x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 37.9 us: 1.02x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.1 us: 1.05x slower                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 162 ms: 1.07x slower                                                     |
| unpickle             | 18.5 us                                                               | 19.9 us: 1.08x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.68 us: 1.08x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 90.9 ms: 1.15x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 130 ms: 1.16x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.23 sec: 1.25x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 467 us: 1.28x slower                                                     |
| unpickle_pure_python | 260 us                                                                | 364 us: 1.40x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                    |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 51.1 ms: 1.26x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 78.6 ms: 1.30x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 36.8 ms: 1.34x slower                                                    |
| mako            | 12.9 ms                                                               | 17.5 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.31x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 522 ms: 1.19x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 637 ms: 1.16x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 505 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.14x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 685 ms: 1.13x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.27 sec: 1.11x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 827 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 807 ms: 1.10x faster                                                     |
| generators                 | 43.5 ms                                                               | 40.7 ms: 1.07x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.4 ms: 1.05x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.43 us: 1.03x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.16 us: 1.02x faster                                                    |
| raytrace                   | 353 ms                                                                | 347 ms: 1.02x faster                                                     |
| pickle_list                | 5.25 us                                                               | 5.31 us: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.02x slower                                                     |
| regex_dna                  | 254 ms                                                                | 258 ms: 1.02x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 37.9 us: 1.02x slower                                                    |
| tornado_http               | 136 ms                                                                | 139 ms: 1.02x slower                                                     |
| thrift                     | 937 us                                                                | 969 us: 1.03x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                   |
| dask                       | 376 ms                                                                | 392 ms: 1.04x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 30.3 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.1 us: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                    |
| async_generators           | 491 ms                                                                | 517 ms: 1.05x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.61 sec: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                    |
| json                       | 5.54 ms                                                               | 5.89 ms: 1.06x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 602 ms: 1.06x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.04 us: 1.07x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 162 ms: 1.07x slower                                                     |
| unpickle                   | 18.5 us                                                               | 19.9 us: 1.08x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 66.7 ms: 1.08x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.68 us: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.10x slower                                                   |
| pylint                     | 355 ms                                                                | 395 ms: 1.11x slower                                                     |
| aiohttp                    | 1.16 ms                                                               | 1.31 ms: 1.13x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 73.8 ms: 1.13x slower                                                    |
| sympy_str                  | 280 ms                                                                | 318 ms: 1.14x slower                                                     |
| coverage                   | 87.3 ms                                                               | 99.3 ms: 1.14x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 176 ms: 1.14x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 90.9 ms: 1.15x slower                                                    |
| sympy_expand               | 454 ms                                                                | 523 ms: 1.15x slower                                                     |
| 2to3                       | 308 ms                                                                | 357 ms: 1.16x slower                                                     |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 130 ms: 1.16x slower                                                     |
| chameleon                  | 8.81 ms                                                               | 10.3 ms: 1.16x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.21 ms: 1.19x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 73.0 ms: 1.19x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.88 us: 1.19x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 151 ms: 1.20x slower                                                     |
| meteor_contest             | 112 ms                                                                | 135 ms: 1.21x slower                                                     |
| gunicorn                   | 1.14 ms                                                               | 1.37 ms: 1.21x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.60 sec: 1.21x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 8.58 ms: 1.22x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 106 ms: 1.22x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 26.6 ms: 1.23x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.25 ms: 1.23x slower                                                    |
| comprehensions             | 25.4 us                                                               | 31.5 us: 1.24x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.23 sec: 1.25x slower                                                   |
| deepcopy                   | 446 us                                                                | 555 us: 1.25x slower                                                     |
| regex_compile              | 137 ms                                                                | 172 ms: 1.25x slower                                                     |
| chaos                      | 71.4 ms                                                               | 89.3 ms: 1.25x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.83 ms: 1.25x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.41 ms: 1.26x slower                                                    |
| django_template            | 40.7 ms                                                               | 51.1 ms: 1.26x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 227 us: 1.26x slower                                                     |
| go                         | 157 ms                                                                | 199 ms: 1.27x slower                                                     |
| telco                      | 8.51 ms                                                               | 10.9 ms: 1.28x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 467 us: 1.28x slower                                                     |
| float                      | 92.1 ms                                                               | 119 ms: 1.29x slower                                                     |
| richards_super             | 58.5 ms                                                               | 75.4 ms: 1.29x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 5.31 ms: 1.29x slower                                                    |
| fannkuch                   | 443 ms                                                                | 574 ms: 1.29x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 78.6 ms: 1.30x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.47 sec: 1.31x slower                                                   |
| pyflate                    | 559 ms                                                                | 738 ms: 1.32x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.21 sec: 1.32x slower                                                   |
| scimark_fft                | 418 ms                                                                | 558 ms: 1.33x slower                                                     |
| scimark_sor                | 150 ms                                                                | 200 ms: 1.34x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 36.8 ms: 1.34x slower                                                    |
| richards                   | 50.9 ms                                                               | 68.9 ms: 1.35x slower                                                    |
| mako                       | 12.9 ms                                                               | 17.5 ms: 1.35x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 134 ms: 1.35x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.41 ms: 1.36x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 364 us: 1.40x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 120 ms: 1.42x slower                                                     |
| nbody                      | 105 ms                                                                | 152 ms: 1.46x slower                                                     |
| spectral_norm              | 131 ms                                                                | 191 ms: 1.46x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 215 ms: 1.48x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 75.8 us: 1.53x slower                                                    |
| logging_silent             | 127 ns                                                                | 199 ns: 1.57x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 11.3 ms: 1.61x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.15x slower                                                             |

Benchmark hidden because not significant (4): mypy2, xml_etree_parse, asyncio_websockets, pickle
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.94x