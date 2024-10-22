# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 382 ms: 1.25x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.94 sec: 1.36x slower                                                  |
| html5lib       | 64.3 ms                                                  | 71.9 ms: 1.12x slower                                                   |
| tornado_http   | 131 ms                                                   | 150 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 556 ms: 1.17x faster                                                    |
| async_tree_none           | 493 ms                                                   | 442 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 426 ms: 1.10x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 589 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 748 ms: 1.02x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| async_generators          | 496 ms                                                   | 512 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| asyncio_tcp               | 568 ms                                                   | 629 ms: 1.11x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 87.5 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                                   |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| regex_compile  | 128 ms                                                   | 196 ms: 1.52x slower                                                    |
| Geometric mean | (ref)                                                    | 1.12x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.3 us: 1.05x faster                                                   |
| unpickle_list        | 6.65 us                                                  | 6.42 us: 1.04x faster                                                   |
| pickle_list          | 5.34 us                                                  | 5.20 us: 1.03x faster                                                   |
| xml_etree_parse      | 188 ms                                                   | 187 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| pickle               | 13.5 us                                                  | 13.7 us: 1.01x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 267 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 392 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, json_loads, pickle_dict, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| django_template | 42.3 ms                                                  | 51.4 ms: 1.22x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 35.0 ms: 1.26x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 80.8 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 37.6 us: 1.36x faster                                                   |
| async_tree_memoization_tg | 649 ms                                                   | 556 ms: 1.17x faster                                                    |
| deepcopy                  | 451 us                                                   | 401 us: 1.12x faster                                                    |
| async_tree_none           | 493 ms                                                   | 442 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 426 ms: 1.10x faster                                                    |
| float                     | 94.4 ms                                                  | 87.5 ms: 1.08x faster                                                   |
| async_tree_memoization    | 626 ms                                                   | 589 ms: 1.06x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.83 us: 1.06x faster                                                   |
| unpickle                  | 20.2 us                                                  | 19.3 us: 1.05x faster                                                   |
| scimark_sor               | 159 ms                                                   | 152 ms: 1.04x faster                                                    |
| unpickle_list             | 6.65 us                                                  | 6.42 us: 1.04x faster                                                   |
| pathlib                   | 22.4 ms                                                  | 21.7 ms: 1.03x faster                                                   |
| mako                      | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| pickle_list               | 5.34 us                                                  | 5.20 us: 1.03x faster                                                   |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 748 ms: 1.02x faster                                                    |
| regex_v8                  | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                                   |
| xml_etree_parse           | 188 ms                                                   | 187 ms: 1.01x faster                                                    |
| xml_etree_iterparse       | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| logging_silent            | 135 ns                                                   | 137 ns: 1.01x slower                                                    |
| bpe_tokeniser             | 5.90 sec                                                 | 5.98 sec: 1.01x slower                                                  |
| pickle                    | 13.5 us                                                  | 13.7 us: 1.01x slower                                                   |
| regex_dna                 | 246 ms                                                   | 252 ms: 1.02x slower                                                    |
| thrift                    | 946 us                                                   | 970 us: 1.03x slower                                                    |
| scimark_fft               | 447 ms                                                   | 459 ms: 1.03x slower                                                    |
| async_generators          | 496 ms                                                   | 512 ms: 1.03x slower                                                    |
| spectral_norm             | 141 ms                                                   | 146 ms: 1.03x slower                                                    |
| coverage                  | 98.5 ms                                                  | 102 ms: 1.04x slower                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 7.57 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.85 ms: 1.04x slower                                                   |
| tomli_loads               | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| unpickle_pure_python      | 254 us                                                   | 267 us: 1.05x slower                                                    |
| logging_format            | 7.83 us                                                  | 8.20 us: 1.05x slower                                                   |
| mdp                       | 3.36 sec                                                 | 3.52 sec: 1.05x slower                                                  |
| bench_thread_pool         | 1.28 ms                                                  | 1.35 ms: 1.05x slower                                                   |
| logging_simple            | 7.04 us                                                  | 7.46 us: 1.06x slower                                                   |
| scimark_lu                | 139 ms                                                   | 148 ms: 1.07x slower                                                    |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.07x slower                                                  |
| crypto_pyaes              | 82.7 ms                                                  | 89.7 ms: 1.08x slower                                                   |
| create_gc_cycles          | 2.12 ms                                                  | 2.31 ms: 1.09x slower                                                   |
| telco                     | 9.73 ms                                                  | 10.6 ms: 1.09x slower                                                   |
| pickle_pure_python        | 359 us                                                   | 392 us: 1.09x slower                                                    |
| meteor_contest            | 113 ms                                                   | 124 ms: 1.10x slower                                                    |
| scimark_monte_carlo       | 83.8 ms                                                  | 92.6 ms: 1.10x slower                                                   |
| asyncio_tcp               | 568 ms                                                   | 629 ms: 1.11x slower                                                    |
| typing_runtime_protocols  | 192 us                                                   | 213 us: 1.11x slower                                                    |
| html5lib                  | 64.3 ms                                                  | 71.9 ms: 1.12x slower                                                   |
| fannkuch                  | 452 ms                                                   | 508 ms: 1.13x slower                                                    |
| gc_traversal              | 4.53 ms                                                  | 5.10 ms: 1.13x slower                                                   |
| tornado_http              | 131 ms                                                   | 150 ms: 1.14x slower                                                    |
| deltablue                 | 3.85 ms                                                  | 4.39 ms: 1.14x slower                                                   |
| raytrace                  | 298 ms                                                   | 348 ms: 1.17x slower                                                    |
| go                        | 163 ms                                                   | 190 ms: 1.17x slower                                                    |
| sqlglot_normalize         | 128 ms                                                   | 150 ms: 1.17x slower                                                    |
| pyflate                   | 556 ms                                                   | 657 ms: 1.18x slower                                                    |
| comprehensions            | 20.4 us                                                  | 24.5 us: 1.20x slower                                                   |
| pycparser                 | 1.26 sec                                                 | 1.53 sec: 1.21x slower                                                  |
| django_template           | 42.3 ms                                                  | 51.4 ms: 1.22x slower                                                   |
| richards                  | 53.5 ms                                                  | 66.3 ms: 1.24x slower                                                   |
| 2to3                      | 306 ms                                                   | 382 ms: 1.25x slower                                                    |
| sqlglot_optimize          | 62.4 ms                                                  | 78.5 ms: 1.26x slower                                                   |
| richards_super            | 60.3 ms                                                  | 75.9 ms: 1.26x slower                                                   |
| genshi_text               | 27.7 ms                                                  | 35.0 ms: 1.26x slower                                                   |
| nqueens                   | 98.7 ms                                                  | 126 ms: 1.27x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.76 ms: 1.27x slower                                                   |
| sqlglot_transpile         | 1.73 ms                                                  | 2.23 ms: 1.29x slower                                                   |
| chaos                     | 68.8 ms                                                  | 92.2 ms: 1.34x slower                                                   |
| genshi_xml                | 60.2 ms                                                  | 80.8 ms: 1.34x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 1.25 sec: 1.34x slower                                                  |
| sympy_expand              | 455 ms                                                   | 613 ms: 1.35x slower                                                    |
| docutils                  | 2.91 sec                                                 | 3.94 sec: 1.36x slower                                                  |
| sympy_integrate           | 21.0 ms                                                  | 28.5 ms: 1.36x slower                                                   |
| pprint_pformat            | 1.90 sec                                                 | 2.61 sec: 1.38x slower                                                  |
| pylint                    | 343 ms                                                   | 479 ms: 1.39x slower                                                    |
| sympy_str                 | 264 ms                                                   | 369 ms: 1.40x slower                                                    |
| hexiom                    | 7.13 ms                                                  | 10.3 ms: 1.45x slower                                                   |
| sympy_sum                 | 143 ms                                                   | 211 ms: 1.47x slower                                                    |
| generators                | 37.8 ms                                                  | 57.6 ms: 1.52x slower                                                   |
| regex_compile             | 128 ms                                                   | 196 ms: 1.52x slower                                                    |
| unpack_sequence           | 57.2 ns                                                  | 150 ns: 2.63x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (14): xml_etree_generate, python_startup, sqlite_synth, async_tree_cpu_io_mixed_tg, json_loads, nbody, pidigits, pickle_dict, python_startup_no_site, xml_etree_process, coroutines, json_dumps, json, regex_effbot
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x