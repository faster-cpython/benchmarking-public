# Results vs. 3.13.0b2

- fork: python
- ref: 0fb18b02c8ad56299d6a
- machine: linux-aarch64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.01x slower
- HPT reliability: 83.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 308 ms: 1.01x slower                                                  |
| chameleon      | 8.95 ms                                                      | 8.81 ms: 1.02x faster                                                 |
| docutils       | 3.10 sec                                                     | 2.98 sec: 1.04x faster                                                |
| html5lib       | 66.1 ms                                                      | 65.1 ms: 1.02x faster                                                 |
| tornado_http   | 128 ms                                                       | 136 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.40 sec: 1.10x slower                                                |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 912 ms: 1.15x slower                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.41 sec: 1.15x slower                                                |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 884 ms: 1.16x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 777 ms: 1.20x slower                                                  |
| async_tree_none_tg         | 476 ms                                                       | 577 ms: 1.21x slower                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 740 ms: 1.22x slower                                                  |
| async_tree_none            | 492 ms                                                       | 624 ms: 1.27x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.18x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 105 ms: 1.09x faster                                                  |
| pidigits       | 234 ms                                                       | 233 ms: 1.01x faster                                                  |
| float          | 91.4 ms                                                      | 92.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 28.3 ms: 1.10x faster                                                 |
| regex_effbot   | 4.98 ms                                                      | 4.64 ms: 1.07x faster                                                 |
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                  |
| regex_compile  | 128 ms                                                       | 137 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 18.5 us: 1.07x faster                                                 |
| json_dumps           | 13.1 ms                                                      | 12.3 ms: 1.07x faster                                                 |
| unpickle_list        | 6.52 us                                                      | 6.17 us: 1.06x faster                                                 |
| json_loads           | 32.1 us                                                      | 30.7 us: 1.05x faster                                                 |
| xml_etree_process    | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                 |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.01x faster                                                  |
| pickle_dict          | 37.6 us                                                      | 37.3 us: 1.01x faster                                                 |
| pickle_list          | 5.27 us                                                      | 5.25 us: 1.00x faster                                                 |
| tomli_loads          | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                |
| pickle_pure_python   | 359 us                                                       | 365 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.03x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 260 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (2): pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 11.4 ms: 1.14x faster                                                 |
| python_startup_no_site | 8.60 ms                                                      | 8.37 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 40.7 ms: 1.04x faster                                                 |
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| create_gc_cycles           | 2.33 ms                                                      | 1.92 ms: 1.22x faster                                                 |
| telco                      | 10.0 ms                                                      | 8.51 ms: 1.18x faster                                                 |
| gc_traversal               | 5.17 ms                                                      | 4.40 ms: 1.18x faster                                                 |
| python_startup             | 13.0 ms                                                      | 11.4 ms: 1.14x faster                                                 |
| coverage                   | 98.4 ms                                                      | 87.3 ms: 1.13x faster                                                 |
| richards                   | 55.9 ms                                                      | 50.9 ms: 1.10x faster                                                 |
| regex_v8                   | 31.1 ms                                                      | 28.3 ms: 1.10x faster                                                 |
| nbody                      | 114 ms                                                       | 105 ms: 1.09x faster                                                  |
| spectral_norm              | 141 ms                                                       | 131 ms: 1.08x faster                                                  |
| regex_effbot               | 4.98 ms                                                      | 4.64 ms: 1.07x faster                                                 |
| typing_runtime_protocols   | 193 us                                                       | 181 us: 1.07x faster                                                  |
| unpickle                   | 19.8 us                                                      | 18.5 us: 1.07x faster                                                 |
| json_dumps                 | 13.1 ms                                                      | 12.3 ms: 1.07x faster                                                 |
| richards_super             | 62.3 ms                                                      | 58.5 ms: 1.07x faster                                                 |
| scimark_sor                | 159 ms                                                       | 150 ms: 1.07x faster                                                  |
| scimark_fft                | 445 ms                                                       | 418 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.19 ms: 1.06x faster                                                 |
| unpickle_list              | 6.52 us                                                      | 6.17 us: 1.06x faster                                                 |
| logging_silent             | 133 ns                                                       | 127 ns: 1.05x faster                                                  |
| json_loads                 | 32.1 us                                                      | 30.7 us: 1.05x faster                                                 |
| gunicorn                   | 1.19 ms                                                      | 1.14 ms: 1.04x faster                                                 |
| django_template            | 42.3 ms                                                      | 40.7 ms: 1.04x faster                                                 |
| docutils                   | 3.10 sec                                                     | 2.98 sec: 1.04x faster                                                |
| sqlite_synth               | 3.90 us                                                      | 3.77 us: 1.04x faster                                                 |
| asyncio_tcp                | 584 ms                                                       | 566 ms: 1.03x faster                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.37 ms: 1.03x faster                                                 |
| thrift                     | 962 us                                                       | 937 us: 1.03x faster                                                  |
| pprint_pformat             | 1.93 sec                                                     | 1.88 sec: 1.03x faster                                                |
| xml_etree_process          | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                 |
| deepcopy_memo              | 50.8 us                                                      | 49.6 us: 1.02x faster                                                 |
| go                         | 161 ms                                                       | 157 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 61.3 ms: 1.02x faster                                                 |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                 |
| pprint_safe_repr           | 933 ms                                                       | 916 ms: 1.02x faster                                                  |
| json                       | 5.64 ms                                                      | 5.54 ms: 1.02x faster                                                 |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                  |
| fannkuch                   | 451 ms                                                       | 443 ms: 1.02x faster                                                  |
| aiohttp                    | 1.18 ms                                                      | 1.16 ms: 1.02x faster                                                 |
| chameleon                  | 8.95 ms                                                      | 8.81 ms: 1.02x faster                                                 |
| html5lib                   | 66.1 ms                                                      | 65.1 ms: 1.02x faster                                                 |
| hexiom                     | 7.08 ms                                                      | 6.98 ms: 1.01x faster                                                 |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.01x faster                                                  |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.19 sec: 1.01x faster                                                |
| sympy_expand               | 457 ms                                                       | 454 ms: 1.01x faster                                                  |
| pickle_dict                | 37.6 us                                                      | 37.3 us: 1.01x faster                                                 |
| pidigits                   | 234 ms                                                       | 233 ms: 1.01x faster                                                  |
| pickle_list                | 5.27 us                                                      | 5.25 us: 1.00x faster                                                 |
| float                      | 91.4 ms                                                      | 92.1 ms: 1.01x slower                                                 |
| tomli_loads                | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                |
| 2to3                       | 305 ms                                                       | 308 ms: 1.01x slower                                                  |
| deepcopy_reduce            | 4.04 us                                                      | 4.10 us: 1.02x slower                                                 |
| pickle_pure_python         | 359 us                                                       | 365 us: 1.02x slower                                                  |
| mdp                        | 3.33 sec                                                     | 3.41 sec: 1.03x slower                                                |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.03x slower                                                  |
| pycparser                  | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                                |
| scimark_lu                 | 141 ms                                                       | 146 ms: 1.03x slower                                                  |
| scimark_monte_carlo        | 82.3 ms                                                      | 85.1 ms: 1.03x slower                                                 |
| unpickle_pure_python       | 251 us                                                       | 260 us: 1.03x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 21.6 ms: 1.04x slower                                                 |
| bench_thread_pool          | 1.26 ms                                                      | 1.31 ms: 1.04x slower                                                 |
| chaos                      | 68.3 ms                                                      | 71.4 ms: 1.05x slower                                                 |
| sympy_str                  | 265 ms                                                       | 280 ms: 1.05x slower                                                  |
| crypto_pyaes               | 82.0 ms                                                      | 86.6 ms: 1.06x slower                                                 |
| tornado_http               | 128 ms                                                       | 136 ms: 1.06x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 62.0 ms: 1.06x slower                                                 |
| logging_simple             | 7.21 us                                                      | 7.63 us: 1.06x slower                                                 |
| deltablue                  | 3.88 ms                                                      | 4.12 ms: 1.06x slower                                                 |
| logging_format             | 7.82 us                                                      | 8.34 us: 1.07x slower                                                 |
| sqlglot_transpile          | 1.71 ms                                                      | 1.83 ms: 1.07x slower                                                 |
| regex_compile              | 128 ms                                                       | 137 ms: 1.07x slower                                                  |
| sympy_sum                  | 144 ms                                                       | 154 ms: 1.08x slower                                                  |
| pathlib                    | 22.8 ms                                                      | 24.5 ms: 1.08x slower                                                 |
| async_tree_io_tg           | 1.27 sec                                                     | 1.40 sec: 1.10x slower                                                |
| mypy2                      | 767 ms                                                       | 873 ms: 1.14x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 912 ms: 1.15x slower                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.41 sec: 1.15x slower                                                |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 884 ms: 1.16x slower                                                  |
| generators                 | 37.1 ms                                                      | 43.5 ms: 1.17x slower                                                 |
| raytrace                   | 297 ms                                                       | 353 ms: 1.19x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 777 ms: 1.20x slower                                                  |
| async_tree_none_tg         | 476 ms                                                       | 577 ms: 1.21x slower                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 740 ms: 1.22x slower                                                  |
| comprehensions             | 20.5 us                                                      | 25.4 us: 1.24x slower                                                 |
| async_tree_none            | 492 ms                                                       | 624 ms: 1.27x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (15): sqlglot_normalize, deepcopy, genshi_text, coroutines, asyncio_websockets, pickle, nqueens, bench_mp_pool, genshi_xml, pyflate, async_generators, dask, xml_etree_parse, sqlglot_parse, pylint
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, flaskblogging
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 83.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x