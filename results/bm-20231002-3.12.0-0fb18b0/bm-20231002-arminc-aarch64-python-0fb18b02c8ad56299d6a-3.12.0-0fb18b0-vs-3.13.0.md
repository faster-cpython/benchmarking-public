# Results vs. 3.13.0

- fork: python
- ref: 0fb18b02c8ad56299d6a
- machine: linux-aarch64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.006x slower
- HPT reliability: 95.45%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 308 ms: 1.01x slower                                                  |
| chameleon      | 9.08 ms                                                  | 8.81 ms: 1.03x faster                                                 |
| docutils       | 2.89 sec                                                 | 2.98 sec: 1.03x slower                                                |
| tornado_http   | 128 ms                                                   | 136 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                 | 28.5 ms                                                  | 29.0 ms: 1.02x slower                                                 |
| async_tree_memoization_tg  | 649 ms                                                   | 740 ms: 1.14x slower                                                  |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 884 ms: 1.15x slower                                                  |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 912 ms: 1.19x slower                                                  |
| async_tree_memoization     | 651 ms                                                   | 777 ms: 1.19x slower                                                  |
| async_tree_none_tg         | 470 ms                                                   | 577 ms: 1.23x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.40 sec: 1.24x slower                                                |
| async_tree_none            | 497 ms                                                   | 624 ms: 1.26x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.27x slower                                                |
| Geometric mean             | (ref)                                                    | 1.15x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 105 ms: 1.09x faster                                                  |
| float          | 93.3 ms                                                  | 92.1 ms: 1.01x faster                                                 |
| pidigits       | 234 ms                                                   | 233 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 28.3 ms: 1.12x faster                                                 |
| regex_effbot   | 4.89 ms                                                  | 4.64 ms: 1.05x faster                                                 |
| regex_compile  | 127 ms                                                   | 137 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                    | 1.02x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 13.6 ms                                                  | 12.3 ms: 1.11x faster                                                 |
| json_loads           | 31.7 us                                                  | 30.7 us: 1.03x faster                                                 |
| tomli_loads          | 2.54 sec                                                 | 2.59 sec: 1.02x slower                                                |
| pickle_pure_python   | 357 us                                                   | 365 us: 1.02x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 260 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.01x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 11.4 ms: 1.36x faster                                                 |
| python_startup_no_site | 8.73 ms                                                  | 8.37 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                    | 1.19x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 12.9 ms: 1.04x faster                                                 |
| django_template | 41.6 ms                                                  | 40.7 ms: 1.02x faster                                                 |
| genshi_text     | 27.7 ms                                                  | 27.4 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.92 ms: 1.75x faster                                                 |
| python_startup             | 15.4 ms                                                  | 11.4 ms: 1.36x faster                                                 |
| mypy2                      | 1.15 sec                                                 | 873 ms: 1.32x faster                                                  |
| gc_traversal               | 5.77 ms                                                  | 4.40 ms: 1.31x faster                                                 |
| telco                      | 9.74 ms                                                  | 8.51 ms: 1.15x faster                                                 |
| coverage                   | 99.1 ms                                                  | 87.3 ms: 1.14x faster                                                 |
| regex_v8                   | 31.8 ms                                                  | 28.3 ms: 1.12x faster                                                 |
| json_dumps                 | 13.6 ms                                                  | 12.3 ms: 1.11x faster                                                 |
| nbody                      | 114 ms                                                   | 105 ms: 1.09x faster                                                  |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.09x faster                                                  |
| bench_mp_pool              | 7.68 ms                                                  | 7.05 ms: 1.09x faster                                                 |
| typing_runtime_protocols   | 193 us                                                   | 181 us: 1.07x faster                                                  |
| scimark_fft                | 447 ms                                                   | 418 ms: 1.07x faster                                                  |
| scimark_sor                | 160 ms                                                   | 150 ms: 1.07x faster                                                  |
| regex_effbot               | 4.89 ms                                                  | 4.64 ms: 1.05x faster                                                 |
| richards                   | 53.6 ms                                                  | 50.9 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.19 ms: 1.05x faster                                                 |
| logging_silent             | 133 ns                                                   | 127 ns: 1.05x faster                                                  |
| python_startup_no_site     | 8.73 ms                                                  | 8.37 ms: 1.04x faster                                                 |
| fannkuch                   | 461 ms                                                   | 443 ms: 1.04x faster                                                  |
| mako                       | 13.4 ms                                                  | 12.9 ms: 1.04x faster                                                 |
| json                       | 5.73 ms                                                  | 5.54 ms: 1.03x faster                                                 |
| thrift                     | 968 us                                                   | 937 us: 1.03x faster                                                  |
| json_loads                 | 31.7 us                                                  | 30.7 us: 1.03x faster                                                 |
| chameleon                  | 9.08 ms                                                  | 8.81 ms: 1.03x faster                                                 |
| richards_super             | 60.1 ms                                                  | 58.5 ms: 1.03x faster                                                 |
| django_template            | 41.6 ms                                                  | 40.7 ms: 1.02x faster                                                 |
| hexiom                     | 7.11 ms                                                  | 6.98 ms: 1.02x faster                                                 |
| go                         | 160 ms                                                   | 157 ms: 1.02x faster                                                  |
| deepcopy_memo              | 50.4 us                                                  | 49.6 us: 1.01x faster                                                 |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 62.2 ms                                                  | 61.3 ms: 1.01x faster                                                 |
| pycparser                  | 1.27 sec                                                 | 1.26 sec: 1.01x faster                                                |
| float                      | 93.3 ms                                                  | 92.1 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 926 ms                                                   | 916 ms: 1.01x faster                                                  |
| genshi_text                | 27.7 ms                                                  | 27.4 ms: 1.01x faster                                                 |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                |
| sqlglot_normalize          | 127 ms                                                   | 126 ms: 1.01x faster                                                  |
| sympy_expand               | 457 ms                                                   | 454 ms: 1.01x faster                                                  |
| pidigits                   | 234 ms                                                   | 233 ms: 1.01x faster                                                  |
| pyflate                    | 556 ms                                                   | 559 ms: 1.00x slower                                                  |
| 2to3                       | 304 ms                                                   | 308 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 83.6 ms                                                  | 85.1 ms: 1.02x slower                                                 |
| coroutines                 | 28.5 ms                                                  | 29.0 ms: 1.02x slower                                                 |
| tomli_loads                | 2.54 sec                                                 | 2.59 sec: 1.02x slower                                                |
| mdp                        | 3.34 sec                                                 | 3.41 sec: 1.02x slower                                                |
| pickle_pure_python         | 357 us                                                   | 365 us: 1.02x slower                                                  |
| bench_thread_pool          | 1.27 ms                                                  | 1.31 ms: 1.03x slower                                                 |
| docutils                   | 2.89 sec                                                 | 2.98 sec: 1.03x slower                                                |
| crypto_pyaes               | 83.7 ms                                                  | 86.6 ms: 1.04x slower                                                 |
| unpickle_pure_python       | 251 us                                                   | 260 us: 1.04x slower                                                  |
| sympy_integrate            | 20.8 ms                                                  | 21.6 ms: 1.04x slower                                                 |
| scimark_lu                 | 139 ms                                                   | 146 ms: 1.04x slower                                                  |
| sqlalchemy_declarative     | 150 ms                                                   | 157 ms: 1.05x slower                                                  |
| chaos                      | 68.0 ms                                                  | 71.4 ms: 1.05x slower                                                 |
| sqlglot_transpile          | 1.73 ms                                                  | 1.83 ms: 1.06x slower                                                 |
| sympy_str                  | 264 ms                                                   | 280 ms: 1.06x slower                                                  |
| tornado_http               | 128 ms                                                   | 136 ms: 1.06x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.46 ms: 1.06x slower                                                 |
| logging_format             | 7.82 us                                                  | 8.34 us: 1.07x slower                                                 |
| sympy_sum                  | 144 ms                                                   | 154 ms: 1.08x slower                                                  |
| deltablue                  | 3.82 ms                                                  | 4.12 ms: 1.08x slower                                                 |
| logging_simple             | 7.07 us                                                  | 7.63 us: 1.08x slower                                                 |
| regex_compile              | 127 ms                                                   | 137 ms: 1.08x slower                                                  |
| pathlib                    | 22.7 ms                                                  | 24.5 ms: 1.08x slower                                                 |
| sqlalchemy_imperative      | 15.1 ms                                                  | 16.7 ms: 1.10x slower                                                 |
| async_tree_memoization_tg  | 649 ms                                                   | 740 ms: 1.14x slower                                                  |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 884 ms: 1.15x slower                                                  |
| generators                 | 37.6 ms                                                  | 43.5 ms: 1.16x slower                                                 |
| raytrace                   | 300 ms                                                   | 353 ms: 1.18x slower                                                  |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 912 ms: 1.19x slower                                                  |
| async_tree_memoization     | 651 ms                                                   | 777 ms: 1.19x slower                                                  |
| async_tree_none_tg         | 470 ms                                                   | 577 ms: 1.23x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.40 sec: 1.24x slower                                                |
| comprehensions             | 20.4 us                                                  | 25.4 us: 1.25x slower                                                 |
| async_tree_none            | 497 ms                                                   | 624 ms: 1.26x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.27x slower                                                |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                          |

Benchmark hidden because not significant (13): html5lib, xml_etree_process, xml_etree_generate, nqueens, xml_etree_parse, deepcopy, asyncio_websockets, async_generators, regex_dna, genshi_xml, xml_etree_iterparse, deepcopy_reduce, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 95.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x