# Results vs. 3.12.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.03x faster
- HPT reliability: 98.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                  |
| html5lib       | 65.1 ms                                                               | 63.1 ms: 1.03x faster                                                   |
| tornado_http   | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 549 ms: 1.35x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 109 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 361 us: 1.01x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 78.5 ms: 1.01x faster                                                   |
| pickle_dict          | 37.3 us                                                               | 37.5 us: 1.01x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.28 us: 1.02x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.83 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.47x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 416 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 549 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 332 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.1 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.45 us: 1.19x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| raytrace                   | 353 ms                                                                | 301 ms: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.0 ms: 1.17x faster                                                   |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.95 us: 1.10x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.62 us: 1.10x faster                                                   |
| tornado_http               | 136 ms                                                                | 124 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 58.8 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| 2to3                       | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.5 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 83.4 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.0 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 63.1 ms: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                                  |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 361 us: 1.01x faster                                                    |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 78.5 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.89 sec: 1.00x slower                                                  |
| pickle_dict                | 37.3 us                                                               | 37.5 us: 1.01x slower                                                   |
| float                      | 92.1 ms                                                               | 92.7 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| pyflate                    | 559 ms                                                                | 566 ms: 1.01x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.5 ms: 1.02x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.28 us: 1.02x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.05 sec: 1.02x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                  |
| sympy_expand               | 454 ms                                                                | 464 ms: 1.02x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.17 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.70 ms: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 456 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.38 ms: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.90 us: 1.03x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.8 ms: 1.04x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.04x slower                                                    |
| nbody                      | 105 ms                                                                | 109 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.83 ms: 1.06x slower                                                   |
| scimark_fft                | 418 ms                                                                | 443 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 192 us: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.91 ms: 1.12x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.5 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.99 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.30 ms: 1.20x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (15): thrift, nqueens, async_generators, bench_mp_pool, pprint_safe_repr, genshi_xml, meteor_contest, asyncio_websockets, genshi_text, pickle_list, pickle, sqlglot_normalize, pylint, asyncio_tcp, sqlglot_optimize
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 98.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x