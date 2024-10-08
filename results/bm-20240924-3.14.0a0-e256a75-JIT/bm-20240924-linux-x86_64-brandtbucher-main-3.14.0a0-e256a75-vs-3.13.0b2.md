# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                        |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                      |
| html5lib       | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 317 ms: 1.19x faster                                        |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                        |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.09x faster                                        |
| async_tree_io_tg           | 936 ms                                                     | 873 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 573 ms: 1.07x faster                                        |
| async_tree_io              | 939 ms                                                     | 885 ms: 1.06x faster                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 555 ms: 1.06x faster                                        |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.2 ms: 1.14x faster                                       |
| nbody          | 88.3 ms                                                    | 79.3 ms: 1.11x faster                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                       |
| regex_dna      | 221 ms                                                     | 225 ms: 1.02x slower                                        |
| regex_compile  | 137 ms                                                     | 142 ms: 1.03x slower                                        |
| regex_effbot   | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                      | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.2 ms: 1.13x faster                                       |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.12x faster                                        |
| xml_etree_process    | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                       |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                       |
| json_loads           | 28.9 us                                                    | 27.0 us: 1.07x faster                                       |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                       |
| unpickle             | 15.1 us                                                    | 14.5 us: 1.04x faster                                       |
| unpickle_list        | 5.34 us                                                    | 5.18 us: 1.03x faster                                       |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                        |
| pickle_dict          | 34.8 us                                                    | 34.3 us: 1.01x faster                                       |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                        |
| pickle_list          | 5.11 us                                                    | 5.16 us: 1.01x slower                                       |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                       |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.80 ms: 1.15x faster                                       |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                       |
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                       |
| genshi_xml      | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                       |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                       |
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                        |
| richards                   | 50.9 ms                                                    | 39.4 ms: 1.29x faster                                       |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                        |
| richards_super             | 57.4 ms                                                    | 45.2 ms: 1.27x faster                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.16 ms: 1.27x faster                                       |
| async_tree_none            | 378 ms                                                     | 317 ms: 1.19x faster                                        |
| crypto_pyaes               | 77.5 ms                                                    | 66.4 ms: 1.17x faster                                       |
| spectral_norm              | 116 ms                                                     | 100.0 ms: 1.16x faster                                      |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                        |
| mako                       | 11.2 ms                                                    | 9.80 ms: 1.15x faster                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                        |
| float                      | 78.9 ms                                                    | 69.2 ms: 1.14x faster                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.42 sec: 1.14x faster                                      |
| xml_etree_generate         | 87.4 ms                                                    | 77.2 ms: 1.13x faster                                       |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.12x faster                                        |
| xml_etree_process          | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.9 ms: 1.12x faster                                       |
| nbody                      | 88.3 ms                                                    | 79.3 ms: 1.11x faster                                       |
| go                         | 145 ms                                                     | 131 ms: 1.10x faster                                        |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                       |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                      |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                        |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                        |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                      |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                       |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                       |
| coverage                   | 93.1 ms                                                    | 85.6 ms: 1.09x faster                                       |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.09x faster                                        |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                        |
| pyflate                    | 484 ms                                                     | 450 ms: 1.08x faster                                        |
| gc_traversal               | 3.98 ms                                                    | 3.70 ms: 1.07x faster                                       |
| async_tree_io_tg           | 936 ms                                                     | 873 ms: 1.07x faster                                        |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 573 ms: 1.07x faster                                        |
| async_tree_io              | 939 ms                                                     | 885 ms: 1.06x faster                                        |
| telco                      | 8.41 ms                                                    | 7.93 ms: 1.06x faster                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 555 ms: 1.06x faster                                        |
| json                       | 5.31 ms                                                    | 5.03 ms: 1.06x faster                                       |
| thrift                     | 823 us                                                     | 782 us: 1.05x faster                                        |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                       |
| unpickle                   | 15.1 us                                                    | 14.5 us: 1.04x faster                                       |
| chaos                      | 61.3 ms                                                    | 59.0 ms: 1.04x faster                                       |
| html5lib                   | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                       |
| logging_format             | 6.47 us                                                    | 6.23 us: 1.04x faster                                       |
| unpickle_list              | 5.34 us                                                    | 5.18 us: 1.03x faster                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                        |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                        |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                        |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                      |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                        |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                        |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                       |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                        |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                        |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                       |
| pickle_dict                | 34.8 us                                                    | 34.3 us: 1.01x faster                                       |
| pprint_safe_repr           | 758 ms                                                     | 748 ms: 1.01x faster                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                      |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                       |
| logging_simple             | 5.74 us                                                    | 5.68 us: 1.01x faster                                       |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                       |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                       |
| dulwich_log                | 67.2 ms                                                    | 67.7 ms: 1.01x slower                                       |
| pickle_pure_python         | 305 us                                                     | 308 us: 1.01x slower                                        |
| pickle_list                | 5.11 us                                                    | 5.16 us: 1.01x slower                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.01x slower                                       |
| regex_dna                  | 221 ms                                                     | 225 ms: 1.02x slower                                        |
| async_generators           | 442 ms                                                     | 450 ms: 1.02x slower                                        |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                       |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                        |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                        |
| regex_compile              | 137 ms                                                     | 142 ms: 1.03x slower                                        |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                       |
| regex_effbot               | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                       |
| docutils                   | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 58.0 ms: 1.05x slower                                       |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                       |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                        |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                        |
| nqueens                    | 81.4 ms                                                    | 86.4 ms: 1.06x slower                                       |
| hexiom                     | 6.30 ms                                                    | 6.86 ms: 1.09x slower                                       |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                        |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                       |
| genshi_xml                 | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                       |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                       |
| pylint                     | 317 ms                                                     | 371 ms: 1.17x slower                                        |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                |

Benchmark hidden because not significant (3): pycparser, tornado_http, bench_thread_pool
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x