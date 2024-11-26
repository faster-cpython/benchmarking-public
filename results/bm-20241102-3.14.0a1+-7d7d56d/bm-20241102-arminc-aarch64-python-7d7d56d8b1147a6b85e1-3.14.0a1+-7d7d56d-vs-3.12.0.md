# Results vs. 3.12.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.001x slower
- HPT reliability: 62.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                   |
| html5lib       | 65.1 ms                                                               | 66.4 ms: 1.02x slower                                                    |
| tornado_http   | 136 ms                                                                | 128 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 457 ms: 1.36x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 611 ms: 1.27x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 457 ms: 1.26x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 99.9 ms: 1.08x slower                                                    |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 5.11 ms: 1.10x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 33.3 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python | 365 us                                                                | 381 us: 1.04x slower                                                     |
| tomli_loads        | 2.59 sec                                                              | 2.74 sec: 1.06x slower                                                   |
| json_loads         | 30.7 us                                                               | 32.7 us: 1.06x slower                                                    |
| xml_etree_process  | 79.0 ms                                                               | 84.7 ms: 1.07x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.95 ms: 1.07x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 29.4 ms: 1.07x slower                                                    |
| django_template | 40.7 ms                                                               | 43.6 ms: 1.07x slower                                                    |
| mako            | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 457 ms: 1.36x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 611 ms: 1.27x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 457 ms: 1.26x faster                                                     |
| deepcopy                   | 446 us                                                                | 355 us: 1.25x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.6 us: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.20x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.2 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                     |
| comprehensions             | 25.4 us                                                               | 21.3 us: 1.19x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| go                         | 157 ms                                                                | 143 ms: 1.10x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 143 ms: 1.10x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.73 us: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.20 us: 1.06x faster                                                    |
| tornado_http               | 136 ms                                                                | 128 ms: 1.06x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.05x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                                   |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 66.4 ms: 1.02x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 103 ms: 1.03x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 381 us: 1.04x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                                   |
| sympy_expand               | 454 ms                                                                | 476 ms: 1.05x slower                                                     |
| thrift                     | 937 us                                                                | 985 us: 1.05x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 963 ms: 1.05x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.74 sec: 1.06x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.99 sec: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.06x slower                                                    |
| json                       | 5.54 ms                                                               | 5.91 ms: 1.07x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.95 ms: 1.07x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 29.4 ms: 1.07x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 84.7 ms: 1.07x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 65.8 ms: 1.07x slower                                                    |
| django_template            | 40.7 ms                                                               | 43.6 ms: 1.07x slower                                                    |
| fannkuch                   | 443 ms                                                                | 478 ms: 1.08x slower                                                     |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                                     |
| pyflate                    | 559 ms                                                                | 605 ms: 1.08x slower                                                     |
| float                      | 92.1 ms                                                               | 99.9 ms: 1.08x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                    |
| richards_super             | 58.5 ms                                                               | 63.8 ms: 1.09x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.77 ms: 1.09x slower                                                    |
| scimark_fft                | 418 ms                                                                | 457 ms: 1.09x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.15 us: 1.10x slower                                                    |
| richards                   | 50.9 ms                                                               | 56.1 ms: 1.10x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 5.11 ms: 1.10x slower                                                    |
| scimark_sor                | 150 ms                                                                | 166 ms: 1.11x slower                                                     |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 208 us: 1.15x slower                                                     |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.87 ms: 1.16x slower                                                    |
| spectral_norm              | 131 ms                                                                | 152 ms: 1.16x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 33.3 ms: 1.17x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.88 ms: 1.57x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.89 ms: 2.03x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.50 sec: 779.23x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.10x slower                                                             |

Benchmark hidden because not significant (26): regex_compile, sqlalchemy_imperative, logging_format, crypto_pyaes, 2to3, dulwich_log, deltablue, xml_etree_parse, sympy_integrate, chaos, sqlglot_parse, sqlglot_transpile, sympy_str, async_generators, pylint, asyncio_websockets, regex_dna, xml_etree_generate, coroutines, unpickle_pure_python, pidigits, scimark_monte_carlo, hexiom, genshi_xml, xml_etree_iterparse, sqlglot_normalize
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 62.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x