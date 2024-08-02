# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 353 ms: 1.15x slower                                                     |
| chameleon      | 8.81 ms                                                               | 10.0 ms: 1.14x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.50 sec: 1.17x slower                                                   |
| html5lib       | 65.1 ms                                                               | 72.1 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 519 ms: 1.20x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 629 ms: 1.18x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 491 ms: 1.17x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 684 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.26 sec: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 793 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 828 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.14x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                     |
| float          | 92.1 ms                                                               | 113 ms: 1.22x slower                                                     |
| nbody          | 105 ms                                                                | 141 ms: 1.35x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                    |
| regex_compile  | 137 ms                                                                | 166 ms: 1.21x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.37 us: 1.02x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.2 us: 1.05x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.62 us: 1.07x slower                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 162 ms: 1.07x slower                                                     |
| unpickle             | 18.5 us                                                               | 19.9 us: 1.08x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 87.0 ms: 1.10x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 124 ms: 1.10x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 13.7 ms: 1.11x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 3.11 sec: 1.20x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 448 us: 1.23x slower                                                     |
| unpickle_pure_python | 260 us                                                                | 348 us: 1.34x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.09x slower                                                             |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                    |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 48.9 ms: 1.20x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 76.1 ms: 1.26x slower                                                    |
| mako            | 12.9 ms                                                               | 16.4 ms: 1.27x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 36.2 ms: 1.32x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.26x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 519 ms: 1.20x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 629 ms: 1.18x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 491 ms: 1.17x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 684 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.26 sec: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 793 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 828 ms: 1.10x faster                                                     |
| generators                 | 43.5 ms                                                               | 40.2 ms: 1.08x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.4 ms: 1.05x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.32 us: 1.04x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.02 us: 1.04x faster                                                    |
| raytrace                   | 353 ms                                                                | 340 ms: 1.04x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                     |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                     |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.37 us: 1.02x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                   |
| dask                       | 376 ms                                                                | 389 ms: 1.03x slower                                                     |
| thrift                     | 937 us                                                                | 969 us: 1.03x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.56 sec: 1.04x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.4 ms: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.2 us: 1.05x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 596 ms: 1.05x slower                                                     |
| json                       | 5.54 ms                                                               | 5.84 ms: 1.05x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.99 us: 1.06x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 65.9 ms: 1.06x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.62 us: 1.07x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 162 ms: 1.07x slower                                                     |
| unpickle                   | 18.5 us                                                               | 19.9 us: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                    |
| async_generators           | 491 ms                                                                | 538 ms: 1.10x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 87.0 ms: 1.10x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 124 ms: 1.10x slower                                                     |
| aiohttp                    | 1.16 ms                                                               | 1.28 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 72.1 ms: 1.11x slower                                                    |
| pylint                     | 355 ms                                                                | 393 ms: 1.11x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.11x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 173 ms: 1.12x slower                                                     |
| sympy_str                  | 280 ms                                                                | 314 ms: 1.12x slower                                                     |
| chameleon                  | 8.81 ms                                                               | 10.0 ms: 1.14x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.06 ms: 1.14x slower                                                    |
| 2to3                       | 308 ms                                                                | 353 ms: 1.15x slower                                                     |
| sympy_expand               | 454 ms                                                                | 521 ms: 1.15x slower                                                     |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.10 ms: 1.16x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.70 ms: 1.16x slower                                                    |
| comprehensions             | 25.4 us                                                               | 29.6 us: 1.17x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.78 us: 1.17x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 101 ms: 1.17x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.50 sec: 1.17x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.15 ms: 1.18x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 72.7 ms: 1.18x slower                                                    |
| meteor_contest             | 112 ms                                                                | 133 ms: 1.19x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 150 ms: 1.19x slower                                                     |
| gunicorn                   | 1.14 ms                                                               | 1.35 ms: 1.19x slower                                                    |
| chaos                      | 71.4 ms                                                               | 85.2 ms: 1.19x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.0 ms: 1.20x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.11 sec: 1.20x slower                                                   |
| django_template            | 40.7 ms                                                               | 48.9 ms: 1.20x slower                                                    |
| regex_compile              | 137 ms                                                                | 166 ms: 1.21x slower                                                     |
| deepcopy                   | 446 us                                                                | 539 us: 1.21x slower                                                     |
| float                      | 92.1 ms                                                               | 113 ms: 1.22x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 448 us: 1.23x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 222 us: 1.23x slower                                                     |
| fannkuch                   | 443 ms                                                                | 547 ms: 1.23x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 5.13 ms: 1.25x slower                                                    |
| go                         | 157 ms                                                                | 196 ms: 1.25x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 76.1 ms: 1.26x slower                                                    |
| richards_super             | 58.5 ms                                                               | 73.6 ms: 1.26x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.41 ms: 1.26x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.26x slower                                                   |
| pyflate                    | 559 ms                                                                | 706 ms: 1.26x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.27x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.8 ms: 1.27x slower                                                    |
| mako                       | 12.9 ms                                                               | 16.4 ms: 1.27x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 128 ms: 1.29x slower                                                     |
| scimark_fft                | 418 ms                                                                | 543 ms: 1.30x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.05 ms: 1.30x slower                                                    |
| richards                   | 50.9 ms                                                               | 66.4 ms: 1.30x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 36.2 ms: 1.32x slower                                                    |
| scimark_sor                | 150 ms                                                                | 199 ms: 1.33x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 348 us: 1.34x slower                                                     |
| nbody                      | 105 ms                                                                | 141 ms: 1.35x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 116 ms: 1.36x slower                                                     |
| spectral_norm              | 131 ms                                                                | 183 ms: 1.40x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 72.0 us: 1.45x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 211 ms: 1.45x slower                                                     |
| logging_silent             | 127 ns                                                                | 188 ns: 1.48x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 10.5 ms: 1.50x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (4): tornado_http, mypy2, pickle, asyncio_websockets
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.93x