# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-aarch64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 361 ms: 1.17x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.2 ms: 1.09x slower                                                   |
| tornado_http   | 136 ms                                                                | 144 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 408 ms: 1.41x faster                                                    |
| async_tree_none            | 624 ms                                                                | 447 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 587 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 737 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 722 ms: 1.22x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.2 ms: 1.03x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 122 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 259 ms: 1.02x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 175 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 279 us: 1.07x slower                                                    |
| json_loads           | 30.7 us                                                               | 33.2 us: 1.08x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 411 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.90 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| django_template | 40.7 ms                                                               | 50.3 ms: 1.24x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.6 ms: 1.26x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 84.9 ms: 1.40x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 408 ms: 1.41x faster                                                    |
| async_tree_none            | 624 ms                                                                | 447 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 587 ms: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.8 us: 1.28x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 737 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 722 ms: 1.22x faster                                                    |
| deepcopy                   | 446 us                                                                | 382 us: 1.17x faster                                                    |
| generators                 | 43.5 ms                                                               | 38.3 ms: 1.13x faster                                                   |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.7 us: 1.07x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.90 us: 1.06x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.28 us: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| float                      | 92.1 ms                                                               | 89.2 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| regex_dna                  | 254 ms                                                                | 259 ms: 1.02x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 29.6 ms: 1.02x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.21 us: 1.03x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| dask                       | 376 ms                                                                | 390 ms: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 90.0 ms: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 511 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 978 us: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.05x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.1 ms: 1.06x slower                                                   |
| tornado_http               | 136 ms                                                                | 144 ms: 1.06x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.90 ms: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                   |
| fannkuch                   | 443 ms                                                                | 474 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 279 us: 1.07x slower                                                    |
| richards                   | 50.9 ms                                                               | 54.8 ms: 1.07x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 91.5 ms: 1.08x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| deltablue                  | 4.12 ms                                                               | 4.47 ms: 1.08x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 71.2 ms: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.61 ms: 1.10x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 625 ms: 1.10x slower                                                    |
| pyflate                    | 559 ms                                                                | 621 ms: 1.11x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.04 ms: 1.12x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 68.5 ms: 1.12x slower                                                   |
| logging_silent             | 127 ns                                                                | 142 ns: 1.12x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 411 us: 1.13x slower                                                    |
| scimark_fft                | 418 ms                                                                | 472 ms: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.00 ms: 1.13x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 143 ms: 1.14x slower                                                    |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 99.7 ms: 1.14x slower                                                   |
| spectral_norm              | 131 ms                                                                | 149 ms: 1.14x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.04 ms: 1.15x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 208 us: 1.15x slower                                                    |
| pylint                     | 355 ms                                                                | 408 ms: 1.15x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| sympy_str                  | 280 ms                                                                | 323 ms: 1.16x slower                                                    |
| nbody                      | 105 ms                                                                | 122 ms: 1.17x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 72.6 ms: 1.17x slower                                                   |
| 2to3                       | 308 ms                                                                | 361 ms: 1.17x slower                                                    |
| scimark_sor                | 150 ms                                                                | 177 ms: 1.18x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 117 ms: 1.18x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 183 ms: 1.18x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                                  |
| sympy_expand               | 454 ms                                                                | 542 ms: 1.20x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.3 ms: 1.21x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.37 ms: 1.24x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.3 ms: 1.24x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.26x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.6 ms: 1.26x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.81 ms: 1.26x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.27x slower                                                  |
| regex_compile              | 137 ms                                                                | 175 ms: 1.27x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.42 sec: 1.28x slower                                                  |
| chaos                      | 71.4 ms                                                               | 93.3 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 84.9 ms: 1.40x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 13.2 ms: 1.88x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (2): mdp, xml_etree_process
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x