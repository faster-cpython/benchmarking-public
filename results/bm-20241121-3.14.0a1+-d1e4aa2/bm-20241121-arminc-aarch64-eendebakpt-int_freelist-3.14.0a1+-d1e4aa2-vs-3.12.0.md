# Results vs. 3.12.0

- fork: eendebakpt
- ref: int_freelist
- machine: linux-aarch64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.007x faster
- HPT reliability: 88.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 545 ms: 1.36x faster                                                 |
| async_tree_memoization     | 777 ms                                                                | 603 ms: 1.29x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 452 ms: 1.28x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 760 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 754 ms: 1.17x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                               |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 241 ms: 1.04x slower                                                 |
| float          | 92.1 ms                                                               | 96.8 ms: 1.05x slower                                                |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.07x faster                                                 |
| regex_effbot   | 4.64 ms                                                               | 5.17 ms: 1.11x slower                                                |
| regex_v8       | 28.3 ms                                                               | 32.1 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                               |
| xml_etree_process    | 79.0 ms                                                               | 82.5 ms: 1.05x slower                                                |
| xml_etree_generate   | 112 ms                                                                | 117 ms: 1.05x slower                                                 |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.05x slower                                                |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.07x slower                                                 |
| pickle_pure_python   | 365 us                                                                | 396 us: 1.08x slower                                                 |
| json_dumps           | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                         |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.86 ms: 1.06x slower                                                |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.40x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.2 ms: 1.03x slower                                                |
| mako           | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                         |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 448 ms: 1.39x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 545 ms: 1.36x faster                                                 |
| async_tree_memoization     | 777 ms                                                                | 603 ms: 1.29x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 452 ms: 1.28x faster                                                 |
| deepcopy                   | 446 us                                                                | 353 us: 1.26x faster                                                 |
| deepcopy_memo              | 49.6 us                                                               | 40.6 us: 1.22x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.20x faster                                               |
| generators                 | 43.5 ms                                                               | 36.2 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 760 ms: 1.20x faster                                                 |
| comprehensions             | 25.4 us                                                               | 21.6 us: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 754 ms: 1.17x faster                                                 |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                |
| deepcopy_reduce            | 4.10 us                                                               | 3.66 us: 1.12x faster                                                |
| raytrace                   | 353 ms                                                                | 321 ms: 1.10x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                               |
| go                         | 157 ms                                                                | 143 ms: 1.10x faster                                                 |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                 |
| regex_compile              | 137 ms                                                                | 129 ms: 1.07x faster                                                 |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                 |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.05x faster                                                 |
| sympy_str                  | 280 ms                                                                | 266 ms: 1.05x faster                                                 |
| dulwich_log                | 62.0 ms                                                               | 59.6 ms: 1.04x faster                                                |
| deltablue                  | 4.12 ms                                                               | 3.99 ms: 1.03x faster                                                |
| tomli_loads                | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                               |
| genshi_xml                 | 60.6 ms                                                               | 62.2 ms: 1.03x slower                                                |
| sqlglot_optimize           | 61.3 ms                                                               | 63.1 ms: 1.03x slower                                                |
| pidigits                   | 233 ms                                                                | 241 ms: 1.04x slower                                                 |
| nqueens                    | 99.2 ms                                                               | 103 ms: 1.04x slower                                                 |
| pprint_pformat             | 1.88 sec                                                              | 1.96 sec: 1.04x slower                                               |
| pyflate                    | 559 ms                                                                | 582 ms: 1.04x slower                                                 |
| pprint_safe_repr           | 916 ms                                                                | 955 ms: 1.04x slower                                                 |
| docutils                   | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                               |
| xml_etree_process          | 79.0 ms                                                               | 82.5 ms: 1.05x slower                                                |
| thrift                     | 937 us                                                                | 980 us: 1.05x slower                                                 |
| xml_etree_generate         | 112 ms                                                                | 117 ms: 1.05x slower                                                 |
| float                      | 92.1 ms                                                               | 96.8 ms: 1.05x slower                                                |
| richards                   | 50.9 ms                                                               | 53.6 ms: 1.05x slower                                                |
| hexiom                     | 6.98 ms                                                               | 7.34 ms: 1.05x slower                                                |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.05x slower                                                |
| sympy_expand               | 454 ms                                                                | 479 ms: 1.06x slower                                                 |
| python_startup_no_site     | 8.37 ms                                                               | 8.86 ms: 1.06x slower                                                |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                 |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.07x slower                                                 |
| richards_super             | 58.5 ms                                                               | 62.7 ms: 1.07x slower                                                |
| sqlglot_normalize          | 126 ms                                                                | 135 ms: 1.08x slower                                                 |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.08x slower                                                 |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                 |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                |
| fannkuch                   | 443 ms                                                                | 491 ms: 1.11x slower                                                 |
| regex_effbot               | 4.64 ms                                                               | 5.17 ms: 1.11x slower                                                |
| sqlite_synth               | 3.77 us                                                               | 4.27 us: 1.13x slower                                                |
| typing_runtime_protocols   | 181 us                                                                | 204 us: 1.13x slower                                                 |
| regex_v8                   | 28.3 ms                                                               | 32.1 ms: 1.13x slower                                                |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                 |
| telco                      | 8.51 ms                                                               | 9.91 ms: 1.16x slower                                                |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                 |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.40x slower                                                |
| gc_traversal               | 4.40 ms                                                               | 6.66 ms: 1.51x slower                                                |
| create_gc_cycles           | 1.92 ms                                                               | 3.93 ms: 2.05x slower                                                |
| bench_mp_pool              | 7.05 ms                                                               | 6.73 sec: 953.35x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                         |

Benchmark hidden because not significant (28): sqlalchemy_imperative, logging_format, crypto_pyaes, scimark_monte_carlo, logging_simple, 2to3, spectral_norm, chaos, xml_etree_iterparse, regex_dna, scimark_sparse_mat_mult, bench_thread_pool, sqlglot_parse, scimark_fft, mdp, coroutines, django_template, html5lib, sqlglot_transpile, pycparser, async_generators, sympy_integrate, asyncio_websockets, pylint, json, xml_etree_parse, genshi_text, meteor_contest
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 88.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x