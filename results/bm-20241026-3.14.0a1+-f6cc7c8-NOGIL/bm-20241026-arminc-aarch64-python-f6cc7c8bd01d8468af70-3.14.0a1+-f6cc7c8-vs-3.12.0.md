# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.362x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.39x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 512 ms: 1.66x slower                                                     |
| docutils       | 2.98 sec                                                              | 4.09 sec: 1.37x slower                                                   |
| html5lib       | 65.1 ms                                                               | 119 ms: 1.83x slower                                                     |
| tornado_http   | 136 ms                                                                | 205 ms: 1.51x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.58x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization    | 777 ms                                                                | 742 ms: 1.05x faster                                                     |
| async_tree_memoization_tg | 740 ms                                                                | 710 ms: 1.04x faster                                                     |
| async_tree_io_tg          | 1.40 sec                                                              | 1.36 sec: 1.03x faster                                                   |
| async_tree_none           | 624 ms                                                                | 608 ms: 1.03x faster                                                     |
| async_tree_io             | 1.41 sec                                                              | 1.39 sec: 1.02x faster                                                   |
| async_tree_none_tg        | 577 ms                                                                | 583 ms: 1.01x slower                                                     |
| Geometric mean            | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 209 ms: 2.27x slower                                                     |
| nbody          | 105 ms                                                                | 286 ms: 2.74x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.84x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.48 ms: 1.04x faster                                                    |
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.9 ms: 1.16x slower                                                    |
| regex_compile  | 137 ms                                                                | 250 ms: 1.82x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 153 ms: 1.02x slower                                                     |
| json_loads           | 30.7 us                                                               | 37.3 us: 1.21x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 158 ms: 1.41x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 18.9 ms: 1.54x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 127 ms: 1.61x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 4.19 sec: 1.62x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 532 us: 2.05x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 778 us: 2.13x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.45x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.4 ms: 1.79x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.61x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 101 ms: 1.67x slower                                                     |
| genshi_text     | 27.4 ms                                                               | 51.4 ms: 1.88x slower                                                    |
| django_template | 40.7 ms                                                               | 80.6 ms: 1.98x slower                                                    |
| mako            | 12.9 ms                                                               | 29.2 ms: 2.26x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.94x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse           | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| async_tree_memoization    | 777 ms                                                                | 742 ms: 1.05x faster                                                     |
| async_tree_memoization_tg | 740 ms                                                                | 710 ms: 1.04x faster                                                     |
| regex_effbot              | 4.64 ms                                                               | 4.48 ms: 1.04x faster                                                    |
| async_tree_io_tg          | 1.40 sec                                                              | 1.36 sec: 1.03x faster                                                   |
| async_tree_none           | 624 ms                                                                | 608 ms: 1.03x faster                                                     |
| async_tree_io             | 1.41 sec                                                              | 1.39 sec: 1.02x faster                                                   |
| regex_dna                 | 254 ms                                                                | 251 ms: 1.01x faster                                                     |
| async_tree_none_tg        | 577 ms                                                                | 583 ms: 1.01x slower                                                     |
| xml_etree_iterparse       | 150 ms                                                                | 153 ms: 1.02x slower                                                     |
| asyncio_websockets        | 658 ms                                                                | 673 ms: 1.02x slower                                                     |
| pathlib                   | 24.5 ms                                                               | 26.1 ms: 1.06x slower                                                    |
| regex_v8                  | 28.3 ms                                                               | 32.9 ms: 1.16x slower                                                    |
| deepcopy                  | 446 us                                                                | 536 us: 1.20x slower                                                     |
| json_loads                | 30.7 us                                                               | 37.3 us: 1.21x slower                                                    |
| json                      | 5.54 ms                                                               | 6.75 ms: 1.22x slower                                                    |
| mdp                       | 3.41 sec                                                              | 4.31 sec: 1.26x slower                                                   |
| create_gc_cycles          | 1.92 ms                                                               | 2.56 ms: 1.34x slower                                                    |
| async_generators          | 491 ms                                                                | 658 ms: 1.34x slower                                                     |
| scimark_fft               | 418 ms                                                                | 569 ms: 1.36x slower                                                     |
| generators                | 43.5 ms                                                               | 59.3 ms: 1.36x slower                                                    |
| docutils                  | 2.98 sec                                                              | 4.09 sec: 1.37x slower                                                   |
| coroutines                | 29.0 ms                                                               | 40.0 ms: 1.38x slower                                                    |
| deepcopy_memo             | 49.6 us                                                               | 69.5 us: 1.40x slower                                                    |
| xml_etree_generate        | 112 ms                                                                | 158 ms: 1.41x slower                                                     |
| scimark_sparse_mat_mult   | 6.19 ms                                                               | 8.82 ms: 1.42x slower                                                    |
| deepcopy_reduce           | 4.10 us                                                               | 5.84 us: 1.42x slower                                                    |
| pylint                    | 355 ms                                                                | 507 ms: 1.43x slower                                                     |
| python_startup_no_site    | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                                    |
| telco                     | 8.51 ms                                                               | 12.6 ms: 1.48x slower                                                    |
| meteor_contest            | 112 ms                                                                | 166 ms: 1.48x slower                                                     |
| bench_thread_pool         | 1.31 ms                                                               | 1.96 ms: 1.50x slower                                                    |
| tornado_http              | 136 ms                                                                | 205 ms: 1.51x slower                                                     |
| coverage                  | 87.3 ms                                                               | 133 ms: 1.52x slower                                                     |
| json_dumps                | 12.3 ms                                                               | 18.9 ms: 1.54x slower                                                    |
| nqueens                   | 99.2 ms                                                               | 153 ms: 1.54x slower                                                     |
| dulwich_log               | 62.0 ms                                                               | 95.8 ms: 1.55x slower                                                    |
| xml_etree_process         | 79.0 ms                                                               | 127 ms: 1.61x slower                                                     |
| tomli_loads               | 2.59 sec                                                              | 4.19 sec: 1.62x slower                                                   |
| crypto_pyaes              | 86.6 ms                                                               | 140 ms: 1.62x slower                                                     |
| comprehensions            | 25.4 us                                                               | 41.2 us: 1.62x slower                                                    |
| sympy_integrate           | 21.6 ms                                                               | 35.2 ms: 1.63x slower                                                    |
| pycparser                 | 1.26 sec                                                              | 2.05 sec: 1.63x slower                                                   |
| 2to3                      | 308 ms                                                                | 512 ms: 1.66x slower                                                     |
| genshi_xml                | 60.6 ms                                                               | 101 ms: 1.67x slower                                                     |
| fannkuch                  | 443 ms                                                                | 751 ms: 1.69x slower                                                     |
| sqlalchemy_declarative    | 157 ms                                                                | 268 ms: 1.70x slower                                                     |
| sqlglot_normalize         | 126 ms                                                                | 222 ms: 1.77x slower                                                     |
| spectral_norm             | 131 ms                                                                | 231 ms: 1.77x slower                                                     |
| sqlalchemy_imperative     | 16.7 ms                                                               | 29.7 ms: 1.78x slower                                                    |
| python_startup            | 11.4 ms                                                               | 20.4 ms: 1.79x slower                                                    |
| typing_runtime_protocols  | 181 us                                                                | 325 us: 1.80x slower                                                     |
| thrift                    | 937 us                                                                | 1.69 ms: 1.80x slower                                                    |
| sympy_str                 | 280 ms                                                                | 506 ms: 1.81x slower                                                     |
| regex_compile             | 137 ms                                                                | 250 ms: 1.82x slower                                                     |
| pyflate                   | 559 ms                                                                | 1.02 sec: 1.83x slower                                                   |
| html5lib                  | 65.1 ms                                                               | 119 ms: 1.83x slower                                                     |
| sqlglot_optimize          | 61.3 ms                                                               | 113 ms: 1.84x slower                                                     |
| pprint_pformat            | 1.88 sec                                                              | 3.47 sec: 1.84x slower                                                   |
| pprint_safe_repr          | 916 ms                                                                | 1.69 sec: 1.85x slower                                                   |
| genshi_text               | 27.4 ms                                                               | 51.4 ms: 1.88x slower                                                    |
| logging_format            | 8.34 us                                                               | 15.7 us: 1.88x slower                                                    |
| logging_simple            | 7.63 us                                                               | 14.4 us: 1.89x slower                                                    |
| django_template           | 40.7 ms                                                               | 80.6 ms: 1.98x slower                                                    |
| sympy_sum                 | 154 ms                                                                | 311 ms: 2.01x slower                                                     |
| unpickle_pure_python      | 260 us                                                                | 532 us: 2.05x slower                                                     |
| sympy_expand              | 454 ms                                                                | 948 ms: 2.09x slower                                                     |
| scimark_monte_carlo       | 85.1 ms                                                               | 181 ms: 2.13x slower                                                     |
| pickle_pure_python        | 365 us                                                                | 778 us: 2.13x slower                                                     |
| chaos                     | 71.4 ms                                                               | 159 ms: 2.23x slower                                                     |
| hexiom                    | 6.98 ms                                                               | 15.7 ms: 2.25x slower                                                    |
| logging_silent            | 127 ns                                                                | 285 ns: 2.25x slower                                                     |
| mako                      | 12.9 ms                                                               | 29.2 ms: 2.26x slower                                                    |
| float                     | 92.1 ms                                                               | 209 ms: 2.27x slower                                                     |
| scimark_lu                | 146 ms                                                                | 333 ms: 2.29x slower                                                     |
| scimark_sor               | 150 ms                                                                | 346 ms: 2.31x slower                                                     |
| richards                  | 50.9 ms                                                               | 118 ms: 2.32x slower                                                     |
| raytrace                  | 353 ms                                                                | 821 ms: 2.33x slower                                                     |
| sqlglot_transpile         | 1.83 ms                                                               | 4.26 ms: 2.33x slower                                                    |
| richards_super            | 58.5 ms                                                               | 141 ms: 2.41x slower                                                     |
| go                        | 157 ms                                                                | 391 ms: 2.49x slower                                                     |
| sqlglot_parse             | 1.46 ms                                                               | 3.72 ms: 2.54x slower                                                    |
| nbody                     | 105 ms                                                                | 286 ms: 2.74x slower                                                     |
| deltablue                 | 4.12 ms                                                               | 12.6 ms: 3.06x slower                                                    |
| bench_mp_pool             | 7.05 ms                                                               | 61.1 ms: 8.66x slower                                                    |
| Geometric mean            | (ref)                                                                 | 1.61x slower                                                             |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, pidigits, gc_traversal
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.362x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.39x

# Memory
- memory change: 1.20x