# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5f50be9
- commit date: 2024-07-26
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                        |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 67.2 ms                                                    | 64.4 ms: 1.04x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 92.9 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 420 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                        |
| async_tree_io              | 939 ms                                                     | 902 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 78.9 ms: 1.12x faster                                                       |
| float          | 78.9 ms                                                    | 71.2 ms: 1.11x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                                       |
| regex_v8       | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 144 ms: 1.12x faster                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 79.9 ms: 1.09x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                      |
| xml_etree_process    | 61.2 ms                                                    | 56.3 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 99.2 ms: 1.08x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 293 us: 1.04x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                       |
| json_loads           | 28.9 us                                                    | 28.0 us: 1.03x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                       |
| django_template | 34.8 ms                                                    | 35.0 ms: 1.01x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.8 us: 1.38x faster                                                       |
| deepcopy                   | 367 us                                                     | 269 us: 1.37x faster                                                        |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                        |
| richards                   | 50.9 ms                                                    | 40.4 ms: 1.26x faster                                                       |
| richards_super             | 57.4 ms                                                    | 46.6 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.40 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.81 us: 1.19x faster                                                       |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 67.2 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.2 ms: 1.15x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                                      |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.13x faster                                                        |
| xml_etree_parse            | 162 ms                                                     | 144 ms: 1.12x faster                                                        |
| nbody                      | 88.3 ms                                                    | 78.9 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                                        |
| float                      | 78.9 ms                                                    | 71.2 ms: 1.11x faster                                                       |
| pyflate                    | 484 ms                                                     | 438 ms: 1.11x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 420 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                        |
| xml_etree_generate         | 87.4 ms                                                    | 79.9 ms: 1.09x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                       |
| fannkuch                   | 402 ms                                                     | 368 ms: 1.09x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 56.3 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 99.2 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 758 ms                                                     | 706 ms: 1.07x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                      |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                                       |
| telco                      | 8.41 ms                                                    | 7.94 ms: 1.06x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.15 us: 1.05x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 64.4 ms: 1.04x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 293 us: 1.04x faster                                                        |
| async_tree_io              | 939 ms                                                     | 902 ms: 1.04x faster                                                        |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.55 us: 1.04x faster                                                       |
| generators                 | 29.6 ms                                                    | 28.7 ms: 1.03x faster                                                       |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| thrift                     | 823 us                                                     | 798 us: 1.03x faster                                                        |
| json                       | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.87 ms: 1.03x faster                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 497 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                                        |
| tornado_http               | 94.6 ms                                                    | 92.9 ms: 1.02x faster                                                       |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 827 us: 1.01x faster                                                        |
| coverage                   | 93.1 ms                                                    | 92.3 ms: 1.01x faster                                                       |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                                        |
| go                         | 145 ms                                                     | 144 ms: 1.01x faster                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 55.9 ms: 1.01x slower                                                       |
| raytrace                   | 267 ms                                                     | 268 ms: 1.01x slower                                                        |
| django_template            | 34.8 ms                                                    | 35.0 ms: 1.01x slower                                                       |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                      |
| scimark_lu                 | 122 ms                                                     | 125 ms: 1.03x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 6.52 ms: 1.04x slower                                                       |
| regex_v8                   | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                       |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.05x slower                                                        |
| async_generators           | 442 ms                                                     | 462 ms: 1.05x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 86.2 ms: 1.06x slower                                                       |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.50 ms: 1.08x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                       |
| pylint                     | 317 ms                                                     | 350 ms: 1.10x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 58.8 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (6): dask, comprehensions, coroutines, regex_dna, logging_silent, pycparser
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x