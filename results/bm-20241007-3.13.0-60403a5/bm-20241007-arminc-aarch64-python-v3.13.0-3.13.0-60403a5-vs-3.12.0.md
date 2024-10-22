# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-aarch64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 97.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 306 ms: 1.01x faster                                     |
| chameleon      | 8.81 ms                                                               | 9.02 ms: 1.02x slower                                    |
| docutils       | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.09 sec: 1.29x faster                                   |
| async_tree_io              | 1.41 sec                                                              | 1.11 sec: 1.28x faster                                   |
| async_tree_none            | 624 ms                                                                | 493 ms: 1.26x faster                                     |
| async_tree_memoization     | 777 ms                                                                | 626 ms: 1.24x faster                                     |
| async_tree_none_tg         | 577 ms                                                                | 467 ms: 1.23x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 736 ms: 1.20x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 764 ms: 1.19x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 649 ms: 1.14x faster                                     |
| Geometric mean             | (ref)                                                                 | 1.23x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 92.1 ms                                                               | 94.4 ms: 1.03x slower                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                     |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                     |
| regex_effbot   | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                    |
| regex_v8       | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                     |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.03x faster                                     |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                   |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                     |
| pickle_pure_python   | 365 us                                                                | 359 us: 1.02x faster                                     |
| pickle_list          | 5.25 us                                                               | 5.34 us: 1.02x slower                                    |
| pickle_dict          | 37.3 us                                                               | 38.1 us: 1.02x slower                                    |
| json_loads           | 30.7 us                                                               | 31.4 us: 1.02x slower                                    |
| unpickle_list        | 6.17 us                                                               | 6.65 us: 1.08x slower                                    |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                    |
| unpickle             | 18.5 us                                                               | 20.2 us: 1.09x slower                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                             |

Benchmark hidden because not significant (3): pickle, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                    |
| python_startup         | 11.4 ms                                                               | 13.3 ms: 1.17x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 60.2 ms: 1.01x faster                                    |
| genshi_text     | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                    |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                    |
| django_template | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.09 sec: 1.29x faster                                   |
| async_tree_io              | 1.41 sec                                                              | 1.11 sec: 1.28x faster                                   |
| async_tree_none            | 624 ms                                                                | 493 ms: 1.26x faster                                     |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.25x faster                                    |
| async_tree_memoization     | 777 ms                                                                | 626 ms: 1.24x faster                                     |
| async_tree_none_tg         | 577 ms                                                                | 467 ms: 1.23x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 736 ms: 1.20x faster                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 764 ms: 1.19x faster                                     |
| raytrace                   | 353 ms                                                                | 298 ms: 1.19x faster                                     |
| generators                 | 43.5 ms                                                               | 37.8 ms: 1.15x faster                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 649 ms: 1.14x faster                                     |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.10x faster                                    |
| logging_simple             | 7.63 us                                                               | 7.04 us: 1.08x faster                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                     |
| dask                       | 376 ms                                                                | 350 ms: 1.07x faster                                     |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                    |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                     |
| logging_format             | 8.34 us                                                               | 7.83 us: 1.07x faster                                    |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.38 ms: 1.06x faster                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                    |
| crypto_pyaes               | 86.6 ms                                                               | 82.7 ms: 1.05x faster                                    |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.04x faster                                     |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                     |
| chaos                      | 71.4 ms                                                               | 68.8 ms: 1.04x faster                                    |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                     |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                    |
| coroutines                 | 29.0 ms                                                               | 28.2 ms: 1.03x faster                                    |
| docutils                   | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                   |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.03x faster                                     |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.03x faster                                    |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                     |
| pickle_pure_python         | 365 us                                                                | 359 us: 1.02x faster                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.8 ms: 1.01x faster                                    |
| mdp                        | 3.41 sec                                                              | 3.36 sec: 1.01x faster                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.07 us: 1.01x faster                                    |
| 2to3                       | 308 ms                                                                | 306 ms: 1.01x faster                                     |
| genshi_xml                 | 60.6 ms                                                               | 60.2 ms: 1.01x faster                                    |
| pyflate                    | 559 ms                                                                | 556 ms: 1.01x faster                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                   |
| thrift                     | 937 us                                                                | 946 us: 1.01x slower                                     |
| genshi_text                | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                    |
| pprint_safe_repr           | 916 ms                                                                | 926 ms: 1.01x slower                                     |
| async_generators           | 491 ms                                                                | 496 ms: 1.01x slower                                     |
| deepcopy                   | 446 us                                                                | 451 us: 1.01x slower                                     |
| json                       | 5.54 ms                                                               | 5.61 ms: 1.01x slower                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 62.4 ms: 1.02x slower                                    |
| pickle_list                | 5.25 us                                                               | 5.34 us: 1.02x slower                                    |
| fannkuch                   | 443 ms                                                                | 452 ms: 1.02x slower                                     |
| sqlite_synth               | 3.77 us                                                               | 3.84 us: 1.02x slower                                    |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                     |
| pickle_dict                | 37.3 us                                                               | 38.1 us: 1.02x slower                                    |
| hexiom                     | 6.98 ms                                                               | 7.13 ms: 1.02x slower                                    |
| chameleon                  | 8.81 ms                                                               | 9.02 ms: 1.02x slower                                    |
| json_loads                 | 30.7 us                                                               | 31.4 us: 1.02x slower                                    |
| float                      | 92.1 ms                                                               | 94.4 ms: 1.03x slower                                    |
| deepcopy_memo              | 49.6 us                                                               | 51.0 us: 1.03x slower                                    |
| gc_traversal               | 4.40 ms                                                               | 4.53 ms: 1.03x slower                                    |
| richards_super             | 58.5 ms                                                               | 60.3 ms: 1.03x slower                                    |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                    |
| go                         | 157 ms                                                                | 163 ms: 1.03x slower                                     |
| bench_mp_pool              | 7.05 ms                                                               | 7.30 ms: 1.03x slower                                    |
| django_template            | 40.7 ms                                                               | 42.3 ms: 1.04x slower                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.75 ms: 1.05x slower                                    |
| regex_effbot               | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                    |
| richards                   | 50.9 ms                                                               | 53.5 ms: 1.05x slower                                    |
| gunicorn                   | 1.14 ms                                                               | 1.20 ms: 1.06x slower                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.58 ms: 1.06x slower                                    |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                     |
| typing_runtime_protocols   | 181 us                                                                | 192 us: 1.06x slower                                     |
| logging_silent             | 127 ns                                                                | 135 ns: 1.07x slower                                     |
| scimark_fft                | 418 ms                                                                | 447 ms: 1.07x slower                                     |
| unpickle_list              | 6.17 us                                                               | 6.65 us: 1.08x slower                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                     |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                     |
| unpickle                   | 18.5 us                                                               | 20.2 us: 1.09x slower                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.12 ms: 1.11x slower                                    |
| regex_v8                   | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                    |
| coverage                   | 87.3 ms                                                               | 98.5 ms: 1.13x slower                                    |
| telco                      | 8.51 ms                                                               | 9.73 ms: 1.14x slower                                    |
| python_startup             | 11.4 ms                                                               | 13.3 ms: 1.17x slower                                    |
| mypy2                      | 873 ms                                                                | 1.18 sec: 1.35x slower                                   |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                             |

Benchmark hidden because not significant (14): pylint, tornado_http, html5lib, nqueens, asyncio_websockets, asyncio_tcp_ssl, sympy_expand, asyncio_tcp, pickle, pycparser, pidigits, xml_etree_generate, xml_etree_process, aiohttp
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, flaskblogging, unpack_sequence

# HPT report

- Reliability score: 97.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x