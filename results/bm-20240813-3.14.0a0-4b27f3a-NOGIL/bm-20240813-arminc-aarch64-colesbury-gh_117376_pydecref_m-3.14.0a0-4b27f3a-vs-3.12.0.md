# Results vs. 3.12.0

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-aarch64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.55x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 513 ms: 1.66x slower                                                       |
| docutils       | 2.98 sec                                                              | 4.09 sec: 1.37x slower                                                     |
| html5lib       | 65.1 ms                                                               | 120 ms: 1.85x slower                                                       |
| tornado_http   | 136 ms                                                                | 206 ms: 1.52x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.59x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 683 ms: 1.08x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 739 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.34 sec: 1.05x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 557 ms: 1.04x faster                                                       |
| async_tree_none            | 624 ms                                                                | 607 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 867 ms: 1.02x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.40 sec: 1.01x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                       |
| float          | 92.1 ms                                                               | 208 ms: 2.26x slower                                                       |
| nbody          | 105 ms                                                                | 281 ms: 2.69x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.83x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.51 ms: 1.03x faster                                                      |
| regex_dna      | 254 ms                                                                | 259 ms: 1.02x slower                                                       |
| regex_v8       | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                      |
| regex_compile  | 137 ms                                                                | 254 ms: 1.85x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 150 ms                                                                | 158 ms: 1.05x slower                                                       |
| json_loads           | 30.7 us                                                               | 39.1 us: 1.27x slower                                                      |
| xml_etree_generate   | 112 ms                                                                | 161 ms: 1.44x slower                                                       |
| json_dumps           | 12.3 ms                                                               | 17.8 ms: 1.45x slower                                                      |
| tomli_loads          | 2.59 sec                                                              | 4.20 sec: 1.62x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 131 ms: 1.66x slower                                                       |
| unpickle_pure_python | 260 us                                                                | 541 us: 2.08x slower                                                       |
| pickle_pure_python   | 365 us                                                                | 783 us: 2.14x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.47x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.9 ms: 1.42x slower                                                      |
| python_startup         | 11.4 ms                                                               | 17.8 ms: 1.57x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.49x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 104 ms: 1.72x slower                                                       |
| genshi_text     | 27.4 ms                                                               | 53.9 ms: 1.97x slower                                                      |
| django_template | 40.7 ms                                                               | 82.2 ms: 2.02x slower                                                      |
| mako            | 12.9 ms                                                               | 29.0 ms: 2.25x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.98x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.44 ms: 1.28x faster                                                      |
| create_gc_cycles           | 1.92 ms                                                               | 1.61 ms: 1.19x faster                                                      |
| async_tree_memoization_tg  | 740 ms                                                                | 683 ms: 1.08x faster                                                       |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 739 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.34 sec: 1.05x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 557 ms: 1.04x faster                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.51 ms: 1.03x faster                                                      |
| async_tree_none            | 624 ms                                                                | 607 ms: 1.03x faster                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 6.91 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 867 ms: 1.02x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.40 sec: 1.01x faster                                                     |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                       |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                       |
| regex_dna                  | 254 ms                                                                | 259 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 150 ms                                                                | 158 ms: 1.05x slower                                                       |
| pathlib                    | 24.5 ms                                                               | 26.4 ms: 1.08x slower                                                      |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.43 sec: 1.11x slower                                                     |
| asyncio_tcp                | 566 ms                                                                | 661 ms: 1.17x slower                                                       |
| regex_v8                   | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                      |
| deepcopy                   | 446 us                                                                | 560 us: 1.26x slower                                                       |
| mdp                        | 3.41 sec                                                              | 4.32 sec: 1.27x slower                                                     |
| json_loads                 | 30.7 us                                                               | 39.1 us: 1.27x slower                                                      |
| json                       | 5.54 ms                                                               | 7.09 ms: 1.28x slower                                                      |
| generators                 | 43.5 ms                                                               | 56.6 ms: 1.30x slower                                                      |
| coroutines                 | 29.0 ms                                                               | 39.1 ms: 1.35x slower                                                      |
| async_generators           | 491 ms                                                                | 668 ms: 1.36x slower                                                       |
| scimark_fft                | 418 ms                                                                | 572 ms: 1.37x slower                                                       |
| docutils                   | 2.98 sec                                                              | 4.09 sec: 1.37x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 11.9 ms: 1.42x slower                                                      |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.79 ms: 1.42x slower                                                      |
| pylint                     | 355 ms                                                                | 507 ms: 1.43x slower                                                       |
| xml_etree_generate         | 112 ms                                                                | 161 ms: 1.44x slower                                                       |
| json_dumps                 | 12.3 ms                                                               | 17.8 ms: 1.45x slower                                                      |
| deepcopy_memo              | 49.6 us                                                               | 72.5 us: 1.46x slower                                                      |
| deepcopy_reduce            | 4.10 us                                                               | 6.00 us: 1.46x slower                                                      |
| telco                      | 8.51 ms                                                               | 12.8 ms: 1.50x slower                                                      |
| meteor_contest             | 112 ms                                                                | 169 ms: 1.51x slower                                                       |
| coverage                   | 87.3 ms                                                               | 132 ms: 1.52x slower                                                       |
| tornado_http               | 136 ms                                                                | 206 ms: 1.52x slower                                                       |
| nqueens                    | 99.2 ms                                                               | 151 ms: 1.52x slower                                                       |
| python_startup             | 11.4 ms                                                               | 17.8 ms: 1.57x slower                                                      |
| crypto_pyaes               | 86.6 ms                                                               | 136 ms: 1.57x slower                                                       |
| sympy_integrate            | 21.6 ms                                                               | 34.8 ms: 1.61x slower                                                      |
| bench_thread_pool          | 1.31 ms                                                               | 2.11 ms: 1.61x slower                                                      |
| comprehensions             | 25.4 us                                                               | 41.0 us: 1.62x slower                                                      |
| tomli_loads                | 2.59 sec                                                              | 4.20 sec: 1.62x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 2.06 sec: 1.64x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 131 ms: 1.66x slower                                                       |
| 2to3                       | 308 ms                                                                | 513 ms: 1.66x slower                                                       |
| fannkuch                   | 443 ms                                                                | 738 ms: 1.66x slower                                                       |
| genshi_xml                 | 60.6 ms                                                               | 104 ms: 1.72x slower                                                       |
| spectral_norm              | 131 ms                                                                | 227 ms: 1.74x slower                                                       |
| pyflate                    | 559 ms                                                                | 1.01 sec: 1.80x slower                                                     |
| thrift                     | 937 us                                                                | 1.70 ms: 1.82x slower                                                      |
| sqlglot_normalize          | 126 ms                                                                | 230 ms: 1.83x slower                                                       |
| sympy_str                  | 280 ms                                                                | 516 ms: 1.84x slower                                                       |
| regex_compile              | 137 ms                                                                | 254 ms: 1.85x slower                                                       |
| html5lib                   | 65.1 ms                                                               | 120 ms: 1.85x slower                                                       |
| logging_format             | 8.34 us                                                               | 15.6 us: 1.87x slower                                                      |
| logging_simple             | 7.63 us                                                               | 14.4 us: 1.88x slower                                                      |
| sqlglot_optimize           | 61.3 ms                                                               | 116 ms: 1.89x slower                                                       |
| pprint_safe_repr           | 916 ms                                                                | 1.75 sec: 1.91x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 3.61 sec: 1.92x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 347 us: 1.92x slower                                                       |
| genshi_text                | 27.4 ms                                                               | 53.9 ms: 1.97x slower                                                      |
| django_template            | 40.7 ms                                                               | 82.2 ms: 2.02x slower                                                      |
| scimark_monte_carlo        | 85.1 ms                                                               | 173 ms: 2.03x slower                                                       |
| sympy_sum                  | 154 ms                                                                | 316 ms: 2.05x slower                                                       |
| unpickle_pure_python       | 260 us                                                                | 541 us: 2.08x slower                                                       |
| sympy_expand               | 454 ms                                                                | 952 ms: 2.10x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 783 us: 2.14x slower                                                       |
| logging_silent             | 127 ns                                                                | 279 ns: 2.20x slower                                                       |
| chaos                      | 71.4 ms                                                               | 158 ms: 2.21x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 15.6 ms: 2.24x slower                                                      |
| mako                       | 12.9 ms                                                               | 29.0 ms: 2.25x slower                                                      |
| scimark_sor                | 150 ms                                                                | 336 ms: 2.25x slower                                                       |
| float                      | 92.1 ms                                                               | 208 ms: 2.26x slower                                                       |
| raytrace                   | 353 ms                                                                | 803 ms: 2.27x slower                                                       |
| richards                   | 50.9 ms                                                               | 116 ms: 2.27x slower                                                       |
| sqlglot_transpile          | 1.83 ms                                                               | 4.30 ms: 2.35x slower                                                      |
| richards_super             | 58.5 ms                                                               | 140 ms: 2.40x slower                                                       |
| scimark_lu                 | 146 ms                                                                | 353 ms: 2.42x slower                                                       |
| sqlglot_parse              | 1.46 ms                                                               | 3.59 ms: 2.45x slower                                                      |
| nbody                      | 105 ms                                                                | 281 ms: 2.69x slower                                                       |
| go                         | 157 ms                                                                | 442 ms: 2.81x slower                                                       |
| deltablue                  | 4.12 ms                                                               | 12.5 ms: 3.05x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.55x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240813-3.14.0a0-4b27f3a-NOGIL/bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.42x
- 95% likely to have a slowdown of 1.39x
- 99% likely to have a slowdown of 1.34x

# Memory
- memory change: 1.07x