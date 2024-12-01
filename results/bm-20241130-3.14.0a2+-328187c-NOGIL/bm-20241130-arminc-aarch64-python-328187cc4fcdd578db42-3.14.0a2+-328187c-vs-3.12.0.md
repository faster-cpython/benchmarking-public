# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.328x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 494 ms: 1.60x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                   |
| html5lib       | 65.1 ms                                                               | 117 ms: 1.80x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.56x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.38 sec: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 915 ms: 1.04x slower                                                     |
| async_tree_none_tg         | 577 ms                                                                | 603 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 199 ms: 1.90x slower                                                     |
| float          | 92.1 ms                                                               | 203 ms: 2.21x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.61x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.20 ms: 1.10x faster                                                    |
| regex_dna      | 254 ms                                                                | 266 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 33.6 ms: 1.19x slower                                                    |
| regex_compile  | 137 ms                                                                | 224 ms: 1.63x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 140 ms: 1.07x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| json_loads           | 30.7 us                                                               | 37.9 us: 1.24x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 150 ms: 1.34x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 121 ms: 1.54x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.99 sec: 1.54x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 19.3 ms: 1.57x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 518 us: 1.99x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 735 us: 2.01x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.41x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.7 ms: 1.52x slower                                                    |
| python_startup         | 11.4 ms                                                               | 21.4 ms: 1.89x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.69x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 89.7 ms: 1.48x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 45.8 ms: 1.67x slower                                                    |
| django_template | 40.7 ms                                                               | 73.6 ms: 1.81x slower                                                    |
| mako            | 12.9 ms                                                               | 28.6 ms: 2.21x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.77x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot               | 4.64 ms                                                               | 4.20 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 140 ms: 1.07x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.38 sec: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 915 ms: 1.04x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 684 ms: 1.04x slower                                                     |
| async_tree_none_tg         | 577 ms                                                                | 603 ms: 1.05x slower                                                     |
| regex_dna                  | 254 ms                                                                | 266 ms: 1.05x slower                                                     |
| deepcopy                   | 446 us                                                                | 482 us: 1.08x slower                                                     |
| pathlib                    | 24.5 ms                                                               | 26.6 ms: 1.08x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.18 us: 1.11x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.10 ms: 1.16x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 33.6 ms: 1.19x slower                                                    |
| json_loads                 | 30.7 us                                                               | 37.9 us: 1.24x slower                                                    |
| json                       | 5.54 ms                                                               | 6.87 ms: 1.24x slower                                                    |
| mdp                        | 3.41 sec                                                              | 4.26 sec: 1.25x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 62.9 us: 1.27x slower                                                    |
| scimark_fft                | 418 ms                                                                | 533 ms: 1.27x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 150 ms: 1.34x slower                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 5.53 us: 1.35x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 39.3 ms: 1.35x slower                                                    |
| async_generators           | 491 ms                                                                | 670 ms: 1.37x slower                                                     |
| generators                 | 43.5 ms                                                               | 59.5 ms: 1.37x slower                                                    |
| spectral_norm              | 131 ms                                                                | 181 ms: 1.39x slower                                                     |
| pylint                     | 355 ms                                                                | 495 ms: 1.39x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.81 ms: 1.42x slower                                                    |
| meteor_contest             | 112 ms                                                                | 161 ms: 1.44x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 89.7 ms: 1.48x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 148 ms: 1.49x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 92.8 ms: 1.50x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.7 ms: 1.52x slower                                                    |
| telco                      | 8.51 ms                                                               | 13.0 ms: 1.53x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 2.01 ms: 1.53x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.94 ms: 1.53x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 121 ms: 1.54x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 3.99 sec: 1.54x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 134 ms: 1.55x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 19.3 ms: 1.57x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 97.1 ms: 1.58x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 2.00 sec: 1.59x slower                                                   |
| 2to3                       | 308 ms                                                                | 494 ms: 1.60x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 202 ms: 1.61x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 35.1 ms: 1.63x slower                                                    |
| comprehensions             | 25.4 us                                                               | 41.3 us: 1.63x slower                                                    |
| regex_compile              | 137 ms                                                                | 224 ms: 1.63x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 296 us: 1.64x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 3.10 sec: 1.65x slower                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 259 ms: 1.65x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.51 sec: 1.65x slower                                                   |
| coverage                   | 87.3 ms                                                               | 145 ms: 1.66x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 45.8 ms: 1.67x slower                                                    |
| fannkuch                   | 443 ms                                                                | 746 ms: 1.68x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 28.6 ms: 1.71x slower                                                    |
| sympy_str                  | 280 ms                                                                | 486 ms: 1.74x slower                                                     |
| logging_simple             | 7.63 us                                                               | 13.6 us: 1.78x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 117 ms: 1.80x slower                                                     |
| pyflate                    | 559 ms                                                                | 1.01 sec: 1.80x slower                                                   |
| django_template            | 40.7 ms                                                               | 73.6 ms: 1.81x slower                                                    |
| thrift                     | 937 us                                                                | 1.70 ms: 1.81x slower                                                    |
| logging_format             | 8.34 us                                                               | 15.3 us: 1.83x slower                                                    |
| python_startup             | 11.4 ms                                                               | 21.4 ms: 1.89x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 292 ms: 1.89x slower                                                     |
| nbody                      | 105 ms                                                                | 199 ms: 1.90x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 287 ms: 1.97x slower                                                     |
| sympy_expand               | 454 ms                                                                | 895 ms: 1.97x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 518 us: 1.99x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 170 ms: 2.00x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 735 us: 2.01x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 14.7 ms: 2.11x slower                                                    |
| scimark_sor                | 150 ms                                                                | 316 ms: 2.11x slower                                                     |
| chaos                      | 71.4 ms                                                               | 158 ms: 2.21x slower                                                     |
| float                      | 92.1 ms                                                               | 203 ms: 2.21x slower                                                     |
| mako                       | 12.9 ms                                                               | 28.6 ms: 2.21x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.20 ms: 2.30x slower                                                    |
| raytrace                   | 353 ms                                                                | 811 ms: 2.30x slower                                                     |
| logging_silent             | 127 ns                                                                | 293 ns: 2.31x slower                                                     |
| richards_super             | 58.5 ms                                                               | 136 ms: 2.33x slower                                                     |
| richards                   | 50.9 ms                                                               | 119 ms: 2.34x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 3.52 ms: 2.40x slower                                                    |
| go                         | 157 ms                                                                | 387 ms: 2.46x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 12.3 ms: 2.99x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 65.5 ms: 9.29x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.56x slower                                                             |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_io, async_tree_none, async_tree_memoization_tg, pidigits, async_tree_cpu_io_mixed
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.328x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.40x
- 95% likely to have a slowdown of 1.37x
- 99% likely to have a slowdown of 1.32x

# Memory
- memory change: 1.23x