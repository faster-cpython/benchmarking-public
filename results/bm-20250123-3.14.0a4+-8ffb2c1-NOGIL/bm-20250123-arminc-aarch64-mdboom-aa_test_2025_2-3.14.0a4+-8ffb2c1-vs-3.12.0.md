# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-aarch64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.136x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 383 ms: 1.24x slower                                               |
| docutils       | 2.98 sec                                                              | 3.41 sec: 1.14x slower                                             |
| html5lib       | 65.1 ms                                                               | 78.8 ms: 1.21x slower                                              |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 926 ms: 1.52x faster                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 495 ms: 1.50x faster                                               |
| async_tree_io              | 1.41 sec                                                              | 954 ms: 1.48x faster                                               |
| async_tree_memoization     | 777 ms                                                                | 531 ms: 1.46x faster                                               |
| async_tree_none            | 624 ms                                                                | 428 ms: 1.46x faster                                               |
| async_tree_none_tg         | 577 ms                                                                | 398 ms: 1.45x faster                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 686 ms: 1.29x faster                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                               |
| Geometric mean             | (ref)                                                                 | 1.42x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 107 ms: 1.16x slower                                               |
| nbody          | 105 ms                                                                | 189 ms: 1.81x slower                                               |
| Geometric mean | (ref)                                                                 | 1.29x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.18 ms: 1.11x faster                                              |
| regex_dna      | 254 ms                                                                | 274 ms: 1.08x slower                                               |
| regex_v8       | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                              |
| regex_compile  | 137 ms                                                                | 164 ms: 1.20x slower                                               |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 132 ms: 1.14x faster                                               |
| json_loads           | 30.7 us                                                               | 37.0 us: 1.20x slower                                              |
| tomli_loads          | 2.59 sec                                                              | 3.26 sec: 1.26x slower                                             |
| xml_etree_generate   | 112 ms                                                                | 141 ms: 1.26x slower                                               |
| unpickle_pure_python | 260 us                                                                | 341 us: 1.31x slower                                               |
| pickle_pure_python   | 365 us                                                                | 499 us: 1.37x slower                                               |
| xml_etree_process    | 79.0 ms                                                               | 108 ms: 1.37x slower                                               |
| json_dumps           | 12.3 ms                                                               | 17.1 ms: 1.40x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.21x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                              |
| python_startup         | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                              |
| Geometric mean         | (ref)                                                                 | 1.60x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 80.5 ms: 1.33x slower                                              |
| genshi_text     | 27.4 ms                                                               | 38.4 ms: 1.40x slower                                              |
| django_template | 40.7 ms                                                               | 57.3 ms: 1.41x slower                                              |
| mako            | 12.9 ms                                                               | 23.0 ms: 1.78x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.47x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 926 ms: 1.52x faster                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 495 ms: 1.50x faster                                               |
| async_tree_io              | 1.41 sec                                                              | 954 ms: 1.48x faster                                               |
| async_tree_memoization     | 777 ms                                                                | 531 ms: 1.46x faster                                               |
| async_tree_none            | 624 ms                                                                | 428 ms: 1.46x faster                                               |
| async_tree_none_tg         | 577 ms                                                                | 398 ms: 1.45x faster                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 686 ms: 1.29x faster                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                               |
| xml_etree_iterparse        | 150 ms                                                                | 132 ms: 1.14x faster                                               |
| regex_effbot               | 4.64 ms                                                               | 4.18 ms: 1.11x faster                                              |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                              |
| deepcopy                   | 446 us                                                                | 426 us: 1.05x faster                                               |
| sqlite_synth               | 3.77 us                                                               | 3.60 us: 1.05x faster                                              |
| asyncio_websockets         | 658 ms                                                                | 689 ms: 1.05x slower                                               |
| deepcopy_memo              | 49.6 us                                                               | 53.1 us: 1.07x slower                                              |
| regex_dna                  | 254 ms                                                                | 274 ms: 1.08x slower                                               |
| async_generators           | 491 ms                                                                | 537 ms: 1.10x slower                                               |
| pylint                     | 355 ms                                                                | 389 ms: 1.10x slower                                               |
| regex_v8                   | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                              |
| comprehensions             | 25.4 us                                                               | 28.6 us: 1.13x slower                                              |
| create_gc_cycles           | 1.92 ms                                                               | 2.17 ms: 1.13x slower                                              |
| coroutines                 | 29.0 ms                                                               | 32.8 ms: 1.13x slower                                              |
| mdp                        | 3.41 sec                                                              | 3.87 sec: 1.14x slower                                             |
| dulwich_log                | 62.0 ms                                                               | 70.5 ms: 1.14x slower                                              |
| docutils                   | 2.98 sec                                                              | 3.41 sec: 1.14x slower                                             |
| go                         | 157 ms                                                                | 181 ms: 1.15x slower                                               |
| spectral_norm              | 131 ms                                                                | 151 ms: 1.16x slower                                               |
| float                      | 92.1 ms                                                               | 107 ms: 1.16x slower                                               |
| json                       | 5.54 ms                                                               | 6.44 ms: 1.16x slower                                              |
| deepcopy_reduce            | 4.10 us                                                               | 4.77 us: 1.16x slower                                              |
| pycparser                  | 1.26 sec                                                              | 1.47 sec: 1.17x slower                                             |
| scimark_fft                | 418 ms                                                                | 495 ms: 1.18x slower                                               |
| pyflate                    | 559 ms                                                                | 665 ms: 1.19x slower                                               |
| scimark_sor                | 150 ms                                                                | 179 ms: 1.20x slower                                               |
| regex_compile              | 137 ms                                                                | 164 ms: 1.20x slower                                               |
| raytrace                   | 353 ms                                                                | 425 ms: 1.20x slower                                               |
| json_loads                 | 30.7 us                                                               | 37.0 us: 1.20x slower                                              |
| logging_format             | 8.34 us                                                               | 10.1 us: 1.21x slower                                              |
| logging_simple             | 7.63 us                                                               | 9.22 us: 1.21x slower                                              |
| html5lib                   | 65.1 ms                                                               | 78.8 ms: 1.21x slower                                              |
| gc_traversal               | 4.40 ms                                                               | 5.36 ms: 1.22x slower                                              |
| sympy_sum                  | 154 ms                                                                | 190 ms: 1.23x slower                                               |
| logging_silent             | 127 ns                                                                | 157 ns: 1.23x slower                                               |
| 2to3                       | 308 ms                                                                | 383 ms: 1.24x slower                                               |
| sqlglot_normalize          | 126 ms                                                                | 156 ms: 1.24x slower                                               |
| tomli_loads                | 2.59 sec                                                              | 3.26 sec: 1.26x slower                                             |
| xml_etree_generate         | 112 ms                                                                | 141 ms: 1.26x slower                                               |
| chaos                      | 71.4 ms                                                               | 90.1 ms: 1.26x slower                                              |
| sqlglot_optimize           | 61.3 ms                                                               | 77.8 ms: 1.27x slower                                              |
| pprint_safe_repr           | 916 ms                                                                | 1.17 sec: 1.27x slower                                             |
| pprint_pformat             | 1.88 sec                                                              | 2.41 sec: 1.28x slower                                             |
| crypto_pyaes               | 86.6 ms                                                               | 111 ms: 1.28x slower                                               |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.95 ms: 1.28x slower                                              |
| scimark_lu                 | 146 ms                                                                | 189 ms: 1.30x slower                                               |
| unpickle_pure_python       | 260 us                                                                | 341 us: 1.31x slower                                               |
| scimark_monte_carlo        | 85.1 ms                                                               | 112 ms: 1.31x slower                                               |
| sqlalchemy_declarative     | 157 ms                                                                | 208 ms: 1.32x slower                                               |
| sympy_str                  | 280 ms                                                                | 370 ms: 1.32x slower                                               |
| genshi_xml                 | 60.6 ms                                                               | 80.5 ms: 1.33x slower                                              |
| thrift                     | 937 us                                                                | 1.26 ms: 1.34x slower                                              |
| sympy_integrate            | 21.6 ms                                                               | 29.2 ms: 1.35x slower                                              |
| sympy_expand               | 454 ms                                                                | 617 ms: 1.36x slower                                               |
| nqueens                    | 99.2 ms                                                               | 135 ms: 1.36x slower                                               |
| pickle_pure_python         | 365 us                                                                | 499 us: 1.37x slower                                               |
| xml_etree_process          | 79.0 ms                                                               | 108 ms: 1.37x slower                                               |
| sqlglot_transpile          | 1.83 ms                                                               | 2.52 ms: 1.38x slower                                              |
| sqlglot_parse              | 1.46 ms                                                               | 2.02 ms: 1.38x slower                                              |
| telco                      | 8.51 ms                                                               | 11.8 ms: 1.38x slower                                              |
| hexiom                     | 6.98 ms                                                               | 9.66 ms: 1.39x slower                                              |
| json_dumps                 | 12.3 ms                                                               | 17.1 ms: 1.40x slower                                              |
| genshi_text                | 27.4 ms                                                               | 38.4 ms: 1.40x slower                                              |
| django_template            | 40.7 ms                                                               | 57.3 ms: 1.41x slower                                              |
| meteor_contest             | 112 ms                                                                | 158 ms: 1.41x slower                                               |
| sqlalchemy_imperative      | 16.7 ms                                                               | 23.9 ms: 1.43x slower                                              |
| python_startup_no_site     | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                              |
| richards_super             | 58.5 ms                                                               | 85.0 ms: 1.45x slower                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.91 ms: 1.46x slower                                              |
| coverage                   | 87.3 ms                                                               | 129 ms: 1.48x slower                                               |
| deltablue                  | 4.12 ms                                                               | 6.16 ms: 1.50x slower                                              |
| richards                   | 50.9 ms                                                               | 77.1 ms: 1.51x slower                                              |
| fannkuch                   | 443 ms                                                                | 677 ms: 1.53x slower                                               |
| typing_runtime_protocols   | 181 us                                                                | 305 us: 1.69x slower                                               |
| python_startup             | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                              |
| mako                       | 12.9 ms                                                               | 23.0 ms: 1.78x slower                                              |
| nbody                      | 105 ms                                                                | 189 ms: 1.81x slower                                               |
| bench_mp_pool              | 7.05 ms                                                               | 59.7 ms: 8.47x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.21x slower                                                       |

Benchmark hidden because not significant (3): xml_etree_parse, pidigits, generators
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250123-3.14.0a4+-8ffb2c1-NOGIL/bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.136x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.25x