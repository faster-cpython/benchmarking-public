# Results vs. 3.13.0b2

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| html5lib       | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                  |
| async_tree_io              | 939 ms                                                     | 857 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 575 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 555 ms: 1.06x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.0 ms: 1.13x faster                                                 |
| nbody          | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                 |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 216 ms: 1.03x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                 |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.80 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.12x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 78.7 ms: 1.11x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 55.6 ms: 1.10x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 97.9 ms: 1.10x faster                                                 |
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                 |
| unpickle             | 15.1 us                                                    | 14.6 us: 1.04x faster                                                 |
| unpickle_list        | 5.34 us                                                    | 5.17 us: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 34.5 us: 1.01x faster                                                 |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.17 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.88 ms: 1.14x faster                                                 |
| django_template | 34.8 ms                                                    | 35.3 ms: 1.02x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 60.0 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.2 us: 1.46x faster                                                 |
| deepcopy                   | 367 us                                                     | 258 us: 1.42x faster                                                  |
| richards                   | 50.9 ms                                                    | 39.9 ms: 1.28x faster                                                 |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.28x faster                                                  |
| richards_super             | 57.4 ms                                                    | 45.6 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.21 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                 |
| spectral_norm              | 116 ms                                                     | 98.4 ms: 1.18x faster                                                 |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 65.8 ms: 1.18x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                  |
| mako                       | 11.2 ms                                                    | 9.88 ms: 1.14x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.44 sec: 1.13x faster                                                |
| float                      | 78.9 ms                                                    | 70.0 ms: 1.13x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.12x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 78.7 ms: 1.11x faster                                                 |
| go                         | 145 ms                                                     | 131 ms: 1.11x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.10x faster                                                  |
| nbody                      | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 55.6 ms: 1.10x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.0 ms: 1.10x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| xml_etree_iterparse        | 107 ms                                                     | 97.9 ms: 1.10x faster                                                 |
| async_tree_io              | 939 ms                                                     | 857 ms: 1.10x faster                                                  |
| coverage                   | 93.1 ms                                                    | 85.2 ms: 1.09x faster                                                 |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                                 |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                 |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                 |
| pyflate                    | 484 ms                                                     | 448 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                  |
| json                       | 5.31 ms                                                    | 4.94 ms: 1.07x faster                                                 |
| fannkuch                   | 402 ms                                                     | 375 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 575 ms: 1.06x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 555 ms: 1.06x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.0 ms: 1.06x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.66 sec: 1.05x faster                                                |
| telco                      | 8.41 ms                                                    | 8.05 ms: 1.05x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                 |
| thrift                     | 823 us                                                     | 790 us: 1.04x faster                                                  |
| unpickle                   | 15.1 us                                                    | 14.6 us: 1.04x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.24 us: 1.04x faster                                                 |
| unpickle_list              | 5.34 us                                                    | 5.17 us: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.03x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 748 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.94 ms: 1.01x faster                                                 |
| pickle_dict                | 34.8 us                                                    | 34.5 us: 1.01x faster                                                 |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| bench_thread_pool          | 834 us                                                     | 839 us: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                  |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                 |
| dulwich_log                | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                 |
| pickle_list                | 5.11 us                                                    | 5.17 us: 1.01x slower                                                 |
| django_template            | 34.8 ms                                                    | 35.3 ms: 1.02x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.60 sec: 1.03x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                  |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.80 ms: 1.03x slower                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.04x slower                                                 |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                                  |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 58.2 ms: 1.05x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 85.5 ms: 1.05x slower                                                 |
| raytrace                   | 267 ms                                                     | 281 ms: 1.05x slower                                                  |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                  |
| sympy_expand               | 473 ms                                                     | 506 ms: 1.07x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.86 ms: 1.09x slower                                                 |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 60.0 ms: 1.16x slower                                                 |
| pylint                     | 317 ms                                                     | 375 ms: 1.18x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (6): pycparser, tornado_http, pickle_pure_python, logging_simple, comprehensions, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x