# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_shim
- machine: linux-aarch64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.024x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                            |
| html5lib       | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.58x faster                                              |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                              |
| async_tree_none            | 624 ms                                                                | 399 ms: 1.56x faster                                              |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.54x faster                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.36x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                              |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.5 ms: 1.12x faster                                             |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                              |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                             |
| regex_dna      | 254 ms                                                                | 221 ms: 1.15x faster                                              |
| regex_compile  | 137 ms                                                                | 120 ms: 1.14x faster                                              |
| regex_v8       | 28.3 ms                                                               | 27.2 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                            |
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                              |
| unpickle_pure_python | 260 us                                                                | 249 us: 1.04x faster                                              |
| xml_etree_iterparse  | 150 ms                                                                | 145 ms: 1.04x faster                                              |
| xml_etree_process    | 79.0 ms                                                               | 77.8 ms: 1.02x faster                                             |
| json_loads           | 30.7 us                                                               | 32.8 us: 1.07x slower                                             |
| pickle_pure_python   | 365 us                                                                | 394 us: 1.08x slower                                              |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                             |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.4 ms: 1.04x faster                                             |
| mako           | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                             |
| genshi_xml     | 60.6 ms                                                               | 62.0 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.62 sec: 2.11x faster                                            |
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.58x faster                                              |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                              |
| async_tree_none            | 624 ms                                                                | 399 ms: 1.56x faster                                              |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.54x faster                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 922 ms: 1.52x faster                                              |
| deepcopy_memo              | 49.6 us                                                               | 36.0 us: 1.38x faster                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.36x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                              |
| deepcopy                   | 446 us                                                                | 337 us: 1.32x faster                                              |
| generators                 | 43.5 ms                                                               | 35.7 ms: 1.22x faster                                             |
| regex_effbot               | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                             |
| richards                   | 50.9 ms                                                               | 43.3 ms: 1.18x faster                                             |
| richards_super             | 58.5 ms                                                               | 49.7 ms: 1.18x faster                                             |
| dulwich_log                | 62.0 ms                                                               | 53.2 ms: 1.17x faster                                             |
| comprehensions             | 25.4 us                                                               | 21.9 us: 1.16x faster                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.54 us: 1.16x faster                                             |
| regex_dna                  | 254 ms                                                                | 221 ms: 1.15x faster                                              |
| regex_compile              | 137 ms                                                                | 120 ms: 1.14x faster                                              |
| tomli_loads                | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                            |
| float                      | 92.1 ms                                                               | 82.5 ms: 1.12x faster                                             |
| spectral_norm              | 131 ms                                                                | 117 ms: 1.11x faster                                              |
| logging_format             | 8.34 us                                                               | 7.55 us: 1.11x faster                                             |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.10x faster                                             |
| pylint                     | 355 ms                                                                | 321 ms: 1.10x faster                                              |
| logging_simple             | 7.63 us                                                               | 7.00 us: 1.09x faster                                             |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                              |
| scimark_sor                | 150 ms                                                                | 139 ms: 1.08x faster                                              |
| deltablue                  | 4.12 ms                                                               | 3.83 ms: 1.08x faster                                             |
| raytrace                   | 353 ms                                                                | 330 ms: 1.07x faster                                              |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                              |
| sympy_integrate            | 21.6 ms                                                               | 20.5 ms: 1.05x faster                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.0 ms: 1.05x faster                                             |
| html5lib                   | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                             |
| sqlite_synth               | 3.77 us                                                               | 3.61 us: 1.05x faster                                             |
| go                         | 157 ms                                                                | 150 ms: 1.04x faster                                              |
| unpickle_pure_python       | 260 us                                                                | 249 us: 1.04x faster                                              |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                             |
| regex_v8                   | 28.3 ms                                                               | 27.2 ms: 1.04x faster                                             |
| xml_etree_iterparse        | 150 ms                                                                | 145 ms: 1.04x faster                                              |
| genshi_text                | 27.4 ms                                                               | 26.4 ms: 1.04x faster                                             |
| pyflate                    | 559 ms                                                                | 541 ms: 1.03x faster                                              |
| xml_etree_process          | 79.0 ms                                                               | 77.8 ms: 1.02x faster                                             |
| mako                       | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                             |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                              |
| coroutines                 | 29.0 ms                                                               | 29.4 ms: 1.01x slower                                             |
| genshi_xml                 | 60.6 ms                                                               | 62.0 ms: 1.02x slower                                             |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                              |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                             |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                            |
| thrift                     | 937 us                                                                | 988 us: 1.05x slower                                              |
| fannkuch                   | 443 ms                                                                | 470 ms: 1.06x slower                                              |
| hexiom                     | 6.98 ms                                                               | 7.41 ms: 1.06x slower                                             |
| json                       | 5.54 ms                                                               | 5.89 ms: 1.06x slower                                             |
| nqueens                    | 99.2 ms                                                               | 106 ms: 1.06x slower                                              |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                             |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.07x slower                                            |
| crypto_pyaes               | 86.6 ms                                                               | 93.2 ms: 1.08x slower                                             |
| pickle_pure_python         | 365 us                                                                | 394 us: 1.08x slower                                              |
| sympy_expand               | 454 ms                                                                | 490 ms: 1.08x slower                                              |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                             |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.15 ms: 1.15x slower                                             |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.24 sec: 1.19x slower                                            |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                              |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                            |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                             |
| gc_traversal               | 4.40 ms                                                               | 6.75 ms: 1.54x slower                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.78 ms: 1.97x slower                                             |
| telco                      | 8.51 ms                                                               | 164 ms: 19.28x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                      |

Benchmark hidden because not significant (9): scimark_fft, scimark_lu, xml_etree_generate, django_template, async_generators, 2to3, logging_silent, sympy_str, asyncio_websockets
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.12x