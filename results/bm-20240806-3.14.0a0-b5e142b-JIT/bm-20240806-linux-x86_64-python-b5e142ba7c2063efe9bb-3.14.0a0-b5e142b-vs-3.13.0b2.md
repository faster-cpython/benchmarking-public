# Results vs. 3.13.0b2

- fork: python
- ref: b5e142ba7c2063efe9bb
- machine: linux-x86_64
- commit hash: b5e142b
- commit date: 2024-08-06
- overall geometric mean: 1.05x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                |
| html5lib       | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 92.6 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 864 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                                  |
| async_tree_io              | 939 ms                                                     | 910 ms: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                 |
| nbody          | 88.3 ms                                                    | 79.1 ms: 1.12x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                 |
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                                  |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 99.2 ms: 1.08x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 81.6 ms: 1.07x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 24.5 ms: 1.03x slower                                                 |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 53.4 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.1 us: 1.36x faster                                                 |
| deepcopy                   | 367 us                                                     | 273 us: 1.34x faster                                                  |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                  |
| richards                   | 50.9 ms                                                    | 41.2 ms: 1.24x faster                                                 |
| richards_super             | 57.4 ms                                                    | 47.5 ms: 1.21x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.78 us: 1.20x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                                 |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.55 ms: 1.16x faster                                                 |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                  |
| mako                       | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.7 ms: 1.14x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                  |
| pyflate                    | 484 ms                                                     | 432 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                  |
| float                      | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                  |
| nbody                      | 88.3 ms                                                    | 79.1 ms: 1.12x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.52 sec: 1.11x faster                                                |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                  |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                |
| fannkuch                   | 402 ms                                                     | 371 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 864 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 99.2 ms: 1.08x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 81.6 ms: 1.07x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                 |
| telco                      | 8.41 ms                                                    | 7.97 ms: 1.06x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.1 ms: 1.06x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 722 ms: 1.05x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.17 us: 1.05x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.04x faster                                                |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                                 |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                  |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                                 |
| async_tree_io              | 939 ms                                                     | 910 ms: 1.03x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.57 us: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.02x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 92.6 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 822 us: 1.01x faster                                                  |
| coverage                   | 93.1 ms                                                    | 91.8 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                 |
| logging_silent             | 105 ns                                                     | 104 ns: 1.00x faster                                                  |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 55.9 ms: 1.01x slower                                                 |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                 |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                  |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                  |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.02x slower                                                |
| async_generators           | 442 ms                                                     | 453 ms: 1.02x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 84.0 ms: 1.03x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                |
| genshi_text                | 23.7 ms                                                    | 24.5 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                  |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 53.4 ms: 1.04x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.83 ms: 1.04x slower                                                 |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.71 ms: 1.07x slower                                                 |
| sympy_expand               | 473 ms                                                     | 508 ms: 1.08x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                 |
| deltablue                  | 3.25 ms                                                    | 3.58 ms: 1.10x slower                                                 |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                                 |
| pylint                     | 317 ms                                                     | 356 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x