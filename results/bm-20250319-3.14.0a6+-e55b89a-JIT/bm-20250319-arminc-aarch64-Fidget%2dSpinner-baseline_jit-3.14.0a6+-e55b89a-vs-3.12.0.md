# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: linux-aarch64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.013x faster
- HPT reliability: 80.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                               |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 485 ms: 1.60x faster                                                       |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 902 ms: 1.56x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 477 ms: 1.55x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 921 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                                       |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.9 ms: 1.02x faster                                                      |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                       |
| nbody          | 105 ms                                                                | 127 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                                      |
| regex_v8       | 28.3 ms                                                               | 27.5 ms: 1.03x faster                                                      |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 174 ms: 1.12x faster                                                       |
| tomli_loads          | 2.59 sec                                                              | 2.41 sec: 1.08x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.07x faster                                                       |
| xml_etree_process    | 79.0 ms                                                               | 82.4 ms: 1.04x slower                                                      |
| pickle_pure_python   | 365 us                                                                | 400 us: 1.10x slower                                                       |
| json_loads           | 30.7 us                                                               | 34.0 us: 1.11x slower                                                      |
| unpickle_pure_python | 260 us                                                                | 293 us: 1.13x slower                                                       |
| json_dumps           | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                      |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 61.4 ms: 1.01x slower                                                      |
| mako           | 12.9 ms                                                               | 15.0 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                               |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 485 ms: 1.60x faster                                                       |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 902 ms: 1.56x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 477 ms: 1.55x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 921 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 668 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                                       |
| deepcopy                   | 446 us                                                                | 340 us: 1.31x faster                                                       |
| deepcopy_memo              | 49.6 us                                                               | 38.3 us: 1.29x faster                                                      |
| generators                 | 43.5 ms                                                               | 36.3 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 4.10 us                                                               | 3.55 us: 1.15x faster                                                      |
| regex_effbot               | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                                      |
| dulwich_log                | 62.0 ms                                                               | 55.1 ms: 1.13x faster                                                      |
| xml_etree_parse            | 195 ms                                                                | 174 ms: 1.12x faster                                                       |
| pylint                     | 355 ms                                                                | 319 ms: 1.11x faster                                                       |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.10x faster                                                      |
| logging_simple             | 7.63 us                                                               | 6.98 us: 1.09x faster                                                      |
| tomli_loads                | 2.59 sec                                                              | 2.41 sec: 1.08x faster                                                     |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                                       |
| logging_format             | 8.34 us                                                               | 7.80 us: 1.07x faster                                                      |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                       |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                       |
| async_generators           | 491 ms                                                                | 470 ms: 1.04x faster                                                       |
| regex_v8                   | 28.3 ms                                                               | 27.5 ms: 1.03x faster                                                      |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                       |
| float                      | 92.1 ms                                                               | 89.9 ms: 1.02x faster                                                      |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.4 ms: 1.02x faster                                                      |
| sympy_str                  | 280 ms                                                                | 277 ms: 1.01x faster                                                       |
| go                         | 157 ms                                                                | 156 ms: 1.01x faster                                                       |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                       |
| thrift                     | 937 us                                                                | 949 us: 1.01x slower                                                       |
| genshi_xml                 | 60.6 ms                                                               | 61.4 ms: 1.01x slower                                                      |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.02x slower                                                      |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                       |
| scimark_lu                 | 146 ms                                                                | 150 ms: 1.03x slower                                                       |
| logging_silent             | 127 ns                                                                | 131 ns: 1.04x slower                                                       |
| docutils                   | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 82.4 ms: 1.04x slower                                                      |
| richards_super             | 58.5 ms                                                               | 61.4 ms: 1.05x slower                                                      |
| richards                   | 50.9 ms                                                               | 53.6 ms: 1.05x slower                                                      |
| deltablue                  | 4.12 ms                                                               | 4.34 ms: 1.05x slower                                                      |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                                      |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.06x slower                                                       |
| chaos                      | 71.4 ms                                                               | 75.5 ms: 1.06x slower                                                      |
| nqueens                    | 99.2 ms                                                               | 106 ms: 1.07x slower                                                       |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                                     |
| pyflate                    | 559 ms                                                                | 597 ms: 1.07x slower                                                       |
| json                       | 5.54 ms                                                               | 5.93 ms: 1.07x slower                                                      |
| sympy_expand               | 454 ms                                                                | 488 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 85.1 ms                                                               | 91.9 ms: 1.08x slower                                                      |
| pprint_pformat             | 1.88 sec                                                              | 2.04 sec: 1.08x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 94.3 ms: 1.09x slower                                                      |
| comprehensions             | 25.4 us                                                               | 27.7 us: 1.09x slower                                                      |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.10x slower                                                       |
| pprint_safe_repr           | 916 ms                                                                | 1.01 sec: 1.10x slower                                                     |
| json_loads                 | 30.7 us                                                               | 34.0 us: 1.11x slower                                                      |
| coverage                   | 87.3 ms                                                               | 98.3 ms: 1.13x slower                                                      |
| unpickle_pure_python       | 260 us                                                                | 293 us: 1.13x slower                                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.00 ms: 1.13x slower                                                      |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                      |
| mako                       | 12.9 ms                                                               | 15.0 ms: 1.16x slower                                                      |
| fannkuch                   | 443 ms                                                                | 528 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 181 us                                                                | 216 us: 1.20x slower                                                       |
| nbody                      | 105 ms                                                                | 127 ms: 1.21x slower                                                       |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                      |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                      |
| hexiom                     | 6.98 ms                                                               | 8.74 ms: 1.25x slower                                                      |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                      |
| gc_traversal               | 4.40 ms                                                               | 6.61 ms: 1.50x slower                                                      |
| create_gc_cycles           | 1.92 ms                                                               | 3.67 ms: 1.91x slower                                                      |
| bench_mp_pool              | 7.05 ms                                                               | 2.37 sec: 335.74x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                               |

Benchmark hidden because not significant (12): regex_compile, sqlalchemy_declarative, 2to3, spectral_norm, django_template, genshi_text, scimark_fft, coroutines, scimark_sor, xml_etree_generate, sympy_integrate, html5lib
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-arminc-aarch64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 80.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x