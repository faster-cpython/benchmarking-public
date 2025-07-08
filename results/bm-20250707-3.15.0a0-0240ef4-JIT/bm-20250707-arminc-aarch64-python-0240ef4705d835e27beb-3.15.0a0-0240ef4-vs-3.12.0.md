# Results vs. 3.12.0

- fork: python
- ref: 0240ef4705d835e27beb
- machine: linux-aarch64
- commit hash: 0240ef4
- commit date: 2025-07-07
- overall geometric mean: 1.017x faster
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 310 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 476 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 905 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 902 ms: 1.56x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 385 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 667 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.4 ms: 1.12x faster                                                   |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                    |
| nbody          | 105 ms                                                                | 127 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.75 ms: 1.24x faster                                                   |
| regex_dna      | 254 ms                                                                | 218 ms: 1.17x faster                                                    |
| regex_compile  | 137 ms                                                                | 123 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.6 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                  |
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 250 us: 1.04x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 77.9 ms: 1.01x faster                                                   |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.07x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 400 us: 1.10x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.7 ms: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| genshi_xml     | 60.6 ms                                                               | 63.2 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.69 sec: 2.02x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 476 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 905 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 902 ms: 1.56x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 385 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 667 ms: 1.37x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 36.7 us: 1.35x faster                                                   |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 655 ms: 1.35x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.75 ms: 1.24x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.7 ms: 1.22x faster                                                   |
| regex_dna                  | 254 ms                                                                | 218 ms: 1.17x faster                                                    |
| richards_super             | 58.5 ms                                                               | 50.4 ms: 1.16x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.0 us: 1.16x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.60 us: 1.14x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 54.5 ms: 1.14x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                  |
| regex_compile              | 137 ms                                                                | 123 ms: 1.12x faster                                                    |
| float                      | 92.1 ms                                                               | 82.4 ms: 1.12x faster                                                   |
| richards                   | 50.9 ms                                                               | 45.6 ms: 1.12x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.91 us: 1.11x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.3 ms: 1.10x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| spectral_norm              | 131 ms                                                                | 120 ms: 1.08x faster                                                    |
| pylint                     | 355 ms                                                                | 329 ms: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.79 us: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                                   |
| raytrace                   | 353 ms                                                                | 331 ms: 1.07x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.6 ms: 1.07x faster                                                   |
| pyflate                    | 559 ms                                                                | 525 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.7 ms: 1.05x faster                                                   |
| scimark_sor                | 150 ms                                                                | 142 ms: 1.05x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 250 us: 1.04x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| scimark_fft                | 418 ms                                                                | 409 ms: 1.02x faster                                                    |
| async_generators           | 491 ms                                                                | 481 ms: 1.02x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 77.9 ms: 1.01x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.74 us: 1.01x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 147 ms: 1.01x slower                                                    |
| 2to3                       | 308 ms                                                                | 310 ms: 1.01x slower                                                    |
| logging_silent             | 127 ns                                                                | 128 ns: 1.01x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.76 ms: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 63.2 ms: 1.04x slower                                                   |
| thrift                     | 937 us                                                                | 978 us: 1.04x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                                   |
| fannkuch                   | 443 ms                                                                | 473 ms: 1.07x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 93.3 ms: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.08x slower                                                  |
| sympy_expand               | 454 ms                                                                | 492 ms: 1.09x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.10x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.70 ms: 1.10x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.11x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 204 us: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.15 ms: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                    |
| nbody                      | 105 ms                                                                | 127 ms: 1.21x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.34 sec: 1.25x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.15 sec: 1.25x slower                                                  |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.86 ms: 1.56x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.80 ms: 1.98x slower                                                   |
| telco                      | 8.51 ms                                                               | 168 ms: 19.72x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (11): chaos, html5lib, sympy_str, genshi_text, django_template, go, meteor_contest, xml_etree_generate, asyncio_websockets, nqueens, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 99.60% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x