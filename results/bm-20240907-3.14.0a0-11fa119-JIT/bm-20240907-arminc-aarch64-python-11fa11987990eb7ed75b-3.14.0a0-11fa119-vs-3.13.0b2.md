# Results vs. 3.13.0b2

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 380 ms: 1.25x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.94 sec: 1.27x slower                                                  |
| html5lib       | 66.1 ms                                                      | 70.2 ms: 1.06x slower                                                   |
| tornado_http   | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                        | 1.18x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 570 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 429 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.15 sec: 1.10x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 555 ms: 1.09x faster                                                    |
| async_tree_none            | 492 ms                                                       | 457 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 748 ms: 1.06x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.18 sec: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.1 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                       | 188 ms: 1.47x slower                                                    |
| Geometric mean | (ref)                                                        | 1.10x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 6.52 us                                                      | 6.26 us: 1.04x faster                                                   |
| xml_etree_process    | 80.8 ms                                                      | 78.7 ms: 1.03x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 265 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 393 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_dict, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.90 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| django_template | 42.3 ms                                                      | 51.4 ms: 1.21x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.1 ms: 1.24x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 80.1 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.3 us: 1.36x faster                                                   |
| deepcopy                   | 448 us                                                       | 388 us: 1.15x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 570 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 429 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.15 sec: 1.10x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 555 ms: 1.09x faster                                                    |
| async_tree_none            | 492 ms                                                       | 457 ms: 1.08x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.80 us: 1.06x faster                                                   |
| scimark_sor                | 159 ms                                                       | 150 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 748 ms: 1.06x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.93 ms: 1.05x faster                                                   |
| unpickle_list              | 6.52 us                                                      | 6.26 us: 1.04x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 22.0 ms: 1.04x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.18 sec: 1.03x faster                                                  |
| xml_etree_process          | 80.8 ms                                                      | 78.7 ms: 1.03x faster                                                   |
| float                      | 91.4 ms                                                      | 89.1 ms: 1.03x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| mako                       | 13.2 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| coverage                   | 98.4 ms                                                      | 99.8 ms: 1.01x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                  |
| tomli_loads                | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                                  |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.96 sec: 1.02x slower                                                  |
| logging_silent             | 133 ns                                                       | 137 ns: 1.02x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.42 us: 1.03x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| async_generators           | 488 ms                                                       | 504 ms: 1.03x slower                                                    |
| scimark_fft                | 445 ms                                                       | 460 ms: 1.03x slower                                                    |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.03x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.09 us: 1.03x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.90 ms: 1.04x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.47 sec: 1.04x slower                                                  |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.82 ms: 1.04x slower                                                   |
| json                       | 5.64 ms                                                      | 5.88 ms: 1.04x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 265 us: 1.05x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 70.2 ms: 1.06x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 151 ms: 1.06x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 625 ms: 1.07x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 89.3 ms: 1.09x slower                                                   |
| meteor_contest             | 113 ms                                                       | 124 ms: 1.09x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 393 us: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 214 us: 1.11x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.82 ms: 1.11x slower                                                   |
| fannkuch                   | 451 ms                                                       | 504 ms: 1.12x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.34 ms: 1.12x slower                                                   |
| pyflate                    | 557 ms                                                       | 627 ms: 1.13x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 93.7 ms: 1.14x slower                                                   |
| tornado_http               | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 149 ms: 1.15x slower                                                    |
| go                         | 161 ms                                                       | 188 ms: 1.17x slower                                                    |
| raytrace                   | 297 ms                                                       | 352 ms: 1.19x slower                                                    |
| richards                   | 55.9 ms                                                      | 66.8 ms: 1.20x slower                                                   |
| comprehensions             | 20.5 us                                                      | 24.6 us: 1.20x slower                                                   |
| richards_super             | 62.3 ms                                                      | 75.0 ms: 1.20x slower                                                   |
| django_template            | 42.3 ms                                                      | 51.4 ms: 1.21x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.73 ms: 1.22x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.49 sec: 1.22x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 77.4 ms: 1.24x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 34.1 ms: 1.24x slower                                                   |
| 2to3                       | 305 ms                                                       | 380 ms: 1.25x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 124 ms: 1.25x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.94 sec: 1.27x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 2.19 ms: 1.28x slower                                                   |
| sympy_expand               | 457 ms                                                       | 606 ms: 1.32x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 80.1 ms: 1.33x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 77.7 ms: 1.33x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.25 sec: 1.34x slower                                                  |
| chaos                      | 68.3 ms                                                      | 91.4 ms: 1.34x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.59 sec: 1.34x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 28.5 ms: 1.37x slower                                                   |
| sympy_str                  | 265 ms                                                       | 366 ms: 1.38x slower                                                    |
| pylint                     | 337 ms                                                       | 466 ms: 1.38x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.2 ms: 1.44x slower                                                   |
| regex_compile              | 128 ms                                                       | 188 ms: 1.47x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 214 ms: 1.49x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.3 ms: 1.54x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                            |

Benchmark hidden because not significant (13): xml_etree_parse, coroutines, regex_effbot, sqlite_synth, pickle_dict, create_gc_cycles, unpickle, nbody, pidigits, regex_v8, pickle_list, asyncio_websockets, thrift
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x