# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-aarch64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.016x faster
- HPT reliability: 83.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 304 ms: 1.01x faster                                           |
| chameleon      | 8.81 ms                                                               | 9.16 ms: 1.04x slower                                          |
| docutils       | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                         |
| html5lib       | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                          |
| tornado_http   | 136 ms                                                                | 128 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 494 ms: 1.26x faster                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 599 ms: 1.24x faster                                           |
| async_tree_none_tg         | 577 ms                                                                | 477 ms: 1.21x faster                                           |
| async_tree_memoization     | 777 ms                                                                | 649 ms: 1.20x faster                                           |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.17x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 784 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.2 ms: 1.01x faster                                          |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                           |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                           |
| regex_effbot   | 4.64 ms                                                               | 4.98 ms: 1.07x slower                                          |
| regex_v8       | 28.3 ms                                                               | 31.3 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                | 355 us: 1.03x faster                                           |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                         |
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                           |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                           |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                           |
| xml_etree_process    | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                          |
| json_loads           | 30.7 us                                                               | 31.4 us: 1.02x slower                                          |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                          |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 62.0 ms: 1.02x slower                                          |
| genshi_text     | 27.4 ms                                                               | 28.4 ms: 1.03x slower                                          |
| django_template | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                          |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 494 ms: 1.26x faster                                           |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                          |
| async_tree_memoization_tg  | 740 ms                                                                | 599 ms: 1.24x faster                                           |
| async_tree_none_tg         | 577 ms                                                                | 477 ms: 1.21x faster                                           |
| async_tree_memoization     | 777 ms                                                                | 649 ms: 1.20x faster                                           |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                           |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.17x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 784 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                           |
| generators                 | 43.5 ms                                                               | 37.7 ms: 1.15x faster                                          |
| mypy2                      | 873 ms                                                                | 765 ms: 1.14x faster                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                         |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                          |
| logging_simple             | 7.63 us                                                               | 7.06 us: 1.08x faster                                          |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                           |
| sqlglot_transpile          | 1.83 ms                                                               | 1.71 ms: 1.07x faster                                          |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                           |
| logging_format             | 8.34 us                                                               | 7.83 us: 1.07x faster                                          |
| tornado_http               | 136 ms                                                                | 128 ms: 1.06x faster                                           |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                          |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                          |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.05x faster                                          |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                           |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                           |
| chaos                      | 71.4 ms                                                               | 68.5 ms: 1.04x faster                                          |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.5 ms: 1.03x faster                                          |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                         |
| pickle_pure_python         | 365 us                                                                | 355 us: 1.03x faster                                           |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                         |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                           |
| deepcopy_reduce            | 4.10 us                                                               | 4.01 us: 1.02x faster                                          |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.02x faster                                          |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                           |
| mdp                        | 3.41 sec                                                              | 3.36 sec: 1.01x faster                                         |
| 2to3                       | 308 ms                                                                | 304 ms: 1.01x faster                                           |
| json                       | 5.54 ms                                                               | 5.47 ms: 1.01x faster                                          |
| float                      | 92.1 ms                                                               | 91.2 ms: 1.01x faster                                          |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                           |
| deepcopy                   | 446 us                                                                | 450 us: 1.01x slower                                           |
| bench_mp_pool              | 7.05 ms                                                               | 7.12 ms: 1.01x slower                                          |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                           |
| thrift                     | 937 us                                                                | 949 us: 1.01x slower                                           |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.01x slower                                           |
| xml_etree_process          | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                          |
| deepcopy_memo              | 49.6 us                                                               | 50.5 us: 1.02x slower                                          |
| html5lib                   | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                          |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                           |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                           |
| hexiom                     | 6.98 ms                                                               | 7.12 ms: 1.02x slower                                          |
| fannkuch                   | 443 ms                                                                | 453 ms: 1.02x slower                                           |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                           |
| json_loads                 | 30.7 us                                                               | 31.4 us: 1.02x slower                                          |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.02x slower                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.02x slower                                         |
| genshi_xml                 | 60.6 ms                                                               | 62.0 ms: 1.02x slower                                          |
| sqlglot_optimize           | 61.3 ms                                                               | 62.8 ms: 1.02x slower                                          |
| richards_super             | 58.5 ms                                                               | 59.9 ms: 1.02x slower                                          |
| asyncio_tcp                | 566 ms                                                                | 582 ms: 1.03x slower                                           |
| genshi_text                | 27.4 ms                                                               | 28.4 ms: 1.03x slower                                          |
| pprint_safe_repr           | 916 ms                                                                | 948 ms: 1.04x slower                                           |
| docutils                   | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                         |
| django_template            | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                          |
| chameleon                  | 8.81 ms                                                               | 9.16 ms: 1.04x slower                                          |
| richards                   | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                          |
| python_startup_no_site     | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                          |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.51 ms: 1.05x slower                                          |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                          |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                           |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                           |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                           |
| regex_effbot               | 4.64 ms                                                               | 4.98 ms: 1.07x slower                                          |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                           |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                           |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                           |
| regex_v8                   | 28.3 ms                                                               | 31.3 ms: 1.10x slower                                          |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                          |
| telco                      | 8.51 ms                                                               | 9.54 ms: 1.12x slower                                          |
| coverage                   | 87.3 ms                                                               | 97.9 ms: 1.12x slower                                          |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.15x slower                                          |
| gc_traversal               | 4.40 ms                                                               | 5.07 ms: 1.15x slower                                          |
| create_gc_cycles           | 1.92 ms                                                               | 2.34 ms: 1.22x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (10): sympy_integrate, dask, nqueens, regex_dna, pyflate, coroutines, async_generators, asyncio_websockets, xml_etree_parse, pylint
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, dulwich_log, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 83.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x