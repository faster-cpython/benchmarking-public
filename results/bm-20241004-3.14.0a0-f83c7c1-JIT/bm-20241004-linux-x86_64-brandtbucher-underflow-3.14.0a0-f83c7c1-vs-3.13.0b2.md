# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: f83c7c1
- commit date: 2024-10-04
- overall geometric mean: 1.01x faster
- HPT reliability: 99.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 291 ms: 1.06x slower                                             |
| docutils       | 2.83 sec                                                   | 3.07 sec: 1.09x slower                                           |
| html5lib       | 67.2 ms                                                    | 71.3 ms: 1.06x slower                                            |
| tornado_http   | 94.6 ms                                                    | 102 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                      | 1.07x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                             |
| async_tree_io              | 939 ms                                                     | 890 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 557 ms: 1.05x faster                                             |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.3 ms: 1.11x faster                                            |
| nbody          | 88.3 ms                                                    | 81.5 ms: 1.08x faster                                            |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                      | 1.07x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                             |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                            |
| regex_compile  | 137 ms                                                     | 155 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                      | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.0 ms: 1.14x faster                                            |
| xml_etree_process    | 61.2 ms                                                    | 55.4 ms: 1.10x faster                                            |
| xml_etree_iterparse  | 107 ms                                                     | 97.4 ms: 1.10x faster                                            |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                             |
| unpickle_pure_python | 218 us                                                     | 202 us: 1.08x faster                                             |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                            |
| unpickle_list        | 5.34 us                                                    | 5.14 us: 1.04x faster                                            |
| unpickle             | 15.1 us                                                    | 14.6 us: 1.04x faster                                            |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                           |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                            |
| pickle_list          | 5.11 us                                                    | 5.07 us: 1.01x faster                                            |
| pickle               | 11.5 us                                                    | 11.6 us: 1.02x slower                                            |
| pickle_pure_python   | 305 us                                                     | 318 us: 1.04x slower                                             |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                     |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                            |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                            |
| genshi_text     | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                            |
| django_template | 34.8 ms                                                    | 41.1 ms: 1.18x slower                                            |
| genshi_xml      | 51.6 ms                                                    | 70.3 ms: 1.36x slower                                            |
| Geometric mean  | (ref)                                                      | 1.10x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.6 us: 1.49x faster                                            |
| deepcopy                   | 367 us                                                     | 267 us: 1.38x faster                                             |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                             |
| richards                   | 50.9 ms                                                    | 40.6 ms: 1.25x faster                                            |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                            |
| richards_super             | 57.4 ms                                                    | 46.2 ms: 1.24x faster                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.44 ms: 1.19x faster                                            |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                             |
| crypto_pyaes               | 77.5 ms                                                    | 67.0 ms: 1.16x faster                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.0 ms: 1.15x faster                                            |
| mako                       | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                            |
| xml_etree_generate         | 87.4 ms                                                    | 77.0 ms: 1.14x faster                                            |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.13x faster                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                             |
| telco                      | 8.41 ms                                                    | 7.51 ms: 1.12x faster                                            |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                             |
| float                      | 78.9 ms                                                    | 71.3 ms: 1.11x faster                                            |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.11x faster                                            |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.10x faster                                           |
| xml_etree_process          | 61.2 ms                                                    | 55.4 ms: 1.10x faster                                            |
| xml_etree_iterparse        | 107 ms                                                     | 97.4 ms: 1.10x faster                                            |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                             |
| pyflate                    | 484 ms                                                     | 440 ms: 1.10x faster                                             |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                            |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.09x faster                                             |
| nbody                      | 88.3 ms                                                    | 81.5 ms: 1.08x faster                                            |
| unpickle_pure_python       | 218 us                                                     | 202 us: 1.08x faster                                             |
| gc_traversal               | 3.98 ms                                                    | 3.69 ms: 1.08x faster                                            |
| coverage                   | 93.1 ms                                                    | 86.5 ms: 1.08x faster                                            |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                             |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                            |
| go                         | 145 ms                                                     | 136 ms: 1.06x faster                                             |
| fannkuch                   | 402 ms                                                     | 380 ms: 1.06x faster                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.06x faster                                            |
| async_tree_io              | 939 ms                                                     | 890 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 557 ms: 1.05x faster                                             |
| json                       | 5.31 ms                                                    | 5.05 ms: 1.05x faster                                            |
| thrift                     | 823 us                                                     | 784 us: 1.05x faster                                             |
| scimark_sor                | 127 ms                                                     | 122 ms: 1.05x faster                                             |
| unpickle_list              | 5.34 us                                                    | 5.14 us: 1.04x faster                                            |
| unpickle                   | 15.1 us                                                    | 14.6 us: 1.04x faster                                            |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                             |
| pprint_safe_repr           | 758 ms                                                     | 738 ms: 1.03x faster                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                           |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                             |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                           |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                            |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                            |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                             |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                             |
| chaos                      | 61.3 ms                                                    | 60.4 ms: 1.02x faster                                            |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                            |
| asyncio_tcp                | 508 ms                                                     | 502 ms: 1.01x faster                                             |
| pickle_list                | 5.11 us                                                    | 5.07 us: 1.01x faster                                            |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                            |
| logging_format             | 6.47 us                                                    | 6.52 us: 1.01x slower                                            |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                            |
| deltablue                  | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                            |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                            |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                             |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.02x slower                                            |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                             |
| genshi_text                | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                            |
| pickle_pure_python         | 305 us                                                     | 318 us: 1.04x slower                                             |
| logging_simple             | 5.74 us                                                    | 5.99 us: 1.04x slower                                            |
| nqueens                    | 81.4 ms                                                    | 85.1 ms: 1.05x slower                                            |
| raytrace                   | 267 ms                                                     | 282 ms: 1.06x slower                                             |
| 2to3                       | 274 ms                                                     | 291 ms: 1.06x slower                                             |
| html5lib                   | 67.2 ms                                                    | 71.3 ms: 1.06x slower                                            |
| logging_silent             | 105 ns                                                     | 111 ns: 1.06x slower                                             |
| bench_thread_pool          | 834 us                                                     | 902 us: 1.08x slower                                             |
| tornado_http               | 94.6 ms                                                    | 102 ms: 1.08x slower                                             |
| docutils                   | 2.83 sec                                                   | 3.07 sec: 1.09x slower                                           |
| dulwich_log                | 67.2 ms                                                    | 73.6 ms: 1.10x slower                                            |
| hexiom                     | 6.30 ms                                                    | 6.97 ms: 1.11x slower                                            |
| sqlglot_transpile          | 1.63 ms                                                    | 1.83 ms: 1.12x slower                                            |
| pycparser                  | 1.16 sec                                                   | 1.30 sec: 1.12x slower                                           |
| regex_compile              | 137 ms                                                     | 155 ms: 1.13x slower                                             |
| sympy_expand               | 473 ms                                                     | 537 ms: 1.14x slower                                             |
| sqlglot_normalize          | 110 ms                                                     | 126 ms: 1.14x slower                                             |
| sympy_str                  | 282 ms                                                     | 323 ms: 1.14x slower                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 63.8 ms: 1.15x slower                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.54 ms: 1.16x slower                                            |
| django_template            | 34.8 ms                                                    | 41.1 ms: 1.18x slower                                            |
| generators                 | 29.6 ms                                                    | 35.3 ms: 1.19x slower                                            |
| sympy_sum                  | 156 ms                                                     | 191 ms: 1.23x slower                                             |
| pylint                     | 317 ms                                                     | 400 ms: 1.26x slower                                             |
| sympy_integrate            | 20.5 ms                                                    | 26.1 ms: 1.27x slower                                            |
| genshi_xml                 | 51.6 ms                                                    | 70.3 ms: 1.36x slower                                            |
| bench_mp_pool              | 23.9 ms                                                    | 60.9 ms: 2.55x slower                                            |
| Geometric mean             | (ref)                                                      | 1.01x faster                                                     |

Benchmark hidden because not significant (3): pickle_dict, regex_effbot, pprint_pformat
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-f83c7c1-JIT/bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1.json: unpack_sequence

# HPT report

- Reliability score: 99.40% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x