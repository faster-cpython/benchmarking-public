# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 374 ms: 1.22x slower                                             |
| docutils       | 2.91 sec                                                 | 3.63 sec: 1.25x slower                                           |
| html5lib       | 64.3 ms                                                  | 71.3 ms: 1.11x slower                                            |
| tornado_http   | 131 ms                                                   | 142 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                    | 1.16x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|---------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 561 ms: 1.16x faster                                             |
| async_tree_none           | 493 ms                                                   | 448 ms: 1.10x faster                                             |
| async_tree_none_tg        | 467 ms                                                   | 426 ms: 1.10x faster                                             |
| async_tree_memoization    | 626 ms                                                   | 591 ms: 1.06x faster                                             |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 752 ms: 1.02x faster                                             |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                             |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                            |
| async_generators          | 496 ms                                                   | 507 ms: 1.02x slower                                             |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                           |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.29 sec: 1.05x slower                                           |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                           |
| asyncio_tcp               | 568 ms                                                   | 622 ms: 1.10x slower                                             |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 90.0 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                    | 1.02x faster                                                     |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 181 ms: 1.41x slower                                             |
| Geometric mean | (ref)                                                    | 1.09x slower                                                     |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.2 us: 1.05x faster                                            |
| unpickle_list        | 6.65 us                                                  | 6.40 us: 1.04x faster                                            |
| pickle_list          | 5.34 us                                                  | 5.21 us: 1.02x faster                                            |
| json_loads           | 31.4 us                                                  | 31.0 us: 1.01x faster                                            |
| pickle               | 13.5 us                                                  | 13.6 us: 1.01x slower                                            |
| tomli_loads          | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                           |
| xml_etree_iterparse  | 147 ms                                                   | 152 ms: 1.03x slower                                             |
| unpickle_pure_python | 254 us                                                   | 267 us: 1.05x slower                                             |
| pickle_pure_python   | 359 us                                                   | 384 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                     |

