# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.047x faster
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                              |
| html5lib       | 65.1 ms                                                               | 63.3 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 477 ms: 1.63x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 895 ms: 1.58x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                |
| async_tree_none            | 624 ms                                                                | 402 ms: 1.55x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                                |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.1 ms: 1.12x faster                                               |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                |
| nbody          | 105 ms                                                                | 119 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.90 ms: 1.19x faster                                               |
| regex_dna      | 254 ms                                                                | 220 ms: 1.15x faster                                                |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                |
| regex_v8       | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.38 sec: 1.09x faster                                              |
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.09x faster                                                |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                |
| xml_etree_generate  | 112 ms                                                                | 108 ms: 1.04x faster                                                |
| xml_etree_process   | 79.0 ms                                                               | 78.4 ms: 1.01x faster                                               |
| pickle_pure_python  | 365 us                                                                | 393 us: 1.08x slower                                                |
| json_loads          | 30.7 us                                                               | 33.2 us: 1.08x slower                                               |
| json_dumps          | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                               |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.58 ms: 1.03x slower                                               |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                               |
| mako           | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                               |
| genshi_xml     | 60.6 ms                                                               | 63.2 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                              |
| async_tree_memoization     | 777 ms                                                                | 477 ms: 1.63x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 895 ms: 1.58x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                |
| async_tree_none            | 624 ms                                                                | 402 ms: 1.55x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                |
| deepcopy_memo              | 49.6 us                                                               | 36.6 us: 1.36x faster                                               |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                                |
| generators                 | 43.5 ms                                                               | 36.3 ms: 1.20x faster                                               |
| regex_effbot               | 4.64 ms                                                               | 3.90 ms: 1.19x faster                                               |
| dulwich_log                | 62.0 ms                                                               | 53.3 ms: 1.16x faster                                               |
| regex_dna                  | 254 ms                                                                | 220 ms: 1.15x faster                                                |
| deepcopy_reduce            | 4.10 us                                                               | 3.60 us: 1.14x faster                                               |
| comprehensions             | 25.4 us                                                               | 22.6 us: 1.12x faster                                               |
| float                      | 92.1 ms                                                               | 82.1 ms: 1.12x faster                                               |
| richards                   | 50.9 ms                                                               | 45.6 ms: 1.12x faster                                               |
| richards_super             | 58.5 ms                                                               | 52.5 ms: 1.11x faster                                               |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                |
| pylint                     | 355 ms                                                                | 320 ms: 1.11x faster                                                |
| tomli_loads                | 2.59 sec                                                              | 2.38 sec: 1.09x faster                                              |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.09x faster                                                |
| raytrace                   | 353 ms                                                                | 331 ms: 1.07x faster                                                |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                |
| pyflate                    | 559 ms                                                                | 529 ms: 1.06x faster                                                |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.06x faster                                               |
| regex_v8                   | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                               |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                               |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.0 ms: 1.05x faster                                               |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                |
| xml_etree_generate         | 112 ms                                                                | 108 ms: 1.04x faster                                                |
| html5lib                   | 65.1 ms                                                               | 63.3 ms: 1.03x faster                                               |
| genshi_text                | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                               |
| async_generators           | 491 ms                                                                | 480 ms: 1.02x faster                                                |
| sqlite_synth               | 3.77 us                                                               | 3.73 us: 1.01x faster                                               |
| xml_etree_process          | 79.0 ms                                                               | 78.4 ms: 1.01x faster                                               |
| thrift                     | 937 us                                                                | 943 us: 1.01x slower                                                |
| nqueens                    | 99.2 ms                                                               | 100 ms: 1.01x slower                                                |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                               |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.02x slower                                                |
| python_startup_no_site     | 8.37 ms                                                               | 8.58 ms: 1.03x slower                                               |
| json                       | 5.54 ms                                                               | 5.68 ms: 1.03x slower                                               |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                |
| genshi_xml                 | 60.6 ms                                                               | 63.2 ms: 1.04x slower                                               |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.05x slower                                              |
| fannkuch                   | 443 ms                                                                | 474 ms: 1.07x slower                                                |
| hexiom                     | 6.98 ms                                                               | 7.48 ms: 1.07x slower                                               |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                               |
| sympy_expand               | 454 ms                                                                | 492 ms: 1.08x slower                                                |
| crypto_pyaes               | 86.6 ms                                                               | 94.0 ms: 1.08x slower                                               |
| pycparser                  | 1.26 sec                                                              | 1.40 sec: 1.11x slower                                              |
| telco                      | 8.51 ms                                                               | 9.52 ms: 1.12x slower                                               |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                               |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.02 ms: 1.13x slower                                               |
| nbody                      | 105 ms                                                                | 119 ms: 1.13x slower                                                |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.18x slower                                                |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                               |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.58 sec: 1.37x slower                                              |
| gc_traversal               | 4.40 ms                                                               | 6.78 ms: 1.54x slower                                               |
| create_gc_cycles           | 1.92 ms                                                               | 3.77 ms: 1.97x slower                                               |
| logging_silent             | 127 ns                                                                | 611 ns: 4.82x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                        |

Benchmark hidden because not significant (14): chaos, unpickle_pure_python, scimark_sor, sympy_integrate, scimark_fft, logging_format, django_template, 2to3, spectral_norm, asyncio_websockets, logging_simple, sympy_str, go, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250620-3.15.0a0-4cfabf5-JIT/bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.19% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x