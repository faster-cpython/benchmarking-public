# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-aarch64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.03x faster
- HPT reliability: 80.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 304 ms: 1.01x faster                                                              |
| docutils       | 2.98 sec                                                              | 3.17 sec: 1.06x slower                                                            |
| html5lib       | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 402 ms: 1.43x faster                                                              |
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 558 ms: 1.39x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 1.09 sec: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 710 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 736 ms: 1.24x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.24x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                              |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                              |
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                             |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                            |
| unpickle_pure_python | 260 us                                                                | 249 us: 1.04x faster                                                              |
| pickle_pure_python   | 365 us                                                                | 360 us: 1.01x faster                                                              |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.07x slower                                                             |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                             |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                             |
| genshi_xml      | 60.6 ms                                                               | 62.2 ms: 1.03x slower                                                             |
| django_template | 40.7 ms                                                               | 42.2 ms: 1.04x slower                                                             |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 402 ms: 1.43x faster                                                              |
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 558 ms: 1.39x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                              |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 1.09 sec: 1.29x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 38.6 us: 1.28x faster                                                             |
| generators                 | 43.5 ms                                                               | 34.9 ms: 1.25x faster                                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 710 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 736 ms: 1.24x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.14 sec: 1.24x faster                                                            |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.44 us: 1.19x faster                                                             |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                                             |
| logging_simple             | 7.63 us                                                               | 6.95 us: 1.10x faster                                                             |
| logging_format             | 8.34 us                                                               | 7.63 us: 1.09x faster                                                             |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                              |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                              |
| deltablue                  | 4.12 ms                                                               | 3.84 ms: 1.07x faster                                                             |
| sqlglot_transpile          | 1.83 ms                                                               | 1.71 ms: 1.07x faster                                                             |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                             |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                            |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                                             |
| crypto_pyaes               | 86.6 ms                                                               | 83.0 ms: 1.04x faster                                                             |
| unpickle_pure_python       | 260 us                                                                | 249 us: 1.04x faster                                                              |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                              |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                             |
| dask                       | 376 ms                                                                | 364 ms: 1.03x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.0 ms: 1.02x faster                                                             |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                            |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                            |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                             |
| async_generators           | 491 ms                                                                | 480 ms: 1.02x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 21.3 ms: 1.01x faster                                                             |
| pickle_pure_python         | 365 us                                                                | 360 us: 1.01x faster                                                              |
| 2to3                       | 308 ms                                                                | 304 ms: 1.01x faster                                                              |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                              |
| pyflate                    | 559 ms                                                                | 563 ms: 1.01x slower                                                              |
| go                         | 157 ms                                                                | 158 ms: 1.01x slower                                                              |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.01x slower                                                              |
| sqlglot_optimize           | 61.3 ms                                                               | 62.3 ms: 1.02x slower                                                             |
| html5lib                   | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                                             |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                              |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.02x slower                                                            |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                                              |
| json                       | 5.54 ms                                                               | 5.65 ms: 1.02x slower                                                             |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                             |
| richards                   | 50.9 ms                                                               | 52.2 ms: 1.02x slower                                                             |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.03x slower                                                            |
| genshi_xml                 | 60.6 ms                                                               | 62.2 ms: 1.03x slower                                                             |
| thrift                     | 937 us                                                                | 962 us: 1.03x slower                                                              |
| pprint_safe_repr           | 916 ms                                                                | 946 ms: 1.03x slower                                                              |
| asyncio_tcp                | 566 ms                                                                | 585 ms: 1.03x slower                                                              |
| hexiom                     | 6.98 ms                                                               | 7.22 ms: 1.03x slower                                                             |
| django_template            | 40.7 ms                                                               | 42.2 ms: 1.04x slower                                                             |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.48 ms: 1.05x slower                                                             |
| fannkuch                   | 443 ms                                                                | 466 ms: 1.05x slower                                                              |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                              |
| scimark_fft                | 418 ms                                                                | 442 ms: 1.06x slower                                                              |
| docutils                   | 2.98 sec                                                              | 3.17 sec: 1.06x slower                                                            |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                                             |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                             |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                             |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.08x slower                                                              |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                              |
| coverage                   | 87.3 ms                                                               | 98.0 ms: 1.12x slower                                                             |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 5.04 ms: 1.15x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.76 ms: 1.15x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 2.32 ms: 1.21x slower                                                             |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                                      |

Benchmark hidden because not significant (12): tornado_http, xml_etree_iterparse, asyncio_websockets, pylint, regex_dna, float, bench_mp_pool, meteor_contest, richards_super, xml_etree_process, sqlglot_normalize, xml_etree_generate
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: bpe_tokeniser

# HPT report

- Reliability score: 80.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x