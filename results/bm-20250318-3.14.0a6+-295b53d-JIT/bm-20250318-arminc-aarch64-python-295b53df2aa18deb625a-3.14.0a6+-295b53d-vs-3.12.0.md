# Results vs. 3.12.0

- fork: python
- ref: 295b53df2aa18deb625a
- machine: linux-aarch64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.005x faster
- HPT reliability: 50.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 311 ms: 1.01x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.23 sec: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 483 ms: 1.61x faster                                                     |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 484 ms: 1.53x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 923 ms: 1.52x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 674 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.34x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.6 ms: 1.06x faster                                                    |
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| nbody          | 105 ms                                                                | 129 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 173 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                   |
| xml_etree_generate   | 112 ms                                                                | 109 ms: 1.03x faster                                                     |
| unpickle_pure_python | 260 us                                                                | 286 us: 1.10x slower                                                     |
| json_loads           | 30.7 us                                                               | 34.0 us: 1.11x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 408 us: 1.12x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.4 ms: 1.05x slower                                                    |
| mako           | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 483 ms: 1.61x faster                                                     |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 484 ms: 1.53x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 923 ms: 1.52x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 674 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.34x faster                                                     |
| deepcopy                   | 446 us                                                                | 339 us: 1.32x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 38.9 us: 1.28x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.57 us: 1.15x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 173 ms: 1.13x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 56.4 ms: 1.10x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.15 us: 1.07x faster                                                    |
| pylint                     | 355 ms                                                                | 332 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| float                      | 92.1 ms                                                               | 86.6 ms: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.88 us: 1.06x faster                                                    |
| raytrace                   | 353 ms                                                                | 338 ms: 1.05x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 152 ms: 1.04x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.03x faster                                                     |
| richards_super             | 58.5 ms                                                               | 56.8 ms: 1.03x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.03x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.3 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                   |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                     |
| regex_v8                   | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                                    |
| thrift                     | 937 us                                                                | 929 us: 1.01x faster                                                     |
| 2to3                       | 308 ms                                                                | 311 ms: 1.01x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.17 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                     |
| pyflate                    | 559 ms                                                                | 575 ms: 1.03x slower                                                     |
| scimark_fft                | 418 ms                                                                | 431 ms: 1.03x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                    |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                     |
| richards                   | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 63.4 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.3 ms: 1.05x slower                                                    |
| spectral_norm              | 131 ms                                                                | 138 ms: 1.05x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 153 ms: 1.05x slower                                                     |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.07x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.23 sec: 1.08x slower                                                   |
| meteor_contest             | 112 ms                                                                | 122 ms: 1.09x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 286 us: 1.10x slower                                                     |
| json_loads                 | 30.7 us                                                               | 34.0 us: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.5 ms: 1.12x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 408 us: 1.12x slower                                                     |
| sympy_expand               | 454 ms                                                                | 509 ms: 1.12x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.42 sec: 1.13x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| fannkuch                   | 443 ms                                                                | 515 ms: 1.16x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.20 ms: 1.16x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.17x slower                                                     |
| go                         | 157 ms                                                                | 185 ms: 1.18x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 102 ms: 1.18x slower                                                     |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| nbody                      | 105 ms                                                                | 129 ms: 1.24x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 8.63 ms: 1.24x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.59 sec: 1.37x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.77 ms: 1.54x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.77 ms: 1.96x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.88 sec: 266.68x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (12): async_generators, django_template, sympy_str, comprehensions, html5lib, genshi_text, xml_etree_process, chaos, sympy_integrate, coroutines, scimark_sor, sqlite_synth
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 50.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x