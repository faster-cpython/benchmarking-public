# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.082x slower
- HPT reliability: 99.69%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 350 ms: 1.14x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.0 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 827 ms: 1.70x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 438 ms: 1.69x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 846 ms: 1.67x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                    |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 362 ms: 1.59x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 633 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.58x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 94.0 ms: 1.02x slower                                                   |
| nbody          | 105 ms                                                                | 183 ms: 1.75x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.22x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 25.9 ms: 1.10x faster                                                   |
| regex_dna      | 254 ms                                                                | 238 ms: 1.07x faster                                                    |
| regex_compile  | 137 ms                                                                | 153 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 130 ms: 1.16x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 38.8 us: 1.04x slower                                                   |
| unpickle             | 18.5 us                                                               | 20.1 us: 1.09x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.86 sec: 1.10x slower                                                  |
| pickle_list          | 5.25 us                                                               | 5.83 us: 1.11x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.87 us: 1.11x slower                                                   |
| pickle               | 13.4 us                                                               | 15.3 us: 1.14x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 300 us: 1.15x slower                                                    |
| json_loads           | 30.7 us                                                               | 36.6 us: 1.19x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 442 us: 1.21x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.9 ms: 1.21x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 139 ms: 1.24x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.0 ms: 1.43x slower                                                   |
| python_startup         | 11.4 ms                                                               | 19.9 ms: 1.75x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.58x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 50.9 ms: 1.25x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 76.0 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 36.2 ms: 1.32x slower                                                   |
| mako            | 12.9 ms                                                               | 21.4 ms: 1.66x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.36x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.93 sec: 1.77x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 827 ms: 1.70x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 438 ms: 1.69x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 846 ms: 1.67x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                    |
| async_tree_none            | 624 ms                                                                | 390 ms: 1.60x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 362 ms: 1.59x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 2.87 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 633 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 130 ms: 1.16x faster                                                    |
| deepcopy                   | 446 us                                                                | 386 us: 1.16x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.44 us: 1.10x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 45.3 us: 1.10x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 25.9 ms: 1.10x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.08x faster                                                   |
| generators                 | 43.5 ms                                                               | 40.7 ms: 1.07x faster                                                   |
| regex_dna                  | 254 ms                                                                | 238 ms: 1.07x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.1 us: 1.06x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.1 ms: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| go                         | 157 ms                                                                | 152 ms: 1.03x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 94.0 ms: 1.02x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                   |
| pyflate                    | 559 ms                                                                | 584 ms: 1.04x slower                                                    |
| pylint                     | 355 ms                                                                | 373 ms: 1.05x slower                                                    |
| async_generators           | 491 ms                                                                | 519 ms: 1.06x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.33 sec: 1.06x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 4.39 us: 1.07x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 70.0 ms: 1.08x slower                                                   |
| logging_simple             | 7.63 us                                                               | 8.24 us: 1.08x slower                                                   |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.08x slower                                                    |
| unpickle                   | 18.5 us                                                               | 20.1 us: 1.09x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 31.6 ms: 1.09x slower                                                   |
| logging_silent             | 127 ns                                                                | 139 ns: 1.10x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.86 sec: 1.10x slower                                                  |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                                    |
| logging_format             | 8.34 us                                                               | 9.21 us: 1.10x slower                                                   |
| regex_compile              | 137 ms                                                                | 153 ms: 1.11x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.83 us: 1.11x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.43 sec: 1.11x slower                                                  |
| scimark_fft                | 418 ms                                                                | 466 ms: 1.11x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.87 us: 1.11x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.77 ms: 1.11x slower                                                   |
| raytrace                   | 353 ms                                                                | 398 ms: 1.13x slower                                                    |
| json                       | 5.54 ms                                                               | 6.25 ms: 1.13x slower                                                   |
| 2to3                       | 308 ms                                                                | 350 ms: 1.14x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.3 us: 1.14x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.14 sec: 1.14x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.04 sec: 1.14x slower                                                  |
| chaos                      | 71.4 ms                                                               | 82.0 ms: 1.15x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 300 us: 1.15x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.80 ms: 1.16x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 116 ms: 1.17x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.27 ms: 1.18x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 25.6 ms: 1.18x slower                                                   |
| json_loads                 | 30.7 us                                                               | 36.6 us: 1.19x slower                                                   |
| sympy_str                  | 280 ms                                                                | 337 ms: 1.20x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 186 ms: 1.21x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 442 us: 1.21x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.9 ms: 1.21x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 103 ms: 1.21x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 107 ms: 1.23x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 139 ms: 1.24x slower                                                    |
| meteor_contest             | 112 ms                                                                | 139 ms: 1.25x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.73 ms: 1.25x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.9 ms: 1.25x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 76.0 ms: 1.25x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 186 ms: 1.28x slower                                                    |
| thrift                     | 937 us                                                                | 1.20 ms: 1.29x slower                                                   |
| sympy_expand               | 454 ms                                                                | 586 ms: 1.29x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 36.2 ms: 1.32x slower                                                   |
| fannkuch                   | 443 ms                                                                | 588 ms: 1.33x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 244 us: 1.35x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.80 ms: 1.37x slower                                                   |
| richards_super             | 58.5 ms                                                               | 80.3 ms: 1.37x slower                                                   |
| richards                   | 50.9 ms                                                               | 70.7 ms: 1.39x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 12.0 ms: 1.43x slower                                                   |
| coverage                   | 87.3 ms                                                               | 142 ms: 1.62x slower                                                    |
| mako                       | 12.9 ms                                                               | 21.4 ms: 1.66x slower                                                   |
| nbody                      | 105 ms                                                                | 183 ms: 1.75x slower                                                    |
| python_startup             | 11.4 ms                                                               | 19.9 ms: 1.75x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 63.8 ms: 9.05x slower                                                   |
| telco                      | 8.51 ms                                                               | 186 ms: 21.92x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (2): asyncio_tcp, pidigits
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.082x slower

# HPT report

- Reliability score: 99.69% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.32x