# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_compa
- machine: linux-aarch64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.03x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                            |
| html5lib       | 65.1 ms                                                               | 61.2 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                              |
| async_tree_none            | 624 ms                                                                | 393 ms: 1.59x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 466 ms: 1.59x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 893 ms: 1.58x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.54x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 666 ms: 1.37x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 657 ms: 1.35x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.5 ms: 1.08x faster                                                             |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                              |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                             |
| regex_dna      | 254 ms                                                                | 219 ms: 1.16x faster                                                              |
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                              |
| regex_v8       | 28.3 ms                                                               | 27.2 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                              |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                              |
| tomli_loads         | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                            |
| xml_etree_generate  | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| json_loads          | 30.7 us                                                               | 32.8 us: 1.07x slower                                                             |
| pickle_pure_python  | 365 us                                                                | 394 us: 1.08x slower                                                              |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                              |
| async_tree_none            | 624 ms                                                                | 393 ms: 1.59x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 466 ms: 1.59x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 893 ms: 1.58x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.54x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 666 ms: 1.37x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 657 ms: 1.35x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                             |
| deepcopy                   | 446 us                                                                | 338 us: 1.32x faster                                                              |
| comprehensions             | 25.4 us                                                               | 20.1 us: 1.27x faster                                                             |
| generators                 | 43.5 ms                                                               | 35.4 ms: 1.23x faster                                                             |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                              |
| regex_effbot               | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 52.3 ms: 1.18x faster                                                             |
| regex_dna                  | 254 ms                                                                | 219 ms: 1.16x faster                                                              |
| pylint                     | 355 ms                                                                | 316 ms: 1.12x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.74 us: 1.10x faster                                                             |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                              |
| async_generators           | 491 ms                                                                | 451 ms: 1.09x faster                                                              |
| spectral_norm              | 131 ms                                                                | 120 ms: 1.09x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                             |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                              |
| pyflate                    | 559 ms                                                                | 518 ms: 1.08x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                              |
| float                      | 92.1 ms                                                               | 85.5 ms: 1.08x faster                                                             |
| html5lib                   | 65.1 ms                                                               | 61.2 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                            |
| sympy_integrate            | 21.6 ms                                                               | 20.5 ms: 1.05x faster                                                             |
| sympy_str                  | 280 ms                                                                | 266 ms: 1.05x faster                                                              |
| crypto_pyaes               | 86.6 ms                                                               | 82.7 ms: 1.05x faster                                                             |
| regex_v8                   | 28.3 ms                                                               | 27.2 ms: 1.04x faster                                                             |
| deltablue                  | 4.12 ms                                                               | 3.96 ms: 1.04x faster                                                             |
| scimark_sor                | 150 ms                                                                | 144 ms: 1.04x faster                                                              |
| meteor_contest             | 112 ms                                                                | 108 ms: 1.04x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.4 ms: 1.03x faster                                                             |
| 2to3                       | 308 ms                                                                | 301 ms: 1.03x faster                                                              |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                            |
| docutils                   | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                            |
| logging_format             | 8.34 us                                                               | 8.22 us: 1.02x faster                                                             |
| logging_simple             | 7.63 us                                                               | 7.55 us: 1.01x faster                                                             |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| scimark_lu                 | 146 ms                                                                | 147 ms: 1.01x slower                                                              |
| richards_super             | 58.5 ms                                                               | 59.3 ms: 1.01x slower                                                             |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.02x slower                                                              |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                              |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                              |
| json                       | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                             |
| fannkuch                   | 443 ms                                                                | 468 ms: 1.05x slower                                                              |
| richards                   | 50.9 ms                                                               | 54.3 ms: 1.07x slower                                                             |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 394 us: 1.08x slower                                                              |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.09x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                             |
| pprint_pformat             | 1.88 sec                                                              | 2.08 sec: 1.11x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 1.01 sec: 1.11x slower                                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.91 ms: 1.12x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.70 ms: 1.14x slower                                                             |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                              |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                              |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.97 ms: 1.59x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.72 ms: 1.94x slower                                                             |
| logging_silent             | 127 ns                                                                | 646 ns: 5.09x slower                                                              |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                                      |

Benchmark hidden because not significant (12): chaos, django_template, nqueens, genshi_text, hexiom, genshi_xml, thrift, scimark_fft, xml_etree_process, coroutines, unpickle_pure_python, sqlite_synth
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-arminc-aarch64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.10x