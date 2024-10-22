# Results vs. 3.12.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-aarch64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.04x faster
- HPT reliability: 97.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                              |
| docutils       | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                            |
| html5lib       | 65.1 ms                                                               | 67.4 ms: 1.04x slower                                                             |
| tornado_http   | 136 ms                                                                | 126 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 405 ms: 1.42x faster                                                              |
| async_tree_none            | 624 ms                                                                | 439 ms: 1.42x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 552 ms: 1.41x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 540 ms: 1.37x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 1.09 sec: 1.29x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 707 ms: 1.25x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                              |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                              |
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                              |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                             |
| regex_v8       | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                              |
| pickle_pure_python   | 365 us                                                                | 355 us: 1.03x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                            |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.02x faster                                                              |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                                             |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.89 ms: 1.06x slower                                                             |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                             |
| django_template | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                                             |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 405 ms: 1.42x faster                                                              |
| async_tree_none            | 624 ms                                                                | 439 ms: 1.42x faster                                                              |
| async_tree_memoization     | 777 ms                                                                | 552 ms: 1.41x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 540 ms: 1.37x faster                                                              |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 1.09 sec: 1.29x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 38.9 us: 1.28x faster                                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 707 ms: 1.25x faster                                                              |
| generators                 | 43.5 ms                                                               | 35.0 ms: 1.24x faster                                                             |
| comprehensions             | 25.4 us                                                               | 20.9 us: 1.21x faster                                                             |
| deepcopy_reduce            | 4.10 us                                                               | 3.42 us: 1.20x faster                                                             |
| raytrace                   | 353 ms                                                                | 298 ms: 1.18x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.14x faster                                                             |
| logging_simple             | 7.63 us                                                               | 6.96 us: 1.10x faster                                                             |
| tornado_http               | 136 ms                                                                | 126 ms: 1.08x faster                                                              |
| logging_format             | 8.34 us                                                               | 7.75 us: 1.08x faster                                                             |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                              |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                              |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.07x faster                                                              |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                             |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                                             |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                             |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                                             |
| chaos                      | 71.4 ms                                                               | 67.7 ms: 1.06x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 58.8 ms: 1.05x faster                                                             |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.9 ms: 1.04x faster                                                             |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                                             |
| dask                       | 376 ms                                                                | 365 ms: 1.03x faster                                                              |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                            |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                              |
| pickle_pure_python         | 365 us                                                                | 355 us: 1.03x faster                                                              |
| coroutines                 | 29.0 ms                                                               | 28.2 ms: 1.03x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                            |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                              |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.02x faster                                                              |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                              |
| mdp                        | 3.41 sec                                                              | 3.37 sec: 1.01x faster                                                            |
| genshi_xml                 | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                             |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                              |
| bench_mp_pool              | 7.05 ms                                                               | 7.12 ms: 1.01x slower                                                             |
| sympy_expand               | 454 ms                                                                | 458 ms: 1.01x slower                                                              |
| go                         | 157 ms                                                                | 159 ms: 1.01x slower                                                              |
| hexiom                     | 6.98 ms                                                               | 7.06 ms: 1.01x slower                                                             |
| sqlglot_optimize           | 61.3 ms                                                               | 62.2 ms: 1.01x slower                                                             |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.01x slower                                                            |
| thrift                     | 937 us                                                                | 954 us: 1.02x slower                                                              |
| django_template            | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                                             |
| docutils                   | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                            |
| richards                   | 50.9 ms                                                               | 52.1 ms: 1.02x slower                                                             |
| logging_silent             | 127 ns                                                                | 130 ns: 1.03x slower                                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.38 ms: 1.03x slower                                                             |
| pyflate                    | 559 ms                                                                | 576 ms: 1.03x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 1.94 sec: 1.03x slower                                                            |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.03x slower                                                             |
| html5lib                   | 65.1 ms                                                               | 67.4 ms: 1.04x slower                                                             |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                             |
| pprint_safe_repr           | 916 ms                                                                | 952 ms: 1.04x slower                                                              |
| fannkuch                   | 443 ms                                                                | 463 ms: 1.04x slower                                                              |
| scimark_fft                | 418 ms                                                                | 440 ms: 1.05x slower                                                              |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                             |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                              |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.89 ms: 1.06x slower                                                             |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                              |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                             |
| typing_runtime_protocols   | 181 us                                                                | 198 us: 1.10x slower                                                              |
| regex_v8                   | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 4.88 ms: 1.11x slower                                                             |
| telco                      | 8.51 ms                                                               | 9.60 ms: 1.13x slower                                                             |
| coverage                   | 87.3 ms                                                               | 99.3 ms: 1.14x slower                                                             |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                             |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                                      |

Benchmark hidden because not significant (13): sqlglot_parse, xml_etree_parse, pylint, meteor_contest, nqueens, float, sqlglot_normalize, async_generators, asyncio_websockets, genshi_text, asyncio_tcp, richards_super, xml_etree_process
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: bpe_tokeniser

# HPT report

- Reliability score: 97.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x