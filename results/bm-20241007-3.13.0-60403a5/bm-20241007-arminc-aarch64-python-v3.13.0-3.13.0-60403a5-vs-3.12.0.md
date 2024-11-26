# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-aarch64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.010x faster
- HPT reliability: 95.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 304 ms: 1.01x faster                                     |
| chameleon      | 8.81 ms                                                               | 9.08 ms: 1.03x slower                                    |
| docutils       | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                   |
| tornado_http   | 136 ms                                                                | 128 ms: 1.06x faster                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.11 sec: 1.27x faster                                   |
| async_tree_none            | 624 ms                                                                | 497 ms: 1.26x faster                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.13 sec: 1.24x faster                                   |
| async_tree_none_tg         | 577 ms                                                                | 470 ms: 1.23x faster                                     |
| async_tree_memoization     | 777 ms                                                                | 651 ms: 1.19x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 766 ms: 1.19x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 769 ms: 1.15x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 649 ms: 1.14x faster                                     |
| Geometric mean             | (ref)                                                                 | 1.21x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                     |
| float          | 92.1 ms                                                               | 93.3 ms: 1.01x slower                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                     |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                    |
| regex_v8       | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                     |
| pickle_pure_python   | 365 us                                                                | 357 us: 1.02x faster                                     |
| tomli_loads          | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                   |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                    |
| json_dumps           | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                             |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                    |
| python_startup         | 11.4 ms                                                               | 15.4 ms: 1.36x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.19x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                    |
| django_template | 40.7 ms                                                               | 41.6 ms: 1.02x slower                                    |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.11 sec: 1.27x faster                                   |
| async_tree_none            | 624 ms                                                                | 497 ms: 1.26x faster                                     |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.25x faster                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.13 sec: 1.24x faster                                   |
| async_tree_none_tg         | 577 ms                                                                | 470 ms: 1.23x faster                                     |
| async_tree_memoization     | 777 ms                                                                | 651 ms: 1.19x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 766 ms: 1.19x faster                                     |
| raytrace                   | 353 ms                                                                | 300 ms: 1.18x faster                                     |
| generators                 | 43.5 ms                                                               | 37.6 ms: 1.16x faster                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 769 ms: 1.15x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 649 ms: 1.14x faster                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.1 ms: 1.10x faster                                    |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                    |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                     |
| logging_simple             | 7.63 us                                                               | 7.07 us: 1.08x faster                                    |
| deltablue                  | 4.12 ms                                                               | 3.82 ms: 1.08x faster                                    |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.08x faster                                     |
| logging_format             | 8.34 us                                                               | 7.82 us: 1.07x faster                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.38 ms: 1.06x faster                                    |
| tornado_http               | 136 ms                                                                | 128 ms: 1.06x faster                                     |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                    |
| chaos                      | 71.4 ms                                                               | 68.0 ms: 1.05x faster                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                     |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.04x faster                                     |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                    |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                     |
| crypto_pyaes               | 86.6 ms                                                               | 83.7 ms: 1.04x faster                                    |
| docutils                   | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                    |
| pickle_pure_python         | 365 us                                                                | 357 us: 1.02x faster                                     |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                   |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                   |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.6 ms: 1.02x faster                                    |
| 2to3                       | 308 ms                                                                | 304 ms: 1.01x faster                                     |
| pyflate                    | 559 ms                                                                | 556 ms: 1.00x faster                                     |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                     |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                     |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                   |
| genshi_text                | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                    |
| pprint_safe_repr           | 916 ms                                                                | 926 ms: 1.01x slower                                     |
| float                      | 92.1 ms                                                               | 93.3 ms: 1.01x slower                                    |
| pycparser                  | 1.26 sec                                                              | 1.27 sec: 1.01x slower                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.2 ms: 1.01x slower                                    |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.01x slower                                     |
| deepcopy_memo              | 49.6 us                                                               | 50.4 us: 1.01x slower                                    |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                     |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                    |
| django_template            | 40.7 ms                                                               | 41.6 ms: 1.02x slower                                    |
| richards_super             | 58.5 ms                                                               | 60.1 ms: 1.03x slower                                    |
| chameleon                  | 8.81 ms                                                               | 9.08 ms: 1.03x slower                                    |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                    |
| thrift                     | 937 us                                                                | 968 us: 1.03x slower                                     |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.03x slower                                    |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                    |
| fannkuch                   | 443 ms                                                                | 461 ms: 1.04x slower                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                    |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.51 ms: 1.05x slower                                    |
| richards                   | 50.9 ms                                                               | 53.6 ms: 1.05x slower                                    |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                    |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                     |
| scimark_fft                | 418 ms                                                                | 447 ms: 1.07x slower                                     |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                     |
| bench_mp_pool              | 7.05 ms                                                               | 7.68 ms: 1.09x slower                                    |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.09x slower                                     |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                     |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                    |
| regex_v8                   | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                    |
| coverage                   | 87.3 ms                                                               | 99.1 ms: 1.14x slower                                    |
| telco                      | 8.51 ms                                                               | 9.74 ms: 1.15x slower                                    |
| gc_traversal               | 4.40 ms                                                               | 5.77 ms: 1.31x slower                                    |
| mypy2                      | 873 ms                                                                | 1.15 sec: 1.32x slower                                   |
| python_startup             | 11.4 ms                                                               | 15.4 ms: 1.36x slower                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.35 ms: 1.75x slower                                    |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                             |

Benchmark hidden because not significant (13): pylint, deepcopy_reduce, xml_etree_iterparse, genshi_xml, regex_dna, async_generators, asyncio_websockets, deepcopy, xml_etree_parse, nqueens, xml_etree_generate, xml_etree_process, html5lib
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 95.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x