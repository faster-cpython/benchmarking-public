# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.054x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 334 ms: 1.08x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.39 sec: 1.14x slower                                                   |
| html5lib       | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 471 ms: 1.32x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 598 ms: 1.30x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 579 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 772 ms: 1.18x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 490 ms: 1.18x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 775 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                     |
| float          | 92.1 ms                                                               | 97.9 ms: 1.06x slower                                                    |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.13 ms: 1.12x faster                                                    |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                     |
| regex_compile  | 137 ms                                                                | 151 ms: 1.10x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process  | 79.0 ms                                                               | 82.7 ms: 1.05x slower                                                    |
| json_loads         | 30.7 us                                                               | 32.5 us: 1.06x slower                                                    |
| pickle_pure_python | 365 us                                                                | 410 us: 1.12x slower                                                     |
| json_dumps         | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, tomli_loads, xml_etree_generate, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.08 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| django_template | 40.7 ms                                                               | 47.5 ms: 1.17x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 32.3 ms: 1.18x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 79.5 ms: 1.31x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.18x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 471 ms: 1.32x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 598 ms: 1.30x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 579 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 772 ms: 1.18x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 490 ms: 1.18x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.17x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 42.9 us: 1.16x faster                                                    |
| deepcopy                   | 446 us                                                                | 389 us: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 775 ms: 1.14x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.13 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                    |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.41 us: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                    |
| json                       | 5.54 ms                                                               | 5.60 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                     |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                     |
| richards_super             | 58.5 ms                                                               | 60.5 ms: 1.03x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 82.7 ms: 1.05x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.60 sec: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 91.9 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                                     |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                     |
| float                      | 92.1 ms                                                               | 97.9 ms: 1.06x slower                                                    |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                     |
| thrift                     | 937 us                                                                | 997 us: 1.06x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.01 us: 1.06x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 17.8 ms: 1.07x slower                                                    |
| richards                   | 50.9 ms                                                               | 55.1 ms: 1.08x slower                                                    |
| 2to3                       | 308 ms                                                                | 334 ms: 1.08x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.08 ms: 1.09x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.4 ms: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                    |
| async_generators           | 491 ms                                                                | 538 ms: 1.10x slower                                                     |
| regex_compile              | 137 ms                                                                | 151 ms: 1.10x slower                                                     |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 24.1 ms: 1.11x slower                                                    |
| pyflate                    | 559 ms                                                                | 625 ms: 1.12x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 410 us: 1.12x slower                                                     |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.05 ms: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.2 ms: 1.12x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.66 ms: 1.13x slower                                                    |
| sympy_str                  | 280 ms                                                                | 317 ms: 1.13x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.64 ms: 1.13x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.39 sec: 1.14x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 143 ms: 1.14x slower                                                     |
| generators                 | 43.5 ms                                                               | 49.8 ms: 1.14x slower                                                    |
| fannkuch                   | 443 ms                                                                | 509 ms: 1.15x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 70.8 ms: 1.15x slower                                                    |
| spectral_norm              | 131 ms                                                                | 152 ms: 1.17x slower                                                     |
| django_template            | 40.7 ms                                                               | 47.5 ms: 1.17x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.28 ms: 1.17x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 182 ms: 1.18x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 32.3 ms: 1.18x slower                                                    |
| chaos                      | 71.4 ms                                                               | 84.2 ms: 1.18x slower                                                    |
| sympy_expand               | 454 ms                                                                | 536 ms: 1.18x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.50 sec: 1.19x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 75.1 ms: 1.21x slower                                                    |
| go                         | 157 ms                                                                | 196 ms: 1.25x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 228 us: 1.26x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 129 ms: 1.30x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 79.5 ms: 1.31x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.24 sec: 1.36x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.62 sec: 1.39x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 9.84 ms: 1.41x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.36 ms: 1.45x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.77 ms: 1.96x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.53 sec: 216.39x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.14x slower                                                             |

Benchmark hidden because not significant (12): pylint, logging_format, xml_etree_parse, deepcopy_reduce, tomli_loads, xml_etree_generate, unpickle_pure_python, comprehensions, raytrace, deltablue, sqlalchemy_declarative, xml_etree_iterparse
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.05x