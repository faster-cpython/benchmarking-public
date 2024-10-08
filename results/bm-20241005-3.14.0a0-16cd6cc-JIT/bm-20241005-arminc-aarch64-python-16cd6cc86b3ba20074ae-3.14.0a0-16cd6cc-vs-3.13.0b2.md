# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 383 ms: 1.26x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.71 sec: 1.20x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.0 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                        | 1.17x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 420 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 445 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 591 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 561 ms: 1.08x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 753 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 739 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| float          | 91.4 ms                                                      | 90.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 262 ms: 1.01x slower                                                    |
| regex_compile  | 128 ms                                                       | 184 ms: 1.44x slower                                                    |
| Geometric mean | (ref)                                                        | 1.10x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.1 us: 1.03x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.2 us: 1.03x faster                                                   |
| unpickle_list        | 6.52 us                                                      | 6.37 us: 1.02x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| pickle_list          | 5.27 us                                                      | 5.21 us: 1.01x faster                                                   |
| json_dumps           | 13.1 ms                                                      | 13.1 ms: 1.00x faster                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 268 us: 1.07x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 386 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_dict, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.73 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                      | 51.8 ms: 1.22x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.4 ms: 1.25x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 83.1 ms: 1.38x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.9 us: 1.34x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 420 ms: 1.13x faster                                                    |
| deepcopy                   | 448 us                                                       | 400 us: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 445 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 591 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 561 ms: 1.08x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 753 ms: 1.05x faster                                                    |
| scimark_sor                | 159 ms                                                       | 152 ms: 1.05x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.8 ms: 1.04x faster                                                   |
| json_loads                 | 32.1 us                                                      | 31.1 us: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 739 ms: 1.03x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.2 us: 1.03x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.93 us: 1.03x faster                                                   |
| telco                      | 10.0 ms                                                      | 9.75 ms: 1.03x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.05 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| unpickle_list              | 6.52 us                                                      | 6.37 us: 1.02x faster                                                   |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                    |
| float                      | 91.4 ms                                                      | 90.0 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| pickle_list                | 5.27 us                                                      | 5.21 us: 1.01x faster                                                   |
| mako                       | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                   |
| python_startup             | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.1 ms: 1.00x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 664 ms: 1.01x slower                                                    |
| regex_dna                  | 259 ms                                                       | 262 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.73 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 5.97 sec: 1.02x slower                                                  |
| spectral_norm              | 141 ms                                                       | 145 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                                  |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| logging_format             | 7.82 us                                                      | 8.11 us: 1.04x slower                                                   |
| async_generators           | 488 ms                                                       | 508 ms: 1.04x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.48 sec: 1.04x slower                                                  |
| asyncio_tcp                | 584 ms                                                       | 611 ms: 1.05x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.54 us: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.87 ms: 1.05x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 150 ms: 1.06x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 268 us: 1.07x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 71.0 ms: 1.07x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 386 us: 1.08x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 89.1 ms: 1.08x slower                                                   |
| meteor_contest             | 113 ms                                                       | 124 ms: 1.09x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.37 ms: 1.09x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 89.9 ms: 1.10x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 213 us: 1.10x slower                                                    |
| fannkuch                   | 451 ms                                                       | 503 ms: 1.11x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.35 ms: 1.12x slower                                                   |
| richards                   | 55.9 ms                                                      | 63.8 ms: 1.14x slower                                                   |
| pyflate                    | 557 ms                                                       | 640 ms: 1.15x slower                                                    |
| tornado_http               | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| go                         | 161 ms                                                       | 185 ms: 1.15x slower                                                    |
| richards_super             | 62.3 ms                                                      | 72.0 ms: 1.16x slower                                                   |
| raytrace                   | 297 ms                                                       | 350 ms: 1.18x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.71 sec: 1.20x slower                                                  |
| sqlglot_normalize          | 129 ms                                                       | 156 ms: 1.21x slower                                                    |
| comprehensions             | 20.5 us                                                      | 24.9 us: 1.21x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.48 sec: 1.21x slower                                                  |
| sqlglot_parse              | 1.42 ms                                                      | 1.74 ms: 1.22x slower                                                   |
| django_template            | 42.3 ms                                                      | 51.8 ms: 1.22x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 124 ms: 1.25x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 34.4 ms: 1.25x slower                                                   |
| 2to3                       | 305 ms                                                       | 383 ms: 1.26x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.21 ms: 1.29x slower                                                   |
| sympy_expand               | 457 ms                                                       | 598 ms: 1.31x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 82.2 ms: 1.31x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.23 sec: 1.32x slower                                                  |
| chaos                      | 68.3 ms                                                      | 90.5 ms: 1.33x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.61 sec: 1.35x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 80.1 ms: 1.37x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 83.1 ms: 1.38x slower                                                   |
| sympy_str                  | 265 ms                                                       | 366 ms: 1.38x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 29.6 ms: 1.42x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 10.1 ms: 1.43x slower                                                   |
| regex_compile              | 128 ms                                                       | 184 ms: 1.44x slower                                                    |
| pylint                     | 337 ms                                                       | 486 ms: 1.44x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 218 ms: 1.52x slower                                                    |
| generators                 | 37.1 ms                                                      | 59.2 ms: 1.59x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 2.07 sec: 294.05x slower                                                |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmark hidden because not significant (13): create_gc_cycles, xml_etree_parse, json, regex_v8, thrift, pidigits, coroutines, scimark_fft, sqlite_synth, pickle_dict, regex_effbot, xml_etree_process, coverage
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.06x