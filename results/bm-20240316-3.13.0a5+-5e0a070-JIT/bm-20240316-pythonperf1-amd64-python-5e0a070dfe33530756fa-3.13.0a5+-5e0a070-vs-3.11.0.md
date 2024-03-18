# Results vs. 3.11.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 222 ms: 1.04x slower                                                        |
| chameleon      | 5.26 ms                                                     | 4.74 ms: 1.11x faster                                                       |
| docutils       | 1.64 sec                                                    | 1.60 sec: 1.02x faster                                                      |
| html5lib       | 38.9 ms                                                     | 36.5 ms: 1.06x faster                                                       |
| tornado_http   | 92.8 ms                                                     | 85.1 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 262 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 446 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 342 ms: 1.18x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 338 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 269 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 725 ms: 1.14x faster                                                        |
| async_tree_io              | 808 ms                                                      | 710 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 471 ms: 1.11x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.3 ms                                                     | 58.2 ms: 1.21x faster                                                       |
| float          | 54.4 ms                                                     | 48.8 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 83.6 ms: 1.09x faster                                                       |
| regex_dna      | 116 ms                                                      | 118 ms: 1.02x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.53 ms: 1.46x faster                                                       |
| tomli_loads          | 1.46 sec                                                    | 1.19 sec: 1.23x faster                                                      |
| unpickle_pure_python | 157 us                                                      | 128 us: 1.22x faster                                                        |
| pickle_pure_python   | 208 us                                                      | 178 us: 1.17x faster                                                        |
| xml_etree_parse      | 97.6 ms                                                     | 91.0 ms: 1.07x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 17.4 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.6 ms                                                     | 61.8 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.2 ms                                                     | 36.2 ms: 1.03x faster                                                       |
| json_loads           | 13.0 us                                                     | 13.6 us: 1.05x slower                                                       |
| unpickle_list        | 2.59 us                                                     | 2.76 us: 1.07x slower                                                       |
| pickle               | 6.64 us                                                     | 7.15 us: 1.08x slower                                                       |
| pickle_list          | 2.70 us                                                     | 2.93 us: 1.09x slower                                                       |
| unpickle             | 7.57 us                                                     | 8.56 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 24.0 ms: 1.21x slower                                                       |
| python_startup_no_site | 16.8 ms                                                     | 21.8 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 5.65 ms: 1.34x faster                                                       |
| genshi_text     | 18.4 ms                                                     | 15.2 ms: 1.21x faster                                                       |
| genshi_xml      | 39.9 ms                                                     | 33.9 ms: 1.18x faster                                                       |
| django_template | 24.4 ms                                                     | 21.4 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 68.7 us: 4.74x faster                                                       |
| generators                 | 34.0 ms                                                     | 19.7 ms: 1.72x faster                                                       |
| pylint                     | 323 ms                                                      | 209 ms: 1.54x faster                                                        |
| asyncio_tcp                | 726 ms                                                      | 474 ms: 1.53x faster                                                        |
| comprehensions             | 15.6 us                                                     | 10.3 us: 1.52x faster                                                       |
| json_dumps                 | 8.09 ms                                                     | 5.53 ms: 1.46x faster                                                       |
| mako                       | 7.58 ms                                                     | 5.65 ms: 1.34x faster                                                       |
| deltablue                  | 2.70 ms                                                     | 2.03 ms: 1.33x faster                                                       |
| spectral_norm              | 68.3 ms                                                     | 51.8 ms: 1.32x faster                                                       |
| logging_silent             | 71.8 ns                                                     | 55.1 ns: 1.30x faster                                                       |
| async_tree_none            | 332 ms                                                      | 262 ms: 1.27x faster                                                        |
| richards_super             | 38.7 ms                                                     | 31.1 ms: 1.25x faster                                                       |
| tomli_loads                | 1.46 sec                                                    | 1.19 sec: 1.23x faster                                                      |
| unpickle_pure_python       | 157 us                                                      | 128 us: 1.22x faster                                                        |
| sqlglot_parse              | 953 us                                                      | 781 us: 1.22x faster                                                        |
| chaos                      | 48.4 ms                                                     | 39.7 ms: 1.22x faster                                                       |
| genshi_text                | 18.4 ms                                                     | 15.2 ms: 1.21x faster                                                       |
| nbody                      | 70.3 ms                                                     | 58.2 ms: 1.21x faster                                                       |
| raytrace                   | 213 ms                                                      | 179 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 446 ms: 1.19x faster                                                        |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.71 sec: 1.19x faster                                                      |
| deepcopy_memo              | 26.0 us                                                     | 21.9 us: 1.18x faster                                                       |
| async_tree_memoization_tg  | 405 ms                                                      | 342 ms: 1.18x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 338 ms: 1.18x faster                                                        |
| genshi_xml                 | 39.9 ms                                                     | 33.9 ms: 1.18x faster                                                       |
| logging_simple             | 6.86 us                                                     | 5.86 us: 1.17x faster                                                       |
| pickle_pure_python         | 208 us                                                      | 178 us: 1.17x faster                                                        |
| sqlglot_transpile          | 1.16 ms                                                     | 1000 us: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.24 ms: 1.15x faster                                                       |
| async_tree_none_tg         | 309 ms                                                      | 269 ms: 1.15x faster                                                        |
| logging_format             | 7.16 us                                                     | 6.25 us: 1.15x faster                                                       |
| nqueens                    | 68.3 ms                                                     | 59.7 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 829 ms                                                      | 725 ms: 1.14x faster                                                        |
| sympy_sum                  | 100 ms                                                      | 87.6 ms: 1.14x faster                                                       |
| django_template            | 24.4 ms                                                     | 21.4 ms: 1.14x faster                                                       |
| async_tree_io              | 808 ms                                                      | 710 ms: 1.14x faster                                                        |
| sympy_str                  | 185 ms                                                      | 163 ms: 1.13x faster                                                        |
| mdp                        | 1.59 sec                                                    | 1.41 sec: 1.13x faster                                                      |
| pprint_pformat             | 1.09 sec                                                    | 963 ms: 1.13x faster                                                        |
| fannkuch                   | 253 ms                                                      | 225 ms: 1.13x faster                                                        |
| richards                   | 31.4 ms                                                     | 27.9 ms: 1.13x faster                                                       |
| sqlite_synth               | 1.77 us                                                     | 1.58 us: 1.12x faster                                                       |
| crypto_pyaes               | 48.9 ms                                                     | 43.7 ms: 1.12x faster                                                       |
| pprint_safe_repr           | 529 ms                                                      | 473 ms: 1.12x faster                                                        |
| float                      | 54.4 ms                                                     | 48.8 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 471 ms: 1.11x faster                                                        |
| pyflate                    | 312 ms                                                      | 281 ms: 1.11x faster                                                        |
| chameleon                  | 5.26 ms                                                     | 4.74 ms: 1.11x faster                                                       |
| dulwich_log                | 46.4 ms                                                     | 41.8 ms: 1.11x faster                                                       |
| deepcopy                   | 246 us                                                      | 224 us: 1.10x faster                                                        |
| coroutines                 | 15.0 ms                                                     | 13.6 ms: 1.10x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 85.1 ms: 1.09x faster                                                       |
| scimark_monte_carlo        | 45.3 ms                                                     | 41.6 ms: 1.09x faster                                                       |
| regex_compile              | 91.0 ms                                                     | 83.6 ms: 1.09x faster                                                       |
| sqlglot_normalize          | 190 ms                                                      | 175 ms: 1.08x faster                                                        |
| sympy_integrate            | 14.0 ms                                                     | 13.1 ms: 1.07x faster                                                       |
| xml_etree_parse            | 97.6 ms                                                     | 91.0 ms: 1.07x faster                                                       |
| sympy_expand               | 299 ms                                                      | 279 ms: 1.07x faster                                                        |
| hexiom                     | 4.55 ms                                                     | 4.28 ms: 1.06x faster                                                       |
| html5lib                   | 38.9 ms                                                     | 36.5 ms: 1.06x faster                                                       |
| pickle_dict                | 18.5 us                                                     | 17.4 us: 1.06x faster                                                       |
| go                         | 101 ms                                                      | 95.2 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.6 ms                                                     | 61.8 ms: 1.06x faster                                                       |
| scimark_fft                | 179 ms                                                      | 169 ms: 1.06x faster                                                        |
| mypy2                      | 459 ms                                                      | 436 ms: 1.05x faster                                                        |
| deepcopy_reduce            | 2.06 us                                                     | 1.96 us: 1.05x faster                                                       |
| bench_thread_pool          | 872 us                                                      | 830 us: 1.05x faster                                                        |
| pycparser                  | 720 ms                                                      | 690 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.2 ms                                                     | 36.2 ms: 1.03x faster                                                       |
| meteor_contest             | 75.2 ms                                                     | 73.4 ms: 1.03x faster                                                       |
| docutils                   | 1.64 sec                                                    | 1.60 sec: 1.02x faster                                                      |
| gc_traversal               | 1.49 ms                                                     | 1.51 ms: 1.01x slower                                                       |
| aiohttp                    | 883 us                                                      | 899 us: 1.02x slower                                                        |
| regex_dna                  | 116 ms                                                      | 118 ms: 1.02x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                       |
| 2to3                       | 214 ms                                                      | 222 ms: 1.04x slower                                                        |
| create_gc_cycles           | 713 us                                                      | 745 us: 1.04x slower                                                        |
| json_loads                 | 13.0 us                                                     | 13.6 us: 1.05x slower                                                       |
| regex_effbot               | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                                       |
| unpickle_list              | 2.59 us                                                     | 2.76 us: 1.07x slower                                                       |
| scimark_sor                | 78.1 ms                                                     | 83.5 ms: 1.07x slower                                                       |
| coverage                   | 43.4 ms                                                     | 46.5 ms: 1.07x slower                                                       |
| pickle                     | 6.64 us                                                     | 7.15 us: 1.08x slower                                                       |
| pathlib                    | 70.9 ms                                                     | 76.8 ms: 1.08x slower                                                       |
| pickle_list                | 2.70 us                                                     | 2.93 us: 1.09x slower                                                       |
| json                       | 2.98 ms                                                     | 3.27 ms: 1.10x slower                                                       |
| bench_mp_pool              | 63.2 ms                                                     | 70.2 ms: 1.11x slower                                                       |
| unpickle                   | 7.57 us                                                     | 8.56 us: 1.13x slower                                                       |
| telco                      | 4.06 ms                                                     | 4.60 ms: 1.13x slower                                                       |
| scimark_lu                 | 62.8 ms                                                     | 71.9 ms: 1.15x slower                                                       |
| python_startup             | 19.8 ms                                                     | 24.0 ms: 1.21x slower                                                       |
| python_startup_no_site     | 16.8 ms                                                     | 21.8 ms: 1.29x slower                                                       |
| async_generators           | 177 ms                                                      | 239 ms: 1.35x slower                                                        |
| thrift                     | 494 us                                                      | 8.84 ms: 17.90x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (4): pidigits, sqlglot_optimize, unpack_sequence, xml_etree_generate
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x


# Memory

- memory change: unknown