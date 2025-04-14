# Results vs. 3.12.0

- fork: python
- ref: 98fa4a49fecbac3c990a
- machine: linux-aarch64
- commit hash: 98fa4a4
- commit date: 2025-03-09
- overall geometric mean: 1.036x faster
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                                     |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                   |
| html5lib       | 65.1 ms                                                               | 61.7 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                     |
| async_tree_none            | 624 ms                                                                | 382 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 886 ms: 1.59x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 891 ms: 1.58x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 652 ms: 1.36x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.7 ms: 1.11x faster                                                    |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.79 ms: 1.23x faster                                                    |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                     |
| regex_dna      | 254 ms                                                                | 237 ms: 1.07x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 27.8 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.10x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.39 sec: 1.08x faster                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 142 ms: 1.06x faster                                                     |
| xml_etree_generate   | 112 ms                                                                | 107 ms: 1.05x faster                                                     |
| xml_etree_process    | 79.0 ms                                                               | 76.4 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 269 us: 1.03x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 394 us: 1.08x slower                                                     |
| json_loads           | 30.7 us                                                               | 34.6 us: 1.13x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 15.8 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 61.2 ms: 1.01x slower                                                    |
| mako           | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                     |
| async_tree_none            | 624 ms                                                                | 382 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 886 ms: 1.59x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 891 ms: 1.58x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                     |
| deepcopy                   | 446 us                                                                | 324 us: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 652 ms: 1.36x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.79 ms: 1.23x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.0 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.40 us: 1.21x faster                                                    |
| pylint                     | 355 ms                                                                | 313 ms: 1.13x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.84 us: 1.12x faster                                                    |
| float                      | 92.1 ms                                                               | 82.7 ms: 1.11x faster                                                    |
| raytrace                   | 353 ms                                                                | 317 ms: 1.11x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 55.8 ms: 1.11x faster                                                    |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.57 us: 1.10x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                     |
| richards_super             | 58.5 ms                                                               | 53.9 ms: 1.08x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.39 sec: 1.08x faster                                                   |
| async_generators           | 491 ms                                                                | 454 ms: 1.08x faster                                                     |
| chaos                      | 71.4 ms                                                               | 66.4 ms: 1.07x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| regex_dna                  | 254 ms                                                                | 237 ms: 1.07x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                                    |
| richards                   | 50.9 ms                                                               | 48.1 ms: 1.06x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.8 ms: 1.06x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 61.7 ms: 1.05x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 107 ms: 1.05x faster                                                     |
| comprehensions             | 25.4 us                                                               | 24.2 us: 1.05x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 27.7 ms: 1.05x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.28 sec: 1.04x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 76.4 ms: 1.03x faster                                                    |
| sympy_str                  | 280 ms                                                                | 271 ms: 1.03x faster                                                     |
| regex_v8                   | 28.3 ms                                                               | 27.8 ms: 1.02x faster                                                    |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 21.3 ms: 1.01x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.73 us: 1.01x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 84.3 ms: 1.01x faster                                                    |
| spectral_norm              | 131 ms                                                                | 130 ms: 1.00x faster                                                     |
| genshi_xml                 | 60.6 ms                                                               | 61.2 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.01x slower                                                    |
| json                       | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 102 ms: 1.03x slower                                                     |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 269 us: 1.03x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| pyflate                    | 559 ms                                                                | 581 ms: 1.04x slower                                                     |
| sympy_expand               | 454 ms                                                                | 475 ms: 1.05x slower                                                     |
| meteor_contest             | 112 ms                                                                | 119 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.67 ms: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 394 us: 1.08x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                   |
| go                         | 157 ms                                                                | 172 ms: 1.10x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.50 ms: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.1 ms: 1.12x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.6 us: 1.13x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 204 us: 1.13x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 98.3 ms: 1.13x slower                                                    |
| fannkuch                   | 443 ms                                                                | 515 ms: 1.16x slower                                                     |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 8.12 ms: 1.16x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.52 sec: 1.34x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.24 sec: 1.36x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.8 ms: 1.39x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.58 ms: 1.50x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.88x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.67 sec: 378.24x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (8): scimark_lu, django_template, thrift, scimark_fft, scimark_sor, asyncio_websockets, genshi_text, pidigits
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250309-3.14.0a5+-98fa4a4-JIT/bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x