# Results vs. 3.12.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-aarch64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.01x faster
- HPT reliability: 80.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 305 ms: 1.01x faster                                                     |
| chameleon      | 8.81 ms                                                               | 9.12 ms: 1.03x slower                                                    |
| docutils       | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                                   |
| tornado_http   | 136 ms                                                                | 126 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.08 sec: 1.30x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.10 sec: 1.29x faster                                                   |
| async_tree_none            | 624 ms                                                                | 486 ms: 1.28x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 617 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 460 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 730 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 645 ms: 1.15x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| float          | 92.1 ms                                                               | 93.5 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 130 ms: 1.06x faster                                                     |
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| pickle_list          | 5.25 us                                                               | 5.30 us: 1.01x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                    |
| xml_etree_parse      | 195 ms                                                                | 200 ms: 1.02x slower                                                     |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.63 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                    |
| unpickle             | 18.5 us                                                               | 20.1 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_pure_python, pickle, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                    |
| python_startup         | 11.4 ms                                                               | 13.4 ms: 1.18x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                                    |
| django_template | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                                    |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.08 sec: 1.30x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.10 sec: 1.29x faster                                                   |
| async_tree_none            | 624 ms                                                                | 486 ms: 1.28x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 617 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 460 ms: 1.25x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 730 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                     |
| raytrace                   | 353 ms                                                                | 298 ms: 1.18x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.8 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 645 ms: 1.15x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.02 us: 1.09x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.08x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                    |
| tornado_http               | 136 ms                                                                | 126 ms: 1.08x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.79 us: 1.07x faster                                                    |
| dask                       | 376 ms                                                                | 352 ms: 1.07x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.37 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                                    |
| regex_compile              | 137 ms                                                                | 130 ms: 1.06x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 82.1 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.05x faster                                                     |
| chaos                      | 71.4 ms                                                               | 68.3 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                     |
| docutils                   | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.5 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                    |
| nqueens                    | 99.2 ms                                                               | 97.8 ms: 1.01x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| 2to3                       | 308 ms                                                                | 305 ms: 1.01x faster                                                     |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                     |
| pyflate                    | 559 ms                                                                | 561 ms: 1.00x slower                                                     |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                     |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 50.0 us: 1.01x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.30 us: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.05 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                    |
| deepcopy                   | 446 us                                                                | 451 us: 1.01x slower                                                     |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 930 ms: 1.02x slower                                                     |
| float                      | 92.1 ms                                                               | 93.5 ms: 1.02x slower                                                    |
| fannkuch                   | 443 ms                                                                | 451 ms: 1.02x slower                                                     |
| django_template            | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 200 ms: 1.02x slower                                                     |
| thrift                     | 937 us                                                                | 960 us: 1.02x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 62.9 ms: 1.03x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.87 us: 1.03x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 4.52 ms: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.70 ms: 1.03x slower                                                    |
| richards_super             | 58.5 ms                                                               | 60.3 ms: 1.03x slower                                                    |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                                    |
| go                         | 157 ms                                                                | 162 ms: 1.03x slower                                                     |
| chameleon                  | 8.81 ms                                                               | 9.12 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.52 ms: 1.05x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.8 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                     |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                     |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.63 us: 1.07x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                     |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.65 ms: 1.08x slower                                                    |
| gunicorn                   | 1.14 ms                                                               | 1.23 ms: 1.09x slower                                                    |
| unpickle                   | 18.5 us                                                               | 20.1 us: 1.09x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.13 ms: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.7 ms: 1.13x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.78 ms: 1.15x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.4 ms: 1.18x slower                                                    |
| mypy2                      | 873 ms                                                                | 1.18 sec: 1.35x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (15): pylint, xml_etree_iterparse, async_generators, pickle_pure_python, asyncio_tcp, genshi_xml, pickle, asyncio_tcp_ssl, xml_etree_process, asyncio_websockets, deepcopy_reduce, pycparser, xml_etree_generate, aiohttp, html5lib
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: bpe_tokeniser, flaskblogging, unpack_sequence

# HPT report

- Reliability score: 80.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x