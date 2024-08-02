# Results vs. 3.12.0

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.03x faster
- HPT reliability: 79.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                  |
| html5lib       | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                                   |
| tornado_http   | 136 ms                                                                | 127 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 441 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 409 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 533 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 569 ms: 1.37x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 731 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 713 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                    |
| regex_dna      | 254 ms                                                                | 248 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                  |
| pickle_pure_python   | 365 us                                                                | 359 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| json_loads           | 30.7 us                                                               | 33.0 us: 1.08x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.82 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| django_template | 40.7 ms                                                               | 42.9 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 441 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 409 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 533 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 569 ms: 1.37x faster                                                    |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 37.8 us: 1.31x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 731 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 713 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                                   |
| raytrace                   | 353 ms                                                                | 299 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.47 us: 1.18x faster                                                   |
| generators                 | 43.5 ms                                                               | 38.1 ms: 1.14x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.93 us: 1.10x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.69 us: 1.08x faster                                                   |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                                   |
| tornado_http               | 136 ms                                                                | 127 ms: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.06x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 81.7 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.25 ms: 1.05x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.1 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.8 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                                   |
| dask                       | 376 ms                                                                | 364 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 248 ms: 1.02x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 359 us: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 6.97 ms: 1.01x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| float                      | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.2 ms: 1.01x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 29.6 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.14 ms: 1.02x slower                                                   |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 129 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.8 ms: 1.02x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 581 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.03x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.03x slower                                                  |
| fannkuch                   | 443 ms                                                                | 456 ms: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 964 us: 1.03x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 946 ms: 1.03x slower                                                    |
| richards                   | 50.9 ms                                                               | 52.8 ms: 1.04x slower                                                   |
| pyflate                    | 559 ms                                                                | 583 ms: 1.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.82 ms: 1.05x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.9 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.57 ms: 1.06x slower                                                   |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| scimark_fft                | 418 ms                                                                | 448 ms: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.0 us: 1.08x slower                                                   |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.86 ms: 1.10x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.36 ms: 1.23x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (8): pylint, 2to3, async_generators, nqueens, asyncio_websockets, genshi_xml, xml_etree_process, xml_etree_generate
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: bpe_tokeniser

# HPT report

- Reliability score: 79.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x