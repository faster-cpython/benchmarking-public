# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: f133a86
- commit date: 2024-07-14
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 269 ms: 1.02x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                                |
| html5lib       | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                  |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 847 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 77.1 ms: 1.15x faster                                                 |
| float          | 78.9 ms                                                    | 69.6 ms: 1.13x faster                                                 |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                 |
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 99.9 ms: 1.08x faster                                                 |
| json_loads           | 28.9 us                                                    | 27.5 us: 1.05x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 58.8 ms: 1.04x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 84.2 ms: 1.04x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 294 us: 1.04x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                 |
| django_template | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 56.1 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.2 us: 1.41x faster                                                 |
| deepcopy                   | 367 us                                                     | 271 us: 1.35x faster                                                  |
| richards                   | 50.9 ms                                                    | 40.8 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                                 |
| richards_super             | 57.4 ms                                                    | 46.8 ms: 1.23x faster                                                 |
| scimark_fft                | 392 ms                                                     | 322 ms: 1.22x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 66.9 ms: 1.16x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.3 ms: 1.15x faster                                                 |
| nbody                      | 88.3 ms                                                    | 77.1 ms: 1.15x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.13x faster                                                  |
| float                      | 78.9 ms                                                    | 69.6 ms: 1.13x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.70 ms: 1.12x faster                                                 |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 847 ms: 1.10x faster                                                  |
| fannkuch                   | 402 ms                                                     | 365 ms: 1.10x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                  |
| pyflate                    | 484 ms                                                     | 445 ms: 1.09x faster                                                  |
| spectral_norm              | 116 ms                                                     | 107 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 99.9 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.04 us: 1.07x faster                                                 |
| chaos                      | 61.3 ms                                                    | 57.4 ms: 1.07x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.61 sec: 1.07x faster                                                |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| regex_v8                   | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.45 us: 1.05x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.26 ms: 1.05x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 724 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.82 sec: 1.04x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 58.8 ms: 1.04x faster                                                 |
| telco                      | 8.41 ms                                                    | 8.09 ms: 1.04x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 84.2 ms: 1.04x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 294 us: 1.04x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.04x faster                                                 |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                                |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| json                       | 5.31 ms                                                    | 5.15 ms: 1.03x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| dask                       | 369 ms                                                     | 361 ms: 1.02x faster                                                  |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| 2to3                       | 274 ms                                                     | 269 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 54.6 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                 |
| thrift                     | 823 us                                                     | 811 us: 1.01x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 502 ms: 1.01x faster                                                  |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                  |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 836 us: 1.00x slower                                                  |
| dulwich_log                | 67.2 ms                                                    | 67.4 ms: 1.00x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.13 ms: 1.00x slower                                                 |
| generators                 | 29.6 ms                                                    | 29.8 ms: 1.00x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                 |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                 |
| django_template            | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                 |
| docutils                   | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                                |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                  |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                                  |
| logging_silent             | 105 ns                                                     | 106 ns: 1.02x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.47 ms: 1.03x slower                                                 |
| sympy_str                  | 282 ms                                                     | 291 ms: 1.03x slower                                                  |
| coroutines                 | 23.2 ms                                                    | 24.0 ms: 1.03x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.04x slower                                                  |
| sympy_expand               | 473 ms                                                     | 492 ms: 1.04x slower                                                  |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 85.8 ms: 1.05x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 165 ms: 1.06x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 21.7 ms: 1.06x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 56.1 ms: 1.09x slower                                                 |
| deltablue                  | 3.25 ms                                                    | 3.54 ms: 1.09x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (4): coverage, regex_effbot, sqlglot_normalize, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x