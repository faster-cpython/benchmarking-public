# Results vs. 3.11.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.02x faster
- HPT reliability: 97.98%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 223 ms: 1.05x slower                                                        |
| chameleon      | 5.26 ms                                                     | 4.92 ms: 1.07x faster                                                       |
| tornado_http   | 92.8 ms                                                     | 86.4 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 270 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 454 ms: 1.17x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 347 ms: 1.16x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 348 ms: 1.15x faster                                                        |
| async_tree_io              | 808 ms                                                      | 723 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 276 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 469 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 744 ms: 1.11x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                      | 147 ms: 1.02x faster                                                        |
| float          | 54.4 ms                                                     | 56.7 ms: 1.04x slower                                                       |
| nbody          | 70.3 ms                                                     | 74.4 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 116 ms                                                      | 117 ms: 1.01x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.04x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                                       |
| regex_compile  | 91.0 ms                                                     | 96.7 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.76 ms: 1.40x faster                                                       |
| pickle_pure_python   | 208 us                                                      | 183 us: 1.14x faster                                                        |
| xml_etree_parse      | 97.6 ms                                                     | 91.8 ms: 1.06x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 18.2 us: 1.02x faster                                                       |
| unpickle_pure_python | 157 us                                                      | 155 us: 1.01x faster                                                        |
| xml_etree_process    | 37.2 ms                                                     | 38.2 ms: 1.03x slower                                                       |
| unpickle_list        | 2.59 us                                                     | 2.72 us: 1.05x slower                                                       |
| xml_etree_generate   | 52.5 ms                                                     | 55.6 ms: 1.06x slower                                                       |
| json_loads           | 13.0 us                                                     | 13.8 us: 1.06x slower                                                       |
| pickle               | 6.64 us                                                     | 7.19 us: 1.08x slower                                                       |
| unpickle             | 7.57 us                                                     | 8.31 us: 1.10x slower                                                       |
| pickle_list          | 2.70 us                                                     | 3.24 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 20.3 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.8 ms                                                     | 18.0 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 18.4 ms                                                     | 16.2 ms: 1.14x faster                                                       |
| mako            | 7.58 ms                                                     | 6.73 ms: 1.13x faster                                                       |
| genshi_xml      | 39.9 ms                                                     | 36.6 ms: 1.09x faster                                                       |
| django_template | 24.4 ms                                                     | 22.4 ms: 1.09x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 73.1 us: 4.46x faster                                                       |
| generators                 | 34.0 ms                                                     | 20.7 ms: 1.64x faster                                                       |
| pylint                     | 323 ms                                                      | 213 ms: 1.52x faster                                                        |
| asyncio_tcp                | 726 ms                                                      | 480 ms: 1.51x faster                                                        |
| json_dumps                 | 8.09 ms                                                     | 5.76 ms: 1.40x faster                                                       |
| logging_silent             | 71.8 ns                                                     | 54.9 ns: 1.31x faster                                                       |
| deltablue                  | 2.70 ms                                                     | 2.19 ms: 1.23x faster                                                       |
| async_tree_none            | 332 ms                                                      | 270 ms: 1.23x faster                                                        |
| comprehensions             | 15.6 us                                                     | 12.8 us: 1.22x faster                                                       |
| richards_super             | 38.7 ms                                                     | 32.5 ms: 1.19x faster                                                       |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.71 sec: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 454 ms: 1.17x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 347 ms: 1.16x faster                                                        |
| sqlglot_parse              | 953 us                                                      | 819 us: 1.16x faster                                                        |
| unpack_sequence            | 46.9 ns                                                     | 40.9 ns: 1.15x faster                                                       |
| async_tree_memoization     | 399 ms                                                      | 348 ms: 1.15x faster                                                        |
| pickle_pure_python         | 208 us                                                      | 183 us: 1.14x faster                                                        |
| genshi_text                | 18.4 ms                                                     | 16.2 ms: 1.14x faster                                                       |
| raytrace                   | 213 ms                                                      | 189 ms: 1.13x faster                                                        |
| mako                       | 7.58 ms                                                     | 6.73 ms: 1.13x faster                                                       |
| logging_simple             | 6.86 us                                                     | 6.12 us: 1.12x faster                                                       |
| async_tree_io              | 808 ms                                                      | 723 ms: 1.12x faster                                                        |
| sqlglot_transpile          | 1.16 ms                                                     | 1.04 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 309 ms                                                      | 276 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 469 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 744 ms: 1.11x faster                                                        |
| coroutines                 | 15.0 ms                                                     | 13.5 ms: 1.11x faster                                                       |
| chaos                      | 48.4 ms                                                     | 43.6 ms: 1.11x faster                                                       |
| sqlite_synth               | 1.77 us                                                     | 1.60 us: 1.10x faster                                                       |
| logging_format             | 7.16 us                                                     | 6.55 us: 1.09x faster                                                       |
| richards                   | 31.4 ms                                                     | 28.7 ms: 1.09x faster                                                       |
| genshi_xml                 | 39.9 ms                                                     | 36.6 ms: 1.09x faster                                                       |
| sympy_sum                  | 100 ms                                                      | 91.7 ms: 1.09x faster                                                       |
| django_template            | 24.4 ms                                                     | 22.4 ms: 1.09x faster                                                       |
| deepcopy_memo              | 26.0 us                                                     | 24.2 us: 1.08x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 86.4 ms: 1.07x faster                                                       |
| chameleon                  | 5.26 ms                                                     | 4.92 ms: 1.07x faster                                                       |
| xml_etree_parse            | 97.6 ms                                                     | 91.8 ms: 1.06x faster                                                       |
| sympy_str                  | 185 ms                                                      | 175 ms: 1.06x faster                                                        |
| mdp                        | 1.59 sec                                                    | 1.51 sec: 1.06x faster                                                      |
| deepcopy                   | 246 us                                                      | 234 us: 1.06x faster                                                        |
| sympy_integrate            | 14.0 ms                                                     | 13.3 ms: 1.05x faster                                                       |
| dulwich_log                | 46.4 ms                                                     | 44.3 ms: 1.05x faster                                                       |
| bench_thread_pool          | 872 us                                                      | 834 us: 1.05x faster                                                        |
| deepcopy_reduce            | 2.06 us                                                     | 1.97 us: 1.04x faster                                                       |
| mypy2                      | 459 ms                                                      | 443 ms: 1.04x faster                                                        |
| crypto_pyaes               | 48.9 ms                                                     | 47.6 ms: 1.03x faster                                                       |
| pidigits                   | 150 ms                                                      | 147 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.09 sec                                                    | 1.07 sec: 1.02x faster                                                      |
| pickle_dict                | 18.5 us                                                     | 18.2 us: 1.02x faster                                                       |
| pprint_safe_repr           | 529 ms                                                      | 523 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 157 us                                                      | 155 us: 1.01x faster                                                        |
| sqlglot_normalize          | 190 ms                                                      | 189 ms: 1.01x faster                                                        |
| regex_dna                  | 116 ms                                                      | 117 ms: 1.01x slower                                                        |
| sympy_expand               | 299 ms                                                      | 301 ms: 1.01x slower                                                        |
| go                         | 101 ms                                                      | 102 ms: 1.01x slower                                                        |
| gc_traversal               | 1.49 ms                                                     | 1.52 ms: 1.01x slower                                                       |
| python_startup             | 19.8 ms                                                     | 20.3 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.2 ms                                                     | 38.2 ms: 1.03x slower                                                       |
| aiohttp                    | 883 us                                                      | 908 us: 1.03x slower                                                        |
| fannkuch                   | 253 ms                                                      | 260 ms: 1.03x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.04x slower                                                       |
| bench_mp_pool              | 63.2 ms                                                     | 65.7 ms: 1.04x slower                                                       |
| create_gc_cycles           | 713 us                                                      | 744 us: 1.04x slower                                                        |
| coverage                   | 43.4 ms                                                     | 45.3 ms: 1.04x slower                                                       |
| float                      | 54.4 ms                                                     | 56.7 ms: 1.04x slower                                                       |
| 2to3                       | 214 ms                                                      | 223 ms: 1.05x slower                                                        |
| pyflate                    | 312 ms                                                      | 327 ms: 1.05x slower                                                        |
| regex_effbot               | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                                       |
| unpickle_list              | 2.59 us                                                     | 2.72 us: 1.05x slower                                                       |
| nbody                      | 70.3 ms                                                     | 74.4 ms: 1.06x slower                                                       |
| xml_etree_generate         | 52.5 ms                                                     | 55.6 ms: 1.06x slower                                                       |
| json_loads                 | 13.0 us                                                     | 13.8 us: 1.06x slower                                                       |
| regex_compile              | 91.0 ms                                                     | 96.7 ms: 1.06x slower                                                       |
| spectral_norm              | 68.3 ms                                                     | 73.0 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                       |
| json                       | 2.98 ms                                                     | 3.18 ms: 1.07x slower                                                       |
| python_startup_no_site     | 16.8 ms                                                     | 18.0 ms: 1.07x slower                                                       |
| hexiom                     | 4.55 ms                                                     | 4.88 ms: 1.07x slower                                                       |
| pickle                     | 6.64 us                                                     | 7.19 us: 1.08x slower                                                       |
| scimark_monte_carlo        | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                       |
| unpickle                   | 7.57 us                                                     | 8.31 us: 1.10x slower                                                       |
| pathlib                    | 70.9 ms                                                     | 77.8 ms: 1.10x slower                                                       |
| scimark_fft                | 179 ms                                                      | 201 ms: 1.12x slower                                                        |
| scimark_sor                | 78.1 ms                                                     | 89.1 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.99 ms: 1.16x slower                                                       |
| telco                      | 4.06 ms                                                     | 4.76 ms: 1.17x slower                                                       |
| pickle_list                | 2.70 us                                                     | 3.24 us: 1.20x slower                                                       |
| scimark_lu                 | 62.8 ms                                                     | 76.1 ms: 1.21x slower                                                       |
| async_generators           | 177 ms                                                      | 237 ms: 1.34x slower                                                        |
| thrift                     | 494 us                                                      | 9.24 ms: 18.72x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (7): xml_etree_iterparse, docutils, nqueens, meteor_contest, tomli_loads, html5lib, pycparser
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 97.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown