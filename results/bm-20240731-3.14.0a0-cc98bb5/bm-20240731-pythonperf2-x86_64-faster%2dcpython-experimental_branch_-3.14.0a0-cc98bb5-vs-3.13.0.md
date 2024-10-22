# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 283 ms: 1.03x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                                |
| html5lib       | 71.9 ms                                                      | 71.7 ms: 1.00x faster                                                                 |
| tornado_http   | 120 ms                                                       | 117 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 331 ms: 1.12x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 758 ms: 1.08x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 788 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 537 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                                  |
| async_generators           | 359 ms                                                       | 351 ms: 1.02x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 76.8 ms: 1.07x faster                                                                 |
| nbody          | 88.0 ms                                                      | 85.7 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| regex_v8       | 26.2 ms                                                      | 25.3 ms: 1.04x faster                                                                 |
| regex_dna      | 244 ms                                                       | 238 ms: 1.02x faster                                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.16 sec: 1.12x faster                                                                |
| unpickle_pure_python | 214 us                                                       | 205 us: 1.04x faster                                                                  |
| xml_etree_process    | 60.9 ms                                                      | 58.8 ms: 1.04x faster                                                                 |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                                 |
| xml_etree_parse      | 145 ms                                                       | 142 ms: 1.02x faster                                                                  |
| xml_etree_generate   | 85.3 ms                                                      | 84.4 ms: 1.01x faster                                                                 |
| json_loads           | 24.0 us                                                      | 25.7 us: 1.07x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 55.0 ms: 1.04x faster                                                                 |
| genshi_text     | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                                                 |
| django_template | 38.9 ms                                                      | 39.1 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 292 us: 1.36x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 30.5 us: 1.29x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                                  |
| generators                 | 33.5 ms                                                      | 28.1 ms: 1.19x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 331 ms: 1.12x faster                                                                  |
| tomli_loads                | 2.41 sec                                                     | 2.16 sec: 1.12x faster                                                                |
| richards_super             | 59.8 ms                                                      | 54.7 ms: 1.09x faster                                                                 |
| richards                   | 52.7 ms                                                      | 48.4 ms: 1.09x faster                                                                 |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                                 |
| raytrace                   | 289 ms                                                       | 267 ms: 1.08x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 758 ms: 1.08x faster                                                                  |
| telco                      | 8.58 ms                                                      | 7.97 ms: 1.08x faster                                                                 |
| pyflate                    | 492 ms                                                       | 458 ms: 1.07x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 788 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 537 ms: 1.07x faster                                                                  |
| float                      | 81.9 ms                                                      | 76.8 ms: 1.07x faster                                                                 |
| bench_thread_pool          | 901 us                                                       | 853 us: 1.06x faster                                                                  |
| scimark_sor                | 126 ms                                                       | 119 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 572 ms: 1.05x faster                                                                  |
| unpickle_pure_python       | 214 us                                                       | 205 us: 1.04x faster                                                                  |
| bpe_tokeniser              | 5.10 sec                                                     | 4.89 sec: 1.04x faster                                                                |
| genshi_xml                 | 57.3 ms                                                      | 55.0 ms: 1.04x faster                                                                 |
| logging_format             | 7.07 us                                                      | 6.80 us: 1.04x faster                                                                 |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| regex_v8                   | 26.2 ms                                                      | 25.3 ms: 1.04x faster                                                                 |
| xml_etree_process          | 60.9 ms                                                      | 58.8 ms: 1.04x faster                                                                 |
| genshi_text                | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                                                 |
| logging_simple             | 6.40 us                                                      | 6.18 us: 1.04x faster                                                                 |
| coverage                   | 81.1 ms                                                      | 78.7 ms: 1.03x faster                                                                 |
| scimark_lu                 | 97.8 ms                                                      | 95.0 ms: 1.03x faster                                                                 |
| 2to3                       | 291 ms                                                       | 283 ms: 1.03x faster                                                                  |
| nbody                      | 88.0 ms                                                      | 85.7 ms: 1.03x faster                                                                 |
| async_generators           | 359 ms                                                       | 351 ms: 1.02x faster                                                                  |
| regex_dna                  | 244 ms                                                       | 238 ms: 1.02x faster                                                                  |
| tornado_http               | 120 ms                                                       | 117 ms: 1.02x faster                                                                  |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                                 |
| logging_silent             | 97.7 ns                                                      | 95.6 ns: 1.02x faster                                                                 |
| xml_etree_parse            | 145 ms                                                       | 142 ms: 1.02x faster                                                                  |
| hexiom                     | 6.33 ms                                                      | 6.22 ms: 1.02x faster                                                                 |
| go                         | 160 ms                                                       | 158 ms: 1.02x faster                                                                  |
| scimark_fft                | 314 ms                                                       | 309 ms: 1.02x faster                                                                  |
| sympy_expand               | 505 ms                                                       | 496 ms: 1.02x faster                                                                  |
| sympy_str                  | 296 ms                                                       | 291 ms: 1.02x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                                  |
| sqlglot_optimize           | 59.7 ms                                                      | 59.0 ms: 1.01x faster                                                                 |
| xml_etree_generate         | 85.3 ms                                                      | 84.4 ms: 1.01x faster                                                                 |
| deltablue                  | 3.41 ms                                                      | 3.38 ms: 1.01x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 96.7 ms: 1.01x faster                                                                 |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.00x faster                                                                  |
| chaos                      | 61.7 ms                                                      | 61.4 ms: 1.00x faster                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.77 ms: 1.00x faster                                                                 |
| html5lib                   | 71.9 ms                                                      | 71.7 ms: 1.00x faster                                                                 |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.01x slower                                                                  |
| django_template            | 38.9 ms                                                      | 39.1 ms: 1.01x slower                                                                 |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 817 ms: 1.01x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                                |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                                 |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.1 ms: 1.02x slower                                                                 |
| mdp                        | 2.52 sec                                                     | 2.58 sec: 1.02x slower                                                                |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                                  |
| crypto_pyaes               | 72.8 ms                                                      | 74.7 ms: 1.03x slower                                                                 |
| nqueens                    | 88.2 ms                                                      | 91.1 ms: 1.03x slower                                                                 |
| typing_runtime_protocols   | 174 us                                                       | 180 us: 1.04x slower                                                                  |
| regex_effbot               | 3.37 ms                                                      | 3.51 ms: 1.04x slower                                                                 |
| json                       | 5.22 ms                                                      | 5.45 ms: 1.04x slower                                                                 |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.49 ms: 1.05x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                                |
| json_loads                 | 24.0 us                                                      | 25.7 us: 1.07x slower                                                                 |
| gc_traversal               | 4.11 ms                                                      | 4.49 ms: 1.09x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 1.94 ms: 1.11x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (13): dask, asyncio_tcp_ssl, pycparser, pidigits, fannkuch, thrift, sympy_integrate, pickle_pure_python, bench_mp_pool, sqlglot_parse, pylint, xml_etree_iterparse, mako
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x