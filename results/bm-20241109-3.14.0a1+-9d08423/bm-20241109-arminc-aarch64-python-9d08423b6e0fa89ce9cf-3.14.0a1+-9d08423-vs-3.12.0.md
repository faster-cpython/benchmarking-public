# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.001x faster
- HPT reliability: 56.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| html5lib       | 65.1 ms                                                               | 72.8 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 458 ms: 1.36x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 552 ms: 1.34x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 611 ms: 1.27x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 458 ms: 1.26x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 749 ms: 1.18x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.11x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| float          | 92.1 ms                                                               | 98.6 ms: 1.07x slower                                                    |
| nbody          | 105 ms                                                                | 123 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 130 ms: 1.06x faster                                                     |
| regex_dna      | 254 ms                                                                | 272 ms: 1.07x slower                                                     |
| regex_effbot   | 4.64 ms                                                               | 5.07 ms: 1.09x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 32.2 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate | 112 ms                                                                | 114 ms: 1.01x slower                                                     |
| xml_etree_process  | 79.0 ms                                                               | 84.2 ms: 1.07x slower                                                    |
| json_loads         | 30.7 us                                                               | 32.8 us: 1.07x slower                                                    |
| tomli_loads        | 2.59 sec                                                              | 2.78 sec: 1.07x slower                                                   |
| pickle_pure_python | 365 us                                                                | 401 us: 1.10x slower                                                     |
| json_dumps         | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.02 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 43.7 ms: 1.07x slower                                                    |
| mako            | 12.9 ms                                                               | 14.4 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 458 ms: 1.36x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 552 ms: 1.34x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 611 ms: 1.27x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 458 ms: 1.26x faster                                                     |
| deepcopy                   | 446 us                                                                | 355 us: 1.26x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.6 us: 1.22x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.8 ms: 1.22x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.21x faster                                                   |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 749 ms: 1.18x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.59 us: 1.14x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.11x faster                                                   |
| raytrace                   | 353 ms                                                                | 320 ms: 1.10x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.09x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.07x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                     |
| go                         | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.07x faster                                                     |
| regex_compile              | 137 ms                                                                | 130 ms: 1.06x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.30 us: 1.05x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                     |
| logging_format             | 8.34 us                                                               | 8.01 us: 1.04x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 60.8 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 114 ms: 1.01x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 676 ms: 1.03x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.51 sec: 1.03x slower                                                   |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| sympy_expand               | 454 ms                                                                | 470 ms: 1.04x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 63.9 ms: 1.04x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 966 ms: 1.05x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.99 sec: 1.06x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 84.2 ms: 1.07x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.6 ms: 1.07x slower                                                    |
| float                      | 92.1 ms                                                               | 98.6 ms: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.78 sec: 1.07x slower                                                   |
| regex_dna                  | 254 ms                                                                | 272 ms: 1.07x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 135 ms: 1.07x slower                                                     |
| django_template            | 40.7 ms                                                               | 43.7 ms: 1.07x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.02 ms: 1.08x slower                                                    |
| richards                   | 50.9 ms                                                               | 55.0 ms: 1.08x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.56 ms: 1.08x slower                                                    |
| scimark_fft                | 418 ms                                                                | 455 ms: 1.09x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 108 ms: 1.09x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 5.07 ms: 1.09x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 401 us: 1.10x slower                                                     |
| scimark_sor                | 150 ms                                                                | 165 ms: 1.10x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.82 ms: 1.10x slower                                                    |
| pyflate                    | 559 ms                                                                | 616 ms: 1.10x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.40 ms: 1.10x slower                                                    |
| fannkuch                   | 443 ms                                                                | 491 ms: 1.11x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.4 ms: 1.11x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 72.8 ms: 1.12x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.23 us: 1.12x slower                                                    |
| logging_silent             | 127 ns                                                                | 143 ns: 1.13x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 205 us: 1.13x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.2 ms: 1.13x slower                                                    |
| spectral_norm              | 131 ms                                                                | 150 ms: 1.15x slower                                                     |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                                     |
| nbody                      | 105 ms                                                                | 123 ms: 1.18x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.75 ms: 1.54x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.83 ms: 2.00x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.80 sec: 963.98x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.10x slower                                                             |

Benchmark hidden because not significant (20): crypto_pyaes, 2to3, bench_thread_pool, sqlglot_transpile, chaos, sqlglot_parse, async_generators, xml_etree_parse, sympy_str, sympy_integrate, xml_etree_iterparse, scimark_monte_carlo, json, genshi_xml, deltablue, thrift, pylint, unpickle_pure_python, meteor_contest, genshi_text
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 56.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x