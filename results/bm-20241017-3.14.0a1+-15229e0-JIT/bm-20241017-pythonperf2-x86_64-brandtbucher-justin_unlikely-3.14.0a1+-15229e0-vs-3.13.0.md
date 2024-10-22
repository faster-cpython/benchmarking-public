# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.08x slower
- HPT reliability: 59.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 317 ms: 1.09x slower                                                          |
| docutils       | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                        |
| html5lib       | 71.9 ms                                                      | 70.3 ms: 1.02x faster                                                         |
| tornado_http   | 120 ms                                                       | 124 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 373 ms: 1.24x faster                                                          |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                          |
| async_tree_memoization     | 452 ms                                                       | 408 ms: 1.11x faster                                                          |
| async_tree_none_tg         | 340 ms                                                       | 320 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                          |
| async_tree_io              | 847 ms                                                       | 821 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                                          |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 857 ms: 1.05x slower                                                          |
| async_generators           | 359 ms                                                       | 380 ms: 1.06x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 78.7 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 84.6 ms: 1.04x faster                                                         |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 231 ms: 1.06x faster                                                          |
| regex_v8       | 26.2 ms                                                      | 24.9 ms: 1.05x faster                                                         |
| regex_effbot   | 3.37 ms                                                      | 3.42 ms: 1.01x slower                                                         |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                        |
| xml_etree_process    | 60.9 ms                                                      | 56.9 ms: 1.07x faster                                                         |
| xml_etree_generate   | 85.3 ms                                                      | 81.4 ms: 1.05x faster                                                         |
| unpickle             | 15.1 us                                                      | 14.8 us: 1.03x faster                                                         |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                          |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                         |
| json_dumps           | 11.0 ms                                                      | 11.1 ms: 1.02x slower                                                         |
| pickle_dict          | 32.1 us                                                      | 32.9 us: 1.02x slower                                                         |
| unpickle_pure_python | 214 us                                                       | 223 us: 1.04x slower                                                          |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                          |
| unpickle_list        | 4.62 us                                                      | 4.90 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                  |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.02 ms: 1.01x slower                                                         |
| python_startup         | 13.3 ms                                                      | 15.0 ms: 1.13x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.57 ms: 1.09x faster                                                         |
| genshi_text     | 26.6 ms                                                      | 28.8 ms: 1.08x slower                                                         |
| django_template | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                         |
| genshi_xml      | 57.3 ms                                                      | 63.0 ms: 1.10x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 29.7 us: 1.33x faster                                                         |
| deepcopy                   | 397 us                                                       | 319 us: 1.24x faster                                                          |
| async_tree_memoization_tg  | 461 ms                                                       | 373 ms: 1.24x faster                                                          |
| scimark_sor                | 126 ms                                                       | 104 ms: 1.21x faster                                                          |
| richards_super             | 59.8 ms                                                      | 49.8 ms: 1.20x faster                                                         |
| richards                   | 52.7 ms                                                      | 44.5 ms: 1.19x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 3.11 us: 1.14x faster                                                         |
| tomli_loads                | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                        |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                          |
| telco                      | 8.58 ms                                                      | 7.74 ms: 1.11x faster                                                         |
| async_tree_memoization     | 452 ms                                                       | 408 ms: 1.11x faster                                                          |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                         |
| scimark_fft                | 314 ms                                                       | 288 ms: 1.09x faster                                                          |
| mako                       | 10.4 ms                                                      | 9.57 ms: 1.09x faster                                                         |
| pyflate                    | 492 ms                                                       | 460 ms: 1.07x faster                                                          |
| xml_etree_process          | 60.9 ms                                                      | 56.9 ms: 1.07x faster                                                         |
| logging_silent             | 97.7 ns                                                      | 91.4 ns: 1.07x faster                                                         |
| bpe_tokeniser              | 5.10 sec                                                     | 4.77 sec: 1.07x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 320 ms: 1.06x faster                                                          |
| regex_dna                  | 244 ms                                                       | 231 ms: 1.06x faster                                                          |
| regex_v8                   | 26.2 ms                                                      | 24.9 ms: 1.05x faster                                                         |
| xml_etree_generate         | 85.3 ms                                                      | 81.4 ms: 1.05x faster                                                         |
| spectral_norm              | 97.4 ms                                                      | 93.3 ms: 1.04x faster                                                         |
| float                      | 81.9 ms                                                      | 78.7 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                          |
| nbody                      | 88.0 ms                                                      | 84.6 ms: 1.04x faster                                                         |
| json                       | 5.22 ms                                                      | 5.03 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.79 us                                                      | 2.69 us: 1.03x faster                                                         |
| deltablue                  | 3.41 ms                                                      | 3.30 ms: 1.03x faster                                                         |
| scimark_lu                 | 97.8 ms                                                      | 94.7 ms: 1.03x faster                                                         |
| async_tree_io              | 847 ms                                                       | 821 ms: 1.03x faster                                                          |
| pprint_safe_repr           | 812 ms                                                       | 788 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 559 ms: 1.03x faster                                                          |
| unpickle                   | 15.1 us                                                      | 14.8 us: 1.03x faster                                                         |
| go                         | 160 ms                                                       | 156 ms: 1.03x faster                                                          |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.02x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 70.3 ms: 1.02x faster                                                         |
| crypto_pyaes               | 72.8 ms                                                      | 71.4 ms: 1.02x faster                                                         |
| coverage                   | 81.1 ms                                                      | 79.8 ms: 1.02x faster                                                         |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                          |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                          |
| dulwich_log                | 65.5 ms                                                      | 65.0 ms: 1.01x faster                                                         |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                          |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                                        |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                         |
| python_startup_no_site     | 8.94 ms                                                      | 9.02 ms: 1.01x slower                                                         |
| regex_effbot               | 3.37 ms                                                      | 3.42 ms: 1.01x slower                                                         |
| json_dumps                 | 11.0 ms                                                      | 11.1 ms: 1.02x slower                                                         |
| logging_simple             | 6.40 us                                                      | 6.53 us: 1.02x slower                                                         |
| pickle_dict                | 32.1 us                                                      | 32.9 us: 1.02x slower                                                         |
| thrift                     | 877 us                                                       | 898 us: 1.02x slower                                                          |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.41 ms: 1.03x slower                                                         |
| raytrace                   | 289 ms                                                       | 299 ms: 1.03x slower                                                          |
| tornado_http               | 120 ms                                                       | 124 ms: 1.04x slower                                                          |
| mdp                        | 2.52 sec                                                     | 2.62 sec: 1.04x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.30 sec: 1.04x slower                                                        |
| unpickle_pure_python       | 214 us                                                       | 223 us: 1.04x slower                                                          |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                          |
| async_tree_io_tg           | 819 ms                                                       | 857 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 174 us                                                       | 182 us: 1.05x slower                                                          |
| meteor_contest             | 128 ms                                                       | 135 ms: 1.05x slower                                                          |
| chaos                      | 61.7 ms                                                      | 65.2 ms: 1.06x slower                                                         |
| async_generators           | 359 ms                                                       | 380 ms: 1.06x slower                                                          |
| unpickle_list              | 4.62 us                                                      | 4.90 us: 1.06x slower                                                         |
| bench_thread_pool          | 901 us                                                       | 955 us: 1.06x slower                                                          |
| sympy_expand               | 505 ms                                                       | 535 ms: 1.06x slower                                                          |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                          |
| scimark_monte_carlo        | 64.9 ms                                                      | 69.7 ms: 1.07x slower                                                         |
| comprehensions             | 17.3 us                                                      | 18.6 us: 1.08x slower                                                         |
| genshi_text                | 26.6 ms                                                      | 28.8 ms: 1.08x slower                                                         |
| 2to3                       | 291 ms                                                       | 317 ms: 1.09x slower                                                          |
| sympy_str                  | 296 ms                                                       | 322 ms: 1.09x slower                                                          |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.10x slower                                                         |
| django_template            | 38.9 ms                                                      | 42.7 ms: 1.10x slower                                                         |
| genshi_xml                 | 57.3 ms                                                      | 63.0 ms: 1.10x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                                         |
| python_startup             | 13.3 ms                                                      | 15.0 ms: 1.13x slower                                                         |
| sqlglot_normalize          | 118 ms                                                       | 133 ms: 1.13x slower                                                          |
| hexiom                     | 6.33 ms                                                      | 7.18 ms: 1.13x slower                                                         |
| docutils                   | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 176 ms: 1.15x slower                                                          |
| nqueens                    | 88.2 ms                                                      | 101 ms: 1.15x slower                                                          |
| generators                 | 33.5 ms                                                      | 38.9 ms: 1.16x slower                                                         |
| sqlglot_optimize           | 59.7 ms                                                      | 69.9 ms: 1.17x slower                                                         |
| sympy_integrate            | 23.3 ms                                                      | 27.6 ms: 1.18x slower                                                         |
| pylint                     | 346 ms                                                       | 425 ms: 1.23x slower                                                          |
| gc_traversal               | 4.11 ms                                                      | 5.35 ms: 1.30x slower                                                         |
| unpack_sequence            | 56.8 ns                                                      | 90.0 ns: 1.58x slower                                                         |
| create_gc_cycles           | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                         |
| bench_mp_pool              | 4.65 ms                                                      | 3.14 sec: 675.06x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                  |

Benchmark hidden because not significant (7): logging_format, fannkuch, asyncio_websockets, xml_etree_iterparse, coroutines, json_loads, pickle_list
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx

# HPT report

- Reliability score: 59.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x