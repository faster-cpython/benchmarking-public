# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_static_no_
- machine: linux-x86_64
- commit hash: bab095f
- commit date: 2024-08-26
- overall geometric mean: 1.03x faster
- HPT reliability: 98.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 283 ms: 1.03x slower                                                        |
| docutils       | 2.83 sec                                                   | 3.35 sec: 1.18x slower                                                      |
| html5lib       | 67.2 ms                                                    | 71.2 ms: 1.06x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 102 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                      | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                                        |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 556 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 903 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                       |
| nbody          | 88.3 ms                                                    | 81.7 ms: 1.08x faster                                                       |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                       |
| regex_dna      | 221 ms                                                     | 218 ms: 1.02x faster                                                        |
| regex_compile  | 137 ms                                                     | 151 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.1 ms: 1.13x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 54.1 ms: 1.13x faster                                                       |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.8 ms: 1.09x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 9.96 ms: 1.08x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 1.99 sec: 1.07x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 205 us: 1.06x faster                                                        |
| json_loads           | 28.9 us                                                    | 28.4 us: 1.02x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 314 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.60 ms: 1.17x faster                                                       |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                       |
| django_template | 34.8 ms                                                    | 37.2 ms: 1.07x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 25.7 us: 1.55x faster                                                       |
| richards                   | 50.9 ms                                                    | 37.7 ms: 1.35x faster                                                       |
| richards_super             | 57.4 ms                                                    | 43.2 ms: 1.33x faster                                                       |
| deepcopy                   | 367 us                                                     | 278 us: 1.32x faster                                                        |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.24x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.42 ms: 1.19x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 65.5 ms: 1.18x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.60 ms: 1.17x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                                        |
| spectral_norm              | 116 ms                                                     | 99.5 ms: 1.17x faster                                                       |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.17x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.42 sec: 1.14x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 77.1 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 54.1 ms: 1.13x faster                                                       |
| float                      | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 15.6 ms: 1.11x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                        |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 556 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                        |
| pyflate                    | 484 ms                                                     | 442 ms: 1.10x faster                                                        |
| telco                      | 8.41 ms                                                    | 7.70 ms: 1.09x faster                                                       |
| coverage                   | 93.1 ms                                                    | 85.6 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.8 ms: 1.09x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.66 ms: 1.09x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                        |
| nbody                      | 88.3 ms                                                    | 81.7 ms: 1.08x faster                                                       |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 9.96 ms: 1.08x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.99 sec: 1.07x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 205 us: 1.06x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 65.2 ms: 1.06x faster                                                       |
| thrift                     | 823 us                                                     | 779 us: 1.06x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.19 us: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 758 ms                                                     | 729 ms: 1.04x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 903 ms: 1.04x faster                                                        |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                                      |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                                      |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                        |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                       |
| json_loads                 | 28.9 us                                                    | 28.4 us: 1.02x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 165 us                                                     | 164 us: 1.01x faster                                                        |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.00x faster                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                       |
| bench_thread_pool          | 834 us                                                     | 844 us: 1.01x slower                                                        |
| asyncio_tcp                | 508 ms                                                     | 522 ms: 1.03x slower                                                        |
| pickle_pure_python         | 305 us                                                     | 314 us: 1.03x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                      |
| 2to3                       | 274 ms                                                     | 283 ms: 1.03x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 84.4 ms: 1.04x slower                                                       |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                       |
| raytrace                   | 267 ms                                                     | 280 ms: 1.05x slower                                                        |
| html5lib                   | 67.2 ms                                                    | 71.2 ms: 1.06x slower                                                       |
| django_template            | 34.8 ms                                                    | 37.2 ms: 1.07x slower                                                       |
| tornado_http               | 94.6 ms                                                    | 102 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 120 ms: 1.09x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.92 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 61.1 ms: 1.10x slower                                                       |
| regex_compile              | 137 ms                                                     | 151 ms: 1.10x slower                                                        |
| sympy_expand               | 473 ms                                                     | 523 ms: 1.11x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.88 ms: 1.15x slower                                                       |
| sympy_str                  | 282 ms                                                     | 328 ms: 1.16x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.53 ms: 1.16x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.35 sec: 1.18x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 24.5 ms: 1.20x slower                                                       |
| go                         | 145 ms                                                     | 173 ms: 1.20x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 194 ms: 1.24x slower                                                        |
| pylint                     | 317 ms                                                     | 412 ms: 1.30x slower                                                        |
| generators                 | 29.6 ms                                                    | 41.1 ms: 1.39x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                                |

Benchmark hidden because not significant (4): json, chaos, async_tree_io, deltablue
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.28% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x