# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_nops
- machine: linux-aarch64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.055x faster
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 309 ms: 1.00x slower                                              |
| docutils       | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                            |
| html5lib       | 65.1 ms                                                               | 62.6 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.64x faster                                              |
| async_tree_io              | 1.41 sec                                                              | 905 ms: 1.56x faster                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 477 ms: 1.55x faster                                              |
| async_tree_none            | 624 ms                                                                | 404 ms: 1.54x faster                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 927 ms: 1.51x faster                                              |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.49x faster                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 671 ms: 1.36x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 668 ms: 1.32x faster                                              |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.1 ms: 1.11x faster                                             |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                              |
| nbody          | 105 ms                                                                | 126 ms: 1.21x slower                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.88 ms: 1.20x faster                                             |
| regex_dna      | 254 ms                                                                | 218 ms: 1.16x faster                                              |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                              |
| regex_v8       | 28.3 ms                                                               | 26.6 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                            |
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                              |
| unpickle_pure_python | 260 us                                                                | 248 us: 1.05x faster                                              |
| xml_etree_iterparse  | 150 ms                                                                | 144 ms: 1.04x faster                                              |
| xml_etree_generate   | 112 ms                                                                | 108 ms: 1.04x faster                                              |
| xml_etree_process    | 79.0 ms                                                               | 77.2 ms: 1.02x faster                                             |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                             |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                             |
| pickle_pure_python   | 365 us                                                                | 401 us: 1.10x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                             |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.7 ms: 1.03x faster                                             |
| mako           | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                             |
| genshi_xml     | 60.6 ms                                                               | 62.4 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                            |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.64x faster                                              |
| async_tree_io              | 1.41 sec                                                              | 905 ms: 1.56x faster                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 477 ms: 1.55x faster                                              |
| async_tree_none            | 624 ms                                                                | 404 ms: 1.54x faster                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 927 ms: 1.51x faster                                              |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.49x faster                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 671 ms: 1.36x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 668 ms: 1.32x faster                                              |
| deepcopy                   | 446 us                                                                | 337 us: 1.32x faster                                              |
| deepcopy_memo              | 49.6 us                                                               | 37.7 us: 1.32x faster                                             |
| regex_effbot               | 4.64 ms                                                               | 3.88 ms: 1.20x faster                                             |
| generators                 | 43.5 ms                                                               | 36.5 ms: 1.19x faster                                             |
| comprehensions             | 25.4 us                                                               | 21.7 us: 1.17x faster                                             |
| regex_dna                  | 254 ms                                                                | 218 ms: 1.16x faster                                              |
| dulwich_log                | 62.0 ms                                                               | 53.5 ms: 1.16x faster                                             |
| richards                   | 50.9 ms                                                               | 44.1 ms: 1.15x faster                                             |
| richards_super             | 58.5 ms                                                               | 51.1 ms: 1.14x faster                                             |
| tomli_loads                | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                            |
| deepcopy_reduce            | 4.10 us                                                               | 3.65 us: 1.12x faster                                             |
| pylint                     | 355 ms                                                                | 318 ms: 1.11x faster                                              |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                              |
| float                      | 92.1 ms                                                               | 83.1 ms: 1.11x faster                                             |
| logging_simple             | 7.63 us                                                               | 6.99 us: 1.09x faster                                             |
| spectral_norm              | 131 ms                                                                | 120 ms: 1.09x faster                                              |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                              |
| scimark_sor                | 150 ms                                                                | 139 ms: 1.08x faster                                              |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                              |
| logging_format             | 8.34 us                                                               | 7.82 us: 1.07x faster                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.7 ms: 1.07x faster                                             |
| regex_v8                   | 28.3 ms                                                               | 26.6 ms: 1.06x faster                                             |
| deltablue                  | 4.12 ms                                                               | 3.87 ms: 1.06x faster                                             |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.06x faster                                             |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                             |
| unpickle_pure_python       | 260 us                                                                | 248 us: 1.05x faster                                              |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                              |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                              |
| html5lib                   | 65.1 ms                                                               | 62.6 ms: 1.04x faster                                             |
| pyflate                    | 559 ms                                                                | 539 ms: 1.04x faster                                              |
| xml_etree_generate         | 112 ms                                                                | 108 ms: 1.04x faster                                              |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                             |
| genshi_text                | 27.4 ms                                                               | 26.7 ms: 1.03x faster                                             |
| xml_etree_process          | 79.0 ms                                                               | 77.2 ms: 1.02x faster                                             |
| scimark_fft                | 418 ms                                                                | 409 ms: 1.02x faster                                              |
| sqlite_synth               | 3.77 us                                                               | 3.72 us: 1.01x faster                                             |
| go                         | 157 ms                                                                | 156 ms: 1.01x faster                                              |
| 2to3                       | 308 ms                                                                | 309 ms: 1.00x slower                                              |
| coroutines                 | 29.0 ms                                                               | 29.2 ms: 1.01x slower                                             |
| thrift                     | 937 us                                                                | 944 us: 1.01x slower                                              |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                              |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                              |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                             |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                              |
| json                       | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                             |
| docutils                   | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                            |
| genshi_xml                 | 60.6 ms                                                               | 62.4 ms: 1.03x slower                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                             |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                             |
| scimark_lu                 | 146 ms                                                                | 154 ms: 1.06x slower                                              |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                              |
| telco                      | 8.51 ms                                                               | 9.08 ms: 1.07x slower                                             |
| hexiom                     | 6.98 ms                                                               | 7.47 ms: 1.07x slower                                             |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                             |
| sympy_expand               | 454 ms                                                                | 493 ms: 1.09x slower                                              |
| crypto_pyaes               | 86.6 ms                                                               | 94.6 ms: 1.09x slower                                             |
| pickle_pure_python         | 365 us                                                                | 401 us: 1.10x slower                                              |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.10x slower                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.06 ms: 1.14x slower                                             |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                              |
| typing_runtime_protocols   | 181 us                                                                | 213 us: 1.18x slower                                              |
| nbody                      | 105 ms                                                                | 126 ms: 1.21x slower                                              |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.27x slower                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.39 sec: 1.27x slower                                            |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                             |
| gc_traversal               | 4.40 ms                                                               | 6.86 ms: 1.56x slower                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.84 ms: 2.00x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.05x faster                                                      |

Benchmark hidden because not significant (5): django_template, async_generators, sympy_str, nqueens, logging_silent
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-arminc-aarch64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 99.71% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x