# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.01x faster
- HPT reliability: 83.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 305 ms: 1.01x faster                                         |
| chameleon      | 8.81 ms                                                               | 8.95 ms: 1.02x slower                                        |
| docutils       | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                       |
| html5lib       | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                        |
| tornado_http   | 136 ms                                                                | 128 ms: 1.06x faster                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 492 ms: 1.27x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 604 ms: 1.22x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 645 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 763 ms: 1.16x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.15x faster                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 791 ms: 1.15x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.10x faster                                       |
| Geometric mean             | (ref)                                                                 | 1.18x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.4 ms: 1.01x faster                                        |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                         |
| regex_dna      | 254 ms                                                                | 259 ms: 1.02x slower                                         |
| regex_effbot   | 4.64 ms                                                               | 4.98 ms: 1.07x slower                                        |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 251 us: 1.03x faster                                         |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.03x faster                                         |
| pickle_pure_python   | 365 us                                                                | 359 us: 1.02x faster                                         |
| tomli_loads          | 2.59 sec                                                              | 2.57 sec: 1.01x faster                                       |
| pickle_list          | 5.25 us                                                               | 5.27 us: 1.00x slower                                        |
| pickle_dict          | 37.3 us                                                               | 37.6 us: 1.01x slower                                        |
| xml_etree_generate   | 112 ms                                                                | 114 ms: 1.01x slower                                         |
| xml_etree_process    | 79.0 ms                                                               | 80.8 ms: 1.02x slower                                        |
| json_loads           | 30.7 us                                                               | 32.1 us: 1.05x slower                                        |
| unpickle_list        | 6.17 us                                                               | 6.52 us: 1.06x slower                                        |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                        |
| unpickle             | 18.5 us                                                               | 19.8 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                        |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                        |
| django_template | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 492 ms: 1.27x faster                                         |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 604 ms: 1.22x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 645 ms: 1.20x faster                                         |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                         |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 763 ms: 1.16x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.15x faster                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 791 ms: 1.15x faster                                         |
| mypy2                      | 873 ms                                                                | 767 ms: 1.14x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.10x faster                                       |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                        |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.08x faster                                         |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                         |
| sqlglot_transpile          | 1.83 ms                                                               | 1.71 ms: 1.07x faster                                        |
| logging_format             | 8.34 us                                                               | 7.82 us: 1.07x faster                                        |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                        |
| logging_simple             | 7.63 us                                                               | 7.21 us: 1.06x faster                                        |
| dulwich_log                | 62.0 ms                                                               | 58.5 ms: 1.06x faster                                        |
| tornado_http               | 136 ms                                                                | 128 ms: 1.06x faster                                         |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                        |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.05x faster                                         |
| chaos                      | 71.4 ms                                                               | 68.3 ms: 1.05x faster                                        |
| bench_thread_pool          | 1.31 ms                                                               | 1.26 ms: 1.04x faster                                        |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.04x faster                                        |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.03x faster                                         |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                        |
| scimark_lu                 | 146 ms                                                                | 141 ms: 1.03x faster                                         |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                       |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.03x faster                                         |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                       |
| pickle_pure_python         | 365 us                                                                | 359 us: 1.02x faster                                         |
| deepcopy_reduce            | 4.10 us                                                               | 4.04 us: 1.02x faster                                        |
| 2to3                       | 308 ms                                                                | 305 ms: 1.01x faster                                         |
| tomli_loads                | 2.59 sec                                                              | 2.57 sec: 1.01x faster                                       |
| float                      | 92.1 ms                                                               | 91.4 ms: 1.01x faster                                        |
| pickle_list                | 5.25 us                                                               | 5.27 us: 1.00x slower                                        |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| pickle_dict                | 37.3 us                                                               | 37.6 us: 1.01x slower                                        |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                       |
| xml_etree_generate         | 112 ms                                                                | 114 ms: 1.01x slower                                         |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                         |
| hexiom                     | 6.98 ms                                                               | 7.08 ms: 1.01x slower                                        |
| html5lib                   | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                        |
| chameleon                  | 8.81 ms                                                               | 8.95 ms: 1.02x slower                                        |
| aiohttp                    | 1.16 ms                                                               | 1.18 ms: 1.02x slower                                        |
| fannkuch                   | 443 ms                                                                | 451 ms: 1.02x slower                                         |
| regex_dna                  | 254 ms                                                                | 259 ms: 1.02x slower                                         |
| json                       | 5.54 ms                                                               | 5.64 ms: 1.02x slower                                        |
| pprint_safe_repr           | 916 ms                                                                | 933 ms: 1.02x slower                                         |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                        |
| sqlglot_optimize           | 61.3 ms                                                               | 62.6 ms: 1.02x slower                                        |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                         |
| deepcopy_memo              | 49.6 us                                                               | 50.8 us: 1.02x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 80.8 ms: 1.02x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.03x slower                                       |
| thrift                     | 937 us                                                                | 962 us: 1.03x slower                                         |
| python_startup_no_site     | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                        |
| asyncio_tcp                | 566 ms                                                                | 584 ms: 1.03x slower                                         |
| sqlite_synth               | 3.77 us                                                               | 3.90 us: 1.04x slower                                        |
| docutils                   | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                       |
| django_template            | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                        |
| gunicorn                   | 1.14 ms                                                               | 1.19 ms: 1.04x slower                                        |
| json_loads                 | 30.7 us                                                               | 32.1 us: 1.05x slower                                        |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                         |
| unpickle_list              | 6.17 us                                                               | 6.52 us: 1.06x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.55 ms: 1.06x slower                                        |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                         |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.07x slower                                         |
| richards_super             | 58.5 ms                                                               | 62.3 ms: 1.07x slower                                        |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                        |
| unpickle                   | 18.5 us                                                               | 19.8 us: 1.07x slower                                        |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                         |
| regex_effbot               | 4.64 ms                                                               | 4.98 ms: 1.07x slower                                        |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                         |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                         |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                        |
| richards                   | 50.9 ms                                                               | 55.9 ms: 1.10x slower                                        |
| coverage                   | 87.3 ms                                                               | 98.4 ms: 1.13x slower                                        |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                        |
| gc_traversal               | 4.40 ms                                                               | 5.17 ms: 1.18x slower                                        |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                        |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.22x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (15): pylint, sqlglot_parse, xml_etree_parse, dask, async_generators, pyflate, genshi_xml, bench_mp_pool, nqueens, pickle, asyncio_websockets, coroutines, genshi_text, deepcopy, sqlglot_normalize
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, flaskblogging

# HPT report

- Reliability score: 83.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x