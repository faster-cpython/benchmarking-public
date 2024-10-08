# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 4ab420c
- commit date: 2024-09-23
- overall geometric mean: 1.03x faster
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 285 ms: 1.04x slower                                                         |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                       |
| html5lib       | 67.2 ms                                                    | 66.2 ms: 1.02x faster                                                        |
| tornado_http   | 94.6 ms                                                    | 96.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 399 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 878 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                                         |
| async_tree_io              | 939 ms                                                     | 886 ms: 1.06x faster                                                         |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.4 ms: 1.11x faster                                                        |
| nbody          | 88.3 ms                                                    | 82.1 ms: 1.08x faster                                                        |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                         |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                                         |
| regex_effbot   | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                        |
| regex_v8       | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                                        |
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                                         |
| xml_etree_generate   | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 99.7 ms: 1.08x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.06x faster                                                        |
| json_loads           | 28.9 us                                                    | 27.4 us: 1.06x faster                                                        |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                         |
| pickle_dict          | 34.8 us                                                    | 34.6 us: 1.00x faster                                                        |
| unpickle_list        | 5.34 us                                                    | 5.32 us: 1.00x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 219 us: 1.00x slower                                                         |
| pickle_list          | 5.11 us                                                    | 5.18 us: 1.01x slower                                                        |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.94 ms: 1.13x faster                                                        |
| django_template | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                        |
| genshi_text     | 23.7 ms                                                    | 25.7 ms: 1.09x slower                                                        |
| genshi_xml      | 51.6 ms                                                    | 60.8 ms: 1.18x slower                                                        |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                                        |
| deepcopy                   | 367 us                                                     | 269 us: 1.36x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.25x faster                                                        |
| scimark_fft                | 392 ms                                                     | 317 ms: 1.24x faster                                                         |
| richards_super             | 57.4 ms                                                    | 47.0 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.40 ms: 1.20x faster                                                        |
| richards                   | 50.9 ms                                                    | 42.7 ms: 1.19x faster                                                        |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                         |
| async_tree_memoization     | 463 ms                                                     | 399 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                         |
| crypto_pyaes               | 77.5 ms                                                    | 67.9 ms: 1.14x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.94 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                         |
| float                      | 78.9 ms                                                    | 71.4 ms: 1.11x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                                        |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                         |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.7 ms: 1.09x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                                        |
| sqlite_synth               | 2.99 us                                                    | 2.77 us: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 99.7 ms: 1.08x faster                                                        |
| nbody                      | 88.3 ms                                                    | 82.1 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                         |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                                        |
| coverage                   | 93.1 ms                                                    | 86.9 ms: 1.07x faster                                                        |
| fannkuch                   | 402 ms                                                     | 376 ms: 1.07x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 878 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                                         |
| go                         | 145 ms                                                     | 136 ms: 1.06x faster                                                         |
| pyflate                    | 484 ms                                                     | 456 ms: 1.06x faster                                                         |
| async_tree_io              | 939 ms                                                     | 886 ms: 1.06x faster                                                         |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.06x faster                                                        |
| json_loads                 | 28.9 us                                                    | 27.4 us: 1.06x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.06x faster                                                        |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.05x faster                                                         |
| telco                      | 8.41 ms                                                    | 8.03 ms: 1.05x faster                                                        |
| thrift                     | 823 us                                                     | 786 us: 1.05x faster                                                         |
| gc_traversal               | 3.98 ms                                                    | 3.80 ms: 1.05x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.18 us: 1.05x faster                                                        |
| json                       | 5.31 ms                                                    | 5.08 ms: 1.05x faster                                                        |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.04x faster                                                         |
| chaos                      | 61.3 ms                                                    | 59.3 ms: 1.03x faster                                                        |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                         |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                         |
| asyncio_tcp                | 508 ms                                                     | 495 ms: 1.03x faster                                                         |
| bpe_tokeniser              | 5.02 sec                                                   | 4.90 sec: 1.02x faster                                                       |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                                         |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 66.2 ms: 1.02x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.68 us: 1.01x faster                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                        |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                         |
| pickle_dict                | 34.8 us                                                    | 34.6 us: 1.00x faster                                                        |
| unpickle_list              | 5.34 us                                                    | 5.32 us: 1.00x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 219 us: 1.00x slower                                                         |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                                       |
| bench_thread_pool          | 834 us                                                     | 841 us: 1.01x slower                                                         |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                         |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                        |
| dulwich_log                | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                        |
| coroutines                 | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 96.0 ms: 1.01x slower                                                        |
| pickle_list                | 5.11 us                                                    | 5.18 us: 1.01x slower                                                        |
| regex_compile              | 137 ms                                                     | 139 ms: 1.02x slower                                                         |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                                       |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                        |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                         |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                        |
| 2to3                       | 274 ms                                                     | 285 ms: 1.04x slower                                                         |
| regex_v8                   | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                        |
| raytrace                   | 267 ms                                                     | 281 ms: 1.06x slower                                                         |
| pycparser                  | 1.16 sec                                                   | 1.23 sec: 1.06x slower                                                       |
| django_template            | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                        |
| sympy_expand               | 473 ms                                                     | 503 ms: 1.07x slower                                                         |
| sqlglot_normalize          | 110 ms                                                     | 117 ms: 1.07x slower                                                         |
| nqueens                    | 81.4 ms                                                    | 87.7 ms: 1.08x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.7 ms: 1.09x slower                                                        |
| sympy_str                  | 282 ms                                                     | 308 ms: 1.09x slower                                                         |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                                         |
| deltablue                  | 3.25 ms                                                    | 3.65 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 64.3 ms: 1.16x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 60.8 ms: 1.18x slower                                                        |
| pylint                     | 317 ms                                                     | 380 ms: 1.20x slower                                                         |
| generators                 | 29.6 ms                                                    | 35.6 ms: 1.20x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 7.80 ms: 1.24x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 26.7 ms: 1.30x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                                 |

Benchmark hidden because not significant (3): unpickle, pprint_safe_repr, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-4ab420c-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c.json: unpack_sequence

# HPT report

- Reliability score: 99.59% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x