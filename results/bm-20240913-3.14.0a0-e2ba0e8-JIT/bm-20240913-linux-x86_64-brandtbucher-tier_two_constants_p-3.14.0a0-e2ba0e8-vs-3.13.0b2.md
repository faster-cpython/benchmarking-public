# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_constants_p
- machine: linux-x86_64
- commit hash: e2ba0e8
- commit date: 2024-09-13
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                        |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                      |
| html5lib       | 67.2 ms                                                    | 65.6 ms: 1.03x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 95.1 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 400 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 577 ms: 1.06x faster                                                        |
| async_tree_io              | 939 ms                                                     | 888 ms: 1.06x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.6 ms: 1.13x faster                                                       |
| nbody          | 88.3 ms                                                    | 81.7 ms: 1.08x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                       |
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                       |
| regex_compile  | 137 ms                                                     | 142 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 76.9 ms: 1.14x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 54.1 ms: 1.13x faster                                                       |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.6 ms: 1.09x faster                                                       |
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.07x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                                        |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                        |
| pickle_dict          | 34.8 us                                                    | 34.6 us: 1.01x faster                                                       |
| pickle               | 11.5 us                                                    | 11.8 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (3): unpickle, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.73 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                       |
| deepcopy                   | 367 us                                                     | 277 us: 1.33x faster                                                        |
| richards                   | 50.9 ms                                                    | 39.6 ms: 1.28x faster                                                       |
| richards_super             | 57.4 ms                                                    | 45.1 ms: 1.27x faster                                                       |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.23x faster                                                       |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.47 ms: 1.18x faster                                                       |
| spectral_norm              | 116 ms                                                     | 99.6 ms: 1.17x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 400 ms: 1.16x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.73 ms: 1.15x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 67.3 ms: 1.15x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.40 sec: 1.14x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 76.9 ms: 1.14x faster                                                       |
| float                      | 78.9 ms                                                    | 69.6 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 54.1 ms: 1.13x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| go                         | 145 ms                                                     | 131 ms: 1.10x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                        |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.3 ms: 1.09x faster                                                       |
| coverage                   | 93.1 ms                                                    | 85.3 ms: 1.09x faster                                                       |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.6 ms: 1.09x faster                                                       |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                        |
| pyflate                    | 484 ms                                                     | 447 ms: 1.08x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                       |
| nbody                      | 88.3 ms                                                    | 81.7 ms: 1.08x faster                                                       |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                       |
| fannkuch                   | 402 ms                                                     | 374 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.98 sec: 1.07x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 577 ms: 1.06x faster                                                        |
| async_tree_io              | 939 ms                                                     | 888 ms: 1.06x faster                                                        |
| json                       | 5.31 ms                                                    | 5.02 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 722 ms: 1.05x faster                                                        |
| telco                      | 8.41 ms                                                    | 8.07 ms: 1.04x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.21 us: 1.04x faster                                                       |
| chaos                      | 61.3 ms                                                    | 59.2 ms: 1.04x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                       |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                                        |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 65.6 ms: 1.03x faster                                                       |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                        |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.02x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.67 us: 1.01x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 502 ms: 1.01x faster                                                        |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                       |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                        |
| pickle_dict                | 34.8 us                                                    | 34.6 us: 1.01x faster                                                       |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                        |
| tornado_http               | 94.6 ms                                                    | 95.1 ms: 1.00x slower                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| bench_thread_pool          | 834 us                                                     | 839 us: 1.01x slower                                                        |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                       |
| dulwich_log                | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                       |
| 2to3                       | 274 ms                                                     | 280 ms: 1.02x slower                                                        |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.02x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                        |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.36 ms: 1.03x slower                                                       |
| regex_compile              | 137 ms                                                     | 142 ms: 1.03x slower                                                        |
| comprehensions             | 16.6 us                                                    | 17.2 us: 1.04x slower                                                       |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.71 ms: 1.04x slower                                                       |
| docutils                   | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                      |
| raytrace                   | 267 ms                                                     | 280 ms: 1.05x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 58.7 ms: 1.06x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 86.5 ms: 1.06x slower                                                       |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                                        |
| sympy_expand               | 473 ms                                                     | 508 ms: 1.07x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                       |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 7.05 ms: 1.12x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 23.1 ms: 1.12x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 176 ms: 1.13x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                       |
| pylint                     | 317 ms                                                     | 376 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (4): unpickle, typing_runtime_protocols, unpickle_list, pickle_list
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240913-3.14.0a0-e2ba0e8-JIT/bm-20240913-linux-x86_64-brandtbucher-tier_two_constants_p-3.14.0a0-e2ba0e8.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x