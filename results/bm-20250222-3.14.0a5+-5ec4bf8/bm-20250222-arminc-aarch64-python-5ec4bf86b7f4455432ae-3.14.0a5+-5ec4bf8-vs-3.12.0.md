# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.029x faster
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 388 ms: 1.61x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 488 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 929 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 929 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.49x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 681 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 671 ms: 1.32x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.49x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.4 ms: 1.05x faster                                                    |
| nbody          | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.13 ms: 1.12x faster                                                    |
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 31.6 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| xml_etree_process    | 79.0 ms                                                               | 82.6 ms: 1.05x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 276 us: 1.06x slower                                                     |
| pickle_dict          | 37.3 us                                                               | 39.7 us: 1.06x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 397 us: 1.09x slower                                                     |
| pickle_list          | 5.25 us                                                               | 5.73 us: 1.09x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.87 us: 1.11x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                    |
| pickle               | 13.4 us                                                               | 15.5 us: 1.16x slower                                                    |
| json_loads           | 30.7 us                                                               | 35.9 us: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 64.9 ms: 1.07x slower                                                    |
| mako            | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 388 ms: 1.61x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 488 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 929 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 929 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.49x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 681 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 671 ms: 1.32x faster                                                     |
| deepcopy                   | 446 us                                                                | 361 us: 1.23x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.6 us: 1.22x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.5 us: 1.18x faster                                                    |
| pylint                     | 355 ms                                                                | 304 ms: 1.17x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.6 ms: 1.16x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.13 ms: 1.12x faster                                                    |
| go                         | 157 ms                                                                | 142 ms: 1.11x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.2 ms: 1.10x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.08x faster                                                     |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.83 us: 1.07x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                    |
| async_generators           | 491 ms                                                                | 459 ms: 1.07x faster                                                     |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| float                      | 92.1 ms                                                               | 87.4 ms: 1.05x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.05x faster                                                     |
| logging_format             | 8.34 us                                                               | 8.03 us: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.32 ms: 1.02x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.30 sec: 1.03x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 104 ms: 1.04x slower                                                     |
| thrift                     | 937 us                                                                | 978 us: 1.04x slower                                                     |
| sympy_expand               | 454 ms                                                                | 474 ms: 1.05x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 82.6 ms: 1.05x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.3 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 276 us: 1.06x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 39.7 us: 1.06x slower                                                    |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 978 ms: 1.07x slower                                                     |
| meteor_contest             | 112 ms                                                                | 120 ms: 1.07x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 64.9 ms: 1.07x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.49 ms: 1.07x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.03 sec: 1.08x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 66.2 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 397 us: 1.09x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.73 us: 1.09x slower                                                    |
| json                       | 5.54 ms                                                               | 6.06 ms: 1.09x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.20 us: 1.11x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.87 us: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 494 ms: 1.11x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 31.6 ms: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.7 ms: 1.13x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.81 ms: 1.15x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.5 us: 1.16x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                     |
| json_loads                 | 30.7 us                                                               | 35.9 us: 1.17x slower                                                    |
| nbody                      | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 7.33 ms: 1.67x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.72 ms: 1.94x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.33 sec: 1038.71x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (29): spectral_norm, dulwich_log, scimark_lu, chaos, logging_simple, deltablue, sqlglot_transpile, xml_etree_iterparse, sqlglot_parse, coroutines, unpickle, asyncio_tcp, html5lib, crypto_pyaes, genshi_text, sympy_str, mdp, pyflate, scimark_monte_carlo, richards_super, sympy_integrate, bench_thread_pool, 2to3, asyncio_websockets, scimark_fft, pidigits, regex_dna, scimark_sor, xml_etree_generate
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 99.34% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x