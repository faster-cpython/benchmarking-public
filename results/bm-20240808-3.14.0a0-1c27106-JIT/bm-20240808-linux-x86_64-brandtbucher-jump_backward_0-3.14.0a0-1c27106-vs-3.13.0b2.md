# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 1c27106
- commit date: 2024-08-08
- overall geometric mean: 1.01x faster
- HPT reliability: 95.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.02x slower                                                   |
| docutils       | 2.83 sec                                                   | 3.09 sec: 1.09x slower                                                 |
| html5lib       | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 110 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                      | 1.06x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 338 ms: 1.12x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.08x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 879 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.06x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 441 ms: 1.05x faster                                                   |
| Geometric mean             | (ref)                                                      | 1.07x faster                                                           |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                  |
| nbody          | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                  |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.41 ms: 1.08x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                  |
| regex_dna      | 221 ms                                                     | 213 ms: 1.04x faster                                                   |
| regex_compile  | 137 ms                                                     | 139 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 56.1 ms: 1.09x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 80.6 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 99.6 ms: 1.08x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.06x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.02x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.01x slower                                                   |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.3 ms: 1.09x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                  |
| genshi_xml      | 51.6 ms                                                    | 56.9 ms: 1.10x slower                                                  |
| django_template | 34.8 ms                                                    | 39.5 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 275 us: 1.34x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 30.0 us: 1.33x faster                                                  |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.33 ms: 1.22x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 59.2 ms: 1.17x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 66.4 ms: 1.17x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.93 us: 1.14x faster                                                  |
| async_tree_none            | 378 ms                                                     | 338 ms: 1.12x faster                                                   |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.54 sec: 1.11x faster                                                 |
| float                      | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                  |
| nbody                      | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                   |
| mako                       | 11.2 ms                                                    | 10.3 ms: 1.09x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 56.1 ms: 1.09x faster                                                  |
| telco                      | 8.41 ms                                                    | 7.72 ms: 1.09x faster                                                  |
| fannkuch                   | 402 ms                                                     | 369 ms: 1.09x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 80.6 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 99.6 ms: 1.08x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.41 ms: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                                 |
| scimark_sor                | 127 ms                                                     | 119 ms: 1.07x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.61 sec: 1.07x faster                                                 |
| richards                   | 50.9 ms                                                    | 47.6 ms: 1.07x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 879 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.06x faster                                                   |
| richards_super             | 57.4 ms                                                    | 54.0 ms: 1.06x faster                                                  |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.06x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.06x faster                                                  |
| pyflate                    | 484 ms                                                     | 459 ms: 1.05x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 441 ms: 1.05x faster                                                   |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 726 ms: 1.04x faster                                                   |
| regex_v8                   | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                                  |
| json                       | 5.31 ms                                                    | 5.10 ms: 1.04x faster                                                  |
| regex_dna                  | 221 ms                                                     | 213 ms: 1.04x faster                                                   |
| chaos                      | 61.3 ms                                                    | 59.5 ms: 1.03x faster                                                  |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                   |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                   |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.02x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.83 sec: 1.01x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                  |
| regex_compile              | 137 ms                                                     | 139 ms: 1.01x slower                                                   |
| pickle_pure_python         | 305 us                                                     | 310 us: 1.01x slower                                                   |
| unpickle_pure_python       | 218 us                                                     | 222 us: 1.02x slower                                                   |
| comprehensions             | 16.6 us                                                    | 16.9 us: 1.02x slower                                                  |
| 2to3                       | 274 ms                                                     | 281 ms: 1.02x slower                                                   |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                   |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.03x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.37 ms: 1.04x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 84.4 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                   |
| thrift                     | 823 us                                                     | 859 us: 1.04x slower                                                   |
| go                         | 145 ms                                                     | 151 ms: 1.05x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.72 ms: 1.05x slower                                                  |
| asyncio_tcp                | 508 ms                                                     | 535 ms: 1.05x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 117 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 59.2 ms: 1.07x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                  |
| bench_thread_pool          | 834 us                                                     | 893 us: 1.07x slower                                                   |
| docutils                   | 2.83 sec                                                   | 3.09 sec: 1.09x slower                                                 |
| raytrace                   | 267 ms                                                     | 293 ms: 1.10x slower                                                   |
| coroutines                 | 23.2 ms                                                    | 25.5 ms: 1.10x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 56.9 ms: 1.10x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.94 ms: 1.10x slower                                                  |
| django_template            | 34.8 ms                                                    | 39.5 ms: 1.13x slower                                                  |
| sympy_expand               | 473 ms                                                     | 541 ms: 1.14x slower                                                   |
| sympy_str                  | 282 ms                                                     | 325 ms: 1.15x slower                                                   |
| logging_simple             | 5.74 us                                                    | 6.63 us: 1.15x slower                                                  |
| logging_format             | 6.47 us                                                    | 7.47 us: 1.15x slower                                                  |
| generators                 | 29.6 ms                                                    | 34.4 ms: 1.16x slower                                                  |
| tornado_http               | 94.6 ms                                                    | 110 ms: 1.17x slower                                                   |
| sympy_integrate            | 20.5 ms                                                    | 25.1 ms: 1.22x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 197 ms: 1.27x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 4.13 ms: 1.27x slower                                                  |
| pylint                     | 317 ms                                                     | 408 ms: 1.29x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (2): async_tree_io, coverage
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 95.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x