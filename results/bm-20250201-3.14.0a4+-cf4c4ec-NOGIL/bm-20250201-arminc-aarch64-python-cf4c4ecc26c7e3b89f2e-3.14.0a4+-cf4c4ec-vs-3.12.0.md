# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.119x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 379 ms: 1.23x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.38 sec: 1.13x slower                                                   |
| html5lib       | 65.1 ms                                                               | 75.6 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 933 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 503 ms: 1.47x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 966 ms: 1.46x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 549 ms: 1.42x faster                                                     |
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 414 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 695 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.40x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 103 ms: 1.12x slower                                                     |
| nbody          | 105 ms                                                                | 188 ms: 1.80x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.27x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.05 ms: 1.15x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 31.9 ms: 1.12x slower                                                    |
| regex_compile  | 137 ms                                                                | 158 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 130 ms: 1.16x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 184 ms: 1.06x faster                                                     |
| unpickle             | 18.5 us                                                               | 19.9 us: 1.08x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 42.2 us: 1.13x slower                                                    |
| pickle_list          | 5.25 us                                                               | 6.07 us: 1.16x slower                                                    |
| pickle               | 13.4 us                                                               | 15.9 us: 1.19x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 308 us: 1.19x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 7.45 us: 1.21x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 3.20 sec: 1.23x slower                                                   |
| json_loads           | 30.7 us                                                               | 38.3 us: 1.25x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 143 ms: 1.27x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 103 ms: 1.31x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 484 us: 1.33x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 17.1 ms: 1.39x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.60x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 78.9 ms: 1.30x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 37.1 ms: 1.35x slower                                                    |
| django_template | 40.7 ms                                                               | 55.2 ms: 1.36x slower                                                    |
| mako            | 12.9 ms                                                               | 23.5 ms: 1.82x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.44x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 2.70 ms: 1.63x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 933 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 503 ms: 1.47x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 966 ms: 1.46x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 549 ms: 1.42x faster                                                     |
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 414 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 695 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 130 ms: 1.16x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.05 ms: 1.15x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 184 ms: 1.06x faster                                                     |
| deepcopy                   | 446 us                                                                | 421 us: 1.06x faster                                                     |
| generators                 | 43.5 ms                                                               | 42.4 ms: 1.03x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 681 ms: 1.04x slower                                                     |
| coroutines                 | 29.0 ms                                                               | 30.5 ms: 1.05x slower                                                    |
| comprehensions             | 25.4 us                                                               | 26.7 us: 1.05x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 52.5 us: 1.06x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.9 us: 1.08x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 611 ms: 1.08x slower                                                     |
| pylint                     | 355 ms                                                                | 385 ms: 1.09x slower                                                     |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                                     |
| async_generators           | 491 ms                                                                | 542 ms: 1.10x slower                                                     |
| float                      | 92.1 ms                                                               | 103 ms: 1.12x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 31.9 ms: 1.12x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.16 ms: 1.12x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.86 sec: 1.13x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 42.2 us: 1.13x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.38 sec: 1.13x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.67 us: 1.14x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.43 sec: 1.14x slower                                                   |
| go                         | 157 ms                                                                | 180 ms: 1.14x slower                                                     |
| regex_compile              | 137 ms                                                                | 158 ms: 1.15x slower                                                     |
| pickle_list                | 5.25 us                                                               | 6.07 us: 1.16x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 75.6 ms: 1.16x slower                                                    |
| scimark_fft                | 418 ms                                                                | 487 ms: 1.16x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 72.5 ms: 1.17x slower                                                    |
| pyflate                    | 559 ms                                                                | 655 ms: 1.17x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.56 sec: 1.17x slower                                                   |
| raytrace                   | 353 ms                                                                | 415 ms: 1.17x slower                                                     |
| logging_simple             | 7.63 us                                                               | 8.99 us: 1.18x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.9 us: 1.19x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 308 us: 1.19x slower                                                     |
| json                       | 5.54 ms                                                               | 6.59 ms: 1.19x slower                                                    |
| logging_format             | 8.34 us                                                               | 9.96 us: 1.19x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 7.45 us: 1.21x slower                                                    |
| scimark_sor                | 150 ms                                                                | 182 ms: 1.22x slower                                                     |
| logging_silent             | 127 ns                                                                | 156 ns: 1.23x slower                                                     |
| 2to3                       | 308 ms                                                                | 379 ms: 1.23x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 3.20 sec: 1.23x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 156 ms: 1.24x slower                                                     |
| chaos                      | 71.4 ms                                                               | 88.7 ms: 1.24x slower                                                    |
| json_loads                 | 30.7 us                                                               | 38.3 us: 1.25x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.27x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 77.7 ms: 1.27x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.85 ms: 1.27x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.27x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 143 ms: 1.27x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 201 ms: 1.27x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 197 ms: 1.28x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 78.9 ms: 1.30x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.38 ms: 1.30x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 103 ms: 1.31x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 112 ms: 1.31x slower                                                     |
| sympy_str                  | 280 ms                                                                | 368 ms: 1.31x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 484 us: 1.33x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 115 ms: 1.33x slower                                                     |
| thrift                     | 937 us                                                                | 1.24 ms: 1.33x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 195 ms: 1.34x slower                                                     |
| telco                      | 8.51 ms                                                               | 11.4 ms: 1.34x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 22.4 ms: 1.35x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.41 ms: 1.35x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 29.2 ms: 1.35x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 37.1 ms: 1.35x slower                                                    |
| sympy_expand               | 454 ms                                                                | 614 ms: 1.35x slower                                                     |
| meteor_contest             | 112 ms                                                                | 152 ms: 1.36x slower                                                     |
| django_template            | 40.7 ms                                                               | 55.2 ms: 1.36x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 2.00 ms: 1.37x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 17.1 ms: 1.39x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 139 ms: 1.40x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.88 ms: 1.44x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                    |
| richards                   | 50.9 ms                                                               | 75.1 ms: 1.48x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 6.17 ms: 1.50x slower                                                    |
| richards_super             | 58.5 ms                                                               | 88.4 ms: 1.51x slower                                                    |
| fannkuch                   | 443 ms                                                                | 672 ms: 1.51x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 282 us: 1.56x slower                                                     |
| coverage                   | 87.3 ms                                                               | 140 ms: 1.60x slower                                                     |
| python_startup             | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                    |
| nbody                      | 105 ms                                                                | 188 ms: 1.80x slower                                                     |
| mako                       | 12.9 ms                                                               | 23.5 ms: 1.82x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 54.9 ms: 7.78x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.19x slower                                                             |

Benchmark hidden because not significant (3): sqlite_synth, pidigits, regex_dna
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.119x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.25x