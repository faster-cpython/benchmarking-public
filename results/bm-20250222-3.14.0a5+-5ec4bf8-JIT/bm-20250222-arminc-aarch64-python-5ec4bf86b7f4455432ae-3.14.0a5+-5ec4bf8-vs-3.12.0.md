# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.003x slower
- HPT reliability: 58.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 323 ms: 1.05x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.19 sec: 1.07x slower                                                   |
| html5lib       | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 400 ms: 1.56x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 505 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.54x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 936 ms: 1.51x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 938 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 388 ms: 1.49x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 689 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 682 ms: 1.30x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.47x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.3 ms: 1.04x faster                                                    |
| nbody          | 105 ms                                                                | 130 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.97 ms: 1.17x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                   |
| xml_etree_process    | 79.0 ms                                                               | 82.2 ms: 1.04x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 39.5 us: 1.06x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.74 us: 1.09x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.79 us: 1.10x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 404 us: 1.11x slower                                                     |
| unpickle_pure_python | 260 us                                                                | 291 us: 1.12x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| pickle               | 13.4 us                                                               | 15.7 us: 1.17x slower                                                    |
| json_loads           | 30.7 us                                                               | 36.5 us: 1.19x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.6 ms: 1.03x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 64.5 ms: 1.06x slower                                                    |
| mako            | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 400 ms: 1.56x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 505 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.54x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 936 ms: 1.51x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 938 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 388 ms: 1.49x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 689 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 682 ms: 1.30x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.7 us: 1.25x faster                                                    |
| deepcopy                   | 446 us                                                                | 359 us: 1.24x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 3.97 ms: 1.17x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.3 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.65 us: 1.12x faster                                                    |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.11x faster                                                     |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                     |
| float                      | 92.1 ms                                                               | 88.3 ms: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.6 ms: 1.03x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.2 ms: 1.03x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.45 sec: 1.01x slower                                                   |
| scimark_sor                | 150 ms                                                                | 153 ms: 1.02x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                     |
| thrift                     | 937 us                                                                | 962 us: 1.03x slower                                                     |
| scimark_fft                | 418 ms                                                                | 435 ms: 1.04x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 82.2 ms: 1.04x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 64.7 ms: 1.04x slower                                                    |
| pyflate                    | 559 ms                                                                | 584 ms: 1.04x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 22.6 ms: 1.05x slower                                                    |
| 2to3                       | 308 ms                                                                | 323 ms: 1.05x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.95 us: 1.05x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 132 ms: 1.05x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.93 ms: 1.06x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 39.5 us: 1.06x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 64.5 ms: 1.06x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.19 sec: 1.07x slower                                                   |
| json                       | 5.54 ms                                                               | 5.94 ms: 1.07x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.74 us: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.61 ms: 1.10x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.79 us: 1.10x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 67.8 ms: 1.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 404 us: 1.11x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                                    |
| logging_silent             | 127 ns                                                                | 142 ns: 1.12x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 291 us: 1.12x slower                                                     |
| sympy_expand               | 454 ms                                                                | 511 ms: 1.13x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.00 ms: 1.13x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 112 ms: 1.13x slower                                                     |
| meteor_contest             | 112 ms                                                                | 127 ms: 1.14x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.89 ms: 1.16x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.47 sec: 1.17x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 102 ms: 1.18x slower                                                     |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                     |
| json_loads                 | 30.7 us                                                               | 36.5 us: 1.19x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.41 ms: 1.20x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 219 us: 1.21x slower                                                     |
| fannkuch                   | 443 ms                                                                | 549 ms: 1.24x slower                                                     |
| nbody                      | 105 ms                                                                | 130 ms: 1.24x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.27 sec: 1.39x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.66 sec: 1.41x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.96 ms: 1.58x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.58 ms: 1.86x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.23 sec: 315.54x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                             |

Benchmark hidden because not significant (24): pylint, logging_format, logging_simple, comprehensions, regex_compile, xml_etree_iterparse, unpickle, asyncio_tcp, chaos, async_generators, sympy_sum, scimark_lu, richards_super, genshi_text, bench_thread_pool, sympy_str, xml_etree_generate, scimark_monte_carlo, richards, deltablue, pidigits, coroutines, regex_dna, go
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 58.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x