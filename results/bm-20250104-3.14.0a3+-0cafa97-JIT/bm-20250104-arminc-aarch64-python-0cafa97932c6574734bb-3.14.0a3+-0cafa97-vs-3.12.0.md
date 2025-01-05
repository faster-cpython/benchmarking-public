# Results vs. 3.12.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.030x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 321 ms: 1.04x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.27 sec: 1.10x slower                                                   |
| html5lib       | 65.1 ms                                                               | 69.8 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 892 ms: 1.57x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 917 ms: 1.54x faster                                                     |
| async_tree_none            | 624 ms                                                                | 405 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.54x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 510 ms: 1.52x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 672 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 698 ms: 1.31x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.48x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 243 ms: 1.04x slower                                                     |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 142 ms: 1.04x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.7 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 183 ms: 1.07x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| pickle_pure_python  | 365 us                                                                | 384 us: 1.05x slower                                                     |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| xml_etree_process   | 79.0 ms                                                               | 84.1 ms: 1.06x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.01 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| django_template | 40.7 ms                                                               | 48.5 ms: 1.19x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 35.4 ms: 1.29x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 81.5 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 892 ms: 1.57x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 917 ms: 1.54x faster                                                     |
| async_tree_none            | 624 ms                                                                | 405 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.54x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 510 ms: 1.52x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 672 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 698 ms: 1.31x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 38.4 us: 1.29x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                    |
| deepcopy                   | 446 us                                                                | 401 us: 1.11x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.07x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.95 us: 1.04x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 677 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.51 ms: 1.03x slower                                                    |
| regex_compile              | 137 ms                                                                | 142 ms: 1.04x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                    |
| 2to3                       | 308 ms                                                                | 321 ms: 1.04x slower                                                     |
| pidigits                   | 233 ms                                                                | 243 ms: 1.04x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.91 ms: 1.05x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.05x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 384 us: 1.05x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 163 ms: 1.05x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.61 sec: 1.06x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 84.1 ms: 1.06x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.4 ms: 1.07x slower                                                    |
| json                       | 5.54 ms                                                               | 5.91 ms: 1.07x slower                                                    |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                                     |
| pyflate                    | 559 ms                                                                | 598 ms: 1.07x slower                                                     |
| raytrace                   | 353 ms                                                                | 378 ms: 1.07x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 69.8 ms: 1.07x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 23.2 ms: 1.07x slower                                                    |
| logging_simple             | 7.63 us                                                               | 8.19 us: 1.07x slower                                                    |
| async_generators           | 491 ms                                                                | 528 ms: 1.08x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.01 ms: 1.08x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 93.4 ms: 1.08x slower                                                    |
| logging_format             | 8.34 us                                                               | 9.00 us: 1.08x slower                                                    |
| thrift                     | 937 us                                                                | 1.02 ms: 1.09x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.27 sec: 1.10x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.79 ms: 1.10x slower                                                    |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.10x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.52 ms: 1.10x slower                                                    |
| sympy_str                  | 280 ms                                                                | 308 ms: 1.10x slower                                                     |
| go                         | 157 ms                                                                | 174 ms: 1.10x slower                                                     |
| richards                   | 50.9 ms                                                               | 56.4 ms: 1.11x slower                                                    |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.11x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.20 us: 1.11x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 69.9 ms: 1.13x slower                                                    |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                     |
| sympy_expand               | 454 ms                                                                | 519 ms: 1.15x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 145 ms: 1.15x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.7 ms: 1.15x slower                                                    |
| fannkuch                   | 443 ms                                                                | 514 ms: 1.16x slower                                                     |
| logging_silent             | 127 ns                                                                | 147 ns: 1.16x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 71.3 ms: 1.16x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.89 ms: 1.16x slower                                                    |
| generators                 | 43.5 ms                                                               | 51.0 ms: 1.17x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.49 sec: 1.18x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| django_template            | 40.7 ms                                                               | 48.5 ms: 1.19x slower                                                    |
| chaos                      | 71.4 ms                                                               | 85.6 ms: 1.20x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 224 us: 1.24x slower                                                     |
| coverage                   | 87.3 ms                                                               | 111 ms: 1.27x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.11 sec: 1.27x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 35.4 ms: 1.29x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 131 ms: 1.32x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 81.5 ms: 1.35x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.58 sec: 1.37x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 9.81 ms: 1.41x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.91 ms: 1.57x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.71 ms: 1.93x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.42 sec: 201.90x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (11): float, pylint, regex_dna, comprehensions, sqlalchemy_declarative, scimark_fft, coroutines, unpickle_pure_python, sqlalchemy_imperative, xml_etree_generate, scimark_monte_carlo
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 99.79% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x