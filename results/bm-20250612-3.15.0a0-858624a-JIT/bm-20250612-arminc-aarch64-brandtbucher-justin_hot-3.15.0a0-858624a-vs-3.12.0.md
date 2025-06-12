# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: 858624a
- commit date: 2025-06-12
- overall geometric mean: 1.087x slower
- HPT reliability: 54.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 320 ms: 1.04x slower                                                |
| docutils       | 2.98 sec                                                              | 3.15 sec: 1.05x slower                                              |
| html5lib       | 65.1 ms                                                               | 62.5 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 481 ms: 1.61x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.53x faster                                                |
| async_tree_none            | 624 ms                                                                | 406 ms: 1.53x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 929 ms: 1.52x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 945 ms: 1.49x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 393 ms: 1.47x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 672 ms: 1.36x faster                                                |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 670 ms: 1.32x faster                                                |
| Geometric mean             | (ref)                                                                 | 1.48x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.6 ms: 1.03x faster                                               |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                |
| nbody          | 105 ms                                                                | 145 ms: 1.39x slower                                                |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.85 ms: 1.21x faster                                               |
| regex_dna      | 254 ms                                                                | 224 ms: 1.13x faster                                                |
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 150 ms                                                                | 143 ms: 1.05x faster                                                |
| tomli_loads          | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                              |
| xml_etree_generate   | 112 ms                                                                | 116 ms: 1.03x slower                                                |
| xml_etree_process    | 79.0 ms                                                               | 83.0 ms: 1.05x slower                                               |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                               |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                               |
| unpickle_pure_python | 260 us                                                                | 289 us: 1.11x slower                                                |
| pickle_pure_python   | 365 us                                                                | 407 us: 1.12x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                               |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.0 ms: 1.04x slower                                               |
| mako           | 12.9 ms                                                               | 15.2 ms: 1.18x slower                                               |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                        |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.71 sec: 1.99x faster                                              |
| async_tree_memoization     | 777 ms                                                                | 481 ms: 1.61x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.53x faster                                                |
| async_tree_none            | 624 ms                                                                | 406 ms: 1.53x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 929 ms: 1.52x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 945 ms: 1.49x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 393 ms: 1.47x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 672 ms: 1.36x faster                                                |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                |
| deepcopy_memo              | 49.6 us                                                               | 37.3 us: 1.33x faster                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 670 ms: 1.32x faster                                                |
| generators                 | 43.5 ms                                                               | 35.7 ms: 1.22x faster                                               |
| regex_effbot               | 4.64 ms                                                               | 3.85 ms: 1.21x faster                                               |
| regex_dna                  | 254 ms                                                                | 224 ms: 1.13x faster                                                |
| deepcopy_reduce            | 4.10 us                                                               | 3.67 us: 1.12x faster                                               |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                |
| pylint                     | 355 ms                                                                | 327 ms: 1.08x faster                                                |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                               |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                |
| dulwich_log                | 62.0 ms                                                               | 59.1 ms: 1.05x faster                                               |
| html5lib                   | 65.1 ms                                                               | 62.5 ms: 1.04x faster                                               |
| richards_super             | 58.5 ms                                                               | 56.2 ms: 1.04x faster                                               |
| sympy_sum                  | 154 ms                                                                | 150 ms: 1.03x faster                                                |
| raytrace                   | 353 ms                                                                | 343 ms: 1.03x faster                                                |
| float                      | 92.1 ms                                                               | 89.6 ms: 1.03x faster                                               |
| scimark_sor                | 150 ms                                                                | 146 ms: 1.03x faster                                                |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                              |
| async_generators           | 491 ms                                                                | 485 ms: 1.01x faster                                                |
| sympy_str                  | 280 ms                                                                | 281 ms: 1.00x slower                                                |
| logging_format             | 8.34 us                                                               | 8.41 us: 1.01x slower                                               |
| coroutines                 | 29.0 ms                                                               | 29.3 ms: 1.01x slower                                               |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                |
| richards                   | 50.9 ms                                                               | 51.7 ms: 1.01x slower                                               |
| scimark_monte_carlo        | 85.1 ms                                                               | 86.5 ms: 1.02x slower                                               |
| json                       | 5.54 ms                                                               | 5.64 ms: 1.02x slower                                               |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                |
| xml_etree_generate         | 112 ms                                                                | 116 ms: 1.03x slower                                                |
| python_startup_no_site     | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                               |
| 2to3                       | 308 ms                                                                | 320 ms: 1.04x slower                                                |
| genshi_xml                 | 60.6 ms                                                               | 63.0 ms: 1.04x slower                                               |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.05x slower                                                |
| pyflate                    | 559 ms                                                                | 587 ms: 1.05x slower                                                |
| xml_etree_process          | 79.0 ms                                                               | 83.0 ms: 1.05x slower                                               |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                               |
| docutils                   | 2.98 sec                                                              | 3.15 sec: 1.05x slower                                              |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.08x slower                                                |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                               |
| scimark_fft                | 418 ms                                                                | 464 ms: 1.11x slower                                                |
| unpickle_pure_python       | 260 us                                                                | 289 us: 1.11x slower                                                |
| deltablue                  | 4.12 ms                                                               | 4.59 ms: 1.12x slower                                               |
| pickle_pure_python         | 365 us                                                                | 407 us: 1.12x slower                                                |
| sympy_expand               | 454 ms                                                                | 507 ms: 1.12x slower                                                |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.08 ms: 1.14x slower                                               |
| pycparser                  | 1.26 sec                                                              | 1.44 sec: 1.15x slower                                              |
| meteor_contest             | 112 ms                                                                | 129 ms: 1.15x slower                                                |
| spectral_norm              | 131 ms                                                                | 152 ms: 1.16x slower                                                |
| mako                       | 12.9 ms                                                               | 15.2 ms: 1.18x slower                                               |
| crypto_pyaes               | 86.6 ms                                                               | 103 ms: 1.18x slower                                                |
| typing_runtime_protocols   | 181 us                                                                | 214 us: 1.18x slower                                                |
| telco                      | 8.51 ms                                                               | 10.2 ms: 1.20x slower                                               |
| go                         | 157 ms                                                                | 195 ms: 1.24x slower                                                |
| hexiom                     | 6.98 ms                                                               | 8.98 ms: 1.29x slower                                               |
| fannkuch                   | 443 ms                                                                | 582 ms: 1.31x slower                                                |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                               |
| nbody                      | 105 ms                                                                | 145 ms: 1.39x slower                                                |
| gc_traversal               | 4.40 ms                                                               | 6.75 ms: 1.54x slower                                               |
| pprint_safe_repr           | 916 ms                                                                | 1.55 sec: 1.70x slower                                              |
| pprint_pformat             | 1.88 sec                                                              | 3.30 sec: 1.75x slower                                              |
| create_gc_cycles           | 1.92 ms                                                               | 3.74 ms: 1.95x slower                                               |
| logging_silent             | 127 ns                                                                | 614 ns: 4.84x slower                                                |
| coverage                   | 87.3 ms                                                               | 578 ms: 6.62x slower                                                |
| thrift                     | 937 us                                                                | 193 ms: 205.78x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                        |

Benchmark hidden because not significant (8): django_template, comprehensions, regex_v8, sympy_integrate, chaos, genshi_text, logging_simple, sqlite_synth
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250612-3.15.0a0-858624a-JIT/bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.087x slower

# HPT report

- Reliability score: 54.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x