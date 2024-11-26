# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-aarch64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.126x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 413 ms: 1.34x slower                                                           |
| docutils       | 2.98 sec                                                              | 3.83 sec: 1.28x slower                                                         |
| html5lib       | 65.1 ms                                                               | 76.4 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 568 ms: 1.30x faster                                                           |
| async_tree_none            | 624 ms                                                                | 489 ms: 1.28x faster                                                           |
| async_tree_memoization     | 777 ms                                                                | 635 ms: 1.22x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 473 ms: 1.22x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 782 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 809 ms: 1.13x faster                                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.30 sec: 1.08x faster                                                         |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 243 ms: 1.05x slower                                                           |
| float          | 92.1 ms                                                               | 108 ms: 1.17x slower                                                           |
| nbody          | 105 ms                                                                | 133 ms: 1.28x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 277 ms: 1.09x slower                                                           |
| regex_effbot   | 4.64 ms                                                               | 5.38 ms: 1.16x slower                                                          |
| regex_v8       | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                          |
| regex_compile  | 137 ms                                                                | 186 ms: 1.36x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 155 ms: 1.03x slower                                                           |
| xml_etree_generate   | 112 ms                                                                | 119 ms: 1.06x slower                                                           |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.07x slower                                                          |
| tomli_loads          | 2.59 sec                                                              | 2.82 sec: 1.09x slower                                                         |
| xml_etree_process    | 79.0 ms                                                               | 86.1 ms: 1.09x slower                                                          |
| unpickle_pure_python | 260 us                                                                | 292 us: 1.12x slower                                                           |
| pickle_pure_python   | 365 us                                                                | 432 us: 1.18x slower                                                           |
| json_dumps           | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.09x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.16 ms: 1.09x slower                                                          |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                          |
| django_template | 40.7 ms                                                               | 49.8 ms: 1.22x slower                                                          |
| genshi_text     | 27.4 ms                                                               | 36.6 ms: 1.33x slower                                                          |
| genshi_xml      | 60.6 ms                                                               | 84.5 ms: 1.39x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.26x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 568 ms: 1.30x faster                                                           |
| async_tree_none            | 624 ms                                                                | 489 ms: 1.28x faster                                                           |
| async_tree_memoization     | 777 ms                                                                | 635 ms: 1.22x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 473 ms: 1.22x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 782 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 809 ms: 1.13x faster                                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.30 sec: 1.08x faster                                                         |
| deepcopy_memo              | 49.6 us                                                               | 46.4 us: 1.07x faster                                                          |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                                          |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                           |
| xml_etree_iterparse        | 150 ms                                                                | 155 ms: 1.03x slower                                                           |
| logging_format             | 8.34 us                                                               | 8.67 us: 1.04x slower                                                          |
| pidigits                   | 233 ms                                                                | 243 ms: 1.05x slower                                                           |
| xml_etree_generate         | 112 ms                                                                | 119 ms: 1.06x slower                                                           |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                                          |
| logging_simple             | 7.63 us                                                               | 8.11 us: 1.06x slower                                                          |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                                          |
| json                       | 5.54 ms                                                               | 5.93 ms: 1.07x slower                                                          |
| mdp                        | 3.41 sec                                                              | 3.71 sec: 1.09x slower                                                         |
| tomli_loads                | 2.59 sec                                                              | 2.82 sec: 1.09x slower                                                         |
| regex_dna                  | 254 ms                                                                | 277 ms: 1.09x slower                                                           |
| xml_etree_process          | 79.0 ms                                                               | 86.1 ms: 1.09x slower                                                          |
| python_startup_no_site     | 8.37 ms                                                               | 9.16 ms: 1.09x slower                                                          |
| thrift                     | 937 us                                                                | 1.03 ms: 1.10x slower                                                          |
| crypto_pyaes               | 86.6 ms                                                               | 95.3 ms: 1.10x slower                                                          |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                          |
| scimark_lu                 | 146 ms                                                                | 161 ms: 1.11x slower                                                           |
| comprehensions             | 25.4 us                                                               | 28.2 us: 1.11x slower                                                          |
| sqlalchemy_imperative      | 16.7 ms                                                               | 18.5 ms: 1.11x slower                                                          |
| unpickle_pure_python       | 260 us                                                                | 292 us: 1.12x slower                                                           |
| async_generators           | 491 ms                                                                | 552 ms: 1.13x slower                                                           |
| sqlite_synth               | 3.77 us                                                               | 4.24 us: 1.13x slower                                                          |
| raytrace                   | 353 ms                                                                | 402 ms: 1.14x slower                                                           |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                           |
| scimark_fft                | 418 ms                                                                | 483 ms: 1.15x slower                                                           |
| scimark_monte_carlo        | 85.1 ms                                                               | 98.2 ms: 1.15x slower                                                          |
| regex_effbot               | 4.64 ms                                                               | 5.38 ms: 1.16x slower                                                          |
| float                      | 92.1 ms                                                               | 108 ms: 1.17x slower                                                           |
| html5lib                   | 65.1 ms                                                               | 76.4 ms: 1.17x slower                                                          |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.18x slower                                                           |
| regex_v8                   | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                          |
| pickle_pure_python         | 365 us                                                                | 432 us: 1.18x slower                                                           |
| meteor_contest             | 112 ms                                                                | 133 ms: 1.19x slower                                                           |
| fannkuch                   | 443 ms                                                                | 528 ms: 1.19x slower                                                           |
| telco                      | 8.51 ms                                                               | 10.2 ms: 1.20x slower                                                          |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                          |
| pyflate                    | 559 ms                                                                | 678 ms: 1.21x slower                                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.54 ms: 1.22x slower                                                          |
| django_template            | 40.7 ms                                                               | 49.8 ms: 1.22x slower                                                          |
| sqlglot_parse              | 1.46 ms                                                               | 1.80 ms: 1.23x slower                                                          |
| go                         | 157 ms                                                                | 197 ms: 1.25x slower                                                           |
| chaos                      | 71.4 ms                                                               | 90.0 ms: 1.26x slower                                                          |
| sqlalchemy_declarative     | 157 ms                                                                | 200 ms: 1.27x slower                                                           |
| pylint                     | 355 ms                                                                | 451 ms: 1.27x slower                                                           |
| pycparser                  | 1.26 sec                                                              | 1.60 sec: 1.27x slower                                                         |
| nbody                      | 105 ms                                                                | 133 ms: 1.28x slower                                                           |
| dulwich_log                | 62.0 ms                                                               | 79.2 ms: 1.28x slower                                                          |
| docutils                   | 2.98 sec                                                              | 3.83 sec: 1.28x slower                                                         |
| sqlglot_transpile          | 1.83 ms                                                               | 2.35 ms: 1.29x slower                                                          |
| deltablue                  | 4.12 ms                                                               | 5.31 ms: 1.29x slower                                                          |
| typing_runtime_protocols   | 181 us                                                                | 233 us: 1.29x slower                                                           |
| spectral_norm              | 131 ms                                                                | 169 ms: 1.30x slower                                                           |
| sympy_str                  | 280 ms                                                                | 370 ms: 1.32x slower                                                           |
| genshi_text                | 27.4 ms                                                               | 36.6 ms: 1.33x slower                                                          |
| logging_silent             | 127 ns                                                                | 169 ns: 1.33x slower                                                           |
| 2to3                       | 308 ms                                                                | 413 ms: 1.34x slower                                                           |
| regex_compile              | 137 ms                                                                | 186 ms: 1.36x slower                                                           |
| sqlglot_normalize          | 126 ms                                                                | 171 ms: 1.36x slower                                                           |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                                         |
| sympy_expand               | 454 ms                                                                | 619 ms: 1.36x slower                                                           |
| generators                 | 43.5 ms                                                               | 59.5 ms: 1.37x slower                                                          |
| sympy_integrate            | 21.6 ms                                                               | 30.0 ms: 1.39x slower                                                          |
| genshi_xml                 | 60.6 ms                                                               | 84.5 ms: 1.39x slower                                                          |
| sympy_sum                  | 154 ms                                                                | 216 ms: 1.40x slower                                                           |
| nqueens                    | 99.2 ms                                                               | 139 ms: 1.40x slower                                                           |
| pprint_pformat             | 1.88 sec                                                              | 2.64 sec: 1.40x slower                                                         |
| richards_super             | 58.5 ms                                                               | 83.2 ms: 1.42x slower                                                          |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                          |
| sqlglot_optimize           | 61.3 ms                                                               | 88.4 ms: 1.44x slower                                                          |
| richards                   | 50.9 ms                                                               | 73.5 ms: 1.44x slower                                                          |
| gc_traversal               | 4.40 ms                                                               | 6.50 ms: 1.48x slower                                                          |
| hexiom                     | 6.98 ms                                                               | 11.1 ms: 1.59x slower                                                          |
| create_gc_cycles           | 1.92 ms                                                               | 3.75 ms: 1.95x slower                                                          |
| bench_mp_pool              | 7.05 ms                                                               | 1.60 sec: 226.23x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.24x slower                                                                   |

Benchmark hidden because not significant (4): deepcopy, xml_etree_parse, coroutines, deepcopy_reduce
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.126x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.09x