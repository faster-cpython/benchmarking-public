# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.031x slower
- HPT reliability: 99.29%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 321 ms: 1.04x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.26 sec: 1.09x slower                                                   |
| html5lib       | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 935 ms: 1.50x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 502 ms: 1.47x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 962 ms: 1.47x faster                                                     |
| async_tree_none            | 624 ms                                                                | 428 ms: 1.46x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 535 ms: 1.45x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 399 ms: 1.45x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 703 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 683 ms: 1.29x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.42x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.04 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 142 ms: 1.03x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 31.3 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| json_loads          | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 393 us: 1.08x slower                                                     |
| json_dumps          | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.12 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                    |
| django_template | 40.7 ms                                                               | 47.8 ms: 1.17x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.1 ms: 1.21x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 83.4 ms: 1.38x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 935 ms: 1.50x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 502 ms: 1.47x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 962 ms: 1.47x faster                                                     |
| async_tree_none            | 624 ms                                                                | 428 ms: 1.46x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 535 ms: 1.45x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 399 ms: 1.45x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 703 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 683 ms: 1.29x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 38.7 us: 1.28x faster                                                    |
| deepcopy                   | 446 us                                                                | 385 us: 1.16x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.04 ms: 1.15x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| pylint                     | 355 ms                                                                | 336 ms: 1.06x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| regex_compile              | 137 ms                                                                | 142 ms: 1.03x slower                                                     |
| logging_simple             | 7.63 us                                                               | 7.93 us: 1.04x slower                                                    |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| richards_super             | 58.5 ms                                                               | 60.8 ms: 1.04x slower                                                    |
| 2to3                       | 308 ms                                                                | 321 ms: 1.04x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| raytrace                   | 353 ms                                                                | 369 ms: 1.04x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.57 sec: 1.05x slower                                                   |
| logging_format             | 8.34 us                                                               | 8.73 us: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.55 ms: 1.06x slower                                                    |
| pyflate                    | 559 ms                                                                | 592 ms: 1.06x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.94 ms: 1.06x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 155 ms: 1.06x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.00 us: 1.06x slower                                                    |
| json                       | 5.54 ms                                                               | 5.92 ms: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.63 ms: 1.07x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 93.2 ms: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                     |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.44 ms: 1.08x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.42 ms: 1.08x slower                                                    |
| go                         | 157 ms                                                                | 171 ms: 1.09x slower                                                     |
| thrift                     | 937 us                                                                | 1.02 ms: 1.09x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.12 ms: 1.09x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.26 sec: 1.09x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.3 ms: 1.11x slower                                                    |
| richards                   | 50.9 ms                                                               | 56.3 ms: 1.11x slower                                                    |
| async_generators           | 491 ms                                                                | 543 ms: 1.11x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 171 ms: 1.11x slower                                                     |
| sympy_str                  | 280 ms                                                                | 311 ms: 1.11x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 68.2 ms: 1.11x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                     |
| sympy_expand               | 454 ms                                                                | 514 ms: 1.13x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 24.5 ms: 1.13x slower                                                    |
| logging_silent             | 127 ns                                                                | 144 ns: 1.14x slower                                                     |
| meteor_contest             | 112 ms                                                                | 128 ms: 1.15x slower                                                     |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.82 ms: 1.15x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.46 sec: 1.16x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 72.1 ms: 1.16x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.17x slower                                                     |
| django_template            | 40.7 ms                                                               | 47.8 ms: 1.17x slower                                                    |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.17x slower                                                     |
| fannkuch                   | 443 ms                                                                | 524 ms: 1.18x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| generators                 | 43.5 ms                                                               | 51.9 ms: 1.19x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 33.1 ms: 1.21x slower                                                    |
| chaos                      | 71.4 ms                                                               | 87.5 ms: 1.23x slower                                                    |
| mypy2                      | 873 ms                                                                | 1.09 sec: 1.24x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 129 ms: 1.30x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.59 ms: 1.37x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.38x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 83.4 ms: 1.38x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.65 sec: 1.41x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 7.13 ms: 1.62x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.68 ms: 1.92x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.37 sec: 194.12x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (13): deepcopy_reduce, scimark_monte_carlo, comprehensions, sqlalchemy_declarative, scimark_fft, coroutines, xml_etree_generate, float, unpickle_pure_python, asyncio_websockets, xml_etree_process, regex_dna, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.031x slower

# HPT report

- Reliability score: 99.29% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x