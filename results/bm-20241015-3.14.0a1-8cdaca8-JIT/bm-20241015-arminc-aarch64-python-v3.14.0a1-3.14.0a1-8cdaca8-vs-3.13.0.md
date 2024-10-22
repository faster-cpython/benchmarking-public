# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 382 ms: 1.25x slower                                         |
| docutils       | 2.91 sec                                                 | 3.61 sec: 1.24x slower                                       |
| html5lib       | 64.3 ms                                                  | 71.8 ms: 1.12x slower                                        |
| tornado_http   | 131 ms                                                   | 147 ms: 1.12x slower                                         |
| Geometric mean | (ref)                                                    | 1.18x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 542 ms: 1.20x faster                                         |
| async_tree_none           | 493 ms                                                   | 463 ms: 1.06x faster                                         |
| async_tree_none_tg        | 467 ms                                                   | 451 ms: 1.04x faster                                         |
| async_tree_memoization    | 626 ms                                                   | 605 ms: 1.04x faster                                         |
| asyncio_websockets        | 656 ms                                                   | 664 ms: 1.01x slower                                         |
| async_generators          | 496 ms                                                   | 507 ms: 1.02x slower                                         |
| coroutines                | 28.2 ms                                                  | 28.9 ms: 1.02x slower                                        |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                       |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                       |
| asyncio_tcp               | 568 ms                                                   | 630 ms: 1.11x slower                                         |
| async_tree_io_tg          | 1.09 sec                                                 | 1.25 sec: 1.14x slower                                       |
| Geometric mean            | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 97.2 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 246 ms                                                   | 244 ms: 1.01x faster                                         |
| regex_compile  | 128 ms                                                   | 179 ms: 1.39x slower                                         |
| Geometric mean | (ref)                                                    | 1.09x slower                                                 |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.0 us: 1.06x faster                                        |
| pickle_list          | 5.34 us                                                  | 5.12 us: 1.04x faster                                        |
| unpickle_list        | 6.65 us                                                  | 6.52 us: 1.02x faster                                        |
| xml_etree_parse      | 188 ms                                                   | 186 ms: 1.01x faster                                         |
| pickle               | 13.5 us                                                  | 13.8 us: 1.02x slower                                        |
| xml_etree_iterparse  | 147 ms                                                   | 151 ms: 1.03x slower                                         |
| tomli_loads          | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                       |
| unpickle_pure_python | 254 us                                                   | 268 us: 1.05x slower                                         |
| json_dumps           | 13.4 ms                                                  | 14.4 ms: 1.08x slower                                        |
| pickle_pure_python   | 359 us                                                   | 389 us: 1.08x slower                                         |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_dict, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 14.7 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                    | 1.05x slower                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                        |
| genshi_text     | 27.7 ms                                                  | 34.2 ms: 1.23x slower                                        |
| django_template | 42.3 ms                                                  | 52.4 ms: 1.24x slower                                        |
| genshi_xml      | 60.2 ms                                                  | 84.1 ms: 1.40x slower                                        |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 39.2 us: 1.30x faster                                        |
| async_tree_memoization_tg | 649 ms                                                   | 542 ms: 1.20x faster                                         |
| deepcopy                  | 451 us                                                   | 377 us: 1.20x faster                                         |
| async_tree_none           | 493 ms                                                   | 463 ms: 1.06x faster                                         |
| unpickle                  | 20.2 us                                                  | 19.0 us: 1.06x faster                                        |
| pickle_list               | 5.34 us                                                  | 5.12 us: 1.04x faster                                        |
| pathlib                   | 22.4 ms                                                  | 21.6 ms: 1.04x faster                                        |
| async_tree_none_tg        | 467 ms                                                   | 451 ms: 1.04x faster                                         |
| scimark_sor               | 159 ms                                                   | 154 ms: 1.04x faster                                         |
| async_tree_memoization    | 626 ms                                                   | 605 ms: 1.04x faster                                         |
| deepcopy_reduce           | 4.07 us                                                  | 3.98 us: 1.02x faster                                        |
| unpickle_list             | 6.65 us                                                  | 6.52 us: 1.02x faster                                        |
| logging_silent            | 135 ns                                                   | 134 ns: 1.01x faster                                         |
| regex_dna                 | 246 ms                                                   | 244 ms: 1.01x faster                                         |
| mako                      | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                        |
| xml_etree_parse           | 188 ms                                                   | 186 ms: 1.01x faster                                         |
| thrift                    | 946 us                                                   | 956 us: 1.01x slower                                         |
| asyncio_websockets        | 656 ms                                                   | 664 ms: 1.01x slower                                         |
| bpe_tokeniser             | 5.90 sec                                                 | 5.97 sec: 1.01x slower                                       |
| sqlite_synth              | 3.84 us                                                  | 3.89 us: 1.01x slower                                        |
| scimark_fft               | 447 ms                                                   | 454 ms: 1.02x slower                                         |
| pickle                    | 13.5 us                                                  | 13.8 us: 1.02x slower                                        |
| async_generators          | 496 ms                                                   | 507 ms: 1.02x slower                                         |
| coroutines                | 28.2 ms                                                  | 28.9 ms: 1.02x slower                                        |
| coverage                  | 98.5 ms                                                  | 101 ms: 1.03x slower                                         |
| float                     | 94.4 ms                                                  | 97.2 ms: 1.03x slower                                        |
| logging_format            | 7.83 us                                                  | 8.08 us: 1.03x slower                                        |
| xml_etree_iterparse       | 147 ms                                                   | 151 ms: 1.03x slower                                         |
| mdp                       | 3.36 sec                                                 | 3.51 sec: 1.04x slower                                       |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                       |
| tomli_loads               | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                       |
| unpickle_pure_python      | 254 us                                                   | 268 us: 1.05x slower                                         |
| logging_simple            | 7.04 us                                                  | 7.45 us: 1.06x slower                                        |
| scimark_monte_carlo       | 83.8 ms                                                  | 89.5 ms: 1.07x slower                                        |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                       |
| json_dumps                | 13.4 ms                                                  | 14.4 ms: 1.08x slower                                        |
| bench_thread_pool         | 1.28 ms                                                  | 1.37 ms: 1.08x slower                                        |
| pickle_pure_python        | 359 us                                                   | 389 us: 1.08x slower                                         |
| scimark_lu                | 139 ms                                                   | 151 ms: 1.08x slower                                         |
| meteor_contest            | 113 ms                                                   | 123 ms: 1.08x slower                                         |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 7.16 ms: 1.09x slower                                        |
| spectral_norm             | 141 ms                                                   | 155 ms: 1.10x slower                                         |
| crypto_pyaes              | 82.7 ms                                                  | 90.8 ms: 1.10x slower                                        |
| python_startup            | 13.3 ms                                                  | 14.7 ms: 1.11x slower                                        |
| pyflate                   | 556 ms                                                   | 615 ms: 1.11x slower                                         |
| asyncio_tcp               | 568 ms                                                   | 630 ms: 1.11x slower                                         |
| fannkuch                  | 452 ms                                                   | 503 ms: 1.11x slower                                         |
| html5lib                  | 64.3 ms                                                  | 71.8 ms: 1.12x slower                                        |
| tornado_http              | 131 ms                                                   | 147 ms: 1.12x slower                                         |
| go                        | 163 ms                                                   | 184 ms: 1.13x slower                                         |
| typing_runtime_protocols  | 192 us                                                   | 218 us: 1.13x slower                                         |
| async_tree_io_tg          | 1.09 sec                                                 | 1.25 sec: 1.14x slower                                       |
| raytrace                  | 298 ms                                                   | 349 ms: 1.17x slower                                         |
| deltablue                 | 3.85 ms                                                  | 4.55 ms: 1.18x slower                                        |
| richards_super            | 60.3 ms                                                  | 71.4 ms: 1.18x slower                                        |
| richards                  | 53.5 ms                                                  | 64.2 ms: 1.20x slower                                        |
| pycparser                 | 1.26 sec                                                 | 1.52 sec: 1.20x slower                                       |
| comprehensions            | 20.4 us                                                  | 24.7 us: 1.21x slower                                        |
| sqlglot_normalize         | 128 ms                                                   | 157 ms: 1.22x slower                                         |
| sqlglot_parse             | 1.38 ms                                                  | 1.70 ms: 1.23x slower                                        |
| genshi_text               | 27.7 ms                                                  | 34.2 ms: 1.23x slower                                        |
| chaos                     | 68.8 ms                                                  | 85.0 ms: 1.24x slower                                        |
| django_template           | 42.3 ms                                                  | 52.4 ms: 1.24x slower                                        |
| docutils                  | 2.91 sec                                                 | 3.61 sec: 1.24x slower                                       |
| 2to3                      | 306 ms                                                   | 382 ms: 1.25x slower                                         |
| nqueens                   | 98.7 ms                                                  | 125 ms: 1.26x slower                                         |
| sqlglot_transpile         | 1.73 ms                                                  | 2.20 ms: 1.27x slower                                        |
| pprint_safe_repr          | 926 ms                                                   | 1.21 sec: 1.31x slower                                       |
| sympy_expand              | 455 ms                                                   | 594 ms: 1.31x slower                                         |
| sqlglot_optimize          | 62.4 ms                                                  | 82.2 ms: 1.32x slower                                        |
| pprint_pformat            | 1.90 sec                                                 | 2.55 sec: 1.34x slower                                       |
| sympy_str                 | 264 ms                                                   | 357 ms: 1.35x slower                                         |
| gc_traversal              | 4.53 ms                                                  | 6.22 ms: 1.37x slower                                        |
| regex_compile             | 128 ms                                                   | 179 ms: 1.39x slower                                         |
| genshi_xml                | 60.2 ms                                                  | 84.1 ms: 1.40x slower                                        |
| sympy_integrate           | 21.0 ms                                                  | 29.4 ms: 1.40x slower                                        |
| pylint                    | 343 ms                                                   | 494 ms: 1.44x slower                                         |
| hexiom                    | 7.13 ms                                                  | 10.3 ms: 1.44x slower                                        |
| sympy_sum                 | 143 ms                                                   | 215 ms: 1.50x slower                                         |
| generators                | 37.8 ms                                                  | 59.0 ms: 1.56x slower                                        |
| create_gc_cycles          | 2.12 ms                                                  | 3.67 ms: 1.73x slower                                        |
| unpack_sequence           | 57.2 ns                                                  | 146 ns: 2.56x slower                                         |
| bench_mp_pool             | 7.30 ms                                                  | 1.45 sec: 198.72x slower                                     |
| Geometric mean            | (ref)                                                    | 1.17x slower                                                 |

Benchmark hidden because not significant (13): xml_etree_generate, pickle_dict, async_tree_cpu_io_mixed, telco, regex_v8, xml_etree_process, pidigits, python_startup_no_site, regex_effbot, async_tree_cpu_io_mixed_tg, json_loads, json, nbody
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: dulwich_log, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.20x