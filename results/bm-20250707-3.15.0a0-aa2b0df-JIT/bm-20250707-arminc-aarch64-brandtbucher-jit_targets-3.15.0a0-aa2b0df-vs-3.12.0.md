# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_targets
- machine: linux-aarch64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.032x slower
- HPT reliability: 51.56%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 319 ms: 1.04x slower                                                 |
| docutils       | 2.98 sec                                                              | 3.17 sec: 1.06x slower                                               |
| html5lib       | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                 |
| async_tree_memoization     | 777 ms                                                                | 497 ms: 1.56x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.53x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 930 ms: 1.52x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 926 ms: 1.52x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 685 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 672 ms: 1.31x faster                                                 |
| Geometric mean             | (ref)                                                                 | 1.48x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.0 ms: 1.03x faster                                                |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                 |
| nbody          | 105 ms                                                                | 143 ms: 1.37x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.76 ms: 1.23x faster                                                |
| regex_dna      | 254 ms                                                                | 220 ms: 1.16x faster                                                 |
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                 |
| regex_v8       | 28.3 ms                                                               | 26.2 ms: 1.08x faster                                                |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                 |
| tomli_loads          | 2.59 sec                                                              | 2.57 sec: 1.01x faster                                               |
| xml_etree_process    | 79.0 ms                                                               | 81.9 ms: 1.04x slower                                                |
| json_loads           | 30.7 us                                                               | 33.0 us: 1.08x slower                                                |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                |
| unpickle_pure_python | 260 us                                                                | 299 us: 1.15x slower                                                 |
| pickle_pure_python   | 365 us                                                                | 427 us: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                         |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.19x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 65.8 ms: 1.09x slower                                                |
| mako           | 12.9 ms                                                               | 15.2 ms: 1.18x slower                                                |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                         |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.66 sec: 2.06x faster                                               |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                 |
| async_tree_memoization     | 777 ms                                                                | 497 ms: 1.56x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.53x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 930 ms: 1.52x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 926 ms: 1.52x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 685 ms: 1.33x faster                                                 |
| deepcopy                   | 446 us                                                                | 337 us: 1.32x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 672 ms: 1.31x faster                                                 |
| deepcopy_memo              | 49.6 us                                                               | 37.8 us: 1.31x faster                                                |
| regex_effbot               | 4.64 ms                                                               | 3.76 ms: 1.23x faster                                                |
| generators                 | 43.5 ms                                                               | 35.5 ms: 1.23x faster                                                |
| regex_dna                  | 254 ms                                                                | 220 ms: 1.16x faster                                                 |
| deepcopy_reduce            | 4.10 us                                                               | 3.59 us: 1.14x faster                                                |
| dulwich_log                | 62.0 ms                                                               | 55.2 ms: 1.12x faster                                                |
| logging_format             | 8.34 us                                                               | 7.62 us: 1.10x faster                                                |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.09x faster                                                 |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                                |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                 |
| pylint                     | 355 ms                                                                | 327 ms: 1.08x faster                                                 |
| regex_v8                   | 28.3 ms                                                               | 26.2 ms: 1.08x faster                                                |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                |
| scimark_sor                | 150 ms                                                                | 145 ms: 1.04x faster                                                 |
| float                      | 92.1 ms                                                               | 89.0 ms: 1.03x faster                                                |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                 |
| raytrace                   | 353 ms                                                                | 343 ms: 1.03x faster                                                 |
| html5lib                   | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                                |
| sympy_sum                  | 154 ms                                                                | 152 ms: 1.02x faster                                                 |
| tomli_loads                | 2.59 sec                                                              | 2.57 sec: 1.01x faster                                               |
| sqlite_synth               | 3.77 us                                                               | 3.85 us: 1.02x slower                                                |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                 |
| logging_silent             | 127 ns                                                                | 130 ns: 1.03x slower                                                 |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.03x slower                                                |
| 2to3                       | 308 ms                                                                | 319 ms: 1.04x slower                                                 |
| xml_etree_process          | 79.0 ms                                                               | 81.9 ms: 1.04x slower                                                |
| thrift                     | 937 us                                                                | 975 us: 1.04x slower                                                 |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.8 ms: 1.04x slower                                                |
| python_startup_no_site     | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                |
| docutils                   | 2.98 sec                                                              | 3.17 sec: 1.06x slower                                               |
| pyflate                    | 559 ms                                                                | 596 ms: 1.07x slower                                                 |
| scimark_fft                | 418 ms                                                                | 447 ms: 1.07x slower                                                 |
| nqueens                    | 99.2 ms                                                               | 106 ms: 1.07x slower                                                 |
| json_loads                 | 30.7 us                                                               | 33.0 us: 1.08x slower                                                |
| genshi_xml                 | 60.6 ms                                                               | 65.8 ms: 1.09x slower                                                |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.09x slower                                                 |
| deltablue                  | 4.12 ms                                                               | 4.55 ms: 1.10x slower                                                |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                |
| sympy_expand               | 454 ms                                                                | 507 ms: 1.12x slower                                                 |
| meteor_contest             | 112 ms                                                                | 128 ms: 1.15x slower                                                 |
| pycparser                  | 1.26 sec                                                              | 1.44 sec: 1.15x slower                                               |
| unpickle_pure_python       | 260 us                                                                | 299 us: 1.15x slower                                                 |
| pickle_pure_python         | 365 us                                                                | 427 us: 1.17x slower                                                 |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                 |
| mako                       | 12.9 ms                                                               | 15.2 ms: 1.18x slower                                                |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.52 ms: 1.21x slower                                                |
| typing_runtime_protocols   | 181 us                                                                | 221 us: 1.23x slower                                                 |
| crypto_pyaes               | 86.6 ms                                                               | 108 ms: 1.25x slower                                                 |
| go                         | 157 ms                                                                | 198 ms: 1.26x slower                                                 |
| fannkuch                   | 443 ms                                                                | 567 ms: 1.28x slower                                                 |
| hexiom                     | 6.98 ms                                                               | 9.22 ms: 1.32x slower                                                |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                |
| nbody                      | 105 ms                                                                | 143 ms: 1.37x slower                                                 |
| pprint_pformat             | 1.88 sec                                                              | 2.84 sec: 1.51x slower                                               |
| pprint_safe_repr           | 916 ms                                                                | 1.39 sec: 1.52x slower                                               |
| gc_traversal               | 4.40 ms                                                               | 6.79 ms: 1.55x slower                                                |
| create_gc_cycles           | 1.92 ms                                                               | 3.79 ms: 1.98x slower                                                |
| telco                      | 8.51 ms                                                               | 166 ms: 19.55x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                         |

Benchmark hidden because not significant (13): chaos, richards_super, comprehensions, sympy_integrate, richards, django_template, async_generators, asyncio_websockets, genshi_text, xml_etree_generate, sympy_str, scimark_lu, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250707-3.15.0a0-aa2b0df-JIT/bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 51.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x