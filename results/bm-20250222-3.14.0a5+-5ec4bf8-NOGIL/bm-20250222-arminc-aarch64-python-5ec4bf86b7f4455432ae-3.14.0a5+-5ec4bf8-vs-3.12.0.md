# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.118x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 376 ms: 1.22x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.33 sec: 1.12x slower                                                   |
| html5lib       | 65.1 ms                                                               | 77.0 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 919 ms: 1.53x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 499 ms: 1.48x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 532 ms: 1.46x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 968 ms: 1.46x faster                                                     |
| async_tree_none            | 624 ms                                                                | 434 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 669 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 709 ms: 1.29x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.42x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 103 ms: 1.11x slower                                                     |
| nbody          | 105 ms                                                                | 185 ms: 1.77x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.27x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 31.7 ms: 1.12x slower                                                    |
| regex_compile  | 137 ms                                                                | 163 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 131 ms: 1.15x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| unpickle             | 18.5 us                                                               | 20.7 us: 1.12x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 43.0 us: 1.15x slower                                                    |
| pickle_list          | 5.25 us                                                               | 6.08 us: 1.16x slower                                                    |
| pickle               | 13.4 us                                                               | 15.9 us: 1.18x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 3.15 sec: 1.22x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 7.60 us: 1.23x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 323 us: 1.24x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 462 us: 1.27x slower                                                     |
| xml_etree_generate   | 112 ms                                                                | 146 ms: 1.31x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 104 ms: 1.31x slower                                                     |
| json_loads           | 30.7 us                                                               | 40.5 us: 1.32x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.0 ms: 1.39x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.18x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.3 ms: 1.47x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.61x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 79.5 ms: 1.31x slower                                                    |
| django_template | 40.7 ms                                                               | 54.3 ms: 1.34x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 38.0 ms: 1.39x slower                                                    |
| mako            | 12.9 ms                                                               | 22.6 ms: 1.75x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.44x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 2.67 ms: 1.65x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 919 ms: 1.53x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 499 ms: 1.48x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 532 ms: 1.46x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 968 ms: 1.46x faster                                                     |
| async_tree_none            | 624 ms                                                                | 434 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 669 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 709 ms: 1.29x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 131 ms: 1.15x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.62 us: 1.04x faster                                                    |
| comprehensions             | 25.4 us                                                               | 26.4 us: 1.04x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 686 ms: 1.04x slower                                                     |
| coroutines                 | 29.0 ms                                                               | 31.0 ms: 1.07x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 53.0 us: 1.07x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 608 ms: 1.07x slower                                                     |
| create_gc_cycles           | 1.92 ms                                                               | 2.09 ms: 1.09x slower                                                    |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                     |
| pylint                     | 355 ms                                                                | 389 ms: 1.10x slower                                                     |
| async_generators           | 491 ms                                                                | 540 ms: 1.10x slower                                                     |
| float                      | 92.1 ms                                                               | 103 ms: 1.11x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.33 sec: 1.12x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 31.7 ms: 1.12x slower                                                    |
| unpickle                   | 18.5 us                                                               | 20.7 us: 1.12x slower                                                    |
| go                         | 157 ms                                                                | 177 ms: 1.12x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 70.9 ms: 1.14x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.92 sec: 1.15x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.44 sec: 1.15x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 43.0 us: 1.15x slower                                                    |
| pickle_list                | 5.25 us                                                               | 6.08 us: 1.16x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.75 us: 1.16x slower                                                    |
| pyflate                    | 559 ms                                                                | 651 ms: 1.16x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.56 sec: 1.17x slower                                                   |
| logging_format             | 8.34 us                                                               | 9.79 us: 1.17x slower                                                    |
| raytrace                   | 353 ms                                                                | 416 ms: 1.18x slower                                                     |
| logging_silent             | 127 ns                                                                | 149 ns: 1.18x slower                                                     |
| logging_simple             | 7.63 us                                                               | 9.01 us: 1.18x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.9 us: 1.18x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 77.0 ms: 1.18x slower                                                    |
| regex_compile              | 137 ms                                                                | 163 ms: 1.19x slower                                                     |
| scimark_fft                | 418 ms                                                                | 498 ms: 1.19x slower                                                     |
| scimark_sor                | 150 ms                                                                | 178 ms: 1.19x slower                                                     |
| json                       | 5.54 ms                                                               | 6.63 ms: 1.20x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.15 sec: 1.22x slower                                                   |
| 2to3                       | 308 ms                                                                | 376 ms: 1.22x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 154 ms: 1.23x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 194 ms: 1.23x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 190 ms: 1.23x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 7.60 us: 1.23x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 323 us: 1.24x slower                                                     |
| chaos                      | 71.4 ms                                                               | 89.0 ms: 1.25x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.26x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 462 us: 1.27x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 5.24 ms: 1.27x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.40 sec: 1.28x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 112 ms: 1.29x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 146 ms: 1.31x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 21.8 ms: 1.31x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 80.2 ms: 1.31x slower                                                    |
| sympy_str                  | 280 ms                                                                | 367 ms: 1.31x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 104 ms: 1.31x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 79.5 ms: 1.31x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 192 ms: 1.32x slower                                                     |
| json_loads                 | 30.7 us                                                               | 40.5 us: 1.32x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.43 ms: 1.33x slower                                                    |
| thrift                     | 937 us                                                                | 1.25 ms: 1.33x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 113 ms: 1.33x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 28.8 ms: 1.33x slower                                                    |
| django_template            | 40.7 ms                                                               | 54.3 ms: 1.34x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.30 ms: 1.34x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 133 ms: 1.34x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.37 ms: 1.34x slower                                                    |
| sympy_expand               | 454 ms                                                                | 613 ms: 1.35x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 2.02 ms: 1.38x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 38.0 ms: 1.39x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 17.0 ms: 1.39x slower                                                    |
| meteor_contest             | 112 ms                                                                | 157 ms: 1.40x slower                                                     |
| telco                      | 8.51 ms                                                               | 12.1 ms: 1.42x slower                                                    |
| richards_super             | 58.5 ms                                                               | 83.7 ms: 1.43x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.88 ms: 1.44x slower                                                    |
| richards                   | 50.9 ms                                                               | 73.9 ms: 1.45x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.3 ms: 1.47x slower                                                    |
| fannkuch                   | 443 ms                                                                | 681 ms: 1.54x slower                                                     |
| coverage                   | 87.3 ms                                                               | 135 ms: 1.55x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 281 us: 1.56x slower                                                     |
| mako                       | 12.9 ms                                                               | 22.6 ms: 1.75x slower                                                    |
| python_startup             | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                                    |
| nbody                      | 105 ms                                                                | 185 ms: 1.77x slower                                                     |
| bench_mp_pool              | 7.05 ms                                                               | 56.7 ms: 8.04x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.18x slower                                                             |

Benchmark hidden because not significant (5): deepcopy, regex_dna, pathlib, generators, pidigits
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.118x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.25x