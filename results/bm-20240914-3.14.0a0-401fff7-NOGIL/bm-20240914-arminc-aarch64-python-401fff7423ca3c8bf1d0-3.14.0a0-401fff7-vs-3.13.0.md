# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.52x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 509 ms: 1.67x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.97 sec: 1.37x slower                                                  |
| html5lib       | 64.3 ms                                                  | 118 ms: 1.84x slower                                                    |
| tornado_http   | 131 ms                                                   | 203 ms: 1.55x slower                                                    |
| Geometric mean | (ref)                                                    | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 692 ms: 1.07x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 723 ms: 1.16x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 866 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 901 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 677 ms: 1.19x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.61 sec: 1.20x slower                                                  |
| async_tree_none_tg         | 467 ms                                                   | 562 ms: 1.20x slower                                                    |
| async_tree_none            | 493 ms                                                   | 600 ms: 1.22x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.34 sec: 1.23x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.37 sec: 1.24x slower                                                  |
| async_generators           | 496 ms                                                   | 656 ms: 1.32x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 39.2 ms: 1.39x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 205 ms: 2.17x slower                                                    |
| nbody          | 114 ms                                                   | 281 ms: 2.47x slower                                                    |
| Geometric mean | (ref)                                                    | 1.75x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.47 ms: 1.09x faster                                                   |
| regex_v8       | 31.5 ms                                                  | 32.2 ms: 1.02x slower                                                   |
| regex_dna      | 246 ms                                                   | 258 ms: 1.05x slower                                                    |
| regex_compile  | 128 ms                                                   | 246 ms: 1.91x slower                                                    |
| Geometric mean | (ref)                                                    | 1.17x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 183 ms: 1.02x faster                                                    |
| pickle               | 13.5 us                                                  | 13.2 us: 1.02x faster                                                   |
| pickle_dict          | 38.1 us                                                  | 39.0 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 153 ms: 1.04x slower                                                    |
| unpickle_list        | 6.65 us                                                  | 6.98 us: 1.05x slower                                                   |
| unpickle             | 20.2 us                                                  | 21.5 us: 1.07x slower                                                   |
| json_loads           | 31.4 us                                                  | 38.1 us: 1.21x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 17.4 ms: 1.30x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 155 ms: 1.37x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 125 ms: 1.56x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.12 sec: 1.63x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 525 us: 2.06x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 749 us: 2.08x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.27x slower                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 18.1 ms: 1.36x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 12.0 ms: 1.37x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.37x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 100 ms: 1.66x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 51.0 ms: 1.84x slower                                                   |
| django_template | 42.3 ms                                                  | 79.2 ms: 1.87x slower                                                   |
| mako            | 13.3 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.87x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.60 ms: 1.32x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.46 ms: 1.31x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.47 ms: 1.09x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 6.94 ms: 1.05x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 183 ms: 1.02x faster                                                    |
| pickle                     | 13.5 us                                                  | 13.2 us: 1.02x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 32.2 ms: 1.02x slower                                                   |
| pickle_dict                | 38.1 us                                                  | 39.0 us: 1.02x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 153 ms: 1.04x slower                                                    |
| sqlite_synth               | 3.84 us                                                  | 4.01 us: 1.04x slower                                                   |
| regex_dna                  | 246 ms                                                   | 258 ms: 1.05x slower                                                    |
| unpickle_list              | 6.65 us                                                  | 6.98 us: 1.05x slower                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 692 ms: 1.07x slower                                                    |
| unpickle                   | 20.2 us                                                  | 21.5 us: 1.07x slower                                                   |
| async_tree_memoization     | 626 ms                                                   | 723 ms: 1.16x slower                                                    |
| pathlib                    | 22.4 ms                                                  | 26.1 ms: 1.17x slower                                                   |
| deepcopy                   | 451 us                                                   | 530 us: 1.18x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 866 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 901 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 677 ms: 1.19x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.61 sec: 1.20x slower                                                  |
| json                       | 5.61 ms                                                  | 6.75 ms: 1.20x slower                                                   |
| async_tree_none_tg         | 467 ms                                                   | 562 ms: 1.20x slower                                                    |
| json_loads                 | 31.4 us                                                  | 38.1 us: 1.21x slower                                                   |
| async_tree_none            | 493 ms                                                   | 600 ms: 1.22x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.34 sec: 1.23x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.37 sec: 1.24x slower                                                  |
| mdp                        | 3.36 sec                                                 | 4.29 sec: 1.28x slower                                                  |
| scimark_fft                | 447 ms                                                   | 579 ms: 1.29x slower                                                    |
| json_dumps                 | 13.4 ms                                                  | 17.4 ms: 1.30x slower                                                   |
| telco                      | 9.73 ms                                                  | 12.7 ms: 1.30x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.64 ms: 1.31x slower                                                   |
| async_generators           | 496 ms                                                   | 656 ms: 1.32x slower                                                    |
| coverage                   | 98.5 ms                                                  | 130 ms: 1.32x slower                                                    |
| deepcopy_memo              | 51.0 us                                                  | 67.7 us: 1.33x slower                                                   |
| python_startup             | 13.3 ms                                                  | 18.1 ms: 1.36x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.97 sec: 1.37x slower                                                  |
| python_startup_no_site     | 8.75 ms                                                  | 12.0 ms: 1.37x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 155 ms: 1.37x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 39.2 ms: 1.39x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 5.71 us: 1.40x slower                                                   |
| meteor_contest             | 113 ms                                                   | 167 ms: 1.47x slower                                                    |
| pylint                     | 343 ms                                                   | 506 ms: 1.47x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 149 ms: 1.51x slower                                                    |
| generators                 | 37.8 ms                                                  | 58.3 ms: 1.54x slower                                                   |
| tornado_http               | 131 ms                                                   | 203 ms: 1.55x slower                                                    |
| xml_etree_process          | 80.1 ms                                                  | 125 ms: 1.56x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 1.99 sec: 1.58x slower                                                  |
| bpe_tokeniser              | 5.90 sec                                                 | 9.33 sec: 1.58x slower                                                  |
| bench_thread_pool          | 1.28 ms                                                  | 2.02 ms: 1.58x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 4.12 sec: 1.63x slower                                                  |
| spectral_norm              | 141 ms                                                   | 231 ms: 1.64x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 34.4 ms: 1.64x slower                                                   |
| fannkuch                   | 452 ms                                                   | 741 ms: 1.64x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 137 ms: 1.66x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 100 ms: 1.66x slower                                                    |
| 2to3                       | 306 ms                                                   | 509 ms: 1.67x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 324 us: 1.69x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 219 ms: 1.70x slower                                                    |
| thrift                     | 946 us                                                   | 1.63 ms: 1.73x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 109 ms: 1.75x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.65 sec: 1.78x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.40 sec: 1.79x slower                                                  |
| pyflate                    | 556 ms                                                   | 1.00 sec: 1.80x slower                                                  |
| html5lib                   | 64.3 ms                                                  | 118 ms: 1.84x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 51.0 ms: 1.84x slower                                                   |
| django_template            | 42.3 ms                                                  | 79.2 ms: 1.87x slower                                                   |
| regex_compile              | 128 ms                                                   | 246 ms: 1.91x slower                                                    |
| sympy_str                  | 264 ms                                                   | 507 ms: 1.92x slower                                                    |
| comprehensions             | 20.4 us                                                  | 40.1 us: 1.97x slower                                                   |
| logging_format             | 7.83 us                                                  | 15.5 us: 1.98x slower                                                   |
| logging_simple             | 7.04 us                                                  | 14.1 us: 2.00x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 172 ms: 2.05x slower                                                    |
| sympy_expand               | 455 ms                                                   | 936 ms: 2.06x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 525 us: 2.06x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 749 us: 2.08x slower                                                    |
| logging_silent             | 135 ns                                                   | 285 ns: 2.11x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| hexiom                     | 7.13 ms                                                  | 15.3 ms: 2.14x slower                                                   |
| scimark_sor                | 159 ms                                                   | 341 ms: 2.15x slower                                                    |
| float                      | 94.4 ms                                                  | 205 ms: 2.17x slower                                                    |
| sympy_sum                  | 143 ms                                                   | 317 ms: 2.21x slower                                                    |
| richards                   | 53.5 ms                                                  | 119 ms: 2.22x slower                                                    |
| chaos                      | 68.8 ms                                                  | 160 ms: 2.32x slower                                                    |
| richards_super             | 60.3 ms                                                  | 140 ms: 2.32x slower                                                    |
| go                         | 163 ms                                                   | 382 ms: 2.35x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 329 ms: 2.36x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.22 ms: 2.44x slower                                                   |
| nbody                      | 114 ms                                                   | 281 ms: 2.47x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.71 ms: 2.69x slower                                                   |
| raytrace                   | 298 ms                                                   | 813 ms: 2.73x slower                                                    |
| unpack_sequence            | 57.2 ns                                                  | 182 ns: 3.19x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.5 ms: 3.24x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.52x slower                                                            |

Benchmark hidden because not significant (2): pickle_list, pidigits
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.43x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.17x