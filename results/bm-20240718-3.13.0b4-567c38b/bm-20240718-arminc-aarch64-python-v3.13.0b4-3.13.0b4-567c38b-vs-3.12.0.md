# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b4
- machine: linux-aarch64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.016x faster
- HPT reliability: 87.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 8.81 ms                                                               | 8.93 ms: 1.01x slower                                        |
| docutils       | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                       |
| html5lib       | 65.1 ms                                                               | 66.6 ms: 1.02x slower                                        |
| tornado_http   | 136 ms                                                                | 127 ms: 1.06x faster                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 500 ms: 1.25x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 640 ms: 1.21x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 619 ms: 1.20x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 484 ms: 1.19x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.22 sec: 1.16x faster                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 785 ms: 1.13x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 817 ms: 1.12x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.18x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.6 ms: 1.00x faster                                        |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                         |
| nbody          | 105 ms                                                                | 110 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                         |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                        |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                         |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                       |
| pickle_pure_python   | 365 us                                                                | 358 us: 1.02x faster                                         |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                         |
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                         |
| xml_etree_generate   | 112 ms                                                                | 114 ms: 1.02x slower                                         |
| xml_etree_process    | 79.0 ms                                                               | 82.4 ms: 1.04x slower                                        |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                        |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                        |
| python_startup         | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.5 ms: 1.02x faster                                        |
| genshi_text     | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                        |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                        |
| django_template | 40.7 ms                                                               | 42.2 ms: 1.04x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 500 ms: 1.25x faster                                         |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                        |
| async_tree_memoization     | 777 ms                                                                | 640 ms: 1.21x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 619 ms: 1.20x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 484 ms: 1.19x faster                                         |
| raytrace                   | 353 ms                                                                | 299 ms: 1.18x faster                                         |
| generators                 | 43.5 ms                                                               | 37.3 ms: 1.17x faster                                        |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.22 sec: 1.16x faster                                       |
| mypy2                      | 873 ms                                                                | 766 ms: 1.14x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 785 ms: 1.13x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 817 ms: 1.12x faster                                         |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                         |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                         |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                        |
| logging_simple             | 7.63 us                                                               | 7.13 us: 1.07x faster                                        |
| logging_format             | 8.34 us                                                               | 7.81 us: 1.07x faster                                        |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                        |
| sqlglot_transpile          | 1.83 ms                                                               | 1.71 ms: 1.07x faster                                        |
| tornado_http               | 136 ms                                                                | 127 ms: 1.06x faster                                         |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                         |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.05x faster                                        |
| crypto_pyaes               | 86.6 ms                                                               | 82.5 ms: 1.05x faster                                        |
| dulwich_log                | 62.0 ms                                                               | 59.0 ms: 1.05x faster                                        |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                         |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.8 ms: 1.04x faster                                        |
| chaos                      | 71.4 ms                                                               | 68.9 ms: 1.04x faster                                        |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                         |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                        |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                       |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.03x faster                                       |
| pickle_pure_python         | 365 us                                                                | 358 us: 1.02x faster                                         |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                         |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                       |
| genshi_xml                 | 60.6 ms                                                               | 59.5 ms: 1.02x faster                                        |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                         |
| coroutines                 | 29.0 ms                                                               | 28.7 ms: 1.01x faster                                        |
| float                      | 92.1 ms                                                               | 91.6 ms: 1.00x faster                                        |
| asyncio_websockets         | 658 ms                                                                | 661 ms: 1.01x slower                                         |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                       |
| bench_mp_pool              | 7.05 ms                                                               | 7.14 ms: 1.01x slower                                        |
| genshi_text                | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                        |
| sqlglot_optimize           | 61.3 ms                                                               | 62.2 ms: 1.01x slower                                        |
| deepcopy                   | 446 us                                                                | 452 us: 1.01x slower                                         |
| chameleon                  | 8.81 ms                                                               | 8.93 ms: 1.01x slower                                        |
| sympy_expand               | 454 ms                                                                | 460 ms: 1.01x slower                                         |
| xml_etree_generate         | 112 ms                                                                | 114 ms: 1.02x slower                                         |
| deepcopy_memo              | 49.6 us                                                               | 50.4 us: 1.02x slower                                        |
| hexiom                     | 6.98 ms                                                               | 7.09 ms: 1.02x slower                                        |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                         |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                       |
| thrift                     | 937 us                                                                | 956 us: 1.02x slower                                         |
| html5lib                   | 65.1 ms                                                               | 66.6 ms: 1.02x slower                                        |
| docutils                   | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                       |
| asyncio_tcp                | 566 ms                                                                | 580 ms: 1.02x slower                                         |
| go                         | 157 ms                                                                | 161 ms: 1.03x slower                                         |
| richards_super             | 58.5 ms                                                               | 60.0 ms: 1.03x slower                                        |
| fannkuch                   | 443 ms                                                                | 455 ms: 1.03x slower                                         |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.03x slower                                         |
| pprint_safe_repr           | 916 ms                                                                | 941 ms: 1.03x slower                                         |
| json                       | 5.54 ms                                                               | 5.70 ms: 1.03x slower                                        |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                        |
| django_template            | 40.7 ms                                                               | 42.2 ms: 1.04x slower                                        |
| python_startup_no_site     | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 82.4 ms: 1.04x slower                                        |
| richards                   | 50.9 ms                                                               | 53.2 ms: 1.04x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.52 ms: 1.05x slower                                        |
| nbody                      | 105 ms                                                                | 110 ms: 1.05x slower                                         |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                        |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                        |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                         |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                         |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.07x slower                                         |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                         |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                         |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                        |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                        |
| gc_traversal               | 4.40 ms                                                               | 4.98 ms: 1.13x slower                                        |
| telco                      | 8.51 ms                                                               | 9.64 ms: 1.13x slower                                        |
| python_startup             | 11.4 ms                                                               | 12.9 ms: 1.14x slower                                        |
| coverage                   | 87.3 ms                                                               | 99.9 ms: 1.14x slower                                        |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (9): pylint, bench_thread_pool, regex_dna, async_generators, dask, 2to3, deepcopy_reduce, pyflate, nqueens
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b.json: bpe_tokeniser

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 87.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x