# Results vs. 3.11.0

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-amd64
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 209 ms: 1.02x faster                                                        |
| chameleon      | 5.26 ms                                                     | 4.82 ms: 1.09x faster                                                       |
| docutils       | 1.64 sec                                                    | 1.54 sec: 1.07x faster                                                      |
| html5lib       | 38.9 ms                                                     | 37.0 ms: 1.05x faster                                                       |
| tornado_http   | 92.8 ms                                                     | 83.8 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 260 ms: 1.28x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 336 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 444 ms: 1.19x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 337 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 719 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 268 ms: 1.15x faster                                                        |
| async_tree_io              | 808 ms                                                      | 702 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 469 ms: 1.11x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.4 ms                                                     | 52.6 ms: 1.03x faster                                                       |
| pidigits       | 150 ms                                                      | 147 ms: 1.02x faster                                                        |
| nbody          | 70.3 ms                                                     | 73.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 77.3 ms: 1.18x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                                       |
| regex_dna      | 116 ms                                                      | 127 ms: 1.09x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 18.1 ms: 1.27x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.57 ms: 1.45x faster                                                       |
| unpickle_pure_python | 157 us                                                      | 128 us: 1.22x faster                                                        |
| pickle_pure_python   | 208 us                                                      | 176 us: 1.19x faster                                                        |
| xml_etree_parse      | 97.6 ms                                                     | 93.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.6 ms                                                     | 63.0 ms: 1.04x faster                                                       |
| tomli_loads          | 1.46 sec                                                    | 1.43 sec: 1.02x faster                                                      |
| xml_etree_process    | 37.2 ms                                                     | 36.6 ms: 1.02x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 18.4 us: 1.01x faster                                                       |
| xml_etree_generate   | 52.5 ms                                                     | 52.9 ms: 1.01x slower                                                       |
| unpickle_list        | 2.59 us                                                     | 2.71 us: 1.05x slower                                                       |
| json_loads           | 13.0 us                                                     | 13.7 us: 1.06x slower                                                       |
| pickle               | 6.64 us                                                     | 7.05 us: 1.06x slower                                                       |
| pickle_list          | 2.70 us                                                     | 2.91 us: 1.08x slower                                                       |
| unpickle             | 7.57 us                                                     | 8.61 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 20.5 ms: 1.04x slower                                                       |
| python_startup_no_site | 16.8 ms                                                     | 18.0 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 6.23 ms: 1.22x faster                                                       |
| genshi_xml      | 39.9 ms                                                     | 34.3 ms: 1.17x faster                                                       |
| django_template | 24.4 ms                                                     | 21.8 ms: 1.12x faster                                                       |
| genshi_text     | 18.4 ms                                                     | 16.7 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 70.1 us: 4.65x faster                                                       |
| pylint                     | 323 ms                                                      | 203 ms: 1.59x faster                                                        |
| generators                 | 34.0 ms                                                     | 21.4 ms: 1.59x faster                                                       |
| asyncio_tcp                | 726 ms                                                      | 462 ms: 1.57x faster                                                        |
| comprehensions             | 15.6 us                                                     | 10.4 us: 1.50x faster                                                       |
| json_dumps                 | 8.09 ms                                                     | 5.57 ms: 1.45x faster                                                       |
| deltablue                  | 2.70 ms                                                     | 1.97 ms: 1.37x faster                                                       |
| logging_silent             | 71.8 ns                                                     | 54.4 ns: 1.32x faster                                                       |
| raytrace                   | 213 ms                                                      | 163 ms: 1.31x faster                                                        |
| unpack_sequence            | 46.9 ns                                                     | 36.4 ns: 1.29x faster                                                       |
| async_tree_none            | 332 ms                                                      | 260 ms: 1.28x faster                                                        |
| sqlglot_parse              | 953 us                                                      | 752 us: 1.27x faster                                                        |
| richards_super             | 38.7 ms                                                     | 30.7 ms: 1.26x faster                                                       |
| chaos                      | 48.4 ms                                                     | 39.1 ms: 1.24x faster                                                       |
| unpickle_pure_python       | 157 us                                                      | 128 us: 1.22x faster                                                        |
| mako                       | 7.58 ms                                                     | 6.23 ms: 1.22x faster                                                       |
| sympy_sum                  | 100 ms                                                      | 82.8 ms: 1.21x faster                                                       |
| hexiom                     | 4.55 ms                                                     | 3.77 ms: 1.21x faster                                                       |
| async_tree_memoization_tg  | 405 ms                                                      | 336 ms: 1.20x faster                                                        |
| go                         | 101 ms                                                      | 84.4 ms: 1.20x faster                                                       |
| sqlglot_transpile          | 1.16 ms                                                     | 973 us: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 444 ms: 1.19x faster                                                        |
| deepcopy_memo              | 26.0 us                                                     | 21.9 us: 1.19x faster                                                       |
| pickle_pure_python         | 208 us                                                      | 176 us: 1.19x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 337 ms: 1.18x faster                                                        |
| regex_compile              | 91.0 ms                                                     | 77.3 ms: 1.18x faster                                                       |
| sympy_str                  | 185 ms                                                      | 157 ms: 1.18x faster                                                        |
| dulwich_log                | 46.4 ms                                                     | 39.4 ms: 1.18x faster                                                       |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.72 sec: 1.18x faster                                                      |
| nqueens                    | 68.3 ms                                                     | 58.5 ms: 1.17x faster                                                       |
| genshi_xml                 | 39.9 ms                                                     | 34.3 ms: 1.17x faster                                                       |
| logging_simple             | 6.86 us                                                     | 5.92 us: 1.16x faster                                                       |
| async_tree_io_tg           | 829 ms                                                      | 719 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 268 ms: 1.15x faster                                                        |
| async_tree_io              | 808 ms                                                      | 702 ms: 1.15x faster                                                        |
| sympy_integrate            | 14.0 ms                                                     | 12.3 ms: 1.15x faster                                                       |
| richards                   | 31.4 ms                                                     | 27.4 ms: 1.15x faster                                                       |
| coroutines                 | 15.0 ms                                                     | 13.1 ms: 1.14x faster                                                       |
| scimark_lu                 | 62.8 ms                                                     | 55.2 ms: 1.14x faster                                                       |
| crypto_pyaes               | 48.9 ms                                                     | 43.3 ms: 1.13x faster                                                       |
| logging_format             | 7.16 us                                                     | 6.36 us: 1.13x faster                                                       |
| mypy2                      | 459 ms                                                      | 410 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 45.3 ms                                                     | 40.5 ms: 1.12x faster                                                       |
| django_template            | 24.4 ms                                                     | 21.8 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 469 ms: 1.11x faster                                                        |
| sympy_expand               | 299 ms                                                      | 270 ms: 1.11x faster                                                        |
| tornado_http               | 92.8 ms                                                     | 83.8 ms: 1.11x faster                                                       |
| sqlite_synth               | 1.77 us                                                     | 1.60 us: 1.11x faster                                                       |
| genshi_text                | 18.4 ms                                                     | 16.7 ms: 1.10x faster                                                       |
| pyflate                    | 312 ms                                                      | 284 ms: 1.10x faster                                                        |
| deepcopy                   | 246 us                                                      | 224 us: 1.10x faster                                                        |
| spectral_norm              | 68.3 ms                                                     | 62.3 ms: 1.10x faster                                                       |
| bench_thread_pool          | 872 us                                                      | 797 us: 1.09x faster                                                        |
| sqlglot_normalize          | 190 ms                                                      | 174 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.09 sec                                                    | 993 ms: 1.09x faster                                                        |
| chameleon                  | 5.26 ms                                                     | 4.82 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 529 ms                                                      | 487 ms: 1.09x faster                                                        |
| mdp                        | 1.59 sec                                                    | 1.47 sec: 1.08x faster                                                      |
| docutils                   | 1.64 sec                                                    | 1.54 sec: 1.07x faster                                                      |
| meteor_contest             | 75.2 ms                                                     | 71.3 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.45 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.96 us: 1.05x faster                                                       |
| html5lib                   | 38.9 ms                                                     | 37.0 ms: 1.05x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.0 ms: 1.05x faster                                                       |
| xml_etree_parse            | 97.6 ms                                                     | 93.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.6 ms                                                     | 63.0 ms: 1.04x faster                                                       |
| float                      | 54.4 ms                                                     | 52.6 ms: 1.03x faster                                                       |
| pidigits                   | 150 ms                                                      | 147 ms: 1.02x faster                                                        |
| 2to3                       | 214 ms                                                      | 209 ms: 1.02x faster                                                        |
| tomli_loads                | 1.46 sec                                                    | 1.43 sec: 1.02x faster                                                      |
| xml_etree_process          | 37.2 ms                                                     | 36.6 ms: 1.02x faster                                                       |
| pickle_dict                | 18.5 us                                                     | 18.4 us: 1.01x faster                                                       |
| fannkuch                   | 253 ms                                                      | 252 ms: 1.00x faster                                                        |
| xml_etree_generate         | 52.5 ms                                                     | 52.9 ms: 1.01x slower                                                       |
| bench_mp_pool              | 63.2 ms                                                     | 64.4 ms: 1.02x slower                                                       |
| scimark_sor                | 78.1 ms                                                     | 79.6 ms: 1.02x slower                                                       |
| create_gc_cycles           | 713 us                                                      | 730 us: 1.02x slower                                                        |
| python_startup             | 19.8 ms                                                     | 20.5 ms: 1.04x slower                                                       |
| nbody                      | 70.3 ms                                                     | 73.4 ms: 1.04x slower                                                       |
| coverage                   | 43.4 ms                                                     | 45.4 ms: 1.05x slower                                                       |
| unpickle_list              | 2.59 us                                                     | 2.71 us: 1.05x slower                                                       |
| json_loads                 | 13.0 us                                                     | 13.7 us: 1.06x slower                                                       |
| pickle                     | 6.64 us                                                     | 7.05 us: 1.06x slower                                                       |
| python_startup_no_site     | 16.8 ms                                                     | 18.0 ms: 1.07x slower                                                       |
| json                       | 2.98 ms                                                     | 3.20 ms: 1.08x slower                                                       |
| pathlib                    | 70.9 ms                                                     | 76.3 ms: 1.08x slower                                                       |
| regex_effbot               | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                                       |
| pickle_list                | 2.70 us                                                     | 2.91 us: 1.08x slower                                                       |
| regex_dna                  | 116 ms                                                      | 127 ms: 1.09x slower                                                        |
| unpickle                   | 7.57 us                                                     | 8.61 us: 1.14x slower                                                       |
| telco                      | 4.06 ms                                                     | 4.68 ms: 1.15x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 18.1 ms: 1.27x slower                                                       |
| async_generators           | 177 ms                                                      | 232 ms: 1.31x slower                                                        |
| thrift                     | 494 us                                                      | 8.03 ms: 16.26x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (4): pycparser, aiohttp, gc_traversal, scimark_fft
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: unknown