# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.058x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                            |
| html5lib       | 65.1 ms                                                               | 61.9 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 463 ms: 1.68x faster                                                              |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                             |
| pidigits       | 233 ms                                                                | 236 ms: 1.02x slower                                                              |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                             |
| regex_dna      | 254 ms                                                                | 224 ms: 1.13x faster                                                              |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| regex_v8       | 28.3 ms                                                               | 26.8 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.08x faster                                                              |
| xml_etree_iterparse  | 150 ms                                                                | 142 ms: 1.06x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.52 sec: 1.03x faster                                                            |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| xml_etree_process    | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                                             |
| unpickle_pure_python | 260 us                                                                | 270 us: 1.04x slower                                                              |
| json_loads           | 30.7 us                                                               | 32.8 us: 1.07x slower                                                             |
| pickle_pure_python   | 365 us                                                                | 392 us: 1.07x slower                                                              |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.66 ms: 1.03x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 61.1 ms: 1.01x slower                                                             |
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.67 sec: 2.05x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 463 ms: 1.68x faster                                                              |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 658 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 659 ms: 1.34x faster                                                              |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 38.3 us: 1.30x faster                                                             |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                             |
| generators                 | 43.5 ms                                                               | 34.9 ms: 1.25x faster                                                             |
| go                         | 157 ms                                                                | 128 ms: 1.23x faster                                                              |
| dulwich_log                | 62.0 ms                                                               | 52.3 ms: 1.19x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                             |
| regex_dna                  | 254 ms                                                                | 224 ms: 1.13x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.62 us: 1.13x faster                                                             |
| pylint                     | 355 ms                                                                | 316 ms: 1.12x faster                                                              |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| async_generators           | 491 ms                                                                | 450 ms: 1.09x faster                                                              |
| spectral_norm              | 131 ms                                                                | 120 ms: 1.09x faster                                                              |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                             |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                              |
| float                      | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                             |
| pyflate                    | 559 ms                                                                | 522 ms: 1.07x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 20.3 ms: 1.06x faster                                                             |
| regex_v8                   | 28.3 ms                                                               | 26.8 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                              |
| html5lib                   | 65.1 ms                                                               | 61.9 ms: 1.05x faster                                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.0 ms: 1.05x faster                                                             |
| deltablue                  | 4.12 ms                                                               | 3.95 ms: 1.04x faster                                                             |
| chaos                      | 71.4 ms                                                               | 68.7 ms: 1.04x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.52 sec: 1.03x faster                                                            |
| docutils                   | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                            |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                                              |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| xml_etree_process          | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                                             |
| genshi_xml                 | 60.6 ms                                                               | 61.1 ms: 1.01x slower                                                             |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                              |
| pidigits                   | 233 ms                                                                | 236 ms: 1.02x slower                                                              |
| sqlite_synth               | 3.77 us                                                               | 3.85 us: 1.02x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.66 ms: 1.03x slower                                                             |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.03x slower                                                             |
| unpickle_pure_python       | 260 us                                                                | 270 us: 1.04x slower                                                              |
| richards_super             | 58.5 ms                                                               | 61.0 ms: 1.04x slower                                                             |
| richards                   | 50.9 ms                                                               | 53.5 ms: 1.05x slower                                                             |
| scimark_fft                | 418 ms                                                                | 440 ms: 1.05x slower                                                              |
| scimark_lu                 | 146 ms                                                                | 155 ms: 1.07x slower                                                              |
| sympy_expand               | 454 ms                                                                | 485 ms: 1.07x slower                                                              |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                              |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                              |
| fannkuch                   | 443 ms                                                                | 486 ms: 1.10x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.07 sec: 1.10x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 1.01 sec: 1.10x slower                                                            |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.48 ms: 1.11x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.94 ms: 1.12x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                             |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                              |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                              |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.92 ms: 1.57x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.81 ms: 1.99x slower                                                             |
| logging_silent             | 127 ns                                                                | 629 ns: 4.96x slower                                                              |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                                      |

Benchmark hidden because not significant (13): crypto_pyaes, scimark_sor, nqueens, django_template, sympy_str, pycparser, logging_format, meteor_contest, hexiom, genshi_text, logging_simple, thrift, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x