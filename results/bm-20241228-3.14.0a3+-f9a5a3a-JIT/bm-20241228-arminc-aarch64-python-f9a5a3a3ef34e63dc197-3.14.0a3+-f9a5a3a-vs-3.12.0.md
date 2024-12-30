# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.038x slower
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 324 ms: 1.05x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.23 sec: 1.08x slower                                                   |
| html5lib       | 65.1 ms                                                               | 70.2 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 488 ms: 1.52x faster                                                     |
| async_tree_none            | 624 ms                                                                | 421 ms: 1.48x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 951 ms: 1.48x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 956 ms: 1.48x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 534 ms: 1.45x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 400 ms: 1.44x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 714 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 693 ms: 1.28x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.42x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 244 ms: 1.05x slower                                                     |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 145 ms: 1.06x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.09x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| xml_etree_process   | 79.0 ms                                                               | 84.2 ms: 1.07x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 395 us: 1.08x slower                                                     |
| json_loads          | 30.7 us                                                               | 33.3 us: 1.09x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| django_template | 40.7 ms                                                               | 48.3 ms: 1.19x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 35.8 ms: 1.31x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 87.0 ms: 1.44x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 488 ms: 1.52x faster                                                     |
| async_tree_none            | 624 ms                                                                | 421 ms: 1.48x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 951 ms: 1.48x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 956 ms: 1.48x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 534 ms: 1.45x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 400 ms: 1.44x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 714 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 693 ms: 1.28x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.4 us: 1.20x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                    |
| deepcopy                   | 446 us                                                                | 397 us: 1.12x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 151 ms: 1.04x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                     |
| raytrace                   | 353 ms                                                                | 367 ms: 1.04x slower                                                     |
| json                       | 5.54 ms                                                               | 5.76 ms: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| pidigits                   | 233 ms                                                                | 244 ms: 1.05x slower                                                     |
| logging_format             | 8.34 us                                                               | 8.75 us: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                     |
| 2to3                       | 308 ms                                                                | 324 ms: 1.05x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.33 ms: 1.05x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.59 sec: 1.05x slower                                                   |
| regex_compile              | 137 ms                                                                | 145 ms: 1.06x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 17.6 ms: 1.06x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.06x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 154 ms: 1.06x slower                                                     |
| logging_simple             | 7.63 us                                                               | 8.13 us: 1.06x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 84.2 ms: 1.07x slower                                                    |
| go                         | 157 ms                                                                | 168 ms: 1.07x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.57 ms: 1.07x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.2 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.23 sec: 1.08x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 94.0 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.3 us: 1.09x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 23.6 ms: 1.09x slower                                                    |
| thrift                     | 937 us                                                                | 1.03 ms: 1.10x slower                                                    |
| richards                   | 50.9 ms                                                               | 56.0 ms: 1.10x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.83 ms: 1.10x slower                                                    |
| pyflate                    | 559 ms                                                                | 616 ms: 1.10x slower                                                     |
| async_generators           | 491 ms                                                                | 542 ms: 1.10x slower                                                     |
| sympy_str                  | 280 ms                                                                | 310 ms: 1.11x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 171 ms: 1.11x slower                                                     |
| richards_super             | 58.5 ms                                                               | 65.7 ms: 1.12x slower                                                    |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.25 us: 1.13x slower                                                    |
| fannkuch                   | 443 ms                                                                | 506 ms: 1.14x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.14x slower                                                     |
| meteor_contest             | 112 ms                                                                | 128 ms: 1.15x slower                                                     |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                    |
| sympy_expand               | 454 ms                                                                | 525 ms: 1.16x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 71.1 ms: 1.16x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.92 ms: 1.17x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 72.5 ms: 1.17x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.48 sec: 1.18x slower                                                   |
| logging_silent             | 127 ns                                                                | 151 ns: 1.19x slower                                                     |
| django_template            | 40.7 ms                                                               | 48.3 ms: 1.19x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| coverage                   | 87.3 ms                                                               | 105 ms: 1.20x slower                                                     |
| generators                 | 43.5 ms                                                               | 52.2 ms: 1.20x slower                                                    |
| chaos                      | 71.4 ms                                                               | 86.2 ms: 1.21x slower                                                    |
| mypy2                      | 873 ms                                                                | 1.10 sec: 1.26x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 230 us: 1.27x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 35.8 ms: 1.31x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 131 ms: 1.32x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.50 ms: 1.36x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.67 sec: 1.42x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.32 sec: 1.44x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 87.0 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.86 ms: 1.56x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.63 ms: 1.89x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.56 sec: 221.26x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (10): pylint, deepcopy_reduce, comprehensions, regex_dna, scimark_fft, unpickle_pure_python, xml_etree_generate, coroutines, scimark_monte_carlo, float
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x