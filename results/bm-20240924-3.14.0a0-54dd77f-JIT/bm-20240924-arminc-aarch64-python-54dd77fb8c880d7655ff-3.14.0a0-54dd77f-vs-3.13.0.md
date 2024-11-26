# Results vs. 3.13.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: linux-aarch64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.085x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 382 ms: 1.26x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.93 sec: 1.36x slower                                                  |
| html5lib       | 66.4 ms                                                  | 71.2 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                   | 146 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 561 ms: 1.16x faster                                                    |
| async_tree_none            | 497 ms                                                   | 440 ms: 1.13x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 588 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 435 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 746 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 749 ms: 1.02x faster                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                  |
| async_generators           | 489 ms                                                   | 510 ms: 1.04x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 87.4 ms: 1.07x faster                                                   |
| nbody          | 114 ms                                                   | 113 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.8 ms: 1.03x faster                                                   |
| regex_effbot   | 4.89 ms                                                  | 4.96 ms: 1.01x slower                                                   |
| regex_compile  | 127 ms                                                   | 194 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 109 ms: 1.04x faster                                                    |
| json_loads           | 31.7 us                                                  | 31.4 us: 1.01x faster                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.62 sec: 1.03x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 265 us: 1.06x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 404 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, json_dumps, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| django_template | 41.6 ms                                                  | 51.7 ms: 1.24x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 35.1 ms: 1.27x slower                                                   |
| genshi_xml      | 60.3 ms                                                  | 80.8 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.30 ms: 1.45x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 39.8 us: 1.26x faster                                                   |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 561 ms: 1.16x faster                                                    |
| async_tree_none            | 497 ms                                                   | 440 ms: 1.13x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 588 ms: 1.11x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.27 ms: 1.10x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 435 ms: 1.08x faster                                                    |
| deepcopy                   | 447 us                                                   | 417 us: 1.07x faster                                                    |
| float                      | 93.3 ms                                                  | 87.4 ms: 1.07x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.4 ms: 1.06x faster                                                   |
| scimark_sor                | 160 ms                                                   | 152 ms: 1.05x faster                                                    |
| xml_etree_generate         | 113 ms                                                   | 109 ms: 1.04x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.93 us: 1.04x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 30.8 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 746 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 749 ms: 1.02x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.53 ms: 1.02x faster                                                   |
| mako                       | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| nbody                      | 114 ms                                                   | 113 ms: 1.01x faster                                                    |
| json_loads                 | 31.7 us                                                  | 31.4 us: 1.01x faster                                                   |
| thrift                     | 968 us                                                   | 966 us: 1.00x faster                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 5.92 sec: 1.01x slower                                                  |
| logging_silent             | 133 ns                                                   | 135 ns: 1.01x slower                                                    |
| regex_effbot               | 4.89 ms                                                  | 4.96 ms: 1.01x slower                                                   |
| scimark_fft                | 447 ms                                                   | 458 ms: 1.02x slower                                                    |
| coverage                   | 99.1 ms                                                  | 102 ms: 1.03x slower                                                    |
| spectral_norm              | 143 ms                                                   | 147 ms: 1.03x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.62 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                  |
| mdp                        | 3.34 sec                                                 | 3.48 sec: 1.04x slower                                                  |
| async_generators           | 489 ms                                                   | 510 ms: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.81 ms: 1.05x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.34 ms: 1.05x slower                                                   |
| logging_format             | 7.82 us                                                  | 8.21 us: 1.05x slower                                                   |
| telco                      | 9.74 ms                                                  | 10.3 ms: 1.05x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                                  |
| unpickle_pure_python       | 251 us                                                   | 265 us: 1.06x slower                                                    |
| logging_simple             | 7.07 us                                                  | 7.53 us: 1.07x slower                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 89.4 ms: 1.07x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 71.2 ms: 1.07x slower                                                   |
| fannkuch                   | 461 ms                                                   | 505 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 213 us: 1.10x slower                                                    |
| meteor_contest             | 114 ms                                                   | 125 ms: 1.10x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 404 us: 1.13x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 95.3 ms: 1.14x slower                                                   |
| tornado_http               | 128 ms                                                   | 146 ms: 1.14x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 4.40 ms: 1.15x slower                                                   |
| raytrace                   | 300 ms                                                   | 346 ms: 1.16x slower                                                    |
| go                         | 160 ms                                                   | 189 ms: 1.18x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 151 ms: 1.19x slower                                                    |
| pyflate                    | 556 ms                                                   | 664 ms: 1.19x slower                                                    |
| comprehensions             | 20.4 us                                                  | 24.7 us: 1.21x slower                                                   |
| pycparser                  | 1.27 sec                                                 | 1.56 sec: 1.22x slower                                                  |
| django_template            | 41.6 ms                                                  | 51.7 ms: 1.24x slower                                                   |
| richards                   | 53.6 ms                                                  | 67.0 ms: 1.25x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.73 ms: 1.25x slower                                                   |
| 2to3                       | 304 ms                                                   | 382 ms: 1.26x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 78.3 ms: 1.26x slower                                                   |
| richards_super             | 60.1 ms                                                  | 75.9 ms: 1.26x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 35.1 ms: 1.27x slower                                                   |
| nqueens                    | 100 ms                                                   | 127 ms: 1.27x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 2.20 ms: 1.27x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 80.8 ms: 1.34x slower                                                   |
| sympy_expand               | 457 ms                                                   | 613 ms: 1.34x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.26 sec: 1.36x slower                                                  |
| chaos                      | 68.0 ms                                                  | 92.3 ms: 1.36x slower                                                   |
| docutils                   | 2.89 sec                                                 | 3.93 sec: 1.36x slower                                                  |
| sympy_integrate            | 20.8 ms                                                  | 28.5 ms: 1.37x slower                                                   |
| sympy_str                  | 264 ms                                                   | 366 ms: 1.39x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.64 sec: 1.39x slower                                                  |
| pylint                     | 342 ms                                                   | 477 ms: 1.40x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.2 ms: 1.44x slower                                                   |
| sympy_sum                  | 144 ms                                                   | 211 ms: 1.47x slower                                                    |
| generators                 | 37.6 ms                                                  | 57.0 ms: 1.52x slower                                                   |
| regex_compile              | 127 ms                                                   | 194 ms: 1.53x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (10): xml_etree_parse, json_dumps, json, python_startup_no_site, pidigits, regex_dna, asyncio_websockets, coroutines, xml_etree_process, xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.085x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.99x