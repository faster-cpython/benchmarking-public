# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: class_no_vectorcall
- machine: linux-x86_64
- commit hash: bfdd616
- commit date: 2024-08-21
- overall geometric mean: 1.05x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 283 ms: 1.03x slower                                                       |
| docutils       | 2.83 sec                                                   | 3.05 sec: 1.08x slower                                                     |
| html5lib       | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                                      |
| tornado_http   | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 325 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 425 ms: 1.09x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 864 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                       |
| async_tree_io              | 939 ms                                                     | 907 ms: 1.04x faster                                                       |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                                      |
| nbody          | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                      |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                      | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                                      |
| regex_dna      | 221 ms                                                     | 218 ms: 1.01x faster                                                       |
| regex_compile  | 137 ms                                                     | 142 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.7 ms: 1.12x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 55.3 ms: 1.11x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 98.9 ms: 1.09x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.0 ms: 1.07x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                       |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                      |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                      |
| genshi_text     | 23.7 ms                                                    | 25.9 ms: 1.09x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 59.5 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.1 us: 1.47x faster                                                      |
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                                       |
| richards                   | 50.9 ms                                                    | 39.3 ms: 1.30x faster                                                      |
| richards_super             | 57.4 ms                                                    | 44.9 ms: 1.28x faster                                                      |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.41 ms: 1.19x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 66.0 ms: 1.17x faster                                                      |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.17x faster                                                       |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.14x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.44 sec: 1.13x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 77.7 ms: 1.12x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.56 ms: 1.12x faster                                                      |
| float                      | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                       |
| nbody                      | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 55.3 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                       |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                       |
| coverage                   | 93.1 ms                                                    | 84.9 ms: 1.10x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.10x faster                                                     |
| pyflate                    | 484 ms                                                     | 442 ms: 1.09x faster                                                       |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.09x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                       |
| telco                      | 8.41 ms                                                    | 7.71 ms: 1.09x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 425 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.9 ms: 1.09x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.09x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.8 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 864 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.04 us: 1.07x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.0 ms: 1.07x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.50 us: 1.04x faster                                                      |
| logging_silent             | 105 ns                                                     | 100 ns: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                       |
| thrift                     | 823 us                                                     | 792 us: 1.04x faster                                                       |
| chaos                      | 61.3 ms                                                    | 59.2 ms: 1.04x faster                                                      |
| async_tree_io              | 939 ms                                                     | 907 ms: 1.04x faster                                                       |
| deltablue                  | 3.25 ms                                                    | 3.15 ms: 1.03x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                                       |
| regex_effbot               | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                       |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                                       |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                                      |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.01x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                      |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 758 ms                                                     | 771 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                       |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                      |
| raytrace                   | 267 ms                                                     | 272 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                      |
| 2to3                       | 274 ms                                                     | 283 ms: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                       |
| regex_compile              | 137 ms                                                     | 142 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 58.2 ms: 1.05x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 85.8 ms: 1.05x slower                                                      |
| sympy_str                  | 282 ms                                                     | 304 ms: 1.08x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.05 sec: 1.08x slower                                                     |
| sympy_expand               | 473 ms                                                     | 511 ms: 1.08x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 6.83 ms: 1.08x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 25.9 ms: 1.09x slower                                                      |
| generators                 | 29.6 ms                                                    | 32.7 ms: 1.10x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 23.0 ms: 1.12x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 176 ms: 1.13x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 59.5 ms: 1.15x slower                                                      |
| pylint                     | 317 ms                                                     | 369 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                               |

Benchmark hidden because not significant (8): pycparser, sqlglot_parse, comprehensions, pickle_pure_python, python_startup_no_site, json, pprint_pformat, regex_v8
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x