# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc3
- machine: linux-aarch64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.021x faster
- HPT reliability: 95.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                           |
| chameleon      | 8.81 ms                                                               | 9.05 ms: 1.03x slower                                          |
| docutils       | 2.98 sec                                                              | 2.88 sec: 1.03x faster                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.08 sec: 1.30x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.11 sec: 1.28x faster                                         |
| async_tree_none            | 624 ms                                                                | 489 ms: 1.27x faster                                           |
| async_tree_memoization     | 777 ms                                                                | 614 ms: 1.26x faster                                           |
| async_tree_none_tg         | 577 ms                                                                | 464 ms: 1.24x faster                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 726 ms: 1.22x faster                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 761 ms: 1.20x faster                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 643 ms: 1.15x faster                                           |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                           |
| float          | 92.1 ms                                                               | 93.7 ms: 1.02x slower                                          |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                           |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                          |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                           |
| tomli_loads          | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                         |
| unpickle_pure_python | 260 us                                                                | 256 us: 1.01x faster                                           |
| pickle               | 13.4 us                                                               | 13.5 us: 1.01x slower                                          |
| json_loads           | 30.7 us                                                               | 31.3 us: 1.02x slower                                          |
| pickle_dict          | 37.3 us                                                               | 38.1 us: 1.02x slower                                          |
| pickle_list          | 5.25 us                                                               | 5.36 us: 1.02x slower                                          |
| unpickle             | 18.5 us                                                               | 20.0 us: 1.08x slower                                          |
| json_dumps           | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                          |
| unpickle_list        | 6.17 us                                                               | 6.92 us: 1.12x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                   |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                          |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                          |
| django_template | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                          |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.08 sec: 1.30x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.11 sec: 1.28x faster                                         |
| async_tree_none            | 624 ms                                                                | 489 ms: 1.27x faster                                           |
| async_tree_memoization     | 777 ms                                                                | 614 ms: 1.26x faster                                           |
| async_tree_none_tg         | 577 ms                                                                | 464 ms: 1.24x faster                                           |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                          |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 726 ms: 1.22x faster                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 761 ms: 1.20x faster                                           |
| raytrace                   | 353 ms                                                                | 296 ms: 1.19x faster                                           |
| generators                 | 43.5 ms                                                               | 37.8 ms: 1.15x faster                                          |
| async_tree_memoization_tg  | 740 ms                                                                | 643 ms: 1.15x faster                                           |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                           |
| logging_format             | 8.34 us                                                               | 7.67 us: 1.09x faster                                          |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                          |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                          |
| deltablue                  | 4.12 ms                                                               | 3.82 ms: 1.08x faster                                          |
| dask                       | 376 ms                                                                | 350 ms: 1.07x faster                                           |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                           |
| sqlglot_parse              | 1.46 ms                                                               | 1.38 ms: 1.06x faster                                          |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                          |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                           |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                          |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                          |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                           |
| docutils                   | 2.98 sec                                                              | 2.88 sec: 1.03x faster                                         |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                          |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                          |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                           |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.7 ms: 1.03x faster                                          |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                         |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                          |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                         |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                           |
| unpickle_pure_python       | 260 us                                                                | 256 us: 1.01x faster                                           |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                           |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                         |
| pickle                     | 13.4 us                                                               | 13.5 us: 1.01x slower                                          |
| hexiom                     | 6.98 ms                                                               | 7.04 ms: 1.01x slower                                          |
| sympy_expand               | 454 ms                                                                | 458 ms: 1.01x slower                                           |
| thrift                     | 937 us                                                                | 947 us: 1.01x slower                                           |
| pprint_safe_repr           | 916 ms                                                                | 928 ms: 1.01x slower                                           |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.01x slower                                           |
| float                      | 92.1 ms                                                               | 93.7 ms: 1.02x slower                                          |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                          |
| fannkuch                   | 443 ms                                                                | 452 ms: 1.02x slower                                           |
| json_loads                 | 30.7 us                                                               | 31.3 us: 1.02x slower                                          |
| django_template            | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                          |
| pickle_dict                | 37.3 us                                                               | 38.1 us: 1.02x slower                                          |
| pickle_list                | 5.25 us                                                               | 5.36 us: 1.02x slower                                          |
| sqlglot_optimize           | 61.3 ms                                                               | 62.9 ms: 1.03x slower                                          |
| chameleon                  | 8.81 ms                                                               | 9.05 ms: 1.03x slower                                          |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                          |
| deepcopy                   | 446 us                                                                | 459 us: 1.03x slower                                           |
| gunicorn                   | 1.14 ms                                                               | 1.17 ms: 1.03x slower                                          |
| gc_traversal               | 4.40 ms                                                               | 4.56 ms: 1.04x slower                                          |
| go                         | 157 ms                                                                | 163 ms: 1.04x slower                                           |
| bench_mp_pool              | 7.05 ms                                                               | 7.33 ms: 1.04x slower                                          |
| sqlite_synth               | 3.77 us                                                               | 3.92 us: 1.04x slower                                          |
| deepcopy_memo              | 49.6 us                                                               | 51.7 us: 1.04x slower                                          |
| python_startup_no_site     | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                          |
| richards_super             | 58.5 ms                                                               | 61.1 ms: 1.04x slower                                          |
| richards                   | 50.9 ms                                                               | 53.6 ms: 1.05x slower                                          |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                           |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                          |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.54 ms: 1.06x slower                                          |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                           |
| scimark_fft                | 418 ms                                                                | 447 ms: 1.07x slower                                           |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                          |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                           |
| unpickle                   | 18.5 us                                                               | 20.0 us: 1.08x slower                                          |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                           |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                           |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                          |
| create_gc_cycles           | 1.92 ms                                                               | 2.14 ms: 1.12x slower                                          |
| unpickle_list              | 6.17 us                                                               | 6.92 us: 1.12x slower                                          |
| coverage                   | 87.3 ms                                                               | 98.0 ms: 1.12x slower                                          |
| telco                      | 8.51 ms                                                               | 9.69 ms: 1.14x slower                                          |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                          |
| mypy2                      | 873 ms                                                                | 1.18 sec: 1.35x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (20): pylint, tornado_http, xml_etree_parse, regex_dna, pickle_pure_python, nqueens, html5lib, xml_etree_generate, json, asyncio_tcp, pycparser, aiohttp, asyncio_tcp_ssl, asyncio_websockets, async_generators, pyflate, deepcopy_reduce, genshi_xml, meteor_contest, xml_etree_process
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: bpe_tokeniser, flaskblogging, unpack_sequence

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 95.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x