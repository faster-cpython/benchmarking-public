# Results vs. 3.12.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-aarch64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 58.7 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 362 ms: 1.72x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 461 ms: 1.69x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 895 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 369 ms: 1.56x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 656 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 645 ms: 1.37x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.56x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                    |
| nbody          | 105 ms                                                                | 123 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.30 ms: 1.41x faster                                                    |
| regex_dna      | 254 ms                                                                | 197 ms: 1.29x faster                                                     |
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 165 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 138 ms: 1.09x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 33.2 us: 1.08x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 400 us: 1.10x slower                                                     |
| unpickle_pure_python | 260 us                                                                | 287 us: 1.11x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.33 ms: 1.12x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.7 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.28x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 362 ms: 1.72x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 461 ms: 1.69x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 895 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 369 ms: 1.56x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 3.30 ms: 1.41x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 656 ms: 1.39x faster                                                     |
| deepcopy                   | 446 us                                                                | 325 us: 1.37x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 645 ms: 1.37x faster                                                     |
| regex_dna                  | 254 ms                                                                | 197 ms: 1.29x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.1 us: 1.27x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                    |
| async_generators           | 491 ms                                                                | 411 ms: 1.19x faster                                                     |
| generators                 | 43.5 ms                                                               | 36.8 ms: 1.18x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 165 ms: 1.18x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.47 us: 1.18x faster                                                    |
| pylint                     | 355 ms                                                                | 307 ms: 1.16x faster                                                     |
| spectral_norm              | 131 ms                                                                | 116 ms: 1.13x faster                                                     |
| go                         | 157 ms                                                                | 141 ms: 1.12x faster                                                     |
| raytrace                   | 353 ms                                                                | 317 ms: 1.11x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 58.7 ms: 1.11x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 138 ms: 1.09x faster                                                     |
| scimark_fft                | 418 ms                                                                | 384 ms: 1.09x faster                                                     |
| meteor_contest             | 112 ms                                                                | 103 ms: 1.08x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.6 ms: 1.07x faster                                                    |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.14 us: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.06x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.06x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.92 us: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.95 us: 1.05x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 64.5 ms: 1.05x slower                                                    |
| sympy_expand               | 454 ms                                                                | 480 ms: 1.06x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.03 ms: 1.06x slower                                                    |
| thrift                     | 937 us                                                                | 1.00 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.10x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 287 us: 1.11x slower                                                     |
| logging_silent             | 127 ns                                                                | 141 ns: 1.11x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.33 ms: 1.12x slower                                                    |
| json                       | 5.54 ms                                                               | 6.20 ms: 1.12x slower                                                    |
| nbody                      | 105 ms                                                                | 123 ms: 1.18x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.7 ms: 1.47x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.64 ms: 1.51x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.74 ms: 1.95x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.37 sec: 761.56x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (30): scimark_monte_carlo, deltablue, xml_etree_generate, coroutines, django_template, scimark_sparse_mat_mult, pyflate, pidigits, pprint_safe_repr, xml_etree_process, sympy_str, sqlglot_parse, sqlglot_normalize, 2to3, pprint_pformat, docutils, richards_super, nqueens, sympy_integrate, asyncio_websockets, sqlglot_transpile, genshi_text, regex_v8, richards, scimark_sor, genshi_xml, bench_thread_pool, dulwich_log, crypto_pyaes, hexiom
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-arminc-aarch64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x