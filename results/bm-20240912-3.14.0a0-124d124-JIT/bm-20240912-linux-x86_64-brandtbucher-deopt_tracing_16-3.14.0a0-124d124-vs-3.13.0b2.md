# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: deopt_tracing_16
- machine: linux-x86_64
- commit hash: 124d124
- commit date: 2024-09-12
- overall geometric mean: 1.04x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 283 ms: 1.03x slower                                                    |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                  |
| html5lib       | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 314 ms: 1.20x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                                    |
| async_tree_io              | 939 ms                                                     | 885 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.4 ms: 1.14x faster                                                   |
| nbody          | 88.3 ms                                                    | 81.1 ms: 1.09x faster                                                   |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                   |
| regex_compile  | 137 ms                                                     | 144 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.12x faster                                                    |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 98.7 ms: 1.09x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                   |
| json_loads           | 28.9 us                                                    | 27.4 us: 1.06x faster                                                   |
| unpickle_list        | 5.34 us                                                    | 5.12 us: 1.04x faster                                                   |
| pickle_dict          | 34.8 us                                                    | 33.8 us: 1.03x faster                                                   |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                                    |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.00x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.03x slower                                                    |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.71 ms: 1.16x faster                                                   |
| django_template | 34.8 ms                                                    | 37.4 ms: 1.08x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 25.7 ms: 1.09x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 59.8 ms: 1.16x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                   |
| deepcopy                   | 367 us                                                     | 268 us: 1.37x faster                                                    |
| scimark_fft                | 392 ms                                                     | 306 ms: 1.28x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.33 ms: 1.22x faster                                                   |
| async_tree_none            | 378 ms                                                     | 314 ms: 1.20x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 65.9 ms: 1.18x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.71 ms: 1.16x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                    |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                    |
| float                      | 78.9 ms                                                    | 69.4 ms: 1.14x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.53 ms: 1.13x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                   |
| richards_super             | 57.4 ms                                                    | 51.1 ms: 1.12x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.12x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                    |
| pyflate                    | 484 ms                                                     | 437 ms: 1.11x faster                                                    |
| coverage                   | 93.1 ms                                                    | 84.6 ms: 1.10x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.0 ms: 1.10x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                    |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                    |
| richards                   | 50.9 ms                                                    | 46.7 ms: 1.09x faster                                                   |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                                   |
| nbody                      | 88.3 ms                                                    | 81.1 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 98.7 ms: 1.09x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                    |
| fannkuch                   | 402 ms                                                     | 375 ms: 1.07x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.86 ms: 1.07x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.05 us: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                                    |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                   |
| async_tree_io              | 939 ms                                                     | 885 ms: 1.06x faster                                                    |
| json_loads                 | 28.9 us                                                    | 27.4 us: 1.06x faster                                                   |
| go                         | 145 ms                                                     | 137 ms: 1.05x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                   |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                   |
| unpickle_list              | 5.34 us                                                    | 5.12 us: 1.04x faster                                                   |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                    |
| thrift                     | 823 us                                                     | 791 us: 1.04x faster                                                    |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                   |
| json                       | 5.31 ms                                                    | 5.14 ms: 1.03x faster                                                   |
| pickle_dict                | 34.8 us                                                    | 33.8 us: 1.03x faster                                                   |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                   |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                   |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                   |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 745 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.01x faster                                                    |
| pickle_list                | 5.11 us                                                    | 5.08 us: 1.00x faster                                                   |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                   |
| dulwich_log                | 67.2 ms                                                    | 68.0 ms: 1.01x slower                                                   |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                  |
| pickle_pure_python         | 305 us                                                     | 313 us: 1.03x slower                                                    |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                   |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                    |
| 2to3                       | 274 ms                                                     | 283 ms: 1.03x slower                                                    |
| sqlglot_parse              | 1.32 ms                                                    | 1.37 ms: 1.04x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.71 ms: 1.05x slower                                                   |
| docutils                   | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                  |
| regex_compile              | 137 ms                                                     | 144 ms: 1.05x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 86.5 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 59.1 ms: 1.06x slower                                                   |
| raytrace                   | 267 ms                                                     | 286 ms: 1.07x slower                                                    |
| django_template            | 34.8 ms                                                    | 37.4 ms: 1.08x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 25.7 ms: 1.09x slower                                                   |
| sympy_str                  | 282 ms                                                     | 307 ms: 1.09x slower                                                    |
| sympy_expand               | 473 ms                                                     | 521 ms: 1.10x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 122 ms: 1.11x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 7.00 ms: 1.11x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 3.66 ms: 1.13x slower                                                   |
| generators                 | 29.6 ms                                                    | 33.6 ms: 1.14x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 177 ms: 1.14x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 23.4 ms: 1.14x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 59.8 ms: 1.16x slower                                                   |
| pylint                     | 317 ms                                                     | 385 ms: 1.21x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                            |

Benchmark hidden because not significant (5): pprint_pformat, typing_runtime_protocols, bench_thread_pool, regex_dna, tornado_http
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-124d124-JIT/bm-20240912-linux-x86_64-brandtbucher-deopt_tracing_16-3.14.0a0-124d124.json: unpack_sequence

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x