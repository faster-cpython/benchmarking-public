# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.01x faster
- HPT reliability: 85.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 304 ms: 1.01x faster                                                     |
| chameleon      | 8.81 ms                                                               | 8.99 ms: 1.02x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                   |
| html5lib       | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                                    |
| tornado_http   | 136 ms                                                                | 127 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 487 ms: 1.28x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 604 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 473 ms: 1.22x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 647 ms: 1.20x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 781 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 763 ms: 1.16x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.1 ms: 1.01x faster                                                    |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                     |
| pickle_pure_python   | 365 us                                                                | 360 us: 1.01x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 37.6 us: 1.01x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.30 us: 1.01x slower                                                    |
| pickle               | 13.4 us                                                               | 13.6 us: 1.01x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 81.7 ms: 1.03x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.2 us: 1.05x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.48 us: 1.05x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.55 ms: 1.02x slower                                                    |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                    |
| django_template | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                    |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 487 ms: 1.28x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 604 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 473 ms: 1.22x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 647 ms: 1.20x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                                   |
| raytrace                   | 353 ms                                                                | 298 ms: 1.18x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 781 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 763 ms: 1.16x faster                                                     |
| mypy2                      | 873 ms                                                                | 764 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.01 us: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.73 us: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                    |
| tornado_http               | 136 ms                                                                | 127 ms: 1.07x faster                                                     |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.06x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 266 ms: 1.05x faster                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.7 ms: 1.04x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.7 ms: 1.04x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.26 ms: 1.04x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.03x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.5 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                   |
| dask                       | 376 ms                                                                | 369 ms: 1.02x faster                                                     |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                     |
| pickle_pure_python         | 365 us                                                                | 360 us: 1.01x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                     |
| 2to3                       | 308 ms                                                                | 304 ms: 1.01x faster                                                     |
| float                      | 92.1 ms                                                               | 91.1 ms: 1.01x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.06 us: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 37.6 us: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.30 us: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 926 ms: 1.01x slower                                                     |
| json                       | 5.54 ms                                                               | 5.60 ms: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.01x slower                                                    |
| thrift                     | 937 us                                                                | 951 us: 1.02x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                                    |
| fannkuch                   | 443 ms                                                                | 451 ms: 1.02x slower                                                     |
| sympy_expand               | 454 ms                                                                | 461 ms: 1.02x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.10 ms: 1.02x slower                                                    |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 8.99 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.55 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.7 ms: 1.02x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 50.8 us: 1.02x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                   |
| django_template            | 40.7 ms                                                               | 41.8 ms: 1.03x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 81.7 ms: 1.03x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.91 us: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.2 us: 1.05x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.48 us: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.56 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                     |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                     |
| richards_super             | 58.5 ms                                                               | 62.3 ms: 1.07x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                                     |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                    |
| gunicorn                   | 1.14 ms                                                               | 1.24 ms: 1.10x slower                                                    |
| richards                   | 50.9 ms                                                               | 55.9 ms: 1.10x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.3 ms: 1.13x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.87 ms: 1.16x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.22 ms: 1.19x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.20x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (13): pylint, nqueens, bench_mp_pool, pyflate, async_generators, genshi_xml, deepcopy, coroutines, asyncio_websockets, sqlglot_normalize, asyncio_tcp, aiohttp, xml_etree_generate
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging

# HPT report

- Reliability score: 85.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x