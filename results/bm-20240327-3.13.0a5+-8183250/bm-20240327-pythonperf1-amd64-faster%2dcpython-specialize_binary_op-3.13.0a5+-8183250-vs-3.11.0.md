# Results vs. 3.11.0

- fork: faster-cpython
- ref: specialize_binary_op
- machine: windows-amd64
- commit hash: 8183250
- commit date: 2024-03-27
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| chameleon      | 5.26 ms                                                     | 4.76 ms: 1.10x faster                                                                 |
| docutils       | 1.64 sec                                                    | 1.63 sec: 1.01x faster                                                                |
| html5lib       | 38.9 ms                                                     | 36.5 ms: 1.06x faster                                                                 |
| tornado_http   | 92.8 ms                                                     | 84.0 ms: 1.11x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 405 ms                                                      | 269 ms: 1.50x faster                                                                  |
| async_tree_none            | 332 ms                                                      | 223 ms: 1.49x faster                                                                  |
| async_tree_io_tg           | 829 ms                                                      | 562 ms: 1.47x faster                                                                  |
| async_tree_none_tg         | 309 ms                                                      | 210 ms: 1.47x faster                                                                  |
| async_tree_memoization     | 399 ms                                                      | 276 ms: 1.45x faster                                                                  |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 382 ms: 1.39x faster                                                                  |
| async_tree_io              | 808 ms                                                      | 585 ms: 1.38x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 383 ms: 1.36x faster                                                                  |
| Geometric mean             | (ref)                                                       | 1.44x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 54.4 ms                                                     | 51.8 ms: 1.05x faster                                                                 |
| pidigits       | 150 ms                                                      | 147 ms: 1.02x faster                                                                  |
| nbody          | 70.3 ms                                                     | 77.5 ms: 1.10x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 81.3 ms: 1.12x faster                                                                 |
| regex_dna      | 116 ms                                                      | 115 ms: 1.01x faster                                                                  |
| regex_effbot   | 1.50 ms                                                     | 1.55 ms: 1.03x slower                                                                 |
| regex_v8       | 14.2 ms                                                     | 16.3 ms: 1.15x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.55 ms: 1.46x faster                                                                 |
| unpickle_pure_python | 157 us                                                      | 127 us: 1.24x faster                                                                  |
| pickle_pure_python   | 208 us                                                      | 179 us: 1.17x faster                                                                  |
| xml_etree_parse      | 97.6 ms                                                     | 93.8 ms: 1.04x faster                                                                 |
| xml_etree_iterparse  | 65.6 ms                                                     | 63.7 ms: 1.03x faster                                                                 |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.02x faster                                                                 |
| xml_etree_process    | 37.2 ms                                                     | 37.3 ms: 1.00x slower                                                                 |
| tomli_loads          | 1.46 sec                                                    | 1.47 sec: 1.01x slower                                                                |
| xml_etree_generate   | 52.5 ms                                                     | 54.3 ms: 1.03x slower                                                                 |
| pickle_list          | 2.70 us                                                     | 2.87 us: 1.07x slower                                                                 |
| json_loads           | 13.0 us                                                     | 14.1 us: 1.08x slower                                                                 |
| unpickle_list        | 2.59 us                                                     | 2.82 us: 1.09x slower                                                                 |
| pickle               | 6.64 us                                                     | 7.26 us: 1.09x slower                                                                 |
| unpickle             | 7.57 us                                                     | 8.47 us: 1.12x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 20.4 ms: 1.03x slower                                                                 |
| python_startup_no_site | 16.8 ms                                                     | 17.9 ms: 1.07x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 6.35 ms: 1.19x faster                                                                 |
| genshi_text     | 18.4 ms                                                     | 15.8 ms: 1.17x faster                                                                 |
| genshi_xml      | 39.9 ms                                                     | 35.0 ms: 1.14x faster                                                                 |
| django_template | 24.4 ms                                                     | 22.6 ms: 1.08x faster                                                                 |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-pythonperf1-amd64-faster%2dcpython-specialize_binary_op-3.13.0a5+-8183250 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 71.6 us: 4.55x faster                                                                 |
| generators                 | 34.0 ms                                                     | 21.7 ms: 1.56x faster                                                                 |
| pylint                     | 323 ms                                                      | 210 ms: 1.54x faster                                                                  |
| asyncio_tcp                | 726 ms                                                      | 478 ms: 1.52x faster                                                                  |
| async_tree_memoization_tg  | 405 ms                                                      | 269 ms: 1.50x faster                                                                  |
| async_tree_none            | 332 ms                                                      | 223 ms: 1.49x faster                                                                  |
| async_tree_io_tg           | 829 ms                                                      | 562 ms: 1.47x faster                                                                  |
| async_tree_none_tg         | 309 ms                                                      | 210 ms: 1.47x faster                                                                  |
| comprehensions             | 15.6 us                                                     | 10.7 us: 1.46x faster                                                                 |
| json_dumps                 | 8.09 ms                                                     | 5.55 ms: 1.46x faster                                                                 |
| async_tree_memoization     | 399 ms                                                      | 276 ms: 1.45x faster                                                                  |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 382 ms: 1.39x faster                                                                  |
| async_tree_io              | 808 ms                                                      | 585 ms: 1.38x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 383 ms: 1.36x faster                                                                  |
| deltablue                  | 2.70 ms                                                     | 2.04 ms: 1.33x faster                                                                 |
| unpack_sequence            | 46.9 ns                                                     | 36.6 ns: 1.28x faster                                                                 |
| logging_silent             | 71.8 ns                                                     | 56.6 ns: 1.27x faster                                                                 |
| raytrace                   | 213 ms                                                      | 169 ms: 1.27x faster                                                                  |
| unpickle_pure_python       | 157 us                                                      | 127 us: 1.24x faster                                                                  |
| sqlglot_parse              | 953 us                                                      | 784 us: 1.22x faster                                                                  |
| richards_super             | 38.7 ms                                                     | 32.0 ms: 1.21x faster                                                                 |
| hexiom                     | 4.55 ms                                                     | 3.78 ms: 1.21x faster                                                                 |
| sympy_sum                  | 100 ms                                                      | 83.5 ms: 1.20x faster                                                                 |
| deepcopy_memo              | 26.0 us                                                     | 21.7 us: 1.19x faster                                                                 |
| mako                       | 7.58 ms                                                     | 6.35 ms: 1.19x faster                                                                 |
| sqlglot_transpile          | 1.16 ms                                                     | 990 us: 1.18x faster                                                                  |
| pickle_pure_python         | 208 us                                                      | 179 us: 1.17x faster                                                                  |
| genshi_text                | 18.4 ms                                                     | 15.8 ms: 1.17x faster                                                                 |
| sympy_str                  | 185 ms                                                      | 159 ms: 1.16x faster                                                                  |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.74 sec: 1.16x faster                                                                |
| chaos                      | 48.4 ms                                                     | 42.0 ms: 1.15x faster                                                                 |
| go                         | 101 ms                                                      | 88.4 ms: 1.14x faster                                                                 |
| genshi_xml                 | 39.9 ms                                                     | 35.0 ms: 1.14x faster                                                                 |
| sympy_integrate            | 14.0 ms                                                     | 12.3 ms: 1.14x faster                                                                 |
| dulwich_log                | 46.4 ms                                                     | 40.9 ms: 1.14x faster                                                                 |
| deepcopy                   | 246 us                                                      | 217 us: 1.13x faster                                                                  |
| regex_compile              | 91.0 ms                                                     | 81.3 ms: 1.12x faster                                                                 |
| logging_simple             | 6.86 us                                                     | 6.18 us: 1.11x faster                                                                 |
| sympy_expand               | 299 ms                                                      | 270 ms: 1.11x faster                                                                  |
| tornado_http               | 92.8 ms                                                     | 84.0 ms: 1.11x faster                                                                 |
| chameleon                  | 5.26 ms                                                     | 4.76 ms: 1.10x faster                                                                 |
| pprint_pformat             | 1.09 sec                                                    | 985 ms: 1.10x faster                                                                  |
| nqueens                    | 68.3 ms                                                     | 62.0 ms: 1.10x faster                                                                 |
| scimark_lu                 | 62.8 ms                                                     | 57.1 ms: 1.10x faster                                                                 |
| richards                   | 31.4 ms                                                     | 28.6 ms: 1.10x faster                                                                 |
| pprint_safe_repr           | 529 ms                                                      | 485 ms: 1.09x faster                                                                  |
| mdp                        | 1.59 sec                                                    | 1.46 sec: 1.09x faster                                                                |
| sqlite_synth               | 1.77 us                                                     | 1.62 us: 1.09x faster                                                                 |
| bench_thread_pool          | 872 us                                                      | 801 us: 1.09x faster                                                                  |
| django_template            | 24.4 ms                                                     | 22.6 ms: 1.08x faster                                                                 |
| logging_format             | 7.16 us                                                     | 6.65 us: 1.08x faster                                                                 |
| sqlglot_normalize          | 190 ms                                                      | 178 ms: 1.07x faster                                                                  |
| scimark_monte_carlo        | 45.3 ms                                                     | 42.6 ms: 1.06x faster                                                                 |
| html5lib                   | 38.9 ms                                                     | 36.5 ms: 1.06x faster                                                                 |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                                                 |
| pycparser                  | 720 ms                                                      | 684 ms: 1.05x faster                                                                  |
| meteor_contest             | 75.2 ms                                                     | 71.5 ms: 1.05x faster                                                                 |
| float                      | 54.4 ms                                                     | 51.8 ms: 1.05x faster                                                                 |
| mypy2                      | 459 ms                                                      | 438 ms: 1.05x faster                                                                  |
| crypto_pyaes               | 48.9 ms                                                     | 46.7 ms: 1.05x faster                                                                 |
| coroutines                 | 15.0 ms                                                     | 14.4 ms: 1.04x faster                                                                 |
| xml_etree_parse            | 97.6 ms                                                     | 93.8 ms: 1.04x faster                                                                 |
| pyflate                    | 312 ms                                                      | 302 ms: 1.03x faster                                                                  |
| xml_etree_iterparse        | 65.6 ms                                                     | 63.7 ms: 1.03x faster                                                                 |
| sqlglot_optimize           | 34.5 ms                                                     | 33.8 ms: 1.02x faster                                                                 |
| pidigits                   | 150 ms                                                      | 147 ms: 1.02x faster                                                                  |
| pickle_dict                | 18.5 us                                                     | 18.1 us: 1.02x faster                                                                 |
| gc_traversal               | 1.49 ms                                                     | 1.48 ms: 1.01x faster                                                                 |
| regex_dna                  | 116 ms                                                      | 115 ms: 1.01x faster                                                                  |
| docutils                   | 1.64 sec                                                    | 1.63 sec: 1.01x faster                                                                |
| xml_etree_process          | 37.2 ms                                                     | 37.3 ms: 1.00x slower                                                                 |
| bench_mp_pool              | 63.2 ms                                                     | 63.9 ms: 1.01x slower                                                                 |
| tomli_loads                | 1.46 sec                                                    | 1.47 sec: 1.01x slower                                                                |
| aiohttp                    | 883 us                                                      | 901 us: 1.02x slower                                                                  |
| create_gc_cycles           | 713 us                                                      | 729 us: 1.02x slower                                                                  |
| python_startup             | 19.8 ms                                                     | 20.4 ms: 1.03x slower                                                                 |
| regex_effbot               | 1.50 ms                                                     | 1.55 ms: 1.03x slower                                                                 |
| xml_etree_generate         | 52.5 ms                                                     | 54.3 ms: 1.03x slower                                                                 |
| python_startup_no_site     | 16.8 ms                                                     | 17.9 ms: 1.07x slower                                                                 |
| pickle_list                | 2.70 us                                                     | 2.87 us: 1.07x slower                                                                 |
| coverage                   | 43.4 ms                                                     | 46.8 ms: 1.08x slower                                                                 |
| fannkuch                   | 253 ms                                                      | 274 ms: 1.08x slower                                                                  |
| json_loads                 | 13.0 us                                                     | 14.1 us: 1.08x slower                                                                 |
| unpickle_list              | 2.59 us                                                     | 2.82 us: 1.09x slower                                                                 |
| scimark_sor                | 78.1 ms                                                     | 85.2 ms: 1.09x slower                                                                 |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.81 ms: 1.09x slower                                                                 |
| pathlib                    | 70.9 ms                                                     | 77.5 ms: 1.09x slower                                                                 |
| pickle                     | 6.64 us                                                     | 7.26 us: 1.09x slower                                                                 |
| spectral_norm              | 68.3 ms                                                     | 75.0 ms: 1.10x slower                                                                 |
| nbody                      | 70.3 ms                                                     | 77.5 ms: 1.10x slower                                                                 |
| unpickle                   | 7.57 us                                                     | 8.47 us: 1.12x slower                                                                 |
| regex_v8                   | 14.2 ms                                                     | 16.3 ms: 1.15x slower                                                                 |
| scimark_fft                | 179 ms                                                      | 209 ms: 1.17x slower                                                                  |
| telco                      | 4.06 ms                                                     | 4.88 ms: 1.20x slower                                                                 |
| async_generators           | 177 ms                                                      | 233 ms: 1.32x slower                                                                  |
| thrift                     | 494 us                                                      | 8.20 ms: 16.61x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                          |

Benchmark hidden because not significant (2): json, 2to3
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x


# Memory

- memory change: unknown