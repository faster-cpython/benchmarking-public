# Results vs. 3.12.0

- fork: python
- ref: 4f18916c5c28321f363e
- machine: linux-aarch64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 288 ms: 1.07x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                                   |
| html5lib       | 65.1 ms                                                               | 58.2 ms: 1.12x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 441 ms: 1.76x faster                                                     |
| async_tree_none            | 624 ms                                                                | 365 ms: 1.71x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 443 ms: 1.67x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 853 ms: 1.65x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 353 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 865 ms: 1.63x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 713 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 697 ms: 1.27x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.56x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.8 ms: 1.10x faster                                                    |
| nbody          | 105 ms                                                                | 126 ms: 1.20x slower                                                     |
| pidigits       | 233 ms                                                                | 290 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 118 ms: 1.17x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                    |
| regex_dna      | 254 ms                                                                | 234 ms: 1.09x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 29.4 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle             | 18.5 us                                                               | 16.5 us: 1.12x faster                                                    |
| unpickle_list        | 6.17 us                                                               | 5.57 us: 1.11x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.36 sec: 1.10x faster                                                   |
| xml_etree_generate   | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| unpickle_pure_python | 260 us                                                                | 246 us: 1.06x faster                                                     |
| xml_etree_process    | 79.0 ms                                                               | 75.1 ms: 1.05x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 372 us: 1.02x slower                                                     |
| pickle_list          | 5.25 us                                                               | 5.40 us: 1.03x slower                                                    |
| xml_etree_parse      | 195 ms                                                                | 203 ms: 1.04x slower                                                     |
| json_loads           | 30.7 us                                                               | 33.4 us: 1.09x slower                                                    |
| pickle               | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.1 ms: 1.07x faster                                                    |
| genshi_text     | 27.4 ms                                                               | 25.8 ms: 1.06x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 58.0 ms: 1.05x faster                                                    |
| mako            | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.59 sec: 2.15x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 441 ms: 1.76x faster                                                     |
| async_tree_none            | 624 ms                                                                | 365 ms: 1.71x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 443 ms: 1.67x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 853 ms: 1.65x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 353 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 865 ms: 1.63x faster                                                     |
| deepcopy                   | 446 us                                                                | 306 us: 1.46x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 34.8 us: 1.43x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 713 ms: 1.28x faster                                                     |
| comprehensions             | 25.4 us                                                               | 19.9 us: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 697 ms: 1.27x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.32 us: 1.23x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 50.9 ms: 1.22x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.8 ms: 1.22x faster                                                    |
| go                         | 157 ms                                                                | 129 ms: 1.21x faster                                                     |
| async_generators           | 491 ms                                                                | 416 ms: 1.18x faster                                                     |
| regex_compile              | 137 ms                                                                | 118 ms: 1.17x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.1 ms: 1.16x faster                                                    |
| pylint                     | 355 ms                                                                | 307 ms: 1.16x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 137 ms: 1.13x faster                                                     |
| raytrace                   | 353 ms                                                                | 315 ms: 1.12x faster                                                     |
| unpickle                   | 18.5 us                                                               | 16.5 us: 1.12x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 58.2 ms: 1.12x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.47 us: 1.12x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.85 us: 1.11x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 19.4 ms: 1.11x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.57 us: 1.11x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.72 ms: 1.11x faster                                                    |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.11x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.36 sec: 1.10x faster                                                   |
| float                      | 92.1 ms                                                               | 83.8 ms: 1.10x faster                                                    |
| logging_silent             | 127 ns                                                                | 116 ns: 1.09x faster                                                     |
| sympy_str                  | 280 ms                                                                | 256 ms: 1.09x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.1 ms: 1.09x faster                                                    |
| regex_dna                  | 254 ms                                                                | 234 ms: 1.09x faster                                                     |
| chaos                      | 71.4 ms                                                               | 65.9 ms: 1.08x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| django_template            | 40.7 ms                                                               | 38.1 ms: 1.07x faster                                                    |
| 2to3                       | 308 ms                                                                | 288 ms: 1.07x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 25.8 ms: 1.06x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 149 ms: 1.06x faster                                                     |
| pyflate                    | 559 ms                                                                | 528 ms: 1.06x faster                                                     |
| unpickle_pure_python       | 260 us                                                                | 246 us: 1.06x faster                                                     |
| xml_etree_process          | 79.0 ms                                                               | 75.1 ms: 1.05x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 58.0 ms: 1.05x faster                                                    |
| scimark_fft                | 418 ms                                                                | 401 ms: 1.04x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 546 ms: 1.04x faster                                                     |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.03x faster                                                   |
| docutils                   | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 890 ms: 1.03x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 84.7 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.85 sec: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.01x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.82 us: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 372 us: 1.02x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.40 us: 1.03x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 187 us: 1.04x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 29.4 ms: 1.04x slower                                                    |
| telco                      | 8.51 ms                                                               | 8.83 ms: 1.04x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 203 ms: 1.04x slower                                                     |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.55 ms: 1.06x slower                                                    |
| json                       | 5.54 ms                                                               | 5.92 ms: 1.07x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.4 us: 1.09x slower                                                    |
| fannkuch                   | 443 ms                                                                | 493 ms: 1.11x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.5 ms: 1.12x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| nbody                      | 105 ms                                                                | 126 ms: 1.20x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| pidigits                   | 233 ms                                                                | 290 ms: 1.25x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.67 ms: 1.52x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.84 ms: 2.00x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 3.29 sec: 466.78x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (11): coroutines, scimark_sor, richards, scimark_lu, pickle_dict, richards_super, sympy_expand, xml_etree_iterparse, hexiom, nqueens, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.09x