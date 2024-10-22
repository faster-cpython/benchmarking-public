# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 380 ms: 1.24x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.94 sec: 1.36x slower                                                  |
| html5lib       | 64.3 ms                                                  | 70.2 ms: 1.09x slower                                                   |
| tornado_http   | 131 ms                                                   | 147 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 570 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 429 ms: 1.09x faster                                                    |
| async_tree_none            | 493 ms                                                   | 457 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 720 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 748 ms: 1.02x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| async_generators           | 496 ms                                                   | 504 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.15 sec: 1.06x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 625 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 89.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.94 ms: 1.01x slower                                                   |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| regex_compile  | 128 ms                                                   | 188 ms: 1.47x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 6.65 us                                                  | 6.26 us: 1.06x faster                                                   |
| unpickle             | 20.2 us                                                  | 19.7 us: 1.02x faster                                                   |
| pickle_list          | 5.34 us                                                  | 5.28 us: 1.01x faster                                                   |
| xml_etree_parse      | 188 ms                                                   | 187 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| pickle               | 13.5 us                                                  | 13.7 us: 1.01x slower                                                   |
| json_loads           | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 265 us: 1.04x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 393 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, pickle_dict, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.75 ms                                                  | 8.90 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                  | 51.4 ms: 1.22x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 80.1 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.3 us: 1.37x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| deepcopy                   | 451 us                                                   | 388 us: 1.16x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 570 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 429 ms: 1.09x faster                                                    |
| async_tree_none            | 493 ms                                                   | 457 ms: 1.08x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.80 us: 1.07x faster                                                   |
| unpickle_list              | 6.65 us                                                  | 6.26 us: 1.06x faster                                                   |
| float                      | 94.4 ms                                                  | 89.1 ms: 1.06x faster                                                   |
| scimark_sor                | 159 ms                                                   | 150 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 720 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 748 ms: 1.02x faster                                                    |
| unpickle                   | 20.2 us                                                  | 19.7 us: 1.02x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 22.0 ms: 1.02x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                                   |
| pickle_list                | 5.34 us                                                  | 5.28 us: 1.01x faster                                                   |
| mako                       | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 187 ms: 1.01x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.96 sec: 1.01x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                   |
| pickle                     | 13.5 us                                                  | 13.7 us: 1.01x slower                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.94 ms: 1.01x slower                                                   |
| async_generators           | 496 ms                                                   | 504 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.75 ms                                                  | 8.90 ms: 1.02x slower                                                   |
| thrift                     | 946 us                                                   | 971 us: 1.03x slower                                                    |
| scimark_fft                | 447 ms                                                   | 460 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| mdp                        | 3.36 sec                                                 | 3.47 sec: 1.03x slower                                                  |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| logging_format             | 7.83 us                                                  | 8.09 us: 1.03x slower                                                   |
| spectral_norm              | 141 ms                                                   | 146 ms: 1.03x slower                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.32 ms: 1.03x slower                                                   |
| json_loads                 | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.82 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 254 us                                                   | 265 us: 1.04x slower                                                    |
| json                       | 5.61 ms                                                  | 5.88 ms: 1.05x slower                                                   |
| logging_simple             | 7.04 us                                                  | 7.42 us: 1.05x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.15 sec: 1.06x slower                                                  |
| telco                      | 9.73 ms                                                  | 10.4 ms: 1.07x slower                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.82 ms: 1.07x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.08x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 89.3 ms: 1.08x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 4.93 ms: 1.09x slower                                                   |
| meteor_contest             | 113 ms                                                   | 124 ms: 1.09x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 70.2 ms: 1.09x slower                                                   |
| pickle_pure_python         | 359 us                                                   | 393 us: 1.09x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 625 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 214 us: 1.11x slower                                                    |
| fannkuch                   | 452 ms                                                   | 504 ms: 1.11x slower                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 93.7 ms: 1.12x slower                                                   |
| tornado_http               | 131 ms                                                   | 147 ms: 1.12x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 4.34 ms: 1.13x slower                                                   |
| pyflate                    | 556 ms                                                   | 627 ms: 1.13x slower                                                    |
| go                         | 163 ms                                                   | 188 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 149 ms: 1.16x slower                                                    |
| raytrace                   | 298 ms                                                   | 352 ms: 1.18x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 1.49 sec: 1.18x slower                                                  |
| comprehensions             | 20.4 us                                                  | 24.6 us: 1.21x slower                                                   |
| django_template            | 42.3 ms                                                  | 51.4 ms: 1.22x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 77.4 ms: 1.24x slower                                                   |
| 2to3                       | 306 ms                                                   | 380 ms: 1.24x slower                                                    |
| richards_super             | 60.3 ms                                                  | 75.0 ms: 1.24x slower                                                   |
| richards                   | 53.5 ms                                                  | 66.8 ms: 1.25x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.73 ms: 1.25x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 124 ms: 1.25x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 2.19 ms: 1.26x slower                                                   |
| chaos                      | 68.8 ms                                                  | 91.4 ms: 1.33x slower                                                   |
| genshi_xml                 | 60.2 ms                                                  | 80.1 ms: 1.33x slower                                                   |
| sympy_expand               | 455 ms                                                   | 606 ms: 1.33x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.25 sec: 1.35x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.94 sec: 1.36x slower                                                  |
| pylint                     | 343 ms                                                   | 466 ms: 1.36x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 28.5 ms: 1.36x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 2.59 sec: 1.37x slower                                                  |
| sympy_str                  | 264 ms                                                   | 366 ms: 1.39x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 10.2 ms: 1.42x slower                                                   |
| regex_compile              | 128 ms                                                   | 188 ms: 1.47x slower                                                    |
| sympy_sum                  | 143 ms                                                   | 214 ms: 1.49x slower                                                    |
| generators                 | 37.8 ms                                                  | 57.3 ms: 1.52x slower                                                   |
| unpack_sequence            | 57.2 ns                                                  | 149 ns: 2.60x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (10): xml_etree_generate, xml_etree_process, pickle_dict, python_startup, nbody, pidigits, json_dumps, logging_silent, sqlite_synth, coverage
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x