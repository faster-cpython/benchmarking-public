# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: 222cf15
- commit date: 2024-07-25
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 92.7 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 416 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                        |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.1 ms: 1.12x faster                                                       |
| nbody          | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                       |
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                       |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|---------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse     | 162 ms                                                     | 146 ms: 1.10x faster                                                        |
| tomli_loads         | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                      |
| xml_etree_generate  | 87.4 ms                                                    | 80.1 ms: 1.09x faster                                                       |
| xml_etree_process   | 61.2 ms                                                    | 56.3 ms: 1.09x faster                                                       |
| xml_etree_iterparse | 107 ms                                                     | 99.1 ms: 1.08x faster                                                       |
| json_loads          | 28.9 us                                                    | 27.9 us: 1.04x faster                                                       |
| pickle_pure_python  | 305 us                                                     | 295 us: 1.03x faster                                                        |
| json_dumps          | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| Geometric mean      | (ref)                                                      | 1.06x faster                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.7 us: 1.38x faster                                                       |
| deepcopy                   | 367 us                                                     | 272 us: 1.35x faster                                                        |
| scimark_fft                | 392 ms                                                     | 305 ms: 1.29x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.14 ms: 1.27x faster                                                       |
| richards                   | 50.9 ms                                                    | 40.2 ms: 1.27x faster                                                       |
| richards_super             | 57.4 ms                                                    | 46.7 ms: 1.23x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 59.9 ms: 1.15x faster                                                       |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.44 sec: 1.13x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                        |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                        |
| float                      | 78.9 ms                                                    | 70.1 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 416 ms: 1.11x faster                                                        |
| pyflate                    | 484 ms                                                     | 436 ms: 1.11x faster                                                        |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.10x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                      |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                                        |
| nbody                      | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.64 ms: 1.09x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 80.1 ms: 1.09x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 56.3 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.95 ms: 1.06x faster                                                       |
| chaos                      | 61.3 ms                                                    | 58.0 ms: 1.06x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 721 ms: 1.05x faster                                                        |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 64.2 ms: 1.05x faster                                                       |
| thrift                     | 823 us                                                     | 788 us: 1.04x faster                                                        |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                        |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                       |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                                       |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.03x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| regex_compile              | 137 ms                                                     | 133 ms: 1.03x faster                                                        |
| generators                 | 29.6 ms                                                    | 28.9 ms: 1.03x faster                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                       |
| json                       | 5.31 ms                                                    | 5.18 ms: 1.02x faster                                                       |
| tornado_http               | 94.6 ms                                                    | 92.7 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                        |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                       |
| 2to3                       | 274 ms                                                     | 270 ms: 1.01x faster                                                        |
| coverage                   | 93.1 ms                                                    | 92.2 ms: 1.01x faster                                                       |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                        |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 827 us: 1.01x faster                                                        |
| raytrace                   | 267 ms                                                     | 268 ms: 1.00x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 55.8 ms: 1.00x slower                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                       |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                        |
| regex_dna                  | 221 ms                                                     | 226 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                      |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 6.52 ms: 1.04x slower                                                       |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.04x slower                                                        |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                        |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.04x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 25.0 ms: 1.05x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                                       |
| sympy_expand               | 473 ms                                                     | 498 ms: 1.05x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.57 ms: 1.10x slower                                                       |
| pylint                     | 317 ms                                                     | 350 ms: 1.10x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 59.0 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (5): dask, typing_runtime_protocols, comprehensions, scimark_sor, unpickle_pure_python
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x