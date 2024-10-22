# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                                  |
| tornado_http   | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 417 ms: 1.18x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 555 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 417 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 722 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 716 ms: 1.03x faster                                                    |
| async_generators           | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 556 ms: 1.02x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| float          | 94.4 ms                                                  | 92.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| json_dumps          | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| xml_etree_iterparse | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (10): xml_etree_generate, pickle_list, unpickle_list, xml_etree_process, unpickle_pure_python, pickle_dict, json_loads, pickle_pure_python, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.57 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 26.9 ms: 1.03x faster                                                   |
| django_template | 42.3 ms                                                  | 41.5 ms: 1.02x faster                                                   |
| mako            | 13.3 ms                                                  | 13.5 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.6 us: 1.36x faster                                                   |
| deepcopy                   | 451 us                                                   | 334 us: 1.35x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                    |
| go                         | 163 ms                                                   | 138 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 417 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.48 us: 1.17x faster                                                   |
| async_tree_memoization     | 626 ms                                                   | 555 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 417 ms: 1.12x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 20.9 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 722 ms: 1.06x faster                                                    |
| tornado_http               | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| unpickle                   | 20.2 us                                                  | 19.4 us: 1.04x faster                                                   |
| 2to3                       | 306 ms                                                   | 295 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| logging_format             | 7.83 us                                                  | 7.56 us: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| genshi_text                | 27.7 ms                                                  | 26.9 ms: 1.03x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 716 ms: 1.03x faster                                                    |
| regex_compile              | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| python_startup             | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| richards_super             | 60.3 ms                                                  | 58.9 ms: 1.02x faster                                                   |
| sympy_sum                  | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| async_generators           | 496 ms                                                   | 485 ms: 1.02x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 556 ms: 1.02x faster                                                    |
| logging_simple             | 7.04 us                                                  | 6.89 us: 1.02x faster                                                   |
| richards                   | 53.5 ms                                                  | 52.4 ms: 1.02x faster                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 8.57 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.2 ms: 1.02x faster                                                   |
| thrift                     | 946 us                                                   | 928 us: 1.02x faster                                                    |
| json_dumps                 | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| django_template            | 42.3 ms                                                  | 41.5 ms: 1.02x faster                                                   |
| logging_silent             | 135 ns                                                   | 133 ns: 1.02x faster                                                    |
| float                      | 94.4 ms                                                  | 92.9 ms: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 443 ms: 1.01x faster                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.85 sec: 1.01x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| sympy_expand               | 455 ms                                                   | 460 ms: 1.01x slower                                                    |
| fannkuch                   | 452 ms                                                   | 458 ms: 1.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.01x slower                                                   |
| pyflate                    | 556 ms                                                   | 564 ms: 1.01x slower                                                    |
| mako                       | 13.3 ms                                                  | 13.5 ms: 1.02x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 100 ms: 1.02x slower                                                    |
| raytrace                   | 298 ms                                                   | 303 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 196 us: 1.02x slower                                                    |
| telco                      | 9.73 ms                                                  | 9.97 ms: 1.02x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| unpack_sequence            | 57.2 ns                                                  | 60.0 ns: 1.05x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.28 ms: 1.07x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.13 ms: 1.13x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (35): xml_etree_generate, bench_mp_pool, sqlglot_normalize, sympy_integrate, json, scimark_sor, pickle_list, hexiom, pprint_safe_repr, unpickle_list, mdp, crypto_pyaes, genshi_xml, scimark_sparse_mat_mult, sqlglot_transpile, pprint_pformat, chaos, xml_etree_process, sympy_str, pidigits, coverage, unpickle_pure_python, regex_dna, pickle_dict, json_loads, pickle_pure_python, pickle, spectral_norm, sqlite_synth, deltablue, regex_effbot, sqlglot_optimize, xml_etree_parse, html5lib, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: dulwich_log

# HPT report

- Reliability score: 99.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x