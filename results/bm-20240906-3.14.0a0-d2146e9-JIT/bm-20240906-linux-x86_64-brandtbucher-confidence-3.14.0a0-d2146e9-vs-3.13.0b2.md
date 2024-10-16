# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d2146e9
- commit date: 2024-09-06
- overall geometric mean: 1.05x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                              |
| docutils       | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                            |
| html5lib       | 67.2 ms                                                    | 62.3 ms: 1.08x faster                                             |
| tornado_http   | 94.6 ms                                                    | 96.1 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                      | 1.00x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                              |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                              |
| async_tree_memoization_tg  | 444 ms                                                     | 407 ms: 1.09x faster                                              |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                              |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.07x faster                                              |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                              |
| async_tree_io_tg           | 936 ms                                                     | 893 ms: 1.05x faster                                              |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                      |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                             |
| nbody          | 88.3 ms                                                    | 81.2 ms: 1.09x faster                                             |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                      | 1.08x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 210 ms: 1.05x faster                                              |
| regex_effbot   | 3.67 ms                                                    | 3.50 ms: 1.05x faster                                             |
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                             |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                      | 1.03x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 78.3 ms: 1.12x faster                                             |
| xml_etree_process    | 61.2 ms                                                    | 55.1 ms: 1.11x faster                                             |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                            |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 107 ms                                                     | 98.8 ms: 1.09x faster                                             |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                             |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                              |
| unpickle             | 15.1 us                                                    | 14.8 us: 1.02x faster                                             |
| pickle_dict          | 34.8 us                                                    | 34.1 us: 1.02x faster                                             |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                             |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.00x faster                                              |
| unpickle_list        | 5.34 us                                                    | 5.40 us: 1.01x slower                                             |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                             |
| pickle_list          | 5.11 us                                                    | 5.29 us: 1.04x slower                                             |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                             |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                             |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                             |
| genshi_text     | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                             |
| genshi_xml      | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                             |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                             |
| deepcopy                   | 367 us                                                     | 267 us: 1.38x faster                                              |
| richards_super             | 57.4 ms                                                    | 42.9 ms: 1.34x faster                                             |
| richards                   | 50.9 ms                                                    | 38.7 ms: 1.32x faster                                             |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                              |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                             |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.43 ms: 1.19x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                              |
| crypto_pyaes               | 77.5 ms                                                    | 66.4 ms: 1.17x faster                                             |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                              |
| mako                       | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                             |
| pyflate                    | 484 ms                                                     | 424 ms: 1.14x faster                                              |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                            |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                              |
| xml_etree_generate         | 87.4 ms                                                    | 78.3 ms: 1.12x faster                                             |
| float                      | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                             |
| xml_etree_process          | 61.2 ms                                                    | 55.1 ms: 1.11x faster                                             |
| go                         | 145 ms                                                     | 131 ms: 1.10x faster                                              |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.10x faster                                              |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                              |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.9 ms: 1.10x faster                                             |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                              |
| async_tree_memoization_tg  | 444 ms                                                     | 407 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                     | 98.8 ms: 1.09x faster                                             |
| nbody                      | 88.3 ms                                                    | 81.2 ms: 1.09x faster                                             |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                             |
| pprint_safe_repr           | 758 ms                                                     | 700 ms: 1.08x faster                                              |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                              |
| html5lib                   | 67.2 ms                                                    | 62.3 ms: 1.08x faster                                             |
| sqlite_synth               | 2.99 us                                                    | 2.77 us: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                              |
| telco                      | 8.41 ms                                                    | 7.83 ms: 1.08x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.07x faster                                              |
| coverage                   | 93.1 ms                                                    | 86.8 ms: 1.07x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                              |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                            |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                             |
| regex_dna                  | 221 ms                                                     | 210 ms: 1.05x faster                                              |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.05x faster                                             |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                             |
| regex_effbot               | 3.67 ms                                                    | 3.50 ms: 1.05x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 893 ms: 1.05x faster                                              |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                             |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                              |
| asyncio_tcp                | 508 ms                                                     | 486 ms: 1.05x faster                                              |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                             |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                             |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                              |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                              |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                              |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                             |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                              |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                            |
| unpickle                   | 15.1 us                                                    | 14.8 us: 1.02x faster                                             |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                              |
| pickle_dict                | 34.8 us                                                    | 34.1 us: 1.02x faster                                             |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                            |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                             |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                             |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                             |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.00x faster                                              |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                              |
| bench_thread_pool          | 834 us                                                     | 839 us: 1.01x slower                                              |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                             |
| json                       | 5.31 ms                                                    | 5.35 ms: 1.01x slower                                             |
| unpickle_list              | 5.34 us                                                    | 5.40 us: 1.01x slower                                             |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                             |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                             |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.01x slower                                            |
| tornado_http               | 94.6 ms                                                    | 96.1 ms: 1.02x slower                                             |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                             |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                              |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                             |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                              |
| genshi_text                | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                             |
| dulwich_log                | 67.2 ms                                                    | 69.4 ms: 1.03x slower                                             |
| pickle_list                | 5.11 us                                                    | 5.29 us: 1.04x slower                                             |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                              |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                              |
| nqueens                    | 81.4 ms                                                    | 85.1 ms: 1.05x slower                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 58.3 ms: 1.05x slower                                             |
| docutils                   | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                            |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                              |
| sympy_expand               | 473 ms                                                     | 511 ms: 1.08x slower                                              |
| hexiom                     | 6.30 ms                                                    | 6.84 ms: 1.09x slower                                             |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                             |
| sympy_sum                  | 156 ms                                                     | 174 ms: 1.12x slower                                              |
| generators                 | 29.6 ms                                                    | 33.2 ms: 1.12x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                             |
| pylint                     | 317 ms                                                     | 373 ms: 1.18x slower                                              |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                      |

Benchmark hidden because not significant (4): async_tree_io, typing_runtime_protocols, comprehensions, bench_mp_pool
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240906-3.14.0a0-d2146e9-JIT/bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x