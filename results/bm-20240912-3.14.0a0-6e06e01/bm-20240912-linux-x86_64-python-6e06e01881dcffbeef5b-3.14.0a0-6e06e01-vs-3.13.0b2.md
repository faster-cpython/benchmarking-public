# Results vs. 3.13.0b2

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 253 ms: 1.08x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                                |
| html5lib       | 67.2 ms                                                    | 62.4 ms: 1.08x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                  |
| async_tree_io              | 939 ms                                                     | 873 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 558 ms: 1.05x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.7 ms: 1.03x faster                                                 |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                  |
| nbody          | 88.3 ms                                                    | 89.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                                  |
| regex_dna      | 221 ms                                                     | 216 ms: 1.02x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.0 us: 1.07x faster                                                 |
| pickle_list          | 5.11 us                                                    | 4.87 us: 1.05x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 33.8 us: 1.03x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 85.4 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                  |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.01x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                  |
| pickle               | 11.5 us                                                    | 11.4 us: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.7 ms: 1.09x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 48.6 ms: 1.06x faster                                                 |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| django_template | 34.8 ms                                                    | 34.6 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 255 us: 1.44x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.5 us: 1.34x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.63 us: 1.27x faster                                                 |
| go                         | 145 ms                                                     | 117 ms: 1.24x faster                                                  |
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.60 ms: 1.15x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                  |
| richards                   | 50.9 ms                                                    | 45.8 ms: 1.11x faster                                                 |
| richards_super             | 57.4 ms                                                    | 51.7 ms: 1.11x faster                                                 |
| genshi_text                | 23.7 ms                                                    | 21.7 ms: 1.09x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 71.1 ms: 1.09x faster                                                 |
| coverage                   | 93.1 ms                                                    | 85.7 ms: 1.09x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                     | 253 ms: 1.08x faster                                                  |
| scimark_fft                | 392 ms                                                     | 363 ms: 1.08x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 471 ms: 1.08x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 62.4 ms: 1.08x faster                                                 |
| async_tree_io              | 939 ms                                                     | 873 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                  |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                  |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 714 ms: 1.06x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 48.6 ms: 1.06x faster                                                 |
| docutils                   | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                                |
| bench_thread_pool          | 834 us                                                     | 787 us: 1.06x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| thrift                     | 823 us                                                     | 779 us: 1.06x faster                                                  |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                                 |
| sqlite_synth               | 2.99 us                                                    | 2.83 us: 1.06x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 558 ms: 1.05x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                 |
| generators                 | 29.6 ms                                                    | 28.2 ms: 1.05x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                 |
| logging_silent             | 105 ns                                                     | 99.9 ns: 1.05x faster                                                 |
| pickle_list                | 5.11 us                                                    | 4.87 us: 1.05x faster                                                 |
| scimark_sor                | 127 ms                                                     | 122 ms: 1.05x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.49 us: 1.05x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.2 ms: 1.04x faster                                                 |
| dulwich_log                | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 158 us: 1.04x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| sympy_expand               | 473 ms                                                     | 456 ms: 1.04x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.04 sec: 1.04x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.04x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.69 sec: 1.04x faster                                                |
| deltablue                  | 3.25 ms                                                    | 3.14 ms: 1.03x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.86 sec: 1.03x faster                                                |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                                |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                  |
| json                       | 5.31 ms                                                    | 5.15 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.1 ms: 1.03x faster                                                 |
| pickle_dict                | 34.8 us                                                    | 33.8 us: 1.03x faster                                                 |
| float                      | 78.9 ms                                                    | 76.7 ms: 1.03x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 85.4 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                  |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.02x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                  |
| hexiom                     | 6.30 ms                                                    | 6.16 ms: 1.02x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.90 ms: 1.02x faster                                                 |
| pyflate                    | 484 ms                                                     | 476 ms: 1.02x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                  |
| unpickle                   | 15.1 us                                                    | 14.9 us: 1.01x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 80.4 ms: 1.01x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                  |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| async_generators           | 442 ms                                                     | 437 ms: 1.01x faster                                                  |
| django_template            | 34.8 ms                                                    | 34.6 ms: 1.01x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                 |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.00x faster                                                 |
| fannkuch                   | 402 ms                                                     | 403 ms: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                 |
| nbody                      | 88.3 ms                                                    | 89.5 ms: 1.01x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                          |

Benchmark hidden because not significant (4): coroutines, unpickle_list, pylint, telco
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x