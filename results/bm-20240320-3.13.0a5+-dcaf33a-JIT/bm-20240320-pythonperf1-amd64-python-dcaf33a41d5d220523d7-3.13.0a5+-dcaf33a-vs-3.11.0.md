# Results vs. 3.11.0

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: windows-amd64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.14x slower
- HPT reliability: 65.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 235 ms: 1.10x slower                                                        |
| chameleon      | 5.26 ms                                                     | 4.67 ms: 1.13x faster                                                       |
| docutils       | 1.64 sec                                                    | 2.43 sec: 1.48x slower                                                      |
| html5lib       | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                                       |
| tornado_http   | 92.8 ms                                                     | 86.9 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 530 ms                                                      | 2.25 sec: 4.25x slower                                                      |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 2.46 sec: 4.70x slower                                                      |
| async_tree_none            | 332 ms                                                      | 1.81 sec: 5.46x slower                                                      |
| async_tree_memoization     | 399 ms                                                      | 2.32 sec: 5.81x slower                                                      |
| async_tree_memoization_tg  | 405 ms                                                      | 2.53 sec: 6.25x slower                                                      |
| async_tree_none_tg         | 309 ms                                                      | 1.99 sec: 6.46x slower                                                      |
| async_tree_io              | 808 ms                                                      | 7.30 sec: 9.04x slower                                                      |
| async_tree_io_tg           | 829 ms                                                      | 7.85 sec: 9.47x slower                                                      |
| Geometric mean             | (ref)                                                       | 6.20x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.3 ms                                                     | 58.4 ms: 1.20x faster                                                       |
| pidigits       | 150 ms                                                      | 147 ms: 1.02x faster                                                        |
| float          | 54.4 ms                                                     | 81.6 ms: 1.50x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 82.8 ms: 1.10x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| regex_dna      | 116 ms                                                      | 120 ms: 1.04x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.59 ms: 1.45x faster                                                       |
| unpickle_pure_python | 157 us                                                      | 128 us: 1.22x faster                                                        |
| tomli_loads          | 1.46 sec                                                    | 1.21 sec: 1.21x faster                                                      |
| pickle_pure_python   | 208 us                                                      | 177 us: 1.18x faster                                                        |
| pickle_dict          | 18.5 us                                                     | 19.2 us: 1.04x slower                                                       |
| json_loads           | 13.0 us                                                     | 13.6 us: 1.05x slower                                                       |
| unpickle_list        | 2.59 us                                                     | 2.73 us: 1.05x slower                                                       |
| xml_etree_process    | 37.2 ms                                                     | 40.6 ms: 1.09x slower                                                       |
| pickle_list          | 2.70 us                                                     | 3.00 us: 1.11x slower                                                       |
| pickle               | 6.64 us                                                     | 7.42 us: 1.12x slower                                                       |
| unpickle             | 7.57 us                                                     | 8.59 us: 1.13x slower                                                       |
| xml_etree_generate   | 52.5 ms                                                     | 59.7 ms: 1.14x slower                                                       |
| xml_etree_parse      | 97.6 ms                                                     | 123 ms: 1.26x slower                                                        |
| xml_etree_iterparse  | 65.6 ms                                                     | 94.3 ms: 1.44x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 23.9 ms: 1.21x slower                                                       |
| python_startup_no_site | 16.8 ms                                                     | 21.6 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 5.58 ms: 1.36x faster                                                       |
| genshi_text     | 18.4 ms                                                     | 15.7 ms: 1.17x faster                                                       |
| django_template | 24.4 ms                                                     | 21.9 ms: 1.12x faster                                                       |
| genshi_xml      | 39.9 ms                                                     | 37.3 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 71.2 us: 4.57x faster                                                       |
| generators                 | 34.0 ms                                                     | 20.2 ms: 1.68x faster                                                       |
| asyncio_tcp                | 726 ms                                                      | 479 ms: 1.51x faster                                                        |
| comprehensions             | 15.6 us                                                     | 10.7 us: 1.46x faster                                                       |
| json_dumps                 | 8.09 ms                                                     | 5.59 ms: 1.45x faster                                                       |
| mako                       | 7.58 ms                                                     | 5.58 ms: 1.36x faster                                                       |
| spectral_norm              | 68.3 ms                                                     | 51.3 ms: 1.33x faster                                                       |
| logging_silent             | 71.8 ns                                                     | 54.8 ns: 1.31x faster                                                       |
| richards_super             | 38.7 ms                                                     | 30.5 ms: 1.27x faster                                                       |
| deltablue                  | 2.70 ms                                                     | 2.14 ms: 1.26x faster                                                       |
| deepcopy_memo              | 26.0 us                                                     | 21.2 us: 1.22x faster                                                       |
| unpickle_pure_python       | 157 us                                                      | 128 us: 1.22x faster                                                        |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.66 sec: 1.22x faster                                                      |
| chaos                      | 48.4 ms                                                     | 39.9 ms: 1.21x faster                                                       |
| tomli_loads                | 1.46 sec                                                    | 1.21 sec: 1.21x faster                                                      |
| nbody                      | 70.3 ms                                                     | 58.4 ms: 1.20x faster                                                       |
| raytrace                   | 213 ms                                                      | 181 ms: 1.18x faster                                                        |
| pickle_pure_python         | 208 us                                                      | 177 us: 1.18x faster                                                        |
| genshi_text                | 18.4 ms                                                     | 15.7 ms: 1.17x faster                                                       |
| logging_simple             | 6.86 us                                                     | 5.88 us: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.23 ms: 1.16x faster                                                       |
| sympy_sum                  | 100 ms                                                      | 86.7 ms: 1.15x faster                                                       |
| richards                   | 31.4 ms                                                     | 27.2 ms: 1.15x faster                                                       |
| sqlglot_parse              | 953 us                                                      | 840 us: 1.14x faster                                                        |
| nqueens                    | 68.3 ms                                                     | 60.3 ms: 1.13x faster                                                       |
| chameleon                  | 5.26 ms                                                     | 4.67 ms: 1.13x faster                                                       |
| crypto_pyaes               | 48.9 ms                                                     | 43.3 ms: 1.13x faster                                                       |
| coroutines                 | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                                       |
| logging_format             | 7.16 us                                                     | 6.37 us: 1.12x faster                                                       |
| sympy_str                  | 185 ms                                                      | 165 ms: 1.12x faster                                                        |
| deepcopy                   | 246 us                                                      | 221 us: 1.12x faster                                                        |
| dulwich_log                | 46.4 ms                                                     | 41.5 ms: 1.12x faster                                                       |
| django_template            | 24.4 ms                                                     | 21.9 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.77 us                                                     | 1.58 us: 1.12x faster                                                       |
| pyflate                    | 312 ms                                                      | 280 ms: 1.11x faster                                                        |
| fannkuch                   | 253 ms                                                      | 228 ms: 1.11x faster                                                        |
| pprint_pformat             | 1.09 sec                                                    | 983 ms: 1.11x faster                                                        |
| pprint_safe_repr           | 529 ms                                                      | 479 ms: 1.11x faster                                                        |
| scimark_monte_carlo        | 45.3 ms                                                     | 41.2 ms: 1.10x faster                                                       |
| regex_compile              | 91.0 ms                                                     | 82.8 ms: 1.10x faster                                                       |
| sqlglot_transpile          | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                                       |
| gc_traversal               | 1.49 ms                                                     | 1.37 ms: 1.09x faster                                                       |
| mdp                        | 1.59 sec                                                    | 1.47 sec: 1.09x faster                                                      |
| sympy_integrate            | 14.0 ms                                                     | 13.0 ms: 1.08x faster                                                       |
| genshi_xml                 | 39.9 ms                                                     | 37.3 ms: 1.07x faster                                                       |
| scimark_fft                | 179 ms                                                      | 168 ms: 1.07x faster                                                        |
| tornado_http               | 92.8 ms                                                     | 86.9 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                                       |
| sqlglot_normalize          | 190 ms                                                      | 181 ms: 1.05x faster                                                        |
| sympy_expand               | 299 ms                                                      | 285 ms: 1.05x faster                                                        |
| hexiom                     | 4.55 ms                                                     | 4.35 ms: 1.05x faster                                                       |
| go                         | 101 ms                                                      | 96.6 ms: 1.05x faster                                                       |
| bench_thread_pool          | 872 us                                                      | 835 us: 1.04x faster                                                        |
| pidigits                   | 150 ms                                                      | 147 ms: 1.02x faster                                                        |
| meteor_contest             | 75.2 ms                                                     | 74.5 ms: 1.01x faster                                                       |
| html5lib                   | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| regex_dna                  | 116 ms                                                      | 120 ms: 1.04x slower                                                        |
| pickle_dict                | 18.5 us                                                     | 19.2 us: 1.04x slower                                                       |
| scimark_sor                | 78.1 ms                                                     | 81.4 ms: 1.04x slower                                                       |
| regex_effbot               | 1.50 ms                                                     | 1.57 ms: 1.04x slower                                                       |
| json_loads                 | 13.0 us                                                     | 13.6 us: 1.05x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.2 ms: 1.05x slower                                                       |
| unpickle_list              | 2.59 us                                                     | 2.73 us: 1.05x slower                                                       |
| create_gc_cycles           | 713 us                                                      | 757 us: 1.06x slower                                                        |
| aiohttp                    | 883 us                                                      | 941 us: 1.07x slower                                                        |
| coverage                   | 43.4 ms                                                     | 47.2 ms: 1.09x slower                                                       |
| pathlib                    | 70.9 ms                                                     | 77.1 ms: 1.09x slower                                                       |
| mypy2                      | 459 ms                                                      | 501 ms: 1.09x slower                                                        |
| xml_etree_process          | 37.2 ms                                                     | 40.6 ms: 1.09x slower                                                       |
| 2to3                       | 214 ms                                                      | 235 ms: 1.10x slower                                                        |
| scimark_lu                 | 62.8 ms                                                     | 69.5 ms: 1.11x slower                                                       |
| pickle_list                | 2.70 us                                                     | 3.00 us: 1.11x slower                                                       |
| pickle                     | 6.64 us                                                     | 7.42 us: 1.12x slower                                                       |
| bench_mp_pool              | 63.2 ms                                                     | 71.5 ms: 1.13x slower                                                       |
| unpickle                   | 7.57 us                                                     | 8.59 us: 1.13x slower                                                       |
| xml_etree_generate         | 52.5 ms                                                     | 59.7 ms: 1.14x slower                                                       |
| pycparser                  | 720 ms                                                      | 828 ms: 1.15x slower                                                        |
| telco                      | 4.06 ms                                                     | 4.74 ms: 1.17x slower                                                       |
| python_startup             | 19.8 ms                                                     | 23.9 ms: 1.21x slower                                                       |
| xml_etree_parse            | 97.6 ms                                                     | 123 ms: 1.26x slower                                                        |
| python_startup_no_site     | 16.8 ms                                                     | 21.6 ms: 1.28x slower                                                       |
| xml_etree_iterparse        | 65.6 ms                                                     | 94.3 ms: 1.44x slower                                                       |
| docutils                   | 1.64 sec                                                    | 2.43 sec: 1.48x slower                                                      |
| float                      | 54.4 ms                                                     | 81.6 ms: 1.50x slower                                                       |
| async_generators           | 177 ms                                                      | 281 ms: 1.59x slower                                                        |
| pylint                     | 323 ms                                                      | 573 ms: 1.77x slower                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 2.25 sec: 4.25x slower                                                      |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 2.46 sec: 4.70x slower                                                      |
| async_tree_none            | 332 ms                                                      | 1.81 sec: 5.46x slower                                                      |
| async_tree_memoization     | 399 ms                                                      | 2.32 sec: 5.81x slower                                                      |
| async_tree_memoization_tg  | 405 ms                                                      | 2.53 sec: 6.25x slower                                                      |
| async_tree_none_tg         | 309 ms                                                      | 1.99 sec: 6.46x slower                                                      |
| async_tree_io              | 808 ms                                                      | 7.30 sec: 9.04x slower                                                      |
| async_tree_io_tg           | 829 ms                                                      | 7.85 sec: 9.47x slower                                                      |
| thrift                     | 494 us                                                      | 8.90 ms: 18.02x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.14x slower                                                                |

Benchmark hidden because not significant (2): json, unpack_sequence
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 65.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown