# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.026x faster
- HPT reliability: 93.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                     |
| async_tree_none            | 624 ms                                                                | 403 ms: 1.55x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 484 ms: 1.53x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 928 ms: 1.52x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 520 ms: 1.49x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 686 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 680 ms: 1.30x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.47x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 96.1 ms: 1.04x slower                                                    |
| nbody          | 105 ms                                                                | 129 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                                    |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| xml_etree_process   | 79.0 ms                                                               | 83.2 ms: 1.05x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 385 us: 1.06x slower                                                     |
| json_loads          | 30.7 us                                                               | 32.7 us: 1.06x slower                                                    |
| xml_etree_generate  | 112 ms                                                                | 125 ms: 1.11x slower                                                     |
| json_dumps          | 12.3 ms                                                               | 14.5 ms: 1.19x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (2): tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.97 ms: 1.07x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 28.6 ms: 1.04x slower                                                    |
| genshi_xml     | 60.6 ms                                                               | 66.6 ms: 1.10x slower                                                    |
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                     |
| async_tree_none            | 624 ms                                                                | 403 ms: 1.55x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 484 ms: 1.53x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 928 ms: 1.52x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 520 ms: 1.49x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 686 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 680 ms: 1.30x faster                                                     |
| deepcopy                   | 446 us                                                                | 346 us: 1.29x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.3 us: 1.20x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.61 us: 1.14x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                                    |
| comprehensions             | 25.4 us                                                               | 22.4 us: 1.13x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                    |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                                     |
| pylint                     | 355 ms                                                                | 326 ms: 1.09x faster                                                     |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.17 us: 1.06x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 149 ms: 1.05x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.97 us: 1.05x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 83.6 ms: 1.04x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 129 ms: 1.03x slower                                                     |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 28.6 ms: 1.04x slower                                                    |
| float                      | 92.1 ms                                                               | 96.1 ms: 1.04x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                     |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 83.2 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 385 us: 1.06x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.06x slower                                                     |
| sympy_expand               | 454 ms                                                                | 481 ms: 1.06x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 974 ms: 1.06x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.06x slower                                                    |
| pyflate                    | 559 ms                                                                | 596 ms: 1.07x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.02 sec: 1.07x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.97 ms: 1.07x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.51 ms: 1.08x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.07 us: 1.08x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 66.4 ms: 1.08x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 66.6 ms: 1.10x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 492 ms: 1.11x slower                                                     |
| richards                   | 50.9 ms                                                               | 56.7 ms: 1.11x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 125 ms: 1.11x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.52 ms: 1.12x slower                                                    |
| logging_silent             | 127 ns                                                                | 142 ns: 1.12x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.19x slower                                                    |
| mypy2                      | 873 ms                                                                | 1.04 sec: 1.19x slower                                                   |
| nbody                      | 105 ms                                                                | 129 ms: 1.23x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.92 ms: 1.57x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.56 ms: 1.86x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.45 sec: 773.18x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (27): deltablue, scimark_lu, sympy_str, html5lib, coroutines, 2to3, scimark_sparse_mat_mult, mdp, sqlglot_parse, dulwich_log, scimark_monte_carlo, docutils, scimark_fft, tomli_loads, async_generators, spectral_norm, pycparser, chaos, sqlglot_transpile, django_template, unpickle_pure_python, thrift, pidigits, richards_super, bench_thread_pool, sympy_integrate, regex_dna
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 93.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x