Benchmark hidden because not significant (5): xml_etree_generate, json_dumps, pickle_dict, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                    | 1.00x faster                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                            |
| django_template | 42.3 ms                                                  | 51.9 ms: 1.23x slower                                            |
| genshi_text     | 27.7 ms                                                  | 34.8 ms: 1.26x slower                                            |
| genshi_xml      | 60.2 ms                                                  | 83.0 ms: 1.38x slower                                            |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|---------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 37.4 us: 1.36x faster                                            |
| async_tree_memoization_tg | 649 ms                                                   | 561 ms: 1.16x faster                                             |
| deepcopy                  | 451 us                                                   | 405 us: 1.11x faster                                             |
| async_tree_none           | 493 ms                                                   | 448 ms: 1.10x faster                                             |
| async_tree_none_tg        | 467 ms                                                   | 426 ms: 1.10x faster                                             |
| async_tree_memoization    | 626 ms                                                   | 591 ms: 1.06x faster                                             |
| deepcopy_reduce           | 4.07 us                                                  | 3.85 us: 1.06x faster                                            |
| unpickle                  | 20.2 us                                                  | 19.2 us: 1.05x faster                                            |
| float                     | 94.4 ms                                                  | 90.0 ms: 1.05x faster                                            |
| pathlib                   | 22.4 ms                                                  | 21.5 ms: 1.04x faster                                            |
| unpickle_list             | 6.65 us                                                  | 6.40 us: 1.04x faster                                            |
| pickle_list               | 5.34 us                                                  | 5.21 us: 1.02x faster                                            |
| logging_silent            | 135 ns                                                   | 133 ns: 1.02x faster                                             |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 752 ms: 1.02x faster                                             |
| python_startup            | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                            |
| mako                      | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                            |
| json_loads                | 31.4 us                                                  | 31.0 us: 1.01x faster                                            |
| scimark_fft               | 447 ms                                                   | 444 ms: 1.01x faster                                             |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                             |
| pickle                    | 13.5 us                                                  | 13.6 us: 1.01x slower                                            |
| telco                     | 9.73 ms                                                  | 9.86 ms: 1.01x slower                                            |
| thrift                    | 946 us                                                   | 960 us: 1.02x slower                                             |
| bpe_tokeniser             | 5.90 sec                                                 | 5.99 sec: 1.02x slower                                           |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                            |
| async_generators          | 496 ms                                                   | 507 ms: 1.02x slower                                             |
| logging_format            | 7.83 us                                                  | 8.02 us: 1.02x slower                                            |
| spectral_norm             | 141 ms                                                   | 145 ms: 1.03x slower                                             |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.79 ms: 1.03x slower                                            |
| tomli_loads               | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                           |
| xml_etree_iterparse       | 147 ms                                                   | 152 ms: 1.03x slower                                             |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                           |
| mdp                       | 3.36 sec                                                 | 3.50 sec: 1.04x slower                                           |
| scimark_monte_carlo       | 83.8 ms                                                  | 87.5 ms: 1.04x slower                                            |
| unpickle_pure_python      | 254 us                                                   | 267 us: 1.05x slower                                             |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.29 sec: 1.05x slower                                           |
| logging_simple            | 7.04 us                                                  | 7.40 us: 1.05x slower                                            |
| scimark_sor               | 159 ms                                                   | 167 ms: 1.05x slower                                             |
| crypto_pyaes              | 82.7 ms                                                  | 88.1 ms: 1.07x slower                                            |
| pickle_pure_python        | 359 us                                                   | 384 us: 1.07x slower                                             |
| bench_thread_pool         | 1.28 ms                                                  | 1.37 ms: 1.07x slower                                            |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                           |
| scimark_lu                | 139 ms                                                   | 150 ms: 1.08x slower                                             |
| tornado_http              | 131 ms                                                   | 142 ms: 1.08x slower                                             |
| create_gc_cycles          | 2.12 ms                                                  | 2.31 ms: 1.09x slower                                            |
| asyncio_tcp               | 568 ms                                                   | 622 ms: 1.10x slower                                             |
| meteor_contest            | 113 ms                                                   | 125 ms: 1.10x slower                                             |
| typing_runtime_protocols  | 192 us                                                   | 211 us: 1.10x slower                                             |
| html5lib                  | 64.3 ms                                                  | 71.3 ms: 1.11x slower                                            |
| pyflate                   | 556 ms                                                   | 617 ms: 1.11x slower                                             |
| fannkuch                  | 452 ms                                                   | 503 ms: 1.11x slower                                             |
| richards                  | 53.5 ms                                                  | 60.3 ms: 1.13x slower                                            |
| deltablue                 | 3.85 ms                                                  | 4.38 ms: 1.14x slower                                            |
| gc_traversal              | 4.53 ms                                                  | 5.21 ms: 1.15x slower                                            |
| go                        | 163 ms                                                   | 189 ms: 1.16x slower                                             |
| pycparser                 | 1.26 sec                                                 | 1.47 sec: 1.17x slower                                           |
| raytrace                  | 298 ms                                                   | 347 ms: 1.17x slower                                             |
| richards_super            | 60.3 ms                                                  | 70.7 ms: 1.17x slower                                            |
| comprehensions            | 20.4 us                                                  | 24.5 us: 1.20x slower                                            |
| sqlglot_normalize         | 128 ms                                                   | 155 ms: 1.21x slower                                             |
| sqlglot_parse             | 1.38 ms                                                  | 1.68 ms: 1.22x slower                                            |
| 2to3                      | 306 ms                                                   | 374 ms: 1.22x slower                                             |
| django_template           | 42.3 ms                                                  | 51.9 ms: 1.23x slower                                            |
| nqueens                   | 98.7 ms                                                  | 122 ms: 1.24x slower                                             |
| docutils                  | 2.91 sec                                                 | 3.63 sec: 1.25x slower                                           |
| genshi_text               | 27.7 ms                                                  | 34.8 ms: 1.26x slower                                            |
| chaos                     | 68.8 ms                                                  | 88.3 ms: 1.28x slower                                            |
| sqlglot_transpile         | 1.73 ms                                                  | 2.22 ms: 1.28x slower                                            |
| sqlglot_optimize          | 62.4 ms                                                  | 80.2 ms: 1.29x slower                                            |
| pprint_safe_repr          | 926 ms                                                   | 1.20 sec: 1.30x slower                                           |
| sympy_expand              | 455 ms                                                   | 591 ms: 1.30x slower                                             |
| pprint_pformat            | 1.90 sec                                                 | 2.50 sec: 1.32x slower                                           |
| sympy_str                 | 264 ms                                                   | 358 ms: 1.36x slower                                             |
| sympy_integrate           | 21.0 ms                                                  | 28.8 ms: 1.38x slower                                            |
| pylint                    | 343 ms                                                   | 472 ms: 1.38x slower                                             |
| genshi_xml                | 60.2 ms                                                  | 83.0 ms: 1.38x slower                                            |
| regex_compile             | 128 ms                                                   | 181 ms: 1.41x slower                                             |
| hexiom                    | 7.13 ms                                                  | 10.1 ms: 1.42x slower                                            |
| sympy_sum                 | 143 ms                                                   | 214 ms: 1.49x slower                                             |
| generators                | 37.8 ms                                                  | 59.3 ms: 1.57x slower                                            |
| unpack_sequence           | 57.2 ns                                                  | 145 ns: 2.54x slower                                             |
| bench_mp_pool             | 7.30 ms                                                  | 1.89 sec: 259.47x slower                                         |
| Geometric mean            | (ref)                                                    | 1.16x slower                                                     |

Benchmark hidden because not significant (15): xml_etree_generate, json_dumps, sqlite_synth, nbody, json, regex_v8, pickle_dict, xml_etree_process, pidigits, regex_dna, regex_effbot, python_startup_no_site, coverage, async_tree_cpu_io_mixed_tg, xml_etree_parse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x