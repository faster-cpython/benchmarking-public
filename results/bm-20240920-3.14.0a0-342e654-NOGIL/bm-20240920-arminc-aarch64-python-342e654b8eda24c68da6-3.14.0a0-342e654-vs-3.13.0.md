# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.52x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 508 ms: 1.66x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.93 sec: 1.35x slower                                                  |
| html5lib       | 64.3 ms                                                  | 118 ms: 1.84x slower                                                    |
| tornado_http   | 131 ms                                                   | 203 ms: 1.55x slower                                                    |
| Geometric mean | (ref)                                                    | 1.59x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 676 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 689 ms: 1.06x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 862 ms: 1.17x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 897 ms: 1.17x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 735 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 668 ms: 1.18x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.59 sec: 1.19x slower                                                  |
| async_tree_none_tg         | 467 ms                                                   | 565 ms: 1.21x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.34 sec: 1.22x slower                                                  |
| async_tree_none            | 493 ms                                                   | 604 ms: 1.23x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.37 sec: 1.24x slower                                                  |
| async_generators           | 496 ms                                                   | 653 ms: 1.32x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 39.3 ms: 1.39x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 205 ms: 2.17x slower                                                    |
| nbody          | 114 ms                                                   | 279 ms: 2.44x slower                                                    |
| Geometric mean | (ref)                                                    | 1.74x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.42 ms: 1.10x faster                                                   |
| regex_v8       | 31.5 ms                                                  | 32.5 ms: 1.03x slower                                                   |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| regex_compile  | 128 ms                                                   | 248 ms: 1.93x slower                                                    |
| Geometric mean | (ref)                                                    | 1.17x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 182 ms: 1.03x faster                                                    |
| pickle               | 13.5 us                                                  | 13.1 us: 1.03x faster                                                   |
| pickle_list          | 5.34 us                                                  | 5.41 us: 1.01x slower                                                   |
| pickle_dict          | 38.1 us                                                  | 39.4 us: 1.03x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 152 ms: 1.04x slower                                                    |
| unpickle             | 20.2 us                                                  | 21.3 us: 1.06x slower                                                   |
| unpickle_list        | 6.65 us                                                  | 7.12 us: 1.07x slower                                                   |
| json_loads           | 31.4 us                                                  | 37.9 us: 1.21x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 17.8 ms: 1.34x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 155 ms: 1.37x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 125 ms: 1.57x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.11 sec: 1.63x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 526 us: 2.07x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 754 us: 2.10x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.27x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 18.1 ms: 1.37x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 12.1 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.38x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 101 ms: 1.68x slower                                                    |
| django_template | 42.3 ms                                                  | 79.0 ms: 1.87x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 52.1 ms: 1.88x slower                                                   |
| mako            | 13.3 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.88x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.53 ms                                                  | 3.44 ms: 1.32x faster                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 1.61 ms: 1.31x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.42 ms: 1.10x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 6.69 ms: 1.09x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 182 ms: 1.03x faster                                                    |
| pickle                     | 13.5 us                                                  | 13.1 us: 1.03x faster                                                   |
| pickle_list                | 5.34 us                                                  | 5.41 us: 1.01x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 676 ms: 1.03x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 32.5 ms: 1.03x slower                                                   |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| pickle_dict                | 38.1 us                                                  | 39.4 us: 1.03x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 152 ms: 1.04x slower                                                    |
| unpickle                   | 20.2 us                                                  | 21.3 us: 1.06x slower                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 689 ms: 1.06x slower                                                    |
| sqlite_synth               | 3.84 us                                                  | 4.08 us: 1.06x slower                                                   |
| unpickle_list              | 6.65 us                                                  | 7.12 us: 1.07x slower                                                   |
| pathlib                    | 22.4 ms                                                  | 25.7 ms: 1.15x slower                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 862 ms: 1.17x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 897 ms: 1.17x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 735 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 668 ms: 1.18x slower                                                    |
| deepcopy                   | 451 us                                                   | 531 us: 1.18x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.59 sec: 1.19x slower                                                  |
| json_loads                 | 31.4 us                                                  | 37.9 us: 1.21x slower                                                   |
| json                       | 5.61 ms                                                  | 6.77 ms: 1.21x slower                                                   |
| async_tree_none_tg         | 467 ms                                                   | 565 ms: 1.21x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.34 sec: 1.22x slower                                                  |
| async_tree_none            | 493 ms                                                   | 604 ms: 1.23x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.37 sec: 1.24x slower                                                  |
| mdp                        | 3.36 sec                                                 | 4.28 sec: 1.27x slower                                                  |
| scimark_fft                | 447 ms                                                   | 574 ms: 1.28x slower                                                    |
| async_generators           | 496 ms                                                   | 653 ms: 1.32x slower                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.66 ms: 1.32x slower                                                   |
| telco                      | 9.73 ms                                                  | 12.9 ms: 1.32x slower                                                   |
| deepcopy_memo              | 51.0 us                                                  | 67.9 us: 1.33x slower                                                   |
| json_dumps                 | 13.4 ms                                                  | 17.8 ms: 1.34x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.93 sec: 1.35x slower                                                  |
| coverage                   | 98.5 ms                                                  | 133 ms: 1.35x slower                                                    |
| python_startup             | 13.3 ms                                                  | 18.1 ms: 1.37x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 155 ms: 1.37x slower                                                    |
| python_startup_no_site     | 8.75 ms                                                  | 12.1 ms: 1.38x slower                                                   |
| coroutines                 | 28.2 ms                                                  | 39.3 ms: 1.39x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 5.76 us: 1.42x slower                                                   |
| pylint                     | 343 ms                                                   | 499 ms: 1.46x slower                                                    |
| meteor_contest             | 113 ms                                                   | 166 ms: 1.46x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 149 ms: 1.51x slower                                                    |
| generators                 | 37.8 ms                                                  | 57.8 ms: 1.53x slower                                                   |
| tornado_http               | 131 ms                                                   | 203 ms: 1.55x slower                                                    |
| xml_etree_process          | 80.1 ms                                                  | 125 ms: 1.57x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 9.28 sec: 1.57x slower                                                  |
| bench_thread_pool          | 1.28 ms                                                  | 2.01 ms: 1.58x slower                                                   |
| pycparser                  | 1.26 sec                                                 | 2.00 sec: 1.59x slower                                                  |
| spectral_norm              | 141 ms                                                   | 225 ms: 1.59x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 4.11 sec: 1.63x slower                                                  |
| sympy_integrate            | 21.0 ms                                                  | 34.6 ms: 1.65x slower                                                   |
| 2to3                       | 306 ms                                                   | 508 ms: 1.66x slower                                                    |
| fannkuch                   | 452 ms                                                   | 753 ms: 1.67x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 101 ms: 1.68x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 139 ms: 1.68x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 324 us: 1.69x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 217 ms: 1.69x slower                                                    |
| thrift                     | 946 us                                                   | 1.62 ms: 1.72x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 110 ms: 1.76x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.67 sec: 1.80x slower                                                  |
| pyflate                    | 556 ms                                                   | 1.00 sec: 1.80x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.43 sec: 1.81x slower                                                  |
| html5lib                   | 64.3 ms                                                  | 118 ms: 1.84x slower                                                    |
| django_template            | 42.3 ms                                                  | 79.0 ms: 1.87x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 52.1 ms: 1.88x slower                                                   |
| sympy_str                  | 264 ms                                                   | 504 ms: 1.91x slower                                                    |
| regex_compile              | 128 ms                                                   | 248 ms: 1.93x slower                                                    |
| logging_format             | 7.83 us                                                  | 15.4 us: 1.96x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.2 us: 1.97x slower                                                   |
| logging_simple             | 7.04 us                                                  | 14.1 us: 2.00x slower                                                   |
| sympy_expand               | 455 ms                                                   | 936 ms: 2.06x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 526 us: 2.07x slower                                                    |
| logging_silent             | 135 ns                                                   | 284 ns: 2.10x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 754 us: 2.10x slower                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 176 ms: 2.10x slower                                                    |
| scimark_sor                | 159 ms                                                   | 337 ms: 2.12x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| richards                   | 53.5 ms                                                  | 115 ms: 2.15x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 15.4 ms: 2.16x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 310 ms: 2.16x slower                                                    |
| float                      | 94.4 ms                                                  | 205 ms: 2.17x slower                                                    |
| richards_super             | 60.3 ms                                                  | 135 ms: 2.24x slower                                                    |
| chaos                      | 68.8 ms                                                  | 161 ms: 2.34x slower                                                    |
| go                         | 163 ms                                                   | 384 ms: 2.36x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 330 ms: 2.37x slower                                                    |
| nbody                      | 114 ms                                                   | 279 ms: 2.44x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.28 ms: 2.47x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 3.72 ms: 2.69x slower                                                   |
| raytrace                   | 298 ms                                                   | 821 ms: 2.76x slower                                                    |
| unpack_sequence            | 57.2 ns                                                  | 183 ns: 3.19x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.4 ms: 3.22x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.52x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.43x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.17x