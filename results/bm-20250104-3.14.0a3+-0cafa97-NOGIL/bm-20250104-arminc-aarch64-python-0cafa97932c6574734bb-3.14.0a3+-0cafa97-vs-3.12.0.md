# Results vs. 3.12.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.253x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 468 ms: 1.52x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.72 sec: 1.25x slower                                                   |
| html5lib       | 65.1 ms                                                               | 111 ms: 1.70x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.48x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 628 ms: 1.18x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 660 ms: 1.18x faster                                                     |
| async_tree_none            | 624 ms                                                                | 536 ms: 1.16x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 510 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 833 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 814 ms: 1.09x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.15x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 154 ms: 1.67x slower                                                     |
| nbody          | 105 ms                                                                | 186 ms: 1.78x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.46x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.15 ms: 1.12x faster                                                    |
| regex_dna      | 254 ms                                                                | 279 ms: 1.10x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 33.3 ms: 1.17x slower                                                    |
| regex_compile  | 137 ms                                                                | 187 ms: 1.36x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 137 ms: 1.10x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| json_loads           | 30.7 us                                                               | 37.4 us: 1.22x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 145 ms: 1.29x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 109 ms: 1.39x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.60 sec: 1.39x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 18.4 ms: 1.50x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 453 us: 1.74x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 701 us: 1.92x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.33x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.4 ms: 1.48x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.4 ms: 1.80x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.63x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 86.6 ms: 1.43x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 41.3 ms: 1.50x slower                                                    |
| django_template | 40.7 ms                                                               | 65.3 ms: 1.61x slower                                                    |
| mako            | 12.9 ms                                                               | 25.6 ms: 1.98x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.62x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 628 ms: 1.18x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 660 ms: 1.18x faster                                                     |
| async_tree_none            | 624 ms                                                                | 536 ms: 1.16x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 510 ms: 1.13x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.15 ms: 1.12x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 137 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 833 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 814 ms: 1.09x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| deepcopy                   | 446 us                                                                | 432 us: 1.03x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.9 ms: 1.03x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 682 ms: 1.04x slower                                                     |
| regex_dna                  | 254 ms                                                                | 279 ms: 1.10x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 56.6 us: 1.14x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.03 ms: 1.14x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 33.8 ms: 1.17x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 33.3 ms: 1.17x slower                                                    |
| mdp                        | 3.41 sec                                                              | 4.01 sec: 1.18x slower                                                   |
| spectral_norm              | 131 ms                                                                | 154 ms: 1.18x slower                                                     |
| json                       | 5.54 ms                                                               | 6.54 ms: 1.18x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.85 us: 1.18x slower                                                    |
| scimark_fft                | 418 ms                                                                | 501 ms: 1.20x slower                                                     |
| json_loads                 | 30.7 us                                                               | 37.4 us: 1.22x slower                                                    |
| pylint                     | 355 ms                                                                | 438 ms: 1.23x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.72 sec: 1.25x slower                                                   |
| async_generators           | 491 ms                                                                | 619 ms: 1.26x slower                                                     |
| generators                 | 43.5 ms                                                               | 56.1 ms: 1.29x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 145 ms: 1.29x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 82.9 ms: 1.34x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 208 ms: 1.34x slower                                                     |
| regex_compile              | 137 ms                                                                | 187 ms: 1.36x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.49 ms: 1.37x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 136 ms: 1.37x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.73 sec: 1.38x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 109 ms: 1.39x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 3.60 sec: 1.39x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 30.1 ms: 1.39x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 121 ms: 1.40x slower                                                     |
| sympy_expand               | 454 ms                                                                | 635 ms: 1.40x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 86.0 ms: 1.40x slower                                                    |
| sympy_str                  | 280 ms                                                                | 399 ms: 1.43x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 86.6 ms: 1.43x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 180 ms: 1.43x slower                                                     |
| meteor_contest             | 112 ms                                                                | 161 ms: 1.44x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 227 ms: 1.44x slower                                                     |
| telco                      | 8.51 ms                                                               | 12.4 ms: 1.45x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.34 sec: 1.47x slower                                                   |
| logging_format             | 8.34 us                                                               | 12.3 us: 1.47x slower                                                    |
| logging_simple             | 7.63 us                                                               | 11.2 us: 1.47x slower                                                    |
| thrift                     | 937 us                                                                | 1.38 ms: 1.47x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.4 ms: 1.48x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.78 sec: 1.48x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.87 ms: 1.50x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 18.4 ms: 1.50x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 41.3 ms: 1.50x slower                                                    |
| comprehensions             | 25.4 us                                                               | 38.5 us: 1.51x slower                                                    |
| 2to3                       | 308 ms                                                                | 468 ms: 1.52x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 2.00 ms: 1.53x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 25.7 ms: 1.54x slower                                                    |
| fannkuch                   | 443 ms                                                                | 692 ms: 1.56x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 228 ms: 1.57x slower                                                     |
| django_template            | 40.7 ms                                                               | 65.3 ms: 1.61x slower                                                    |
| pyflate                    | 559 ms                                                                | 911 ms: 1.63x slower                                                     |
| coverage                   | 87.3 ms                                                               | 144 ms: 1.65x slower                                                     |
| float                      | 92.1 ms                                                               | 154 ms: 1.67x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 302 us: 1.68x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 111 ms: 1.70x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.51 sec: 1.73x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 453 us: 1.74x slower                                                     |
| nbody                      | 105 ms                                                                | 186 ms: 1.78x slower                                                     |
| python_startup             | 11.4 ms                                                               | 20.4 ms: 1.80x slower                                                    |
| chaos                      | 71.4 ms                                                               | 129 ms: 1.81x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 154 ms: 1.81x slower                                                     |
| richards_super             | 58.5 ms                                                               | 108 ms: 1.85x slower                                                     |
| raytrace                   | 353 ms                                                                | 666 ms: 1.89x slower                                                     |
| scimark_sor                | 150 ms                                                                | 285 ms: 1.91x slower                                                     |
| richards                   | 50.9 ms                                                               | 97.6 ms: 1.92x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 13.4 ms: 1.92x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 701 us: 1.92x slower                                                     |
| mako                       | 12.9 ms                                                               | 25.6 ms: 1.98x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 3.73 ms: 2.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 261 ns: 2.06x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 3.13 ms: 2.14x slower                                                    |
| go                         | 157 ms                                                                | 337 ms: 2.15x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 11.1 ms: 2.69x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 62.6 ms: 8.88x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.41x slower                                                             |

Benchmark hidden because not significant (2): sqlite_synth, pidigits
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.253x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.27x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.24x