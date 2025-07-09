# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_targets
- machine: linux-aarch64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.017x faster
- HPT reliability: 99.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 311 ms: 1.01x slower                                                 |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                               |
| html5lib       | 65.1 ms                                                               | 62.7 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 480 ms: 1.62x faster                                                 |
| async_tree_none            | 624 ms                                                                | 388 ms: 1.61x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 906 ms: 1.56x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 388 ms: 1.49x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 674 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.34x faster                                                 |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.3 ms: 1.12x faster                                                |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                 |
| nbody          | 105 ms                                                                | 128 ms: 1.22x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.77 ms: 1.23x faster                                                |
| regex_dna      | 254 ms                                                                | 217 ms: 1.17x faster                                                 |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                 |
| regex_v8       | 28.3 ms                                                               | 26.7 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.34 sec: 1.11x faster                                               |
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                                 |
| xml_etree_generate   | 112 ms                                                                | 108 ms: 1.04x faster                                                 |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                 |
| xml_etree_process    | 79.0 ms                                                               | 77.3 ms: 1.02x faster                                                |
| json_loads           | 30.7 us                                                               | 32.8 us: 1.07x slower                                                |
| pickle_pure_python   | 365 us                                                                | 400 us: 1.10x slower                                                 |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.0 ms: 1.00x slower                                                |
| genshi_xml     | 60.6 ms                                                               | 63.3 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.66 sec: 2.05x faster                                               |
| async_tree_memoization     | 777 ms                                                                | 480 ms: 1.62x faster                                                 |
| async_tree_none            | 624 ms                                                                | 388 ms: 1.61x faster                                                 |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 906 ms: 1.56x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                                 |
| async_tree_none_tg         | 577 ms                                                                | 388 ms: 1.49x faster                                                 |
| deepcopy                   | 446 us                                                                | 326 us: 1.37x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 674 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.34x faster                                                 |
| deepcopy_memo              | 49.6 us                                                               | 38.4 us: 1.29x faster                                                |
| regex_effbot               | 4.64 ms                                                               | 3.77 ms: 1.23x faster                                                |
| generators                 | 43.5 ms                                                               | 35.8 ms: 1.21x faster                                                |
| comprehensions             | 25.4 us                                                               | 21.6 us: 1.17x faster                                                |
| regex_dna                  | 254 ms                                                                | 217 ms: 1.17x faster                                                 |
| richards                   | 50.9 ms                                                               | 44.1 ms: 1.15x faster                                                |
| dulwich_log                | 62.0 ms                                                               | 54.9 ms: 1.13x faster                                                |
| richards_super             | 58.5 ms                                                               | 52.0 ms: 1.12x faster                                                |
| float                      | 92.1 ms                                                               | 82.3 ms: 1.12x faster                                                |
| tomli_loads                | 2.59 sec                                                              | 2.34 sec: 1.11x faster                                               |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                 |
| logging_format             | 8.34 us                                                               | 7.60 us: 1.10x faster                                                |
| pylint                     | 355 ms                                                                | 323 ms: 1.10x faster                                                 |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                 |
| deepcopy_reduce            | 4.10 us                                                               | 3.75 us: 1.09x faster                                                |
| logging_simple             | 7.63 us                                                               | 7.00 us: 1.09x faster                                                |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                 |
| raytrace                   | 353 ms                                                                | 328 ms: 1.08x faster                                                 |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                                |
| regex_v8                   | 28.3 ms                                                               | 26.7 ms: 1.06x faster                                                |
| pyflate                    | 559 ms                                                                | 526 ms: 1.06x faster                                                 |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                                |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.3 ms: 1.05x faster                                                |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                                |
| xml_etree_generate         | 112 ms                                                                | 108 ms: 1.04x faster                                                 |
| scimark_sor                | 150 ms                                                                | 144 ms: 1.04x faster                                                 |
| html5lib                   | 65.1 ms                                                               | 62.7 ms: 1.04x faster                                                |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                                 |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                                |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                 |
| go                         | 157 ms                                                                | 154 ms: 1.02x faster                                                 |
| xml_etree_process          | 79.0 ms                                                               | 77.3 ms: 1.02x faster                                                |
| sqlite_synth               | 3.77 us                                                               | 3.70 us: 1.02x faster                                                |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.00x slower                                                |
| coroutines                 | 29.0 ms                                                               | 29.3 ms: 1.01x slower                                                |
| 2to3                       | 308 ms                                                                | 311 ms: 1.01x slower                                                 |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                 |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                 |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                 |
| python_startup_no_site     | 8.37 ms                                                               | 8.61 ms: 1.03x slower                                                |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                               |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                 |
| genshi_xml                 | 60.6 ms                                                               | 63.3 ms: 1.05x slower                                                |
| json                       | 5.54 ms                                                               | 5.89 ms: 1.06x slower                                                |
| hexiom                     | 6.98 ms                                                               | 7.46 ms: 1.07x slower                                                |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                               |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                |
| fannkuch                   | 443 ms                                                                | 476 ms: 1.07x slower                                                 |
| sympy_expand               | 454 ms                                                                | 491 ms: 1.08x slower                                                 |
| crypto_pyaes               | 86.6 ms                                                               | 94.1 ms: 1.09x slower                                                |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.10x slower                                                 |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.06 ms: 1.14x slower                                                |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                 |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                 |
| pprint_pformat             | 1.88 sec                                                              | 2.29 sec: 1.22x slower                                               |
| nbody                      | 105 ms                                                                | 128 ms: 1.22x slower                                                 |
| pprint_safe_repr           | 916 ms                                                                | 1.15 sec: 1.26x slower                                               |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                |
| gc_traversal               | 4.40 ms                                                               | 6.91 ms: 1.57x slower                                                |
| create_gc_cycles           | 1.92 ms                                                               | 3.93 ms: 2.05x slower                                                |
| telco                      | 8.51 ms                                                               | 167 ms: 19.66x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (8): scimark_fft, sympy_str, async_generators, genshi_text, django_template, scimark_lu, meteor_contest, thrift
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 99.55% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x