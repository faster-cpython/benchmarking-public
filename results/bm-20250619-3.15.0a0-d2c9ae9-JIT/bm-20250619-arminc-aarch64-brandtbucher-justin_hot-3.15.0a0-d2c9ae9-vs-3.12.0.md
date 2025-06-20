# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.005x faster
- HPT reliability: 65.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 317 ms: 1.03x slower                                                |
| docutils       | 2.98 sec                                                              | 3.15 sec: 1.06x slower                                              |
| html5lib       | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 473 ms: 1.64x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 900 ms: 1.57x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 473 ms: 1.56x faster                                                |
| async_tree_none            | 624 ms                                                                | 403 ms: 1.55x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 665 ms: 1.33x faster                                                |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.6 ms: 1.04x faster                                               |
| pidigits       | 233 ms                                                                | 236 ms: 1.02x slower                                                |
| nbody          | 105 ms                                                                | 147 ms: 1.40x slower                                                |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                               |
| regex_dna      | 254 ms                                                                | 223 ms: 1.14x faster                                                |
| regex_compile  | 137 ms                                                                | 130 ms: 1.06x faster                                                |
| regex_v8       | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.08x faster                                                |
| xml_etree_iterparse  | 150 ms                                                                | 144 ms: 1.05x faster                                                |
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                              |
| xml_etree_process    | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                               |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                               |
| pickle_pure_python   | 365 us                                                                | 404 us: 1.11x slower                                                |
| json_dumps           | 12.3 ms                                                               | 13.8 ms: 1.12x slower                                               |
| unpickle_pure_python | 260 us                                                                | 295 us: 1.13x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                               |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                               |
| genshi_xml      | 60.6 ms                                                               | 64.2 ms: 1.06x slower                                               |
| mako            | 12.9 ms                                                               | 15.1 ms: 1.17x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.72 sec: 1.98x faster                                              |
| async_tree_memoization     | 777 ms                                                                | 473 ms: 1.64x faster                                                |
| async_tree_io              | 1.41 sec                                                              | 900 ms: 1.57x faster                                                |
| async_tree_memoization_tg  | 740 ms                                                                | 473 ms: 1.56x faster                                                |
| async_tree_none            | 624 ms                                                                | 403 ms: 1.55x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                |
| deepcopy_memo              | 49.6 us                                                               | 37.2 us: 1.34x faster                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 665 ms: 1.33x faster                                                |
| generators                 | 43.5 ms                                                               | 36.4 ms: 1.19x faster                                               |
| regex_effbot               | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                               |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                               |
| regex_dna                  | 254 ms                                                                | 223 ms: 1.14x faster                                                |
| dulwich_log                | 62.0 ms                                                               | 56.1 ms: 1.11x faster                                               |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                |
| pylint                     | 355 ms                                                                | 332 ms: 1.07x faster                                                |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                               |
| regex_compile              | 137 ms                                                                | 130 ms: 1.06x faster                                                |
| regex_v8                   | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                               |
| richards_super             | 58.5 ms                                                               | 55.7 ms: 1.05x faster                                               |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                |
| django_template            | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                               |
| float                      | 92.1 ms                                                               | 88.6 ms: 1.04x faster                                               |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.04x faster                                                |
| raytrace                   | 353 ms                                                                | 343 ms: 1.03x faster                                                |
| html5lib                   | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                               |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                               |
| async_generators           | 491 ms                                                                | 479 ms: 1.03x faster                                                |
| logging_simple             | 7.63 us                                                               | 7.49 us: 1.02x faster                                               |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                              |
| logging_format             | 8.34 us                                                               | 8.29 us: 1.01x faster                                               |
| thrift                     | 937 us                                                                | 940 us: 1.00x slower                                                |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                |
| pidigits                   | 233 ms                                                                | 236 ms: 1.02x slower                                                |
| xml_etree_process          | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                               |
| python_startup_no_site     | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                               |
| 2to3                       | 308 ms                                                                | 317 ms: 1.03x slower                                                |
| json                       | 5.54 ms                                                               | 5.76 ms: 1.04x slower                                               |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.04x slower                                                |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                               |
| docutils                   | 2.98 sec                                                              | 3.15 sec: 1.06x slower                                              |
| genshi_xml                 | 60.6 ms                                                               | 64.2 ms: 1.06x slower                                               |
| nqueens                    | 99.2 ms                                                               | 106 ms: 1.07x slower                                                |
| pyflate                    | 559 ms                                                                | 606 ms: 1.08x slower                                                |
| sympy_expand               | 454 ms                                                                | 493 ms: 1.09x slower                                                |
| pickle_pure_python         | 365 us                                                                | 404 us: 1.11x slower                                                |
| deltablue                  | 4.12 ms                                                               | 4.57 ms: 1.11x slower                                               |
| scimark_fft                | 418 ms                                                                | 466 ms: 1.11x slower                                                |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.12x slower                                               |
| unpickle_pure_python       | 260 us                                                                | 295 us: 1.13x slower                                                |
| meteor_contest             | 112 ms                                                                | 127 ms: 1.14x slower                                                |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                |
| pycparser                  | 1.26 sec                                                              | 1.46 sec: 1.16x slower                                              |
| spectral_norm              | 131 ms                                                                | 152 ms: 1.16x slower                                                |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.17x slower                                                |
| mako                       | 12.9 ms                                                               | 15.1 ms: 1.17x slower                                               |
| crypto_pyaes               | 86.6 ms                                                               | 102 ms: 1.18x slower                                                |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                               |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.46 ms: 1.20x slower                                               |
| go                         | 157 ms                                                                | 193 ms: 1.23x slower                                                |
| fannkuch                   | 443 ms                                                                | 557 ms: 1.26x slower                                                |
| hexiom                     | 6.98 ms                                                               | 8.91 ms: 1.28x slower                                               |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                               |
| nbody                      | 105 ms                                                                | 147 ms: 1.40x slower                                                |
| gc_traversal               | 4.40 ms                                                               | 7.06 ms: 1.61x slower                                               |
| pprint_safe_repr           | 916 ms                                                                | 1.54 sec: 1.68x slower                                              |
| pprint_pformat             | 1.88 sec                                                              | 3.25 sec: 1.73x slower                                              |
| create_gc_cycles           | 1.92 ms                                                               | 3.78 ms: 1.97x slower                                               |
| logging_silent             | 127 ns                                                                | 609 ns: 4.80x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                        |

Benchmark hidden because not significant (10): chaos, scimark_sor, genshi_text, comprehensions, sqlite_synth, xml_etree_generate, sympy_str, scimark_monte_carlo, richards, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 65.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x