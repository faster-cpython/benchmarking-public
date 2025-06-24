# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.047x faster
- HPT reliability: 99.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 312 ms: 1.01x slower                                                |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                              |
| html5lib       | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 891 ms: 1.58x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 468 ms: 1.58x faster                                                |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.56x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 658 ms: 1.34x faster                                                |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.3 ms: 1.12x faster                                               |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.95 ms: 1.18x faster                                               |
| regex_dna      | 254 ms                                                                | 218 ms: 1.16x faster                                                |
| regex_compile  | 137 ms                                                                | 121 ms: 1.14x faster                                                |
| regex_v8       | 28.3 ms                                                               | 26.7 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                              |
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                |
| xml_etree_iterparse | 150 ms                                                                | 145 ms: 1.04x faster                                                |
| xml_etree_process   | 79.0 ms                                                               | 78.1 ms: 1.01x faster                                               |
| xml_etree_generate  | 112 ms                                                                | 111 ms: 1.01x faster                                                |
| pickle_pure_python  | 365 us                                                                | 388 us: 1.06x slower                                                |
| json_loads          | 30.7 us                                                               | 32.7 us: 1.06x slower                                               |
| json_dumps          | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                               |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                               |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 61.1 ms: 1.01x slower                                               |
| mako           | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.67 sec: 2.05x faster                                              |
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 891 ms: 1.58x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 468 ms: 1.58x faster                                                |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.56x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                |
| deepcopy_memo              | 49.6 us                                                               | 36.6 us: 1.36x faster                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 658 ms: 1.34x faster                                                |
| deepcopy                   | 446 us                                                                | 340 us: 1.31x faster                                                |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                               |
| regex_effbot               | 4.64 ms                                                               | 3.95 ms: 1.18x faster                                               |
| regex_dna                  | 254 ms                                                                | 218 ms: 1.16x faster                                                |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.15x faster                                               |
| comprehensions             | 25.4 us                                                               | 22.2 us: 1.14x faster                                               |
| dulwich_log                | 62.0 ms                                                               | 54.3 ms: 1.14x faster                                               |
| richards_super             | 58.5 ms                                                               | 51.4 ms: 1.14x faster                                               |
| regex_compile              | 137 ms                                                                | 121 ms: 1.14x faster                                                |
| richards                   | 50.9 ms                                                               | 45.1 ms: 1.13x faster                                               |
| float                      | 92.1 ms                                                               | 82.3 ms: 1.12x faster                                               |
| tomli_loads                | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                              |
| pylint                     | 355 ms                                                                | 323 ms: 1.10x faster                                                |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                               |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                                |
| regex_v8                   | 28.3 ms                                                               | 26.7 ms: 1.06x faster                                               |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                               |
| pyflate                    | 559 ms                                                                | 532 ms: 1.05x faster                                                |
| xml_etree_iterparse        | 150 ms                                                                | 145 ms: 1.04x faster                                                |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.0 ms: 1.04x faster                                               |
| html5lib                   | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                               |
| async_generators           | 491 ms                                                                | 476 ms: 1.03x faster                                                |
| logging_simple             | 7.63 us                                                               | 7.46 us: 1.02x faster                                               |
| logging_format             | 8.34 us                                                               | 8.16 us: 1.02x faster                                               |
| xml_etree_process          | 79.0 ms                                                               | 78.1 ms: 1.01x faster                                               |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                |
| nqueens                    | 99.2 ms                                                               | 100.0 ms: 1.01x slower                                              |
| genshi_xml                 | 60.6 ms                                                               | 61.1 ms: 1.01x slower                                               |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                |
| 2to3                       | 308 ms                                                                | 312 ms: 1.01x slower                                                |
| go                         | 157 ms                                                                | 159 ms: 1.01x slower                                                |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                               |
| scimark_lu                 | 146 ms                                                                | 150 ms: 1.03x slower                                                |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                               |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.03x slower                                                |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                              |
| json                       | 5.54 ms                                                               | 5.80 ms: 1.05x slower                                               |
| pickle_pure_python         | 365 us                                                                | 388 us: 1.06x slower                                                |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.06x slower                                               |
| hexiom                     | 6.98 ms                                                               | 7.52 ms: 1.08x slower                                               |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                                |
| sympy_expand               | 454 ms                                                                | 491 ms: 1.08x slower                                                |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                               |
| crypto_pyaes               | 86.6 ms                                                               | 93.9 ms: 1.08x slower                                               |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.10x slower                                              |
| telco                      | 8.51 ms                                                               | 9.38 ms: 1.10x slower                                               |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.01 ms: 1.13x slower                                               |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.18x slower                                                |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                               |
| pprint_safe_repr           | 916 ms                                                                | 1.24 sec: 1.35x slower                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.58 sec: 1.37x slower                                              |
| gc_traversal               | 4.40 ms                                                               | 6.95 ms: 1.58x slower                                               |
| create_gc_cycles           | 1.92 ms                                                               | 3.87 ms: 2.02x slower                                               |
| logging_silent             | 127 ns                                                                | 618 ns: 4.88x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                        |

Benchmark hidden because not significant (13): django_template, sympy_integrate, genshi_text, chaos, scimark_sor, unpickle_pure_python, spectral_norm, sqlite_synth, thrift, sympy_sum, sympy_str, coroutines, scimark_fft
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.27% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x