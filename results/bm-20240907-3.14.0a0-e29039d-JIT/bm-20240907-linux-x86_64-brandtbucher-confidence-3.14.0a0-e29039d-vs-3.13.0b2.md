# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: e29039d
- commit date: 2024-09-07
- overall geometric mean: 1.05x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                              |
| docutils       | 2.83 sec                                                   | 3.01 sec: 1.06x slower                                            |
| html5lib       | 67.2 ms                                                    | 64.3 ms: 1.04x faster                                             |
| tornado_http   | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                      | 1.01x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.17x faster                                              |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                              |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                              |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                              |
| async_tree_none_tg         | 336 ms                                                     | 312 ms: 1.08x faster                                              |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                              |
| async_tree_io_tg           | 936 ms                                                     | 897 ms: 1.04x faster                                              |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                      |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                             |
| nbody          | 88.3 ms                                                    | 79.5 ms: 1.11x faster                                             |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                      | 1.09x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                             |
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                              |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                              |
| regex_effbot   | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                      | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.3 ms: 1.13x faster                                             |
| xml_etree_process    | 61.2 ms                                                    | 54.8 ms: 1.12x faster                                             |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.12x faster                                              |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                            |
| xml_etree_iterparse  | 107 ms                                                     | 98.3 ms: 1.09x faster                                             |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                             |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                              |
| unpickle_list        | 5.34 us                                                    | 5.18 us: 1.03x faster                                             |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                              |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                             |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.00x faster                                             |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                             |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                      |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                             |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.84 ms: 1.14x faster                                             |
| genshi_text     | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                             |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                             |
| genshi_xml      | 51.6 ms                                                    | 56.7 ms: 1.10x slower                                             |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.8 us: 1.48x faster                                             |
| deepcopy                   | 367 us                                                     | 269 us: 1.37x faster                                              |
| richards_super             | 57.4 ms                                                    | 43.0 ms: 1.34x faster                                             |
| richards                   | 50.9 ms                                                    | 38.9 ms: 1.31x faster                                             |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                              |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.25x faster                                             |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.36 ms: 1.21x faster                                             |
| spectral_norm              | 116 ms                                                     | 98.6 ms: 1.18x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.17x faster                                              |
| crypto_pyaes               | 77.5 ms                                                    | 66.0 ms: 1.17x faster                                             |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                              |
| mako                       | 11.2 ms                                                    | 9.84 ms: 1.14x faster                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.41 sec: 1.14x faster                                            |
| xml_etree_generate         | 87.4 ms                                                    | 77.3 ms: 1.13x faster                                             |
| float                      | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                             |
| pyflate                    | 484 ms                                                     | 432 ms: 1.12x faster                                              |
| xml_etree_process          | 61.2 ms                                                    | 54.8 ms: 1.12x faster                                             |
| scimark_sor                | 127 ms                                                     | 114 ms: 1.12x faster                                              |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.12x faster                                              |
| go                         | 145 ms                                                     | 130 ms: 1.12x faster                                              |
| nbody                      | 88.3 ms                                                    | 79.5 ms: 1.11x faster                                             |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                              |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                              |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.1 ms: 1.10x faster                                             |
| xml_etree_iterparse        | 107 ms                                                     | 98.3 ms: 1.09x faster                                             |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                             |
| coverage                   | 93.1 ms                                                    | 85.8 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                              |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                              |
| telco                      | 8.41 ms                                                    | 7.81 ms: 1.08x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 312 ms: 1.08x faster                                              |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                              |
| mdp                        | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                            |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                             |
| gc_traversal               | 3.98 ms                                                    | 3.74 ms: 1.06x faster                                             |
| pprint_safe_repr           | 758 ms                                                     | 718 ms: 1.06x faster                                              |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                            |
| thrift                     | 823 us                                                     | 782 us: 1.05x faster                                              |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                             |
| html5lib                   | 67.2 ms                                                    | 64.3 ms: 1.04x faster                                             |
| logging_format             | 6.47 us                                                    | 6.19 us: 1.04x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 897 ms: 1.04x faster                                              |
| coroutines                 | 23.2 ms                                                    | 22.3 ms: 1.04x faster                                             |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                             |
| asyncio_tcp                | 508 ms                                                     | 488 ms: 1.04x faster                                              |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                              |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                              |
| unpickle_list              | 5.34 us                                                    | 5.18 us: 1.03x faster                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                             |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                              |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                              |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                              |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                              |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                             |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                             |
| logging_simple             | 5.74 us                                                    | 5.68 us: 1.01x faster                                             |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                             |
| deltablue                  | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                             |
| pickle_list                | 5.11 us                                                    | 5.08 us: 1.00x faster                                             |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                              |
| tornado_http               | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                             |
| bench_thread_pool          | 834 us                                                     | 836 us: 1.00x slower                                              |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                              |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                             |
| genshi_text                | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                             |
| regex_compile              | 137 ms                                                     | 139 ms: 1.02x slower                                              |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                              |
| dulwich_log                | 67.2 ms                                                    | 68.6 ms: 1.02x slower                                             |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                             |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                             |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                             |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                              |
| regex_effbot               | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                             |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                              |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 57.9 ms: 1.04x slower                                             |
| nqueens                    | 81.4 ms                                                    | 85.5 ms: 1.05x slower                                             |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                              |
| docutils                   | 2.83 sec                                                   | 3.01 sec: 1.06x slower                                            |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                              |
| hexiom                     | 6.30 ms                                                    | 6.83 ms: 1.08x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 56.7 ms: 1.10x slower                                             |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                              |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                             |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                             |
| pylint                     | 317 ms                                                     | 371 ms: 1.17x slower                                              |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                      |

Benchmark hidden because not significant (8): async_tree_io, unpickle, typing_runtime_protocols, pickle_dict, json, sqlglot_parse, bench_mp_pool, comprehensions
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-e29039d-JIT/bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d.json: unpack_sequence

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x