# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.39x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 423 ms: 1.46x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.38 sec: 1.20x slower                                                      |
| html5lib       | 71.9 ms                                                      | 107 ms: 1.49x slower                                                        |
| tornado_http   | 120 ms                                                       | 169 ms: 1.41x slower                                                        |
| Geometric mean | (ref)                                                        | 1.38x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 469 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 885 ms: 1.08x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 367 ms: 1.08x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 631 ms: 1.10x slower                                                        |
| async_tree_io              | 847 ms                                                       | 940 ms: 1.11x slower                                                        |
| async_tree_none            | 372 ms                                                       | 416 ms: 1.12x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 675 ms: 1.13x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 515 ms: 1.14x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.86 sec: 1.18x slower                                                      |
| asyncio_tcp                | 380 ms                                                       | 457 ms: 1.20x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 28.0 ms: 1.30x slower                                                       |
| async_generators           | 359 ms                                                       | 488 ms: 1.36x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| float          | 81.9 ms                                                      | 140 ms: 1.71x slower                                                        |
| nbody          | 88.0 ms                                                      | 194 ms: 2.21x slower                                                        |
| Geometric mean | (ref)                                                        | 1.55x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 236 ms: 1.03x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.40 ms: 1.01x slower                                                       |
| regex_v8       | 26.2 ms                                                      | 27.0 ms: 1.03x slower                                                       |
| regex_compile  | 144 ms                                                       | 223 ms: 1.55x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 140 ms: 1.03x faster                                                        |
| pickle_list          | 4.59 us                                                      | 4.50 us: 1.02x faster                                                       |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 105 ms: 1.05x slower                                                        |
| unpickle             | 15.1 us                                                      | 16.8 us: 1.11x slower                                                       |
| unpickle_list        | 4.62 us                                                      | 5.29 us: 1.14x slower                                                       |
| json_loads           | 24.0 us                                                      | 29.0 us: 1.21x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 14.0 ms: 1.28x slower                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 113 ms: 1.32x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 3.31 sec: 1.38x slower                                                      |
| xml_etree_process    | 60.9 ms                                                      | 91.9 ms: 1.51x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 585 us: 1.84x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 396 us: 1.85x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.23x slower                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 17.5 ms: 1.31x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 80.5 ms: 1.40x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 42.6 ms: 1.60x slower                                                       |
| django_template | 38.9 ms                                                      | 66.9 ms: 1.72x slower                                                       |
| mako            | 10.4 ms                                                      | 21.5 ms: 2.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.68x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 2.81 ms: 1.46x faster                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.70 ms: 1.03x faster                                                       |
| regex_dna                  | 244 ms                                                       | 236 ms: 1.03x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 140 ms: 1.03x faster                                                        |
| pickle_list                | 4.59 us                                                      | 4.50 us: 1.02x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.40 ms: 1.01x slower                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 469 ms: 1.02x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 27.0 ms: 1.03x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 4.83 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 105 ms: 1.05x slower                                                        |
| deepcopy                   | 397 us                                                       | 424 us: 1.07x slower                                                        |
| sqlite_synth               | 2.79 us                                                      | 2.98 us: 1.07x slower                                                       |
| async_tree_io_tg           | 819 ms                                                       | 885 ms: 1.08x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 367 ms: 1.08x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 631 ms: 1.10x slower                                                        |
| unpickle                   | 15.1 us                                                      | 16.8 us: 1.11x slower                                                       |
| async_tree_io              | 847 ms                                                       | 940 ms: 1.11x slower                                                        |
| async_tree_none            | 372 ms                                                       | 416 ms: 1.12x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 19.6 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 675 ms: 1.13x slower                                                        |
| json                       | 5.22 ms                                                      | 5.93 ms: 1.14x slower                                                       |
| async_tree_memoization     | 452 ms                                                       | 515 ms: 1.14x slower                                                        |
| unpickle_list              | 4.62 us                                                      | 5.29 us: 1.14x slower                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.86 sec: 1.18x slower                                                      |
| asyncio_tcp                | 380 ms                                                       | 457 ms: 1.20x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.38 sec: 1.20x slower                                                      |
| json_loads                 | 24.0 us                                                      | 29.0 us: 1.21x slower                                                       |
| telco                      | 8.58 ms                                                      | 10.4 ms: 1.21x slower                                                       |
| deepcopy_memo              | 39.5 us                                                      | 48.4 us: 1.23x slower                                                       |
| scimark_fft                | 314 ms                                                       | 388 ms: 1.24x slower                                                        |
| generators                 | 33.5 ms                                                      | 41.4 ms: 1.24x slower                                                       |
| pylint                     | 346 ms                                                       | 436 ms: 1.26x slower                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 4.53 us: 1.28x slower                                                       |
| json_dumps                 | 11.0 ms                                                      | 14.0 ms: 1.28x slower                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 6.54 sec: 1.28x slower                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.52 ms: 1.29x slower                                                       |
| mdp                        | 2.52 sec                                                     | 3.26 sec: 1.29x slower                                                      |
| meteor_contest             | 128 ms                                                       | 166 ms: 1.29x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 28.0 ms: 1.30x slower                                                       |
| python_startup             | 13.3 ms                                                      | 17.5 ms: 1.31x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 113 ms: 1.32x slower                                                        |
| coverage                   | 81.1 ms                                                      | 109 ms: 1.34x slower                                                        |
| async_generators           | 359 ms                                                       | 488 ms: 1.36x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 89.2 ms: 1.36x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 3.31 sec: 1.38x slower                                                      |
| sympy_integrate            | 23.3 ms                                                      | 32.1 ms: 1.38x slower                                                       |
| pycparser                  | 1.26 sec                                                     | 1.74 sec: 1.38x slower                                                      |
| genshi_xml                 | 57.3 ms                                                      | 80.5 ms: 1.40x slower                                                       |
| tornado_http               | 120 ms                                                       | 169 ms: 1.41x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 128 ms: 1.45x slower                                                        |
| 2to3                       | 291 ms                                                       | 423 ms: 1.46x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 107 ms: 1.49x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 261 us: 1.50x slower                                                        |
| xml_etree_process          | 60.9 ms                                                      | 91.9 ms: 1.51x slower                                                       |
| sympy_str                  | 296 ms                                                       | 447 ms: 1.51x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 180 ms: 1.52x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 90.5 ms: 1.52x slower                                                       |
| richards                   | 52.7 ms                                                      | 81.4 ms: 1.54x slower                                                       |
| thrift                     | 877 us                                                       | 1.36 ms: 1.55x slower                                                       |
| regex_compile              | 144 ms                                                       | 223 ms: 1.55x slower                                                        |
| pyflate                    | 492 ms                                                       | 767 ms: 1.56x slower                                                        |
| sympy_expand               | 505 ms                                                       | 807 ms: 1.60x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 42.6 ms: 1.60x slower                                                       |
| richards_super             | 59.8 ms                                                      | 97.4 ms: 1.63x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 120 ms: 1.65x slower                                                        |
| pprint_safe_repr           | 812 ms                                                       | 1.35 sec: 1.67x slower                                                      |
| sympy_sum                  | 154 ms                                                       | 259 ms: 1.68x slower                                                        |
| spectral_norm              | 97.4 ms                                                      | 164 ms: 1.69x slower                                                        |
| fannkuch                   | 365 ms                                                       | 619 ms: 1.70x slower                                                        |
| comprehensions             | 17.3 us                                                      | 29.3 us: 1.70x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.81 sec: 1.70x slower                                                      |
| float                      | 81.9 ms                                                      | 140 ms: 1.71x slower                                                        |
| django_template            | 38.9 ms                                                      | 66.9 ms: 1.72x slower                                                       |
| logging_format             | 7.07 us                                                      | 12.4 us: 1.75x slower                                                       |
| logging_simple             | 6.40 us                                                      | 11.5 us: 1.80x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 11.5 ms: 1.81x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 1.66 ms: 1.84x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 585 us: 1.84x slower                                                        |
| unpickle_pure_python       | 214 us                                                       | 396 us: 1.85x slower                                                        |
| go                         | 160 ms                                                       | 301 ms: 1.88x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.35 ms: 1.88x slower                                                       |
| logging_silent             | 97.7 ns                                                      | 187 ns: 1.91x slower                                                        |
| chaos                      | 61.7 ms                                                      | 122 ms: 1.98x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 131 ms: 2.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.83 ms: 2.05x slower                                                       |
| scimark_sor                | 126 ms                                                       | 258 ms: 2.05x slower                                                        |
| mako                       | 10.4 ms                                                      | 21.5 ms: 2.06x slower                                                       |
| raytrace                   | 289 ms                                                       | 605 ms: 2.09x slower                                                        |
| nbody                      | 88.0 ms                                                      | 194 ms: 2.21x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 217 ms: 2.22x slower                                                        |
| unpack_sequence            | 56.8 ns                                                      | 130 ns: 2.29x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 8.17 ms: 2.40x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.39x slower                                                                |

Benchmark hidden because not significant (2): pickle_dict, asyncio_websockets
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.17x