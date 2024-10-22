# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.02x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 296 ms: 1.03x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.02 sec: 1.04x slower                                                  |
| tornado_http   | 131 ms                                                   | 125 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_none            | 493 ms                                                   | 424 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 421 ms: 1.11x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 563 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 728 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 481 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.01x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_websockets, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| float          | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.6 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle           | 20.2 us                                                  | 19.5 us: 1.03x faster                                                   |
| pickle_list        | 5.34 us                                                  | 5.24 us: 1.02x faster                                                   |
| unpickle_list      | 6.65 us                                                  | 6.55 us: 1.02x faster                                                   |
| json_dumps         | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| pickle             | 13.5 us                                                  | 13.7 us: 1.02x slower                                                   |
| pickle_pure_python | 359 us                                                   | 366 us: 1.02x slower                                                    |
| tomli_loads        | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| Geometric mean     | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (7): xml_etree_generate, xml_etree_parse, pickle_dict, unpickle_pure_python, json_loads, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.63 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| mako           | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 329 us: 1.37x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 37.8 us: 1.35x faster                                                   |
| go                         | 163 ms                                                   | 138 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.48 us: 1.17x faster                                                   |
| async_tree_none            | 493 ms                                                   | 424 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 421 ms: 1.11x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 563 ms: 1.11x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 20.9 ms: 1.07x faster                                                   |
| tornado_http               | 131 ms                                                   | 125 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 728 ms: 1.05x faster                                                    |
| unpack_sequence            | 57.2 ns                                                  | 55.1 ns: 1.04x faster                                                   |
| unpickle                   | 20.2 us                                                  | 19.5 us: 1.03x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.03x faster                                                  |
| 2to3                       | 306 ms                                                   | 296 ms: 1.03x faster                                                    |
| async_generators           | 496 ms                                                   | 481 ms: 1.03x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.6 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.41 ms: 1.03x faster                                                   |
| logging_format             | 7.83 us                                                  | 7.63 us: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.02x faster                                                    |
| genshi_text                | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| nbody                      | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.14 ms: 1.02x faster                                                   |
| logging_silent             | 135 ns                                                   | 132 ns: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| pickle_list                | 5.34 us                                                  | 5.24 us: 1.02x faster                                                   |
| sympy_sum                  | 143 ms                                                   | 141 ms: 1.02x faster                                                    |
| unpickle_list              | 6.65 us                                                  | 6.55 us: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.01x faster                                                    |
| sympy_integrate            | 21.0 ms                                                  | 20.7 ms: 1.01x faster                                                   |
| thrift                     | 946 us                                                   | 933 us: 1.01x faster                                                    |
| float                      | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 8.63 ms: 1.01x faster                                                   |
| json_dumps                 | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 61.7 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 920 ms: 1.01x faster                                                    |
| mdp                        | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                                  |
| mako                       | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| sympy_expand               | 455 ms                                                   | 459 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 195 us: 1.01x slower                                                    |
| pyflate                    | 556 ms                                                   | 564 ms: 1.01x slower                                                    |
| pickle                     | 13.5 us                                                  | 13.7 us: 1.02x slower                                                   |
| fannkuch                   | 452 ms                                                   | 460 ms: 1.02x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 366 us: 1.02x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| deltablue                  | 3.85 ms                                                  | 3.94 ms: 1.02x slower                                                   |
| raytrace                   | 298 ms                                                   | 305 ms: 1.02x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.02 sec: 1.04x slower                                                  |
| sqlite_synth               | 3.84 us                                                  | 4.00 us: 1.04x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.44 ms: 1.05x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.28 ms: 1.07x slower                                                   |
| telco                      | 9.73 ms                                                  | 10.5 ms: 1.08x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 5.12 ms: 1.13x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (36): asyncio_tcp, json, meteor_contest, genshi_xml, scimark_sor, sqlglot_normalize, xml_etree_generate, richards, crypto_pyaes, logging_simple, richards_super, spectral_norm, nqueens, pprint_pformat, sympy_str, bpe_tokeniser, pidigits, scimark_monte_carlo, html5lib, xml_etree_parse, pickle_dict, asyncio_websockets, asyncio_tcp_ssl, django_template, coverage, regex_dna, unpickle_pure_python, json_loads, xml_etree_process, hexiom, comprehensions, chaos, regex_effbot, sqlglot_transpile, xml_etree_iterparse, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: dulwich_log

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x