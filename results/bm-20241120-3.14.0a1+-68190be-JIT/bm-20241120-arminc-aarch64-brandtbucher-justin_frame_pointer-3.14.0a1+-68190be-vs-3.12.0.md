# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-aarch64
- commit hash: 68190be
- commit date: 2024-11-20
- overall geometric mean: 1.081x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 362 ms: 1.17x slower                                                           |
| docutils       | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                         |
| html5lib       | 65.1 ms                                                               | 80.6 ms: 1.24x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 975 ms: 1.44x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.39x faster                                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                           |
| async_tree_memoization     | 777 ms                                                                | 574 ms: 1.35x faster                                                           |
| async_tree_none            | 624 ms                                                                | 462 ms: 1.35x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 437 ms: 1.32x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 727 ms: 1.22x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 752 ms: 1.21x faster                                                           |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 244 ms: 1.05x slower                                                           |
| float          | 92.1 ms                                                               | 111 ms: 1.20x slower                                                           |
| nbody          | 105 ms                                                                | 135 ms: 1.29x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.15 ms: 1.12x faster                                                          |
| regex_dna      | 254 ms                                                                | 265 ms: 1.04x slower                                                           |
| regex_v8       | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                                          |
| regex_compile  | 137 ms                                                                | 172 ms: 1.25x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 30.7 us                                                               | 32.4 us: 1.05x slower                                                          |
| xml_etree_generate   | 112 ms                                                                | 122 ms: 1.09x slower                                                           |
| xml_etree_process    | 79.0 ms                                                               | 86.8 ms: 1.10x slower                                                          |
| tomli_loads          | 2.59 sec                                                              | 2.86 sec: 1.10x slower                                                         |
| pickle_pure_python   | 365 us                                                                | 412 us: 1.13x slower                                                           |
| unpickle_pure_python | 260 us                                                                | 294 us: 1.13x slower                                                           |
| xml_etree_iterparse  | 150 ms                                                                | 175 ms: 1.16x slower                                                           |
| json_dumps           | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.11x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                          |
| python_startup         | 11.4 ms                                                               | 15.8 ms: 1.39x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                          |
| django_template | 40.7 ms                                                               | 50.1 ms: 1.23x slower                                                          |
| genshi_text     | 27.4 ms                                                               | 34.8 ms: 1.27x slower                                                          |
| genshi_xml      | 60.6 ms                                                               | 84.0 ms: 1.39x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.24x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 2.88 ms: 1.53x faster                                                          |
| async_tree_io_tg           | 1.40 sec                                                              | 975 ms: 1.44x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.39x faster                                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                           |
| async_tree_memoization     | 777 ms                                                                | 574 ms: 1.35x faster                                                           |
| async_tree_none            | 624 ms                                                                | 462 ms: 1.35x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 437 ms: 1.32x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 727 ms: 1.22x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 752 ms: 1.21x faster                                                           |
| deepcopy_memo              | 49.6 us                                                               | 44.3 us: 1.12x faster                                                          |
| regex_effbot               | 4.64 ms                                                               | 4.15 ms: 1.12x faster                                                          |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                          |
| deepcopy                   | 446 us                                                                | 413 us: 1.08x faster                                                           |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                                           |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                          |
| logging_format             | 8.34 us                                                               | 8.62 us: 1.03x slower                                                          |
| python_startup_no_site     | 8.37 ms                                                               | 8.68 ms: 1.04x slower                                                          |
| logging_simple             | 7.63 us                                                               | 7.93 us: 1.04x slower                                                          |
| regex_dna                  | 254 ms                                                                | 265 ms: 1.04x slower                                                           |
| pidigits                   | 233 ms                                                                | 244 ms: 1.05x slower                                                           |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.05x slower                                                          |
| pylint                     | 355 ms                                                                | 375 ms: 1.06x slower                                                           |
| sqlalchemy_imperative      | 16.7 ms                                                               | 18.0 ms: 1.08x slower                                                          |
| bench_thread_pool          | 1.31 ms                                                               | 1.42 ms: 1.08x slower                                                          |
| xml_etree_generate         | 112 ms                                                                | 122 ms: 1.09x slower                                                           |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.09x slower                                                          |
| crypto_pyaes               | 86.6 ms                                                               | 94.4 ms: 1.09x slower                                                          |
| thrift                     | 937 us                                                                | 1.02 ms: 1.09x slower                                                          |
| comprehensions             | 25.4 us                                                               | 27.8 us: 1.09x slower                                                          |
| xml_etree_process          | 79.0 ms                                                               | 86.8 ms: 1.10x slower                                                          |
| mdp                        | 3.41 sec                                                              | 3.75 sec: 1.10x slower                                                         |
| tomli_loads                | 2.59 sec                                                              | 2.86 sec: 1.10x slower                                                         |
| async_generators           | 491 ms                                                                | 547 ms: 1.11x slower                                                           |
| scimark_fft                | 418 ms                                                                | 467 ms: 1.12x slower                                                           |
| regex_v8                   | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                                          |
| pickle_pure_python         | 365 us                                                                | 412 us: 1.13x slower                                                           |
| sqlite_synth               | 3.77 us                                                               | 4.26 us: 1.13x slower                                                          |
| unpickle_pure_python       | 260 us                                                                | 294 us: 1.13x slower                                                           |
| scimark_lu                 | 146 ms                                                                | 166 ms: 1.14x slower                                                           |
| raytrace                   | 353 ms                                                                | 405 ms: 1.15x slower                                                           |
| scimark_monte_carlo        | 85.1 ms                                                               | 98.2 ms: 1.15x slower                                                          |
| sympy_sum                  | 154 ms                                                                | 179 ms: 1.16x slower                                                           |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                           |
| meteor_contest             | 112 ms                                                                | 130 ms: 1.16x slower                                                           |
| xml_etree_iterparse        | 150 ms                                                                | 175 ms: 1.16x slower                                                           |
| telco                      | 8.51 ms                                                               | 9.97 ms: 1.17x slower                                                          |
| 2to3                       | 308 ms                                                                | 362 ms: 1.17x slower                                                           |
| sqlglot_transpile          | 1.83 ms                                                               | 2.17 ms: 1.18x slower                                                          |
| docutils                   | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                         |
| sympy_integrate            | 21.6 ms                                                               | 25.6 ms: 1.19x slower                                                          |
| float                      | 92.1 ms                                                               | 111 ms: 1.20x slower                                                           |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                          |
| scimark_sor                | 150 ms                                                                | 183 ms: 1.22x slower                                                           |
| sqlglot_optimize           | 61.3 ms                                                               | 75.3 ms: 1.23x slower                                                          |
| pycparser                  | 1.26 sec                                                              | 1.55 sec: 1.23x slower                                                         |
| django_template            | 40.7 ms                                                               | 50.1 ms: 1.23x slower                                                          |
| pyflate                    | 559 ms                                                                | 689 ms: 1.23x slower                                                           |
| richards_super             | 58.5 ms                                                               | 72.1 ms: 1.23x slower                                                          |
| sympy_str                  | 280 ms                                                                | 345 ms: 1.23x slower                                                           |
| html5lib                   | 65.1 ms                                                               | 80.6 ms: 1.24x slower                                                          |
| sqlglot_parse              | 1.46 ms                                                               | 1.81 ms: 1.24x slower                                                          |
| fannkuch                   | 443 ms                                                                | 551 ms: 1.24x slower                                                           |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.70 ms: 1.24x slower                                                          |
| regex_compile              | 137 ms                                                                | 172 ms: 1.25x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 2.40 ms: 1.25x slower                                                          |
| sqlglot_normalize          | 126 ms                                                                | 158 ms: 1.26x slower                                                           |
| dulwich_log                | 62.0 ms                                                               | 78.5 ms: 1.27x slower                                                          |
| genshi_text                | 27.4 ms                                                               | 34.8 ms: 1.27x slower                                                          |
| spectral_norm              | 131 ms                                                                | 166 ms: 1.27x slower                                                           |
| richards                   | 50.9 ms                                                               | 65.6 ms: 1.29x slower                                                          |
| logging_silent             | 127 ns                                                                | 164 ns: 1.29x slower                                                           |
| go                         | 157 ms                                                                | 203 ms: 1.29x slower                                                           |
| nbody                      | 105 ms                                                                | 135 ms: 1.29x slower                                                           |
| chaos                      | 71.4 ms                                                               | 93.9 ms: 1.32x slower                                                          |
| typing_runtime_protocols   | 181 us                                                                | 239 us: 1.32x slower                                                           |
| deltablue                  | 4.12 ms                                                               | 5.47 ms: 1.33x slower                                                          |
| generators                 | 43.5 ms                                                               | 58.2 ms: 1.34x slower                                                          |
| sympy_expand               | 454 ms                                                                | 608 ms: 1.34x slower                                                           |
| pprint_pformat             | 1.88 sec                                                              | 2.60 sec: 1.38x slower                                                         |
| nqueens                    | 99.2 ms                                                               | 137 ms: 1.38x slower                                                           |
| genshi_xml                 | 60.6 ms                                                               | 84.0 ms: 1.39x slower                                                          |
| python_startup             | 11.4 ms                                                               | 15.8 ms: 1.39x slower                                                          |
| pprint_safe_repr           | 916 ms                                                                | 1.29 sec: 1.41x slower                                                         |
| hexiom                     | 6.98 ms                                                               | 11.6 ms: 1.66x slower                                                          |
| bench_mp_pool              | 7.05 ms                                                               | 1.60 sec: 226.87x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.18x slower                                                                   |

Benchmark hidden because not significant (4): xml_etree_parse, sqlalchemy_declarative, coroutines, deepcopy_reduce
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241120-3.14.0a1+-68190be-JIT/bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.081x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.05x