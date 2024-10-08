# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_cache_dyna
- machine: linux-x86_64
- commit hash: 7e695c6
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 97.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 282 ms: 1.03x slower                                                        |
| docutils       | 2.83 sec                                                   | 3.30 sec: 1.17x slower                                                      |
| html5lib       | 67.2 ms                                                    | 76.2 ms: 1.13x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 99.5 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                      | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 410 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 314 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 550 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 901 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.3 ms: 1.11x faster                                                       |
| float          | 78.9 ms                                                    | 71.1 ms: 1.11x faster                                                       |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                       |
| regex_compile  | 137 ms                                                     | 154 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.1 ms: 1.13x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 54.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 9.94 ms: 1.08x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 203 us: 1.07x faster                                                        |
| tomli_loads          | 2.12 sec                                                   | 1.99 sec: 1.06x faster                                                      |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.01x slower                                                        |
| json_loads           | 28.9 us                                                    | 29.5 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                                       |
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                       |
| django_template | 34.8 ms                                                    | 38.9 ms: 1.12x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 64.0 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.1 us: 1.52x faster                                                       |
| deepcopy                   | 367 us                                                     | 267 us: 1.38x faster                                                        |
| richards                   | 50.9 ms                                                    | 40.4 ms: 1.26x faster                                                       |
| richards_super             | 57.4 ms                                                    | 45.8 ms: 1.25x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                       |
| scimark_fft                | 392 ms                                                     | 315 ms: 1.25x faster                                                        |
| scimark_lu                 | 122 ms                                                     | 101 ms: 1.21x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.40 ms: 1.20x faster                                                       |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.16x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                                       |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 77.1 ms: 1.13x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.44 sec: 1.13x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.7 ms: 1.12x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 54.8 ms: 1.12x faster                                                       |
| nbody                      | 88.3 ms                                                    | 79.3 ms: 1.11x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| float                      | 78.9 ms                                                    | 71.1 ms: 1.11x faster                                                       |
| logging_silent             | 105 ns                                                     | 94.7 ns: 1.11x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.69 ms: 1.09x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 410 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 9.94 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 203 us: 1.07x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 314 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 550 ms: 1.07x faster                                                        |
| pyflate                    | 484 ms                                                     | 454 ms: 1.07x faster                                                        |
| coverage                   | 93.1 ms                                                    | 87.4 ms: 1.07x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.99 sec: 1.06x faster                                                      |
| fannkuch                   | 402 ms                                                     | 380 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 723 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 901 ms: 1.04x faster                                                        |
| thrift                     | 823 us                                                     | 795 us: 1.04x faster                                                        |
| chaos                      | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.29 us: 1.03x faster                                                       |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                        |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                       |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 830 us: 1.00x faster                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                       |
| pickle_pure_python         | 305 us                                                     | 310 us: 1.01x slower                                                        |
| json_loads                 | 28.9 us                                                    | 29.5 us: 1.02x slower                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 83.8 ms: 1.03x slower                                                       |
| 2to3                       | 274 ms                                                     | 282 ms: 1.03x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 99.5 ms: 1.05x slower                                                       |
| async_generators           | 442 ms                                                     | 465 ms: 1.05x slower                                                        |
| raytrace                   | 267 ms                                                     | 282 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 59.7 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 120 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.80 ms: 1.10x slower                                                       |
| django_template            | 34.8 ms                                                    | 38.9 ms: 1.12x slower                                                       |
| sympy_expand               | 473 ms                                                     | 528 ms: 1.12x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 7.04 ms: 1.12x slower                                                       |
| regex_compile              | 137 ms                                                     | 154 ms: 1.13x slower                                                        |
| html5lib                   | 67.2 ms                                                    | 76.2 ms: 1.13x slower                                                       |
| sympy_str                  | 282 ms                                                     | 321 ms: 1.14x slower                                                        |
| sympy_sum                  | 156 ms                                                     | 180 ms: 1.15x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 23.7 ms: 1.16x slower                                                       |
| generators                 | 29.6 ms                                                    | 34.3 ms: 1.16x slower                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.53 ms: 1.16x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.30 sec: 1.17x slower                                                      |
| go                         | 145 ms                                                     | 173 ms: 1.20x slower                                                        |
| scimark_sor                | 127 ms                                                     | 154 ms: 1.21x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.42 sec: 1.22x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 64.0 ms: 1.24x slower                                                       |
| pylint                     | 317 ms                                                     | 406 ms: 1.28x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                                |

Benchmark hidden because not significant (7): typing_runtime_protocols, json, async_tree_io, logging_simple, regex_dna, comprehensions, coroutines
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 97.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x