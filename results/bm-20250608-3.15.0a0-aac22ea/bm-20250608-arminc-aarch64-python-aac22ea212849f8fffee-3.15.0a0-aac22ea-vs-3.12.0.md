# Results vs. 3.12.0

- fork: python
- ref: aac22ea212849f8fffee
- machine: linux-aarch64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.028x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                                  |
| html5lib       | 65.1 ms                                                               | 61.1 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 911 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 661 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                                    |
| regex_dna      | 254 ms                                                                | 232 ms: 1.09x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.6 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                  |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 80.0 ms: 1.01x slower                                                   |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 392 us: 1.07x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.3 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.67 sec: 2.04x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 468 ms: 1.66x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 911 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 661 ms: 1.38x faster                                                    |
| deepcopy                   | 446 us                                                                | 325 us: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                   |
| go                         | 157 ms                                                                | 127 ms: 1.24x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 52.0 ms: 1.19x faster                                                   |
| generators                 | 43.5 ms                                                               | 37.6 ms: 1.16x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.15x faster                                                   |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                                    |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                    |
| regex_dna                  | 254 ms                                                                | 232 ms: 1.09x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                   |
| async_generators           | 491 ms                                                                | 451 ms: 1.09x faster                                                    |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.2 ms: 1.07x faster                                                   |
| float                      | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 61.1 ms: 1.07x faster                                                   |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                  |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.1 ms: 1.05x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.2 ms: 1.05x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 27.6 ms: 1.03x faster                                                   |
| pyflate                    | 559 ms                                                                | 545 ms: 1.03x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                                  |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                    |
| richards_super             | 58.5 ms                                                               | 58.2 ms: 1.01x faster                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| richards                   | 50.9 ms                                                               | 51.6 ms: 1.01x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.0 ms: 1.01x slower                                                   |
| logging_format             | 8.34 us                                                               | 8.46 us: 1.01x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.28 sec: 1.02x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 29.5 ms: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                   |
| sympy_expand               | 454 ms                                                                | 468 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                   |
| scimark_fft                | 418 ms                                                                | 434 ms: 1.04x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.93 us: 1.04x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 471 ms: 1.06x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.03 sec: 1.08x slower                                                  |
| telco                      | 8.51 ms                                                               | 9.27 ms: 1.09x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 999 ms: 1.09x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.91 ms: 1.12x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                   |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.3 ms: 1.34x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.82 ms: 1.55x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.72 ms: 1.94x slower                                                   |
| logging_silent             | 127 ns                                                                | 618 ns: 4.87x slower                                                    |
| coverage                   | 87.3 ms                                                               | 569 ms: 6.51x slower                                                    |
| thrift                     | 937 us                                                                | 197 ms: 209.88x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (12): crypto_pyaes, scimark_sor, django_template, xml_etree_generate, nqueens, hexiom, spectral_norm, unpickle_pure_python, genshi_text, logging_simple, genshi_xml, scimark_lu
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x