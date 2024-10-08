# Results vs. 3.12.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: linux-aarch64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.04x faster
- HPT reliability: 98.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| html5lib       | 65.1 ms                                                               | 63.3 ms: 1.03x faster                                                   |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.48x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 414 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 548 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 731 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.80 ms: 1.04x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 191 ms: 1.02x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| django_template | 40.7 ms                                                               | 42.7 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.48x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 414 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 548 ms: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.5 us: 1.29x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 731 ms: 1.25x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.25x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.0 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 720 ms: 1.23x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| raytrace                   | 353 ms                                                                | 303 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                   |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.05 us: 1.08x faster                                                   |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.76 us: 1.08x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.05x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 82.2 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                   |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.26 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                                  |
| html5lib                   | 65.1 ms                                                               | 63.3 ms: 1.03x faster                                                   |
| async_generators           | 491 ms                                                                | 478 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| xml_etree_parse            | 195 ms                                                                | 191 ms: 1.02x faster                                                    |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| asyncio_tcp                | 566 ms                                                                | 557 ms: 1.02x faster                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.96 ms: 1.01x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                                   |
| thrift                     | 937 us                                                                | 942 us: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.08 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 933 ms: 1.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                    |
| pyflate                    | 559 ms                                                                | 571 ms: 1.02x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                    |
| richards_super             | 58.5 ms                                                               | 60.2 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.80 ms: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.42 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.7 ms: 1.05x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.5 ms: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.94 ms: 1.12x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.0 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (11): xml_etree_iterparse, asyncio_tcp_ssl, pickle_pure_python, asyncio_websockets, genshi_xml, float, docutils, meteor_contest, pylint, xml_etree_generate, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: bpe_tokeniser

# HPT report

- Reliability score: 98.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